from django.urls import path

from . import views

urlpatterns = [
    path('', views.TimeLineListView.as_view(), name='oracion_timeline'),
    path('list', views.OracionListView.as_view(), name='oracion_list'),
    path('<int:pk>', views.OracionDetailView.as_view(), name='oracion_detail'),
    path('<int:pk>/', views.OracionUpdate.as_view(), name='oracion_update'),
    path('add/', views.OracionCreate.as_view(), name='oracion_add'),

]
