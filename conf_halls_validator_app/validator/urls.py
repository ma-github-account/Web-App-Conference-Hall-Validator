from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'validator'
urlpatterns = [

	path('', views.conf_hall_list, name='conf_hall_list'),
	path('<int:id>/', views.conf_hall_detail, name='conf_hall_detail'),
#	path('new/', views.get_name, name='get_name'),
	path('add/', views.add, name='add')

]

if settings.DEBUG:
	
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


