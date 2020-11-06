from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView


# Display all the post list
class PostListView(ListView):
    template_name = 'blog/post_list.html'
    model = Post
    context_object_name = 'queryset'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['published_date'] = Post.objects.all().order_by('published_date')
        return context


# Show post detail
class PostDetail(DetailView):
    template_name = 'blog/post_detail.html'
    model = Post
    context_object_name = 'post'


# Add a post
class PostNew(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create'
        return context

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.published_date = timezone.now()
        form.save()
        return redirect(reverse("post_detail", kwargs={
            'pk': form.instance.pk
        }))


# Update a post
class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update'
        return context

    def form_valid(self, form):
        form.save()
        return redirect(reverse("post_detail", kwargs={
            'pk': form.instance.pk
        }))


# Delete a post
class PostDelete(DeleteView):
    model = Post
    success_url = '/'
    template_name = 'blog/post_delete.html'
