from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main page'),
    path('/', views.main),
    path('news/', views.MoreNews),
    path('news/<int:id>', views.NewsDetail),
    path('story/', views.MoreStorys),
    path('story/<int:id>', views.StoryDetail),
    path('staff&cast/', views.StaffCast),
    path('trailers/<int:id>', views.TrailerDetail),
    path('trailers/', views.MoreTrailers),
    path('music/<int:id>', views.MusicDetail),
    path('Goods/<int:id>', views.GoodsDetail),
    path('Goods/', views.MoreGoods),
    path('contact/', views.add_contact, name='add_contact'),
    
    path('testing/', views.testing, name='testing'),
]