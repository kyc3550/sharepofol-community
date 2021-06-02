from django.urls import path
from .views import *

app_name = 'community'
urlpatterns = [
    path('',post_in_category, name='post_all'),
    path('<slug:category_slug>/',post_in_category,name='post_in_category'),
    path('<int:id>/<post_slug>',post_detail,name='post_detail') #slug: 를 안넣어도 같은동작을 실행
]