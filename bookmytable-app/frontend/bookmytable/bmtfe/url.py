from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('support', views.supportTicket, name='support'),
    path('nutrition', views.handleNutrition, name='nutrition'),
    path('foodreview', views.foodReview, name='foodreview'),
    path('knowmore/<int:restr_id>', views.knowMore, name='knowmore'),
    path('owner/<int:restr_id>', views.ownerPage, name='ownerpage'),
    path('signup', views.handleSignUp, name='handlesignup'),
    path('signin', views.handleSignIn, name='handlesignin'),
    # path('signout', views.handleSignOut, name='handlesignout'),
    path('booking/<int:restr_id>', views.restrBooking, name='resterbooking'),
    path('bookingcomplete/<int:booking_id>', views.bookingComplete, name='bookingcomplete'),
    path('bookingdelete/<int:booking_id>', views.bookingDelete, name='bookingdelete'),
    path('forms', views.formHandler, name='formhandler'),
    path('metrics/', views.prometheus_metrics, name='prometheus_metrics'),
]

