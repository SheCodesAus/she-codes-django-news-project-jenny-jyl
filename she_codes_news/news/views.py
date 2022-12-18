from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


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

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')
    
    @login_required
    def get_queryset(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# @login_required(login_url='/users/login/')
# def story_login(request, pk):
    
    # return render(request, 'news/createStory.html')



#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

# @login_required(login_url="/users/login/")
# def createStory(request):
#     return render(request, 'news/createStory.html')
    
class AuthorView(generic.DetailView):
    template_name = 'news/author.html'
    model = get_user_model()
    context_object_name = 'author_list'

    # def get_queryset(self):
    #     return NewsStory.objects.all()
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['author_stories'] = NewsStory.objects.filter(author='author')
    #     return context

