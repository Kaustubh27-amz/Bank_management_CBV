from django.urls import path
from . import views

urlpatterns=[
   path('',views.index.as_view()),
   path('about/',views.about.as_view(),name='about'),
   path('account_list/',views.users_list.as_view(),name='account_list'),
   path('account_detail/<int:pk>/',views.users_detail.as_view(),name='account_detail'),
   path('account_form/',views.users_create.as_view(),name='account_form'),
   path('account_update/<int:pk>/',views.users_update.as_view(),name='account_update'),
   path('account_delete/<int:pk>/',views.users_delete.as_view(),name='account_delete'),
   path('deposit/<int:pk>/',views.deposit,name='deposit'),
   path('withdraw/<int:pk>/',views.withdraw,name='withdraw'),
]
