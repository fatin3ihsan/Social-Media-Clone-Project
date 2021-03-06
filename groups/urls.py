from django.urls import path
from groups import  views

app_name='groups'

urlpatterns=[
    path('',views.GroupList.as_view(),name='all'),
    path('new/',views.CreateGroup.as_view(),name='create'),
    path('posts/<slug:slug>',views.SingleGroup.as_view(),name='single')
]
