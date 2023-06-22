from django import template
from blog.models import Post

register = template.Library()


@register.inclusion_tag('blog/blog-recent-posts.html')
def recentposts(arg=3):
    posts = Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts': posts}
