from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
#from django.core.paginator import Paginator
from django.views.generic import (ListView, CreateView, DeleteView, UpdateView)
from .models import todo
#from .consts import ITEM_PER_PAGE

# Create your views here.
def index_view(request):
    object_list = todo.objects.all

    #paginator = Paginator(ITEM_PER_PAGE)
    #page_number = request.GET.get('page',1)
    #page_obj = paginator.page(page_number)

    return render(
        request,
        'todo/index.html',
        {'object_list': object_list}#, 'page_obj': page_obj},
    )

class ListtodoView(LoginRequiredMixin, ListView):
    template_name = 'todo/todo_list.html'
    model = todo
    #paginate_by = ITEM_PER_PAGE


class CreatetodoView(LoginRequiredMixin, CreateView):
    template_name = 'todo/todo_create.html'
    model = todo
    fields = {'title', 'text', 'category'}
    success_url = reverse_lazy('list-todo')

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)

class DeletetodoView(LoginRequiredMixin, DeleteView):
    template_name = 'todo/todo_confirm_delete.html'
    model = todo
    success_url = reverse_lazy('list-todo')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj

class UpdatetodoView(LoginRequiredMixin, UpdateView):
    template_name = 'todo/todo_update.html'
    model = todo
    fields = {'title', 'text', 'category'}
    success_url = reverse_lazy('list-todo')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj
