# -*- coding: cp1252 -*-

def is_even():
    x=int(raw_input("Digite o numero para verificar se � par:"))%2
    if x==0:
        print "O numero digitado � par!"
    else:
        print "O numero digitado n�o � par!"
is_even()
