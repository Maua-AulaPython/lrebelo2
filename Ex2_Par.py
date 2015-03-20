# -*- coding: cp1252 -*-

def is_even():
    x=int(raw_input("Digite o numero para verificar se é par:"))%2
    if x==0:
        print "O numero digitado é par!"
    else:
        print "O numero digitado não é par!"
is_even()
