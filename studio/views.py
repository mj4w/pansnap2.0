
from multiprocessing import reduction
from urllib.parse import non_hierarchical
from wsgiref.util import request_uri
from django.shortcuts import redirect, render, HttpResponse,get_object_or_404
from .models import User, Reservation
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib.auth import get_user_model
import datetime
from django.db import IntegrityError
from django.core.exceptions import SuspiciousOperation
from django.db.models import Q
from django.utils.safestring import mark_safe
from .filters import *
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
User = get_user_model()

# Create your views here.

def home(request):
    user = request.user.id
    reserve = Reservation.objects.all()
    user_login = User.objects.all()
    reserve_count = Reservation.objects.all().count()
    count = Reservation.objects.filter(status=True, user=user)
    if 'Send' in request.POST:
        if request.method == 'POST':
            if request.user.is_authenticated:
                message = request.POST.get('message')
                email = request.user.email
                name = f"{request.user.first_name} {request.user.last_name}"
                send_mail(
                    name, # name of recipient
                    f'From: {name} \n Email:{email} \n Message:{message}', #message sender
                    'settings.EMAIL_HOST_USER',
                    ['pansnapstudio26@gmail.com'],
                    fail_silently=False

                )
            else:
                message = request.POST['message']
                email = request.POST['email']
                name = request.POST['name']
                send_mail(
                    name, # name of recipient
                    f'From: {name} \n Email:{email} \n Message:{message}', #message sender
                    'settings.EMAIL_HOST_USER',
                    ['pansnapstudio26@gmail.com'],
                    fail_silently=False

                )
    elif 'signup' in request.POST:
        if request.method == "POST":
            username= request.POST['username']
            email = request.POST['email']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            password = request.POST['password']
            password2 = request.POST['password2']
            if password == password2:
                if User.objects.filter(email=email).exists():
                    messages.info(request,'Email already exists')
                    return redirect(request.META['HTTP_REFERER'])
                elif User.objects.filter(username=username).exists():
                    messages.info(request,'Username already exists')
                    return redirect(request.META['HTTP_REFERER'])
                else:
                    user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password , phone_num=False)
                    user.save()
                    #login
                    login_user = auth.authenticate(username=username, password=password)
                    auth.login(request, login_user)
                    messages.success(request,'Account created successfully!')
                    return redirect('home')
            else:
                messages.info(request,'Password Not Match')
                return redirect(request.META['HTTP_REFERER'])
    context = {
        'user_login':user_login,
        'count':count,
        'reserve_count':reserve_count,
        'reserve':reserve,
    }
    return render(request,'home.html', context)

def about(request):
    user = request.user.id
    reserve_count = Reservation.objects.all().count()
    count = Reservation.objects.filter(status=True, user=user)
    reserve = Reservation.objects.all()
    user_login = User.objects.all()
    context = {
        'reserve':reserve,
        'user_login':user_login,
        'count':count,
        'reserve_count':reserve_count,
    }
    return render(request,'about.html',context)

def services(request):
    user = request.user.id
    reserve_count = Reservation.objects.all().count()
    count = Reservation.objects.filter(status=True,user=user)
    reserve = Reservation.objects.all()
    user_login = User.objects.all()
    context = {
        'reserve':reserve,
        'user_login':user_login,
        'count':count,
        'reserve_count':reserve_count,
    }
    return render(request, 'services.html',context)

