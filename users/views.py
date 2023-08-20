from .forms import PostForm
from .forms import ImageUploadForm, UserRegistrationForm
from .models import Image, Post
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm


def home(request):
    posts = Post.objects.all().order_by('-created_at')  # Fetch all posts, ordered by the latest
    return render(request, 'users/home.html', {'title': 'Home', 'posts': posts})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)

def about(request):
    return render(request, 'users/about.html', {'title': 'About'})




def kids(request):
    form_errors = None
    if request.method == 'POST' and request.user.is_authenticated:
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                image = form.save(commit=False)
                image.user = request.user
                image.save()
                return redirect('kids')
            except Exception as e:
                logger.error(f"Error saving image: {e}")
                form_errors = str(e)
        else:
            form_errors = form.errors
    else:
        form = ImageUploadForm()
    images = Image.objects.filter(image_type='kids')
    return render(request, 'users/kids.html', {'title': 'Kids', 'images': images, 'form': form, 'form_errors': form_errors})
def men(request):
    if request.method == 'POST' and request.user.is_authenticated:
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            return redirect('men')
    else:
        form = ImageUploadForm()
    images = Image.objects.filter(image_type='men')
    return render(request, 'users/men.html', {'title': 'Men', 'images': images, 'form': form})





def women(request):
    if request.method == 'POST' and request.user.is_authenticated:
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            return redirect('women')
    else:
        form = ImageUploadForm()
    images = Image.objects.filter(image_type='women')
    return render(request, 'users/women.html', {'title': 'Women', 'images': images, 'form': form})




def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Post added successfully!')
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'users/post.html', {'title': 'Post', 'form': form})


def profile(request):
    return render(request, 'users/profile.html', {'title': 'Profile'})

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('list_posts')
    else:
        form = PostForm()
    return render(request, 'users/add_post.html', {'form': form})

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('list_posts')
    else:
        form = PostForm()
    return render(request, 'users/add_post.html', {'form': form})

def list_posts(request):
    posts = Post.objects.filter(user=request.user)
    return render(request, 'users/list_posts.html', {'posts': posts})


def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('list_posts')
    else:
        form = PostForm(instance=post)
    return render(request, 'users/edit_post.html', {'form': form})

    post = get_object_or_404(Post, id=post_id, user=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('list_posts')
    else:
        form = PostForm(instance=post)
    return render(request, 'users/edit_post.html', {'form': form})

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('list_posts')
    return render(request, 'users/delete_post.html', {'post': post})

def delete_post(request, post_id):
    # Ensure the user is authenticated
    if not request.user.is_authenticated:
        return redirect('login')
    
    # Fetch the post by ID
    post = get_object_or_404(Post, id=post_id)

    # Ensure the logged-in user is the owner of the post
    if request.user == post.author:
        post.delete()
        messages.success(request, 'Post deleted successfully!')
    else:
        messages.error(request, 'You do not have permission to delete this post.')

    return redirect('home')
