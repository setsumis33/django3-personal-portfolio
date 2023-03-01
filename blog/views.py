from django.shortcuts import render, get_object_or_404
# импортируем данные из базы
from .models import Blog
def all_blog(request):
    blogs = Blog.objects.order_by('-date')[:5] # сортирует посты по времени, и отображает только 5 постов, Blog.object.all() выводит все
    return render(request,'blog/all_blogs.html',{'blogs':blogs})

def detail(request, blog_id): # переносит на страницу с id который указан, в противном случае выдает ошибку 404
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html',{'blog':blog})