def hire_us(request):
    user = request.user.id
    reserve_count = Reservation.objects.all().count()
    count = Reservation.objects.filter(status=True,user=user)
    if 'login' in request.POST:
        if request.method == "POST":
            form = AuthenticationForm(request,data=request.POST)
            if form.is_valid():
                username= request.POST['username']
                password = request.POST['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request,'Login Success!')
                    return redirect('hire-us')
                else:
                    messages.warning(request,'Credentials Invalid')
            else:
                messages.warning(request,'Username & Password Incorrect!')
    elif 'clientnext' in request.POST and request.FILES:
        if request.method == "POST":
            first_name_reserve = request.POST.get('firstname',None)
            last_name_reserve = request.POST.get('lastname',None)
            email_address = request.POST.get('email',None)
            contact_number_reserve = request.POST.get('contact_number_reserve',None)
            facebook_url = request.POST.get('facebook_url',None)
            street_number = request.POST.get('street_number',None)
            baranggay = request.POST.get('baranggay',None)
            zip_code = request.POST.get('zip_code',None)
            municipality = request.POST.get('municipality',None)
            province = request.POST.get('province',None)
            indoor_shoot = request.POST.get('indoor',None)
            outdoor_shoot = request.POST.get('outdoor',None)
            comment_request = request.POST.get('comment_request',None)
            wedding_pre_nuptial = request.POST.get('wedding_pre_nuptial',None)
            pre_debut = request.POST.get('pre-debut',None)
            toddler = request.POST.get('toddler',None)
            pre_birthday= request.POST.get('pre-birthday',None)
            maternity = request.POST.get('maternity',None)
            family_portrait = request.POST.get('family_portrait',None)
            graduation_photo = request.POST.get('graduation_photo',None)
            barkada_shoot = request.POST.get('barkada_shoot',None)
            #packages wedding pre nuptial
            wedding_package1 =request.POST.get('wedding_package1',None)
            wedding_package2 = request.POST.get('wedding_package2',None)
            wedding_package3 = request.POST.get('wedding_package3',None)
            #packages pre debut
            debut_package1 = request.POST.get('debut_package1',None)
            debut_package2 = request.POST.get('debut_package2',None)
            debut_package3 = request.POST.get('debut_package3',None)
            #packages toddler
            toddler_package1 = request.POST.get('toddler_package1',None)
            toddler_package2 = request.POST.get('toddler_package2',None)
            toddler_package3 = request.POST.get('toddler_package3',None)
            #packages pre birthday
            pre_birthday_package1 = request.POST.get('pre_birthday_package1',None)
            pre_birthday_package2 = request.POST.get('pre_birthday_package2',None)
            pre_birthday_package3 = request.POST.get('pre_birthday_package3',None)
            #packages maternity
            maternity_package1 = request.POST.get('maternity_package1',None)
            maternity_package2 = request.POST.get('maternity_package2',None)
            maternity_package3 = request.POST.get('maternity_package3',None)
            #packages family portrait
            family_portrait_package1 = request.POST.get('family_portrait_package1',None)
            family_portrait_package2 = request.POST.get('family_portrait_package2',None)
            family_portrait_package3 = request.POST.get('family_portrait_package3',None)
            #packages graduation photo
            graduation_package1 = request.POST.get('graduation_package1',None)
            graduation_package2 = request.POST.get('graduation_package2',None)
            graduation_package3 = request.POST.get('graduation_package3',None)
            #packages barkada
            barkada_package1 = request.POST.get('barkada_package1',None)
            barkada_package2 = request.POST.get('barkada_package2',None)
            barkada_package3 = request.POST.get('barkada_package3',None)
            #additional extras 
            additional = request.POST.get('additional',None)
            #printed photo
            selection1 = request.POST.get('selection1',None)
            selection2 = request.POST.get('selection2',None)
            selection3 = request.POST.get('selection3',None)
            selection4 = request.POST.get('selection4',None)
            selection5 = request.POST.get('selection5',None)
            selection6 = request.POST.get('selection6',None)
            selection7 = request.POST.get('selection7',None)
            selection8 = request.POST.get('selection8',None)

            #flash drive
            flashdrive = request.POST.get('flashdrive',None)
            #photoframe
            yes = request.POST.get('yes',None)
            no = request.POST.get('no',None)
            #reservation details
            indoor_date = request.POST.get('indoor_date',None)
            indoor_radio1 = request.POST.get('indoor_radio1',None)
            indoor_radio2 = request.POST.get('indoor_radio2',None)
            indoor_radio3 = request.POST.get('indoor_radio3',None)
            indoor_radio4 = request.POST.get('indoor_radio4',None)
            indoor_radio5 = request.POST.get('indoor_radio5',None)
            number_of_people = request.POST.get('number_of_people',None)
            outdoor_date = request.POST.get('outdoor_date',None)
            outdoor_time = request.POST.get('outdoor_time',None)
            outdoor_end = request.POST.get('outdoor_end',None)
            events_location = request.POST.get('events_location',None)
            events_description = request.POST.get('events_description',None)
            check_terms = request.POST.get('check_terms',None)
            verify_image = request.FILES.get('larawan')
            #for outdoor services
            wedding = request.POST.get('wedding',None)
            debut = request.POST.get('debut',None)
            baptismal = request.POST.get('baptismal',None)
            birthday= request.POST.get('birthday',None)
            #church wedding outdoor 
            church_wedding = request.POST.get('church_wedding',None)
            civil_wedding = request.POST.get('civil_wedding',None)
            wedding_event = request.POST.get('wedding_event',None)
            prenup_outdoor = request.POST.get('prenup_outdoor',None)
            #packages wedding outdoor 
            video_package = request.POST.get('video_package',None)
            package_outdoor = request.POST.get('package_outdoor',None)
            package2_outdoor = request.POST.get('package2_outdoor',None)
            video_package2 = request.POST.get('video_package2',None)
            photo_video = request.POST.get('photo_video',None)
            photo_video_2 = request.POST.get('photo_video_2',None)
            #debut outdoor 
            pre_debut_outdoor = request.POST.get('pre_debut_outdoor',None)
            debut_outdoor = request.POST.get('debut_outdoor',None)
            pre_debut_outdoor1 = request.POST.get('predebut_outdoor1',None)
            pre_debut_outdoor2 = request.POST.get('predebut_outdoor2',None)
            pre_debut_outdoor3 = request.POST.get('predebut_outdoor3',None)
            package_debut1 = request.POST.get('package_debut1',None)
            package_debut2 = request.POST.get('package_debut2',None)
            package_debut3 = request.POST.get('package_debut3',None)
            #baptismal outdoor
            baptismal_outdoor1 = request.POST.get('baptismal_outdoor1',None)
            baptismal_outdoor2 = request.POST.get('baptismal_outdoor2',None)
            baptismal_outdoor3 = request.POST.get('baptismal_outdoor3',None)
            #birthday outdoor
            birthday_outdoor1 = request.POST.get('birthday_outdoor1',None)
            birthday_outdoor2 = request.POST.get('birthday_outdoor2',None)
            birthday_outdoor3 = request.POST.get('birthday_outdoor3',None)
            #another package
            v1  = request.POST.get('v1',None)
            v2  = request.POST.get('v2',None)
            v3  = request.POST.get('v3',None)
            v4  = request.POST.get('v4',None)
            v5  = request.POST.get('v5',None)
            v6  = request.POST.get('v6',None)
            try:
                reserve = Reservation.objects.create(
                    user = request.user,
                    first_name_reserve=first_name_reserve,
                    last_name_reserve=last_name_reserve,
                    email_address=email_address,
                    contact_number_reserve=contact_number_reserve,
                    facebook_url=facebook_url,
                    street_number=street_number,
                    baranggay=baranggay,
                    zip_code=zip_code,
                    municipality=municipality,
                    province=province,
                    indoor_shoot=indoor_shoot,
                    outdoor_shoot=outdoor_shoot,
                    comment_request=comment_request,

                    wedding_pre_nuptial=wedding_pre_nuptial,
                    pre_debut=pre_debut,
                    toddler=toddler,
                    pre_birthday=pre_birthday,
                    maternity=maternity,
                    family_portrait=family_portrait,
                    graduation_photo=graduation_photo,
                    barkada_shoot=barkada_shoot,

                    wedding_package1=wedding_package1,
                    wedding_package2=wedding_package2,
                    wedding_package3=wedding_package3,

                    debut_package1=debut_package1,
                    debut_package2=debut_package2,
                    debut_package3=debut_package3,

                    toddler_package1=toddler_package1,
                    toddler_package2=toddler_package2,
                    toddler_package3=toddler_package3,

                    pre_birthday_package1=pre_birthday_package1,
                    pre_birthday_package2=pre_birthday_package2,
                    pre_birthday_package3=pre_birthday_package3,

                    maternity_package1=maternity_package1,
                    maternity_package2=maternity_package2,
                    maternity_package3=maternity_package3,

                    family_portrait_package1=family_portrait_package1,
                    family_portrait_package2=family_portrait_package2,
                    family_portrait_package3=family_portrait_package3,
                    
                    graduation_package1=graduation_package1,
                    graduation_package2=graduation_package2,
                    graduation_package3=graduation_package3,
                    
                    barkada_package1=barkada_package1,
                    barkada_package2=barkada_package2,
                    barkada_package3=barkada_package3,
                    
                    additional=additional,
                    selection1=selection1,
                    selection2=selection2,
                    selection3=selection3,
                    selection4=selection4,
                    selection5=selection5,
                    selection6=selection6,
                    selection7=selection7,
                    selection8=selection8,
                    
                    flashdrive=flashdrive,
                    yes=yes,
                    no=no,
                    
                    indoor_date=indoor_date,
                    indoor_radio1=indoor_radio1,
                    indoor_radio2=indoor_radio2,
                    indoor_radio3=indoor_radio3,
                    indoor_radio4=indoor_radio4,
                    indoor_radio5=indoor_radio5,

                    number_of_people=number_of_people,

                    outdoor_date=outdoor_date,
                    outdoor_time=outdoor_time,
                    outdoor_end=outdoor_end,
                    events_location=events_location,
                    events_description=events_description,

                    check_terms=check_terms,
                    verify_image=verify_image,

                    status = False,
                    completed=False,
                    declined=False,
                    pending= True,
                    reserved=False,

                    wedding = wedding,
                    debut = debut,
                    baptismal = baptismal,
                    birthday= birthday,

                    church_wedding = church_wedding,
                    civil_wedding = civil_wedding,
                    wedding_event = wedding_event,
                    prenup_outdoor = prenup_outdoor, 

                    video_package = video_package,
                    package_outdoor = package_outdoor,
                    package2_outdoor = package2_outdoor,
                    video_package2 = video_package2,
                    photo_video = photo_video,
                    photo_video_2 = photo_video_2,
                    
                    pre_debut_outdoor = pre_debut_outdoor,
                    debut_outdoor = debut_outdoor,
                    pre_debut_outdoor1 =pre_debut_outdoor1,
                    pre_debut_outdoor2 = pre_debut_outdoor2,
                    pre_debut_outdoor3 =pre_debut_outdoor3,
                    package_debut1 =package_debut1,
                    package_debut2 = package_debut2,
                    package_debut3 = package_debut3,

                    baptismal_outdoor1 =baptismal_outdoor1,
                    baptismal_outdoor2 = baptismal_outdoor2,
                    baptismal_outdoor3 = baptismal_outdoor3,
                    
                    birthday_outdoor1 = birthday_outdoor1,
                    birthday_outdoor2 = birthday_outdoor2,
                    birthday_outdoor3 = birthday_outdoor3,
                    v1=v1,
                    v2=v2,
                    v3=v3,
                    v4=v4,
                    v5=v5,
                    v6=v6,
                    
                    
                    
                    
                    )
                
                reserve.save()
                messages.success(request,'Reservation Complete! ')
                return redirect('profile')
            except ValueError:
                messages.error(request,'Incomplete Inputs')
             
    form = AuthenticationForm()
    reserve = Reservation.objects.all()
    user_login = User.objects.all()
    context = {
        'reserve':reserve,
        'user_login':user_login,
        'count':count,
        'reserve_count':reserve_count,
    }
   
    return render(request, 'hire_us.html',context)

def portfolio(request):
    user = request.user.id
    reserve_count = Reservation.objects.all().count()
    count = Reservation.objects.filter(status=True,user=user)
    reserve = Reservation.objects.all()
    user_login = User.objects.all()
    context = {
        'reserve':reserve,
        'user_login':user_login,
        'count':count,
        'reserve_count':reserve_count,
    }
    return render(request, 'portfolio.html',context)

def contact(request):
    user = request.user.id
    reserve_count = Reservation.objects.all().count()
    count = Reservation.objects.filter(status=True,user=user)
    if request.method == 'POST':
        if request.user.is_authenticated:
            message = request.POST['message']
            email = request.user.email
            name = f"{request.user.first_name} {request.user.last_name}"
            send_mail(
                name, # name of recipient
                f'From: {name} \n Email:{email} \n Message:{message}', #message sender
                'settings.EMAIL_HOST_USER',
                ['pansnapstudio26@gmail.com'],
                fail_silently=False

            )
        else:
            message = request.POST['message']
            email = request.POST['email']
            name = request.POST['name']
            send_mail(
                name, # name of recipient
                f'From: {name} \n Email:{email} \n Message:{message}', #message sender
                'settings.EMAIL_HOST_USER',
                ['pansnapstudio26@gmail.com'],
                fail_silently=False

            )
    reserve = Reservation.objects.all()
    user_login = User.objects.all()
    context = {
        'reserve':reserve,
        'user_login':user_login,
        'count':count,
        'reserve_count':reserve_count,
    }
    return render(request, 'contact.html',context)
def studio_shoot(request):
    user = request.user.id
    reserve_count = Reservation.objects.all().count()
    count = Reservation.objects.filter(status=True,user=user)
    reserve = Reservation.objects.all()
    user_login = User.objects.all()
    context = {
        'reserve':reserve,
        'count':count,
        'reserve_count':reserve_count,
        'user_login':user_login,
    }
    return render(request,'studio_shoot.html',context)
def films(request):
    user = request.user.id
    reserve_count = Reservation.objects.all().count()
    count = Reservation.objects.filter(status=True,user=user)
    reserve = Reservation.objects.all()
    user_login = User.objects.all()
    context = {
        'reserve':reserve,
        'user_login':user_login,
        'count':count,
        'reserve_count':reserve_count,
    }
    return render(request, 'films.html',context)



def login_user(request):
    reserve_count = Reservation.objects.all().count()
    count = Reservation.objects.filter(status=True)
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username= request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request,f'Login Success!')
                return redirect('home')
            else:
                messages.warning(request,'Credentials Invalid')
        else:
            messages.warning(request,'Username & Password Incorrect!')
    form = AuthenticationForm()

    return render(request,'login_user.html', {'navbar':'login-user'})

def profile(request):
    user = request.user.id
    reserve_count = Reservation.objects.all().count()
    count = Reservation.objects.filter(status=True, user=user)
    user = request.user
    reserve = Reservation.objects.filter(user=user)

    current = datetime.date.today()
    formatdate = current.strftime("%B, %Y")
    context = {
        'formatdate':formatdate,
        'reserve':reserve,
        'count':count,
        'reserve_count':reserve_count,
    }
    return render(request, 'profile.html',context)
def edit_profile(request, pk):
    user = request.user.id
    reserve_count = Reservation.objects.all().count()
    count = Reservation.objects.filter(status=True,user=user)
    user = request.user
    if request.method == "POST":
        user_change = UserForm(request.POST,request.FILES or None, instance=user)
        if user_change.is_valid():
            user_change.save()
            messages.success(request,'Update Profile Successfully')
            return redirect('profile')
    user_change = UserForm(instance=user)
    context = {
        'user_change':user_change,
        'count':count,
        'reserve_count':reserve_count,
    }
    return render(request, 'edit_profile.html', context)
def logout_user(request):
    
    logout(request)
    messages.info(request, 'Thankyou for visiting!!')
    return redirect('home')
def seemore(request):
    user = request.user.id
    reserve_count = Reservation.objects.all().count()
    count = Reservation.objects.filter(status=True, user=user)
    user = request.user
    reserve = Reservation.objects.filter(user=user)

    context = {
        'reserve':reserve,
        'count':count,
        'reserve_count':reserve_count,

    }
    return render(request,'see_more.html', context)

