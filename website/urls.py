from django.contrib import admin
from django.urls import path
from . import views

handler404 = 'website.views.handler404'

urlpatterns = [
    path("", views.home, name="home"),
    path("aboutus/", views.aboutus, name="aboutus"),
    path("posts/", views.posts, name="posts"),
    path("teams/", views.teams, name="teams"),
    path("teams19/", views.teams19, name="teams19"),
    path("teams21/", views.teams21, name="teams21"),
    path("events/", views.events, name="events"),
    path("csi_show/", views.csi_show, name="csi_show"),
    path("magazines/<int:year>/", views.magazines_single, name="magazines_single"),
    path("magazines/", views.magazines, name="magazines"),
    path("e/<str:event_url>/", views.event_pages, name="event"),
    path("pe/<str:previous_event_url>/",
         views.previous_event_pages, name="previous_event"),
    path("github/", views.github, name="github"),
]
