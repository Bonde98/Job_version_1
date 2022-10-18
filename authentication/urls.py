from django.urls import path
from .views import Login,sigup, logout_page,LoginPage, detail_profile, edit_profile



urlpatterns = [
    path("login/",LoginPage.as_view(),name="login"),
    path("signup/",sigup,name="signup"),
    path("logout/",logout_page,name="logout"),
    path("detail/<int:id>",detail_profile,name="detail_profile"),
    path("edit/<int:profile_id>", edit_profile ,name="edit_profile"),

]