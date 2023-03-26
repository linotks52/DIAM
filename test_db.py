from votacao.models import Questao, Opcao
from django.db.models import Sum


q = Opcao.objects.values('votos')
c = Opcao.objects.aggregate(Sum('votos'))

print(q)
print(c)


q = Questao.objects.all()
for i in q:
    c = i.questao_texto
    d = i.opcao_set.all()
    z = ''
    for i in d:
        max = -1
        if i.votos > max:
            z = i.opcao_texto
    print(c)
    print(z)

