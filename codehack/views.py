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
    value = request.POST.get('value', None)
    if value is not None:
      try:
        # データを処理します（例：データベースに保存するなど）
        context = Post(fields={'value': value})
        context.save()
        return JsonResponse({'status': 'success', 'value': value})
      except ValueError:
        return JsonResponse({'status': 'error', 'message': 'Invalid integer value'})
    else:
      return JsonResponse({'status': 'error', 'message': 'Value not provided'})
  else:
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})