from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='blog-index'),
    path('<int:pid>', blog_single, name='blog-single')
]
