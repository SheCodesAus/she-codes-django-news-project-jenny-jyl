from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(),name='newStory'),
    path('author/<int:pk>/', views.AuthorView.as_view(), name='author'),
    path('edit_post/<int:pk>/', views.EditPostView.as_view(), name='editPost'),
    path('delete_post/<int:pk>/', views.DeletePostView.as_view(), name='deletePost'),
    path('<int:pk>/like/', views.like, name='like'),
]


