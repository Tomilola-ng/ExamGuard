from django.shortcuts import render , get_object_or_404
from posts.models import Post
from taggit.models import Tag 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count



# Create your views here.
def post_list(request, tag_slug=None):
    post_list = Post.objects.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, name=tag_slug)
        post_list = post_list.filter(tags__in=[tag])
    
    # Pagination with 3 posts per page
    paginator = Paginator(post_list, 6)
    page_number = request.GET.get('page', 1)

    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    context = {
        'objects': posts,
        'tag': tag,
    }
    
    return render(request, 'posts/post_list.html', context)


def PostDetailView(request, id):
    post =  get_object_or_404(Post, id = id)

    post.viewcount += 1
    post.save()

    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.objects.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-date')[:4]

    context = {
        'object': post,
        'similar_posts': similar_posts
    }

    return render(request, 'posts/post_detail.html', context )

