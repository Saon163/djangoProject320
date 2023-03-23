from django.urls import path

from polls import views

urlpatterns = [
    path('', views.index, name = 'index'),
]

from django.urls import path

from polls import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('2/', views.if_else, name = 'if_else'),
    ]

from django.urls import path

from polls import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('2/', views.if_else, name = 'if_else'),
    path('3/', views.for_loop, name = 'for_loop'),
    ]

from django.urls import path

from polls import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('2/', views.if_else, name = 'if_else'),
    path('3/', views.for_loop, name = 'for_loop'),
    path('4/', views.ifequal_func, name = 'ifequal_function'),
    ]