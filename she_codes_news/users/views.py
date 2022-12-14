from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from news.models import NewsStory
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect



class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class ProfileView(generic.DetailView):
    template_name = 'users/profile.html'
    model = get_user_model()
    context_object_name = 'profile_details'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    # def get_queryset(self):
    #     return NewsStory.objects.filter(author=self.request.user)
 
    # def get_queryset(self):
    #     list = super().get_queryset()  
    #     list = list.filter(author_id=self.kwargs['pk'])
    #     return list

# @ login_required
# def like_click(request, pk):
#     story = get_object_or_404(NewsStory, pk=pk)
#     if story.likedPost.filter(id=request.user.id).exists():
#         story.likedPost.remove(request.user)
#     else:
#         story.likedPost.add(request.user)
#     return redirect('news:story', pk=story.id)
   

