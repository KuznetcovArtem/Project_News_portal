from django.urls import path
from django.views.decorators.cache import cache_page

from .views import (PostList, PostDetail, PostCreate, PostEdit, PostDelete, subscriptions, CategoryListView)

urlpatterns = [
   path('', cache_page(60*1)(PostList.as_view()), name='post_list'),
   path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
   path('subscriptions/', subscriptions, name='subscriptions'),
]
