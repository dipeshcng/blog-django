from django.views.generic import *
from .models import *
from .forms import*
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["a"] = "hellow sir"
        context["b"] = 1000
        context["bloglist"] = Blog.objects.all().order_by("-id")
        context["newslist"] = News.objects.all().order_by("-id")
        context["eventlist"] = Event.objects.all().order_by("-id")
        context["categorylist"] = Category.objects.all()

        return context


class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        sender = form.cleaned_data["sender"]
        mobile = form.cleaned_data["mobile_number"]
        email = form.cleaned_data["email"]
        subject = form.cleaned_data["subject"]
        message = form.cleaned_data["message"]
        print(sender, mobile, email, subject, message)

        Message.objects.create(name=sender, mobile=mobile,
                               email=email, subject=subject, messagge=message)
        return super().form_valid(form)


class ProfileView(TemplateView):
    template_name = "profile.html"


class NepalView(TemplateView):
    template_name = "nepal.html"


class BlogListView(ListView):
    template_name = "bloglist.html"
    queryset = Blog.objects.all().order_by("-id")
    context_object_name = "allblogs"


class EventListView(ListView):
    template_name = "eventlist.html"
    queryset = Event.objects.all()
    context_object_name = "allevents"


class BlogDetailView(DetailView):
    template_name = "blogdetail.html"
    # queryset=Blog.objects.html()
    model = Blog
    context_object_name = "blog"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog_id = self.kwargs["pk"]
        blog = Blog.objects.get(id=blog_id)
        blog.view_count += 1
        blog.save()

        return context


class EventDetailView(DetailView):
    template_name = "eventdetail.html"
    # queryset=Event.objects.html()
    model = Event
    context_object_name = "event"


class NewsListView(ListView):
    template_name = "newslist.html"
    queryset = News.objects.all()
    context_object_name = "allnews"


class NewsDetailView(DetailView):
    template_name = "newsdetail.html"
    # queryset=News.objects.html()
    model = News
    context_object_name = "news"


class BlogCreateView(LoginRequiredMixin, CreateView):
    login_url = "/login/"
    template_name = "blogcreate.html"
    form_class = BlogForm
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bloglist"] = Blog.objects.all().order_by("-id")

        return context

    def form_valid(self, form):
        title = form.cleaned_data["title"]
        form.instance.author = self.request.user
        print(title)

        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/login/"
    template_name = "blogcreate.html"
    model = Blog
    form_class = BlogForm
    success_url = "/blog/list"


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/login/"
    template_name = "blogdelete.html"
    model = Blog
    # form_class=BlogForm
    success_url = "/blog/list"


class EventCreateView(LoginRequiredMixin, CreateView):
    login_url = "/login/"
    template_name = "eventcreate.html"
    form_class = EventForm
    success_url = "/"


class EventUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/login/"
    template_name = "eventcreate.html"
    model = Event
    form_class = EventForm
    success_url = "/event/list"


class EventDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/login/"
    template_name = "eventdelete.html"
    model = Event
    # form_class=EventForm
    success_url = "/event/list"


class LoginViews(FormView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = "/"

    def form_valid(self, form):
        uname = form.cleaned_data["username"]
        pword = form.cleaned_data["password"]

        user = authenticate(username=uname, password=pword)
        if user is not None:
            login(self.request, user)

        else:
            return render(self.request, self.template_name,
                          {"error": "username or password didn't match", "form": form})

        return super().form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/")


class CategoryDetailView(DetailView):
    template_name = "categorydetail.html"
    model = Category
    context_object_name = "category"


class UserRegistrationView(FormView):
    template_name = "userreg.html"
    form_class = UserForm
    success_url = "/"

    def form_valid(self, form):
        username = form.cleaned_data["username"]
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        print(username, email, password, "######")
        User.objects.create_user(username, email, password)
        return super().form_valid(form)


class SearchView(TemplateView):
    template_name = "searchresult.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        keyword = self.request.GET.get("search")
        searchedblogs = Blog.objects.filter(
            Q(title__icontains=keyword) | Q(description__icontains=keyword))
        context["searchedblogs"] = searchedblogs
        searchednews = News.objects.filter(
            Q(title__icontains=keyword) | Q(detail__icontains=keyword))
        context["searchednews"] = searchednews

        return context

# Create your views here.
