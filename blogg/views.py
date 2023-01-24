from msilib.schema import ListView
from multiprocessing import context
from re import template
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.models import User

#sidor som skapas via funktioner

#definitionen som skapar blogg sidan i html
def hem(request): 

    innehall={'poster':Post.objects.all()}
    return render(request, 'blogg/hem.html',innehall)

class AnvandarePostlista(ListView):
    model=Post
    template_name = 'blogg/anvandare_poster.html'
    context_object_name = 'poster'
    ordering = ['-datum_skapad']
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(forfattare=user).order_by('-datum_skapad')

class Postlista(ListView):
    model=Post
    template_name = 'blogg/hem.html'
    context_object_name = 'poster'
    ordering = ['-datum_skapad']
    paginate_by = 2

class PostSida(DetailView):
    model=Post

class SkapaPost(LoginRequiredMixin, CreateView):
    model=Post
    fields=['titel','innehall']

    def form_valid(self,form):
        form.instance.forfattare=self.request.user
        return super().form_valid(form)


class UppdateraPost(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['titel','innehall']

    def form_valid(self,form):
        form.instance.forfattare=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.forfattare:
            return True
        return False


class RaderaPost(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url= '/'

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.forfattare:
            return True
        return False

def om(request):
    return render(request, 'blogg/om.html',{'titel':'Om'})