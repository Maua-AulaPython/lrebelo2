# -*- coding: cp1252 -*-
# Programa que le notas ate um numero negativo for digitado
#funcao que calcula media dos elementos de uma lista
import sys
def media_lista(a):
    s=0
    for i in a:
          s+=i
    return s/len(a)



a=[]
nota=0
while nota>=0:
  while True:
     try:
       nota=float(raw_input("Digite nova nota:"))
       break
     except:
         print "Voce nao digitou uma nota valida"
  a.append(nota)
          
print ("A media das notas �:%.2f" % (media_lista(a)))


# Nota: 1.0
# Comentario: Bom uso de funcao
