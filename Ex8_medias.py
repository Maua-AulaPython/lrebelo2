# -*- coding: cp1252 -*-
# Programa que le notas ate um numero negativo for digitado
#funcao que calcula media dos elementos de uma lista
import sys
def media_lista(a):
    s=0
    for i in a:
          s+=i
    if len(a)>0:
        return s/len(a)
    else:
        return 0



a=[]
nota=0
while nota!=-1:
  while True:
     try:
       nota=float(raw_input("Digite nova nota:"))
       if nota>10:
           raise Exception('erro')
       break
     except:
         print "Voce nao digitou uma nota valida"

  a.append(nota)
  
a.remove(-1)
b=a[:]
b.sort()
print ("A media das notas é:%.2f" % (media_lista(a)))
print ("A maior nota é:%.2f" % b[-1])

#Nota: 1.0
#Comentario: Bom uso de funcao, bom teste se nota maior que 10.
