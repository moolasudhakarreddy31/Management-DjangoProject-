from django.urls import path, include
from . import views
from django.contrib import admin

app_name = "ticket_manager"


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("index", views.index, name="index"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path('ticket/<int:ticket_id>', views.ticket_by_id, name='ticket_by_id'),
    path("newticket", views.creating_ticket, name="newticket"),
    path("update/<int:ticket_id>", views.update_view, name="update"),

]
