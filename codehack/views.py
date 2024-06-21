from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'codehack/index.html', {'posts': posts})

def post(request):
    context = Post(fields=request.POST['data'])
    context.save()
    return render(request, 'codehack/post.html')