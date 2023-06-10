from django.urls import path

from .views import home
from .views import question
from .views import answer


app_name = "core"
urlpatterns = [path("", home, name="home"),
               path("question/", question, name="question"), 
               path("answer/<str:qid>", answer, name="answer")] 

