from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("SignUp", views.SignUp_view, name="SignUp"),
    path("createEvent", views.createEvent_view, name="createEvent"),
    path("deleteEvent/<int:event_id>", views.deleteEvent_view, name="deleteEvent"),
    path("eventDetails/<int:event_id>", views.eventDetails_view, name="eventDetails"),
    path("register/<int:event_id>", views.register_view, name="register"),
    path("Categories", views.Categories_view, name="Categories"),
    path("search", views.search, name="search"),
    path("pastEvents", views.pastEvents_view, name="pastEvents"),
    path("feedback/<int:event_id>", views.feedback_view, name="feedback"),


]
