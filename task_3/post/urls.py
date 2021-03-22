from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostView.as_view(), name='post'),
    path('newpost', views.newpost, name='newpost'),
    path('<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete')
]