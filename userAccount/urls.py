
from django.urls import path
from .views import login_page,register_page,make_customer,profile_page,logout_page
urlpatterns = [
    path("login_page/",login_page,name="login"),
    path("register_page/",register_page,name="register"),
    path("make-customer/",make_customer,name="make_customer"),
    path("profile/",profile_page,name="profile"),
    path("logout/",logout_page,name="logout"),
]