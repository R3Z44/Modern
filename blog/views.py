from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Comment
from django.db.models.functions import Now
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.forms import CommentForm
from django.contrib import messages

# Create your views here.


def blog_view(request, **kwargs):

    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name') != None:
        lowercase_cat_name = kwargs['cat_name'].lower()
        posts = posts.filter(category__name__iexact=lowercase_cat_name)
    if kwargs.get('author_username') != None:
        lowercase_author_username = kwargs['author_username'].lower()
        posts = posts.filter(
            author__username__iexact=lowercase_author_username)
    if kwargs.get('tag_name') != None:
        lowercase_tag_name = kwargs['tag_name'].lower()
        posts = posts.filter(
            tags__name__iexact=lowercase_tag_name)
    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)


def blog_single(request, pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Your comment has been received successfully!!!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Your comment didn\'t received!!!')
    posts = Post.objects.filter(
        published_date__lte=Now(), status=1).order_by('order')
    post = get_object_or_404(posts, pk=pid)
    if not post.login_require:
        current_index = list(posts).index(post)

        previous_post = None
        next_post = None

        if current_index > 0:
            previous_post = posts[current_index - 1]

        if current_index < len(posts) - 1:
            next_post = posts[current_index + 1]

        comments = Comment.objects.filter(
            post=post.id, approved=True)

        form = CommentForm()
        context = {'post': post, 'comments': comments, 'form': form, 'previous_post': previous_post,
                   'next_post': next_post}
        post.counted_views += 1
        post.save()
        return render(request, 'blog/blog-single.html', context)
    else:
        return redirect('/accounts/login')


def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        # request.GET.get('s')
        posts = posts.filter(content__contains=request.GET.get(
            's')) or posts.filter(title__contains=request.GET.get('s'))
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)
