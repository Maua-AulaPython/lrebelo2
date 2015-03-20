# -*- coding: cp1252 -*-
# Programa que le notas ate um numero negativo for digitado
#funcao que calcula media dos elementos de uma lista
def media_lista(a):
    s=0
    for i in a:
          s+=i
    return s/len(a)


v=True
a=[]
while v:
    nota=float(raw_input("Digite nova nota:"))
    if nota >= 0:
        a.append(nota)
    else:
        v=False

print ("A media das notas é:%.2f" % (media_lista(a)))












    
    
    
