# Importamos a função index() definida no arquivo views.py
from . import views

app_name = 'website'

# urlpatterns a lista de roteamentos de URLs para funoes/Views
urlpatters = [
	# GET /
	url(r'^$', views.index, name='index'),
]