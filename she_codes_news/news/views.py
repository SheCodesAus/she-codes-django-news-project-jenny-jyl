from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect


User = get_user_model()

class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all()[:4]
        context['all_stories'] = NewsStory.objects.all()
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(LoginRequiredMixin, generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     if not self.request.user.is_authenticated:
    #         raise qs.model.DoesNotExist
    #     qs = qs.filter(author=self.request.user)
    #     return qs

class AuthorView(generic.DetailView):
    template_name = 'news/authorDetail.html'
    model = get_user_model()
    context_object_name = 'author'

class EditPostView(LoginRequiredMixin, generic.UpdateView):
    model = NewsStory
    template_name = "news/EditPost.html"
    fields = ['title', 'pub_date', 'category', 'content', 'image']

    def get_success_url(self) -> str:
        return reverse_lazy('news:story', kwargs={"pk":self.kwargs['pk']})

    def get_queryset(self):     
        qs = super().get_queryset()
        qs = qs.filter(author=self.request.user)
        return qs

class DeletePostView(LoginRequiredMixin, generic.DeleteView):
    model = NewsStory
    template_name = "news/DeletePost.html"
    success_url = reverse_lazy('news:index')
    context_object_name = "story"

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(author=self.request.user)
        return qs

@login_required
def like(request, pk):
    news_story = get_object_or_404(NewsStory, pk=pk)
    if news_story.favourited_by.filter(username=request.user.username).exists():
        news_story.favourited_by.remove(request.user)
    else:
        news_story.favourited_by.add(request.user)
    return redirect(reverse_lazy('news:story', kwargs={'pk': pk}))