from django.shortcuts import render
from newspaper.models import Post
from django.views.generic import ListView,DeleteView,UpdateView,CreateView
from django.urls import reverse_lazy
from .forms import PostUpdateForm,PostCreateForm
# Create your views here.



class DashboardView(ListView):
    model = Post
    template_name = "dashboard/dashboard.html" 
    context_object_name = "posts"      


class PostDeleteView(DeleteView):
    model = Post

    def get_success_url(self):
        return reverse_lazy("dashboard:dashboard")
    


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'dashboard/post_update.html'
    success_url = reverse_lazy('dashboard:dashboard')
    context_object_name = 'post'



class PostAddView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'dashboard/post_add.html'
    success_url = reverse_lazy('dashboard:dashboard')

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)