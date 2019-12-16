from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.market, name="market"),
    path('<int:market_id>', views.detail, name="detail"),
    path('new', views.new, name="new"),
    path('market_serach', views.market_search, name="market_search"),
    path('create', views.create, name="create"),
    path('delete/<int:market_id>',views.delete, name="delete"),
    path('menu/create/<int:market_id>', views.menu_create,name="menu_create"),
    path('like/<int:market_id>',views.post_like, name="post_like"), 
    path('menu/<int:market_id>',views.menu_order, name="menu_order"),# 즐겨찾기 위한 url
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
