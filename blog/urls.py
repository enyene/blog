from django.urls import path
from .views import post_index,PostDetail

urlpatterns = [
    path('',post_index,name='home'),
    path('<slug:slug>/',PostDetail.as_view(),name='detail')
]