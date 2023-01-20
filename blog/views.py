from django.shortcuts import render,get_object_or_404 
from .models import blog

# Create your views here.
def home_blog(request):
    blogs = blog.objects.order_by('-date')
    return render(request,'blog/home_blog.html',{'blogs':blogs})

def detail(request, blog_id):
    blogs = get_object_or_404(blog, pk=blog_id)
    return render(request,'blog/detail.html',{'blog':blogs})