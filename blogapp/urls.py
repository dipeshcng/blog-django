from django.urls import path
from .views import *


app_name = "blogapp"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("nepal/", NepalView.as_view(), name="Nepal"),
    path("blog/list/", BlogListView.as_view(), name="bloglist"),
    path("event/list/", EventListView.as_view(), name="eventlist"),
    path("blog/<int:pk>/detail/", BlogDetailView.as_view(), name="blogdetail"),
    path("event/<int:pk>/detail/", EventDetailView.as_view(), name="eventdetail"),
    path("news/list/", NewsListView.as_view(), name="newslist"),
    path("news/<int:pk>/detail/", NewsDetailView.as_view(), name="newsdetail"),
    path("blog/create/", BlogCreateView.as_view(), name="blogcreate"),
    path("blog/<int:pk>/update/", BlogUpdateView.as_view(), name="blogupdate"),
    path("blog/<int:pk>/delete/", BlogDeleteView.as_view(), name="blogdelete"),
    path("event/create/", EventCreateView.as_view(), name="eventcreate"),
    path("event/<int:pk>/update/", EventUpdateView.as_view(), name="eventupdate"),
    path("event/<int:pk>/delete/", EventDeleteView.as_view(), name="eventdelete"),
    path("login/", LoginViews.as_view(), name="login"),
    path("register/", UserRegistrationView.as_view(), name="userreg"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("category/<int:pk>/", CategoryDetailView.as_view(), name="categorydetail"),
    path("search/", SearchView.as_view(), name="search"),


]
