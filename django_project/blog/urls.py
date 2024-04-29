from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreatelView

urlpatterns = [
    path('',PostListView.as_view(),name='blog-home'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/create/',PostCreatelView.as_view(),name='post-create'),
    path('about/',views.about,name='blog-about'),

]