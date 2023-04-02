from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Questao, Opcao, Aluno
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Permission
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required


@login_required(login_url='/votacao/')
def index(request):
    latest_question_list = Questao.objects.order_by('-pub_data')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'votacao/index.html', context)

@login_required(login_url='/votacao/')
def detalhe(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'votacao/detalhe.html', {'questao': questao})

@login_required(login_url='/votacao/')
def voto(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)

    try:
        opcao_seleccionada = questao.opcao_set.get(pk=request.POST['opcao'])
    except (KeyError, Opcao.DoesNotExist):
        # Apresenta de novo o form para votar
        return render(request, 'votacao/detalhe.html', {
            'questao': questao,
            'error_message': "Não escolheu uma opção",
    })
    else:
        if not request.user.is_staff:
            if request.user.aluno.votos < request.user.aluno.votosmax:
                a = request.user.aluno
                a.votos += 1
                a.save()
            else:
                return render(request, 'votacao/detalhe.html', {
                    'questao': questao,
                    'error_message': "Não tem mais votos",
                })
        opcao_seleccionada.votos += 1
        opcao_seleccionada.save()

    # Retorne sempre HttpResponseRedirect depois de
    # tratar os dados POST de um form
    # pois isso impede os dados de serem tratados
    # repetidamente se o utilizador
    # voltar para a página web anterior.
    return HttpResponseRedirect(
        reverse('votacao:resultados',
                args=(questao.id,)))



@login_required(login_url='/votacao/')
def resultados(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'votacao/resultados.html', {'questao': questao})

@permission_required('votacao.add_questao',login_url='/votacao/')
def criarquestao(request):
    return render(request, 'votacao/criarquestao.html')

@permission_required('votacao.add_questao',login_url='/votacao/')
def criar(request):
    print("Lets go")
    texto = request.POST['questao']
    print("texto " + texto)
    if(texto):
        q = Questao(questao_texto=texto, pub_data=timezone.now())
        q.save()
        return HttpResponseRedirect(reverse('votacao:index'))
    else:
        return render(request, 'votacao/criarquestao.html', {
            'error_message': "Não inseriu texto",
        })


@permission_required('votacao.add_opcao',login_url='/votacao/')
def criaropcao(request,questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'votacao/criaropcao.html',{'questao': questao})

@permission_required('votacao.add_opcao',login_url='/votacao/')
def criarop(request,questao_id):
    q = get_object_or_404(Questao, pk=questao_id)
    texto = request.POST['opcao']
    if(texto):
        q.opcao_set.create(opcao_texto=texto,votos=0)
        q.save()
        return HttpResponseRedirect(reverse('votacao:index'))
    else:
        return render(request, 'votacao/criaropcao.html', {
            'error_message': "Não inseriu texto",
        })


def signup(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        curso = request.POST['curso']
        u = User.objects.create_user(username, email, password)
        a = Aluno(user=u, curso=curso)
        a.votosmax=int(curso[-2:]) + 10
        a.save()
        login(request, u)
        return HttpResponseRedirect(reverse('votacao:index'))
        #return render(request, 'votacao/index.html')
    else:
        return render(request, 'votacao/signup.html')


def logar(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('votacao:index'))
        else:
            return render(request, 'votacao/login.html')
    else:
        return render(request, 'votacao/login.html')


@login_required(login_url='/votacao/')
def profile(request):
    return render(request, 'votacao/profile.html')


@login_required(login_url='/votacao/')
def sair(request):
    request.session.flush
    logout(request)
    return HttpResponseRedirect(reverse('votacao:logar'))
#1 for question, 2 for option


@permission_required('votacao.delete_opcao',login_url='/votacao/')
@permission_required('votacao.delete_questao',login_url='/votacao/')
def deletar(request, type, id):
    if type==1:
        questao = get_object_or_404(Questao, pk=id)
        questao.delete()
        return HttpResponseRedirect(reverse('votacao:index'))
    else:
        opcao = get_object_or_404(Opcao, pk=id)
        questao = opcao.questao
        opcao.delete()
        return HttpResponseRedirect(reverse('votacao:detalhe', args=(questao.id,)))



@login_required(login_url='/votacao/')
def fazer_upload(request):
    if request.method == 'POST' and request.FILES.get('myfile') is not None:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url =fs.url(filename)
        a = request.user.aluno
        a.imagem = "media/" + filename
        a.save()
        return render(request , 'votacao/fazer_upload.html', {'uploaded_file_url':uploaded_file_url})
    return render(request ,'votacao/fazer_upload.html')






