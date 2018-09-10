from django import template
from django.utils.safestring import mark_safe
import markdown
from django.shortcuts import get_object_or_404

from ams.models import Billing

register = template.Library()


#
# @register.simple_tag
# def total_posts():
#     return Post.published.count()
#
#
# @register.simple_tag
# def total_posts_pluralize():
#     s = ''
#     if Post.objects.count() > 1:
#         s = 's'
#     return s
#
#
# @register.inclusion_tag('blog/post/latest_posts.html')
# def show_latest_posts(count=5):
#     # latest_posts = Post.published.order_by('-publish')[:count]
#     latest_posts = Post.published.order_by('-publish')[:count]
#     return {'latest_posts': latest_posts}
#
#
# @register.simple_tag
# def get_most_commented_posts(count=5):
#     return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]

@register.filter
# @register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


# @register.inclusion_tag('blog/post/latest_posts.html',name='show_latest_post_pb_test')
# def show_latest_posts_pb(count=5):
#     latest_posts = Post.published.order_by('-publish')[:count]
#     content = {'latest_posts':latest_posts}
#
#     return content

@register.inclusion_tag('ams/payment_tag.html')
def display_tenant_bill_data(rmno):
    tenant_bill = get_object_or_404(Billing, room_no=rmno, status='open')

    return {'tenant_bill': tenant_bill}
