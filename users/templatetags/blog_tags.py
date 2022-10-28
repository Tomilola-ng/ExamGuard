from django import template
from posts.models import Post
from questions.models import Question
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown


register = template.Library()
@register.simple_tag
def total_posts():
    return Post.objects.count()

@register.inclusion_tag('posts/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.objects.order_by('-date')[:count]
    return {'latest_posts': latest_posts}

@register.simple_tag
def get_most_commented_posts(count=5):
    return Question.objects.annotate(total_comments=Count('answer')).order_by('-total_comments')[:count]

@register.simple_tag
def get_tags(count=5):
    return Post.tags.all()[:count]

@register.filter(name='markdown')
def markdown_format(text):
 return mark_safe(markdown.markdown(text))