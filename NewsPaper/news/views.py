from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

from .filters import PostsFilter
from .forms import PostForm
from .models import Post


class PostsList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'news/posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_news'] = Post.objects.all()
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'news/post.html'
    context_object_name = 'post'


class PostsSearch(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'news/search.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['all_news'] = self.filterset.qs
        return context


class NewsCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    raise_exception = True
    permission_required = ('news.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'news/news_create.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.categories = 'NW'
        return super().form_valid(form)


class ArticleCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    raise_exception = True
    permission_required = ('news.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'news/article_create.html'

    def form_valid(self, form):
        article = form.save(commit=False)
        article.categories = 'AR'
        return super().form_valid(form)


class NewsUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    raise_exception = True
    permission_required = ('news.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'news/news_update.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.categories = 'NW'
        return super().form_valid(form)


class ArticleUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    raise_exception = True
    permission_required = ('news.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'news/article_update.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.categories = 'AR'
        return super().form_valid(form)


class NewsDelete(LoginRequiredMixin, DeleteView):
    raise_exception = True
    model = Post
    template_name = 'news/news_delete.html'
    success_url = reverse_lazy('posts_list')


class ArticleDelete(LoginRequiredMixin, DeleteView):
    raise_exception = True
    model = Post
    template_name = 'news/article_delete.html'
    success_url = reverse_lazy('posts_list')
