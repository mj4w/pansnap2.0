from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.template.defaultfilters import date

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True, null=True)
    last_name = models.CharField(max_length=50, null=True)
    first_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True, max_length=100)
    phone_num = models.IntegerField(null=True, blank=True)
    avatar = models.ImageField(upload_to="images_upload/", blank=True)
    created_on = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    # @property
    # def avatarURL(self):
    #     try:
    #         avatar = self.avatarURL.url
    #     except:
    #         avatar = ''

        # return avatar

class Reservation(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name_reserve = models.CharField(null=True, max_length=50, blank=True )
    last_name_reserve = models.CharField(null=True,max_length=50, blank=True)
    email_address = models.EmailField(null=True,max_length=100, blank=True)
    contact_number_reserve = models.IntegerField(null=True, blank=True)
    facebook_url = models.CharField(max_length=100, null=True, blank=True)
    street_number = models.CharField(max_length=50, null=True, blank=True)
    baranggay = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    municipality = models.CharField(max_length=100,null=True, blank=True)
    province = models.CharField(max_length=50, null=True, blank=True)
    indoor_shoot = models.CharField(max_length=50,null=True, blank=True)
    outdoor_shoot = models.CharField(max_length=50,null=True, blank=True)
    #for indoor services
    wedding_pre_nuptial = models.CharField(max_length=50,null=True, blank=True)
    pre_debut = models.CharField(max_length=50,null=True, blank=True)
    toddler = models.CharField(max_length=50,null=True, blank=True)
    pre_birthday= models.CharField(max_length=50,null=True, blank=True)
    maternity= models.CharField(max_length=50,null=True, blank=True)
    family_portrait= models.CharField(max_length=50,null=True, blank=True)
    graduation_photo= models.CharField(max_length=50,null=True, blank=True)
    barkada_shoot= models.CharField(max_length=50,null=True, blank=True)
    #packages wedding pre nuptial
    wedding_package1 = models.CharField(max_length=50,null=True, blank=True)
    wedding_package2 = models.CharField(max_length=50,null=True, blank=True)
    wedding_package3 = models.CharField(max_length=50,null=True, blank=True)
    #packages pre debut
    debut_package1 = models.CharField(max_length=50,null=True, blank=True)
    debut_package2 = models.CharField(max_length=50,null=True, blank=True)
    debut_package3 = models.CharField(max_length=50,null=True, blank=True)
    #packages toddler
    toddler_package1 = models.CharField(max_length=50,null=True, blank=True)
    toddler_package2 = models.CharField(max_length=50,null=True, blank=True)
    toddler_package3 = models.CharField(max_length=50,null=True, blank=True)
    #packages pre birthday
    pre_birthday_package1 = models.CharField(max_length=50,null=True, blank=True)
    pre_birthday_package2 = models.CharField(max_length=50,null=True, blank=True)
    pre_birthday_package3 = models.CharField(max_length=50,null=True, blank=True)
    #packages maternity
    maternity_package1 = models.CharField(max_length=50,null=True, blank=True)
    maternity_package2 = models.CharField(max_length=50,null=True, blank=True)
    maternity_package3 = models.CharField(max_length=50,null=True, blank=True)
    #packages family portrait
    family_portrait_package1 = models.CharField(max_length=50,null=True, blank=True)
    family_portrait_package2 = models.CharField(max_length=50,null=True, blank=True)
    family_portrait_package3 = models.CharField(max_length=50,null=True, blank=True)
    #packages graduation photo
    graduation_package1 = models.CharField(max_length=50,null=True, blank=True)
    graduation_package2 = models.CharField(max_length=50,null=True, blank=True)
    graduation_package3 = models.CharField(max_length=50,null=True, blank=True)
    #packages barkada
    barkada_package1 = models.CharField(max_length=50,null=True, blank=True)
    barkada_package2 = models.CharField(max_length=50,null=True, blank=True)
    barkada_package3 = models.CharField(max_length=50,null=True, blank=True)
    #additional extras 
    additional = models.CharField(max_length=30,null=True, blank=True)
    #printed photo
    selection1 = models.CharField(max_length=50,null=True, blank=True)
    selection2 = models.CharField(max_length=50,null=True, blank=True)
    selection3 = models.CharField(max_length=50,null=True, blank=True)
    selection4 = models.CharField(max_length=50,null=True, blank=True)
    selection5 = models.CharField(max_length=50,null=True, blank=True)
    selection6 = models.CharField(max_length=50,null=True, blank=True)
    selection7 = models.CharField(max_length=50,null=True, blank=True)
    selection8 = models.CharField(max_length=50,null=True, blank=True)

    #flash drive
    flashdrive = models.CharField(max_length=50,null=True, blank=True)
    #photoframe
    yes = models.CharField(max_length=10,null=True, blank=True)
    no = models.CharField(max_length=10,null=True, blank=True)
    #for comments 
    comment_request = models.CharField(max_length=1000, blank=True,null=True)
    #for reservation details
    #indoor 
    indoor_date = models.CharField(max_length=50, null=True, blank=True)
    indoor_radio1 = models.CharField(max_length=50, null=True, blank=True)
    indoor_radio2 = models.CharField(max_length=50, null=True, blank=True)
    indoor_radio3 = models.CharField(max_length=50, null=True, blank=True)
    indoor_radio4 = models.CharField(max_length=50, null=True, blank=True)
    indoor_radio5 = models.CharField(max_length=50, null=True, blank=True)
    number_of_people = models.CharField(null=True, blank=True, max_length=20)
    #outdoor 
    outdoor_date = models.CharField(max_length=50, null=True, blank=True)
    outdoor_time = models.TimeField(null=True, blank=True)
    outdoor_end = models.TimeField(null=True, blank=True)
    events_location = models.CharField(max_length=200, null=True, blank=True)
    events_description =models.TextField(max_length=1000, null=True, blank=True)


    check_terms = models.CharField(max_length=10, null=True, blank=True)
    verify_image = models.ImageField(upload_to="verification/", blank=True, null=True)

    #status  
    status = models.BooleanField(default=False, blank=True)
    completed = models.BooleanField(default=False, blank=True)
    declined = models.BooleanField(default=False, blank=True)
    reserved = models.BooleanField(default=False, blank=True)
    pending = models.BooleanField(default=False, blank=True)

    
    #for outdoor services
    wedding = models.CharField(max_length=50,null=True, blank=True)
    debut = models.CharField(max_length=50,null=True, blank=True)
    baptismal = models.CharField(max_length=50,null=True, blank=True)
    birthday= models.CharField(max_length=50,null=True, blank=True)
    #church wedding outdoor 
    church_wedding = models.CharField(max_length=100,null=True, blank=True)
    civil_wedding = models.CharField(max_length=100,null=True, blank=True)
    wedding_event = models.CharField(max_length=100,null=True, blank=True)
    prenup_outdoor = models.CharField(max_length=100,null=True, blank=True)
    #packages wedding outdoor 
    video_package = models.CharField(max_length=100,null=True, blank=True)
    package_outdoor = models.CharField(max_length=100,null=True, blank=True)
    package2_outdoor = models.CharField(max_length=100,null=True, blank=True)
    
    video_package2 = models.CharField(max_length=100,null=True, blank=True)
    photo_video = models.CharField(max_length=100,null=True, blank=True)
    photo_video_2 = models.CharField(max_length=100,null=True, blank=True)
    
    v1 = models.CharField(max_length=100,null=True, blank=True)
    v2 = models.CharField(max_length=100,null=True, blank=True)
    v3 = models.CharField(max_length=100,null=True, blank=True)
    
    v4 = models.CharField(max_length=100,null=True, blank=True)
    v5 = models.CharField(max_length=100,null=True, blank=True)
    v6 = models.CharField(max_length=100,null=True, blank=True)


    #debut outdoor 
    pre_debut_outdoor = models.CharField(max_length=100,null=True, blank=True)
    debut_outdoor = models.CharField(max_length=100,null=True, blank=True)


    pre_debut_outdoor1 = models.CharField(max_length=100,null=True, blank=True)
    pre_debut_outdoor2 = models.CharField(max_length=100,null=True, blank=True)
    pre_debut_outdoor3 = models.CharField(max_length=100,null=True, blank=True)

    package_debut1 = models.CharField(max_length=100,null=True, blank=True)
    package_debut2 = models.CharField(max_length=100,null=True, blank=True)
    package_debut3 = models.CharField(max_length=100,null=True, blank=True)
    #baptismal outdoor
    baptismal_outdoor1 = models.CharField(max_length=100,null=True, blank=True)
    baptismal_outdoor2 = models.CharField(max_length=100,null=True, blank=True)
    baptismal_outdoor3 = models.CharField(max_length=100,null=True, blank=True)
    #birthday outdoor
    birthday_outdoor1 = models.CharField(max_length=100,null=True, blank=True)
    birthday_outdoor2 = models.CharField(max_length=100,null=True, blank=True)
    birthday_outdoor3 = models.CharField(max_length=100,null=True, blank=True)

    def __str__(self):
        return self.user.username
    
   