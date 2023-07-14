

from .import views
from django.urls import path,include

urlpatterns = [
   path('listeImage',views.imageList , name='annonce123'),
   path('createimage',views.CreateImage),
   path('findimage/<int:pk>/',views.find_image ),
   path('search/', views.tagsSearch.as_view(),name='search'),
 
]