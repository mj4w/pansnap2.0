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
    path('studio-shoot/', views.studio_shoot, name='studio-shoot'),
    path('films/', views.films, name="films"),
    path('profile/',views.profile, name='profile'),
    path('edit-profile/<int:pk>/',views.edit_profile, name="edit-profile"),
    path('contact/', views.contact, name='contact'),
    path('log-in/',views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('see-more/',views.seemore, name='seemore'),
    path('see-more-edit/<int:pk>/',views.edit_seemore, name='edit-seemore'),
    path('delete-seemore/<int:pk>/',views.delete, name='delete-seemore'),
    path('edit-admin/<int:pk>/',views.edit_admin, name='edit-admin'),
    path('search/', views.search, name="search"),
    path('search-reserve',views.search_reserve, name='search-reserve'),
    path('delete-user-admin/<int:pk>/',views.delete_user_admin, name='delete-user-admin'),
     path('delete-reservation-admin/<int:pk>/',views.delete_reservation_admin, name='delete-reservation-admin'),
    #type 
    path('indoor-type/',views.indoor_type, name="indoor"),
    path('outdoor-type/',views.outdoor_type, name="outdoor"),
    path('approve-type/',views.approve, name="approve"),
    path('complete-type/',views.complete, name="complete"),
    path('pending-type/',views.pending, name="pending"),
    path('declined-type/',views.declined, name="declined"),
    path('reserve-type/',views.reserved, name="reserved"),
    #payment
    path('payment/<int:pk>/',views.payment, name='payment'),
    path('notification/',views.notification,name="notification"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
