from django.urls import path, reverse_lazy
from .views import sigup, logout_page,LoginPage, detail_profile, edit_profile
# Import les
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView


urlpatterns = [
    path("login/",LoginPage.as_view(),name="login"),
    path("signup/",sigup,name="signup"),
    path("logout/",logout_page,name="logout"),
    path("detail/<int:id>",detail_profile,name="detail_profile"),
    path("edit/<int:profile_id>", edit_profile ,name="edit_profile"),
    path('password-change',PasswordChangeView.as_view(
        template_name="authentication/password_change.html",
        success_url = reverse_lazy('password-change-done')
    ), name='password_change'),
    path('password-change-done',PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html',
    ), name='password-change-done'),
]