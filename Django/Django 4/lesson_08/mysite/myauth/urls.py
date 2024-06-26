from django.urls import path
from .views import get_cookie_view, set_cookie_view, set_session_view, get_session_view, MylogoutView, AboutMeView, RegisterView, FooBarView, HelloView
from django.contrib.auth.views import LoginView

app_name = "myauth"

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(
            template_name="myauth/login.html",  # имя шаблона, если нет то будет искать registration/login.html
            redirect_authenticated_user=True,  # редирект для уже залогиненых пользоваетлей, в settings, без этого ищет account/profile
        ),
        name="login"),
    # path("logout/", logout_view, name="logout"),
    path("hello/", HelloView.as_view(), name="hello"),
    path("logout/", MylogoutView.as_view(), name="logout"),
    path("about-me/", AboutMeView.as_view(), name="about-me"),
    path("register/", RegisterView.as_view(), name="register"),
    path("cookie/get/", get_cookie_view, name="cookie-get"),
    path("cookie/set/", set_cookie_view, name="cookie-set"),
    path("session/get", get_session_view, name="session-get"),
    path("session/set", set_session_view, name="session-set"),
    path("foo-bar/", FooBarView.as_view(), name="foo-bar")
]
