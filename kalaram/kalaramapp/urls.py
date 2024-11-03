from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views



urlpatterns=[
        path("", views.home ),
        path("history/",views.history, name='history'),
        path("puja/",views.puja, name='puja'),
        path("donation/",views.donation, name='donation'),
        path("events/", views.events, name='events'),
        path("gallary/", views.gallary, name='gallary'),
        path("payment/", views.payment, name='payment'),
        path("projects/", views.projects, name='projects'),
        path('feedback/', views.feedback_view, name='feedback'),
        path("feedback_success/", views.feedback_success, name="feedback_success"),
        path('create-donation/', views.create_donation, name='create_donation'),
        path('donation-success/', views.donation_success, name='donation_success'),



]

if settings. DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)