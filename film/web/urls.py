from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('seznam', views.FilmSeznamView.as_view(), name='seznam'),
    path('detail/<int:pk>', views.FilmDetailView.as_view(), name='detail'),
    path('film/create/', views.FilmCreate.as_view(), name='film-create'),
    path('film/<int:pk>/update/', views.FilmUpdate.as_view(), name='film-update'),
    path('film/<int:pk>/delete/', views.FilmDelete.as_view(), name='film-delete'),

]