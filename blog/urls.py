from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('delete/<int:blog_id>',views.delete, name='delete'),
    path('update/<int:blog_id>',views.update, name='update'),
    path('blog/<int:blog_id>', views.detail, name='detail'),
    path('about/', views.about, name='about'),
    path('list/', views.list, name='list'),
    
    path('comment/<int:post_id>', views.comment, name='comment'),
    path('co_update/<int:post_id>', views.co_update, name='co_update'),
    path('co_delete/<int:post_id>', views.co_delete, name='co_delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)