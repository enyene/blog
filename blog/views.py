from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Post
from django.views.generic import DetailView

# Create your views here.
def post_index(request):
    entry = Post.objects.all()
    context = {
        'entry':entry
    }
    return render(request,'blog/index.html',context)

class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'