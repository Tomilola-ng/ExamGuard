from django.urls import path
from posts.views import PostDetailView , post_list


urlpatterns = [
    path('', post_list, name='post_list'),
    path('tag/<slug:tag_slug>', post_list, name='post_list_by_tag'),
    path('<int:id>/', PostDetailView, name='post_detail')
]
