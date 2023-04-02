from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

# (. significa que importa views da mesma directoria)

app_name = 'votacao'
urlpatterns = [
 # ex: votacao/
 path("index", views.index, name='index'),
 # ex: votacao/1
 path('<int:questao_id>', views.detalhe, name='detalhe'),
 # ex: votacao/3/resultados
 path('<int:questao_id>/resultados', views.resultados, name='resultados'),
 # ex: votacao/5/voto
 path('<int:questao_id>/voto', views.voto, name='voto'),
 # votacao/criarquestao
 path('criarquestao', views.criarquestao, name='criarquestao'),
 path('criarquestao/criar', views.criar, name='criar'),
 # ex: votacao/2/criaropcao
 path('<int:questao_id>/criaropcao', views.criaropcao, name='criaropcao'),
 path('<int:questao_id>/criaropcao/criarop', views.criarop, name='criarop'),
 path("", views.logar, name='logar'),
 path("signup", views.signup, name='signup'),
 path("profile", views.profile, name='profile'),
 path("<int:type>/<int:id>/deletar", views.deletar, name='deletar'),
 path("sair", views.sair, name='sair'),
 path('fazer_upload', views.fazer_upload , name='fazer_upload'),
 path('/login', auth_views.LoginView.as_view())
]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
