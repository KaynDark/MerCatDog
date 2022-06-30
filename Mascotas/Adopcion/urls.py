from django.urls import path
# from django.conf.urls import url
from django.urls import include, re_path
from django.conf import settings
from django.conf.urls.static import static
# from .views import DuenoList, DuenoCreate, DuenoDelete #,DuenoUpdate
from .views import DuenoCreate, DuenoList, DuenoDelete
from rest_framework.urlpatterns import format_suffix_patterns
from .views import API_objects, API_objects_details

urlpatterns = [
    path('api/', API_objects.as_view()),
    path('api/<int:pk>/', API_objects_details.as_view()),
]

urlpatterns += format_suffix_patterns(urlpatterns)

urlpatterns = [
    path('list/', DuenoList.as_view(), name="dueño_list"),

    path('crear/', DuenoCreate.as_view(), name="dueño_form"),

    # path('editar/<int:pk>', DuenoUpdate.as_view(), name="editar_dueño"),
    
    path('borrar/<int:pk>', DuenoDelete.as_view(), name="borrar_dueño"),
]
