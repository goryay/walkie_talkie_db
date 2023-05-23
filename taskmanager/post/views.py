from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


@login_required
def post_list(request):
    posts = Post.objects.all()
    return render(request, "post/list.html", {'posts': posts})


@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect(post_list)
            except:
                pass
    else:
        form = PostForm()
    return render(request, 'post/create.html', {'form': form})


@login_required
def post_update(request, id):
    post = Post.objects.get(id=id)
    form = PostForm(initial={'name': post.name, 'address': post.address})
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect(post_list)
            except Exception as e:
                pass
    return render(request, 'post/update.html', {'form': form})


@login_required
def post_delete(request, id):
    post = Post.objects.get(id=id)
    try:
        post.delete()
    except:
        pass
    return redirect(post_list)
