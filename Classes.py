class Pessoa():
    nome="Nome da Pessoa"
    idade= 100
    profissao = None
    def __init__(self,nome,idade):
         self.nome= nome
         self.idade = idade
    def set_profissao(self,profissao):
        self.profissao =profissao


class Professor(Pessoa):
    profissao = "Professor"
    salario =0

    def set_salario(self,valor):
           self.salario=valor


class Aluno(Pessoa):
     def __init__(self,nome,idade):
         Pessoa.__init__(self,nome,idade)
         self.notas={}
     def add_nota(self,key,valor):
         self.notas[key]=valor
     def media(self):
         soma=0
         for i,j in self.notas.iteritems():
              soma=soma+j
         media = soma / len(self.notas)
         return media
     def aprovado(self):
         if self.media()>=5.0:
             return True
         else:
             return False
     def mostra_notas(self):
         for k,v in self.notas.iteritems():
             print k+":",v
        
     
