from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import DeleteView
# Create your views here.

from .models import *

def post_in_category(request, category_slug = None):
    current_category = None
    categories = Category.objects.all()
    posts = Post.objects.filter(available_post = True) #관리자 모드에서 false하면 사용자에게 안보여짐
    if category_slug:
        current_category = get_object_or_404(Category,slug=category_slug) #카테고리가 없을경우 404페이지
        posts = posts.filter(category=current_category)
    return render(request, 'community/list.html',
    {
        'current_category':current_category,
        'categories' : categories,
        'posts':posts
    
    })

def post_detail(request,id,post_slug=None):
    post = get_object_or_404(Post,id=id,slug = post_slug)
    return render(request,'community/detail.html',
    {
        'post':post
    })

def upload(request):
    categories = Category.objects.all()
    if(request.method == 'POST'):
        post = Post()
        post.author = request.user
        post.title = request.POST['title']
        post.slug = post.title
        post.coment = request.POST['coment']
        post.header_coment = request.POST['header_coment']
        post.category_id = request.POST['category']
        post.save()
        for image in request.FILES.getlist('images'):
            photo = Photo()
            photo.post = post
            photo.image = image
            photo.save()
    
        return redirect('/'+str(post.id)+'/'+str(post.slug))
    else:
        return render(request,'community/upload.html', {
            'categories' : categories
        })

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'
    template_name = 'community/delete.html'