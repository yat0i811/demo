from django.shortcuts import render
import json
from .models import Post
from django.http import JsonResponse

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'codehack/index.html', {'posts': posts})

def post(request):
    datas = json.loads(request.body)
    context = Post(text=datas['value'])
    context.save()
    data = {
        'message': '登録完了'
    }
    return JsonResponse(
        data=data
    )