def edit_seemore(request,pk):
    obj = get_object_or_404(Reservation, id=pk)
    reserves = ReservationForm(request.POST or None,request.FILES or None, instance=obj)
    if reserves.is_valid():
        reserves.save()
        messages.success(request,'Update Successfully!')
        return redirect('seemore')
    context = {
        'reserves':reserves,
        'obj':obj,


    }
    return render(request,'edit_seemore.html',context)

def delete(request,pk):

    reserve_delete = get_object_or_404(Reservation, id=pk)
    reserve_delete.delete()
    messages.success(request,'Reservation Removed Successfully!')
    return redirect('profile')
        
def delete_user_admin(request,pk):
    
    user = get_object_or_404(User, id=pk)
    user.delete()
    messages.success(request,'Removed Successfully!')
    return redirect(request.META['HTTP_REFERER'])
def delete_reservation_admin(request,pk):
    
    reserve = get_object_or_404(Reservation, id=pk)
    reserve.delete()
    messages.success(request,'Removed Successfully!')
    return redirect(request.META['HTTP_REFERER'])
def edit_admin(request,pk):

    obj = get_object_or_404(Reservation, id=pk)
    reserves = ReservationForm(request.POST or None,request.FILES or None,instance=obj)
    if reserves.is_valid():
        reserves.save()
        messages.success(request,'Update Successfully')
        return redirect('home')
    context = {
        'reserves':reserves,
        'obj':obj,
    }
    return render(request,'edit_admin.html',context)

def search(request):
    if request.method == "GET":
        searched = request.GET.get('searched')
        user_search = User.objects.filter(Q(username__icontains=searched) | Q(first_name__icontains=searched) | Q(email__icontains=searched) | Q(phone_num__icontains=searched))
        context = {
            'user_search':user_search,
        }
        return render(request,'search_admin.html',context)

def search_reserve(request):
    if request.method == "GET":
        search_reserve = request.GET.get('search_reserve')
        reservation_search = Reservation.objects.filter(
            Q(first_name_reserve__icontains=search_reserve)
            | Q(last_name_reserve__icontains=search_reserve) 
            | Q(wedding_pre_nuptial__icontains=search_reserve) 
            | Q(pre_debut__icontains=search_reserve) 
            | Q(toddler__icontains=search_reserve) 
            | Q(pre_birthday__icontains=search_reserve) 
            | Q(maternity__icontains=search_reserve) 
            | Q(family_portrait__icontains=search_reserve) 
            | Q(graduation_photo__icontains=search_reserve) 
            | Q(barkada_shoot__icontains=search_reserve) 
            | Q(wedding__icontains=search_reserve) 
            | Q(debut__icontains=search_reserve) 
            | Q(baptismal__icontains=search_reserve) 
            | Q(birthday__icontains=search_reserve) 
            | Q(indoor_shoot__icontains=search_reserve) 
            | Q(outdoor_shoot__icontains=search_reserve) 
            )
        context = {
            'reservation_search':reservation_search,
        }
    return render(request,'search_reserve.html',context)

def indoor_type(request):
    reserve = Reservation.objects.all()
    context = {
        'reserve':reserve,
    }
    return render(request,'type/indoor_type.html', context)

def outdoor_type(request):
    reserve = Reservation.objects.all()
    context = {
        'reserve':reserve,
    }
    return render(request,'type/outdoor_type.html', context)

def approve(request):
    reserve = Reservation.objects.all()
    context = {
        'reserve':reserve,
    }
    return render(request,'type/approve.html', context)

def pending(request):
    reserve = Reservation.objects.all()
    context = {
        'reserve':reserve,
    }
    return render(request,'type/pending.html', context)

def complete(request):
    reserve = Reservation.objects.all()
    context = {
        'reserve':reserve,
    }
    return render(request,'type/complete.html', context)
def declined(request):
    reserve = Reservation.objects.all()
    context = {
        'reserve':reserve,
    }
    return render(request,'type/declined.html', context)

def reserved(request):
    reserve = Reservation.objects.all()
    context = {
        'reserve':reserve,
    }
    return render(request,'type/reserved.html', context)
from django.utils.datastructures import MultiValueDictKeyError
def payment(request,pk):
    obj = Reservation.objects.get(id=pk)
    try:
        email = request.user.email
        i_d = obj.id
        name = f"{request.user.first_name} {request.user.last_name}"
        email = EmailMessage(email,f"{name}\n Email:{email} \n ID_RESERVATION: {i_d}",'settings.EMAIL_HOST_USER',['pansnapstudio26@gmail.com'])
        email.content_subtype='html'
        
        file = request.FILES['image']
        email.attach(file.name,file.read(),file.content_type)
        email.send()
    except MultiValueDictKeyError:
        email = ''
        name = ''
    context = {
        'obj':obj
    }
    return render(request,'payment/payment.html',context)


def notification(request):
    user = request.user.id
    reserve_count = Reservation.objects.all().count()
    count = Reservation.objects.filter(status=True,user=user)
    user = request.user
    reserve = Reservation.objects.filter(user=user)
    context = {
        'reserve':reserve,
        'count':count,
        'reserve_count':reserve_count,
    }
    return render(request,'notification.html', context)