from django.urls import path

from .views import signin
from .views import signout
from .views import signup 


app_name = "account"
urlpatterns = [path("signup/", signup, name="signup"),
               path("signin/", signin, name="signin"),
               path("signout/", signout, name="signout")]

