from django.shortcuts import render, get_object_or_404, redirect
from .models import Portfolio, Comment
from django.db.models import Avg
from .forms import NewBlog, CommentForm
# Create your views here.


#index.html에서 게시글 보여주는 key값 = "posts"
def index(request):
    posts = Portfolio.objects.all()  
    return render(request, 'index.html', {'posts' : posts})


def about(request):
    return render(request, 'about.html')


#list.html에서 게시글 보여주는 key값 = "posts"
def list(request):
    posts = Portfolio.objects.all()  
    return render(request, 'list.html', {'posts' : posts})


def create(request):
    if request.method == 'POST' : 
        form = NewBlog(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False) 
            post.save()
            return redirect('index')

    elif request.method == 'GET' :
        form = NewBlog()
        return render(request, 'create.html', {'form' : form})


def update(request, blog_id):
    blog = get_object_or_404(Portfolio, pk = blog_id )
    form = NewBlog(request.POST, instance = blog) 
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'create.html', {'form' : form})


def delete(request, blog_id):
    post = get_object_or_404(Portfolio, pk = blog_id ) 
    post.delete()
    return redirect('index')


#detail.html에서 평균평점 보여주는 key값 = "average"
def detail(request, blog_id):
    blog_detail = get_object_or_404(Portfolio, pk=blog_id)

    a = Comment.objects.filter(post=blog_id).aggregate(Avg('평점'))
    b = a['평점__avg']
    if b is None:
        average = 0
    else:
        average = round(b,1) 

    return render(request, 'detail.html', {'blog': blog_detail,"average":average})


def comment(request,post_id):

    pos = get_object_or_404(Portfolio, pk = post_id)
    if request.method =="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = pos
            comment.save()
            return redirect('index')
    
    else:
        form = CommentForm()
        return render(request, 'comment.html', {'form':form})


def co_update(request, post_id):
    pos = get_object_or_404(Comment, pk = post_id)
    if request.method =="POST":
        form = CommentForm(request.POST, instance=pos)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('index')
    
    else:
        form = CommentForm()
        return render(request, 'create.html', {'form':form})

def co_delete(request,post_id):
    comment = get_object_or_404(Comment, pk = post_id)
    comment.delete()
    return redirect('index')