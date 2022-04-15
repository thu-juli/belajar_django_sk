from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


def posts(request):
    listPost = Post.objects.all()
    context = {'listPost': listPost}

    return render(request, 'posts/posts.html', context)


def singlePost(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post': post}

    return render(request, 'posts/single-post.html', context)


def createPost(request):
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')

    context = {'form': form}
    return render(request, 'posts/create-post.html', context)
