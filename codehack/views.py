from django.shortcuts import render
import json
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'codehack/index.html', {'posts': posts})

def post(request):
    datas = json.loads(request.body)
    context = Post(fields=datas)
    context.save()
    return render(request, 'codehack/post.html')