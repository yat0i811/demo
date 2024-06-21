from django.shortcuts import render
from .models import Post
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'codehack/index.html', {'posts': posts})

@csrf_exempt
def post(request):
  print(request.method)
  if request.method == 'POST':
    key = request.POST.get('key', None)
    if key is not None:
      try:
        key = int(key)  # 文字列を整数に変換します
        # データを処理します（例：データベースに保存するなど）
        context = Post(text=key)
        context.save()
        return JsonResponse({'status': 'success', 'key': key})
      except ValueError:
        return JsonResponse({'status': 'error', 'message': 'Invalid integer value'})
    else:
      return JsonResponse({'status': 'error', 'message': 'Key not provided'})
  else:
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})