from django.urls import path

from .views import sample1,sample2,sample3,sample4,sample5,sample6,sample7,sample8,custom,destination
from . import views


urlpatterns = [
    path('',views.sample1,name='index'),
    path('destination/',views.sample2,name='destination'),
    path('login/', views.sample4, name='login'),
    path('regester/', views.sample5, name='regester'),
    path('user/', views.sample6, name='user'),
    path('contact/',views.sample7,name='contact'),
    path('about/',views.sample8,name='about'),
    path("SignUpDatafunction",views.SignUpDatafunction,name="SignUpDatafunction"),
    path("checkuserlogin",views.checkuserlogin,name="checkuserlogin"),
    path('payment/<int:id>', views.payment, name='payment'),
    path('custom/', views.custom, name='custom'),
    path('sear/', views.sear, name='sear'),
    path('sucpayment/', views.sucpayment, name='suc'),
    path('addcustom/', views.addcustom, name='addcustom'),
    path('search/<str:city>/<int:days>/<str:type>/<int:n>', views.searchcity, name='city'),
    path('feedback/', views.feedback, name='feedback'),
]
