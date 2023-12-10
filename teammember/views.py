from .models import Teammember
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
class IndexView(ListView):
    model = Teammember
    template_name = 'teammember/index.html'
    context_object_name = 'index'

class SingleView(DetailView):
    model = Teammember
    template_name = 'teammember/single.html'
    context_object_name = 'post'

class PostsView(ListView):
    model = Teammember
    template_name = 'teammember/posts.html'
    context_object_name = 'teammember_list'

class AddView(CreateView):
    model = Teammember
    template_name = 'teammember/add.html'
    fields = '__all__'
    success_url = reverse_lazy('teammember:posts')

class EditView(UpdateView):
    model = Teammember
    template_name = 'teammember/edit.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('teammember:posts')

class Delete(DeleteView):
    model = Teammember
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('teammember:posts')
    template_name = 'teammember/confirm-delete.html'