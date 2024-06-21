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
  if request.method == 'POST':
    value01 = request.POST.get('value01', None)
    value02 = request.POST.get('value02', None)
    if value01 is not None and value02 is not None:
      try:
        value01 = int(value01)  # 文字列を整数に変換します
        value02 = int(value02)  # 文字列を整数に変換します
        # データを処理します（例：データベースに保存するなど）
        context = Post(fields={'value01': value01, 'value02': value02})
        context.save()
        return JsonResponse({'status': 'success', 'value01': value01, 'value02': value02})
      except ValueError:
        return JsonResponse({'status': 'error', 'message': 'Invalid integer value'})
    else:
      return JsonResponse({'status': 'error', 'message': 'Value not provided'})
  else:
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})