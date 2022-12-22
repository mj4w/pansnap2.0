from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home, name="home"),
    path('about/', views.about, name='about'), 
    path('service/', views.services, name='services'),
    path('hire-us/', views.hire_us, name='hire-us'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('sign-up/',views.signup, name="sign-up"),
    path('logout/', views.logout_user, name="logout"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
