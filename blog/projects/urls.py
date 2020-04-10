from django.urls import path
from . import views

urlpatterns = [
    path("portfolio/", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path("",views.index,name="index"),
    path("aboutme",views.aboutme,name="aboutme"),
    path("credits",views.credits,name="credits"),
    path("about",views.about,name="about")
]