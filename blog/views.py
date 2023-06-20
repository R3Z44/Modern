from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.db.models.functions import Now

# Create your views here.


def blog_view(request):
    posts = Post.objects.all().filter(status=1)
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)


def blog_single(request, pid):
    posts = Post.objects.filter(
        published_date__lte=Now(), status=1).order_by('order')
    # post_list = Post.objects.order_by('order')
    post = get_object_or_404(posts, pk=pid)
    current_index = list(posts).index(post)

    previous_post = None
    next_post = None

    if current_index > 0:
        previous_post = posts[current_index - 1]

    if current_index < len(posts) - 1:
        next_post = posts[current_index + 1]

    context = {'post': post, 'previous_post': previous_post,
               'next_post': next_post}
    post.counted_views += 1
    post.save()
    return render(request, 'blog/blog-single.html', context)
