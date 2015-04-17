
    
from Classes import Aluno

a=Aluno("Aluno 1",23)
a.add_nota('Trabalho 1',4.0)
a.add_nota('Trabalho 2',3.5)
a.add_nota('Prova',2.0)

if a.aprovado():
    print "Media: %s - %2.2f - Aprovado" %(a.nome,a.media())
else:
    print "Media: %s - %2.2f - Reprovado" %(a.nome,a.media())
    
a.mostra_notas()

