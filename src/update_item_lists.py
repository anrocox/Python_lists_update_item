#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 2, 2014

@author: anroco

How can you change the value of an item in a python list?

¿Cómo se puede modificar el valor de un elemento en una lista python?
'''

#create a list
lista = [1, 'hello', True, 'a', 2.0]
print (lista)

#to change value of an item is used the = operator followed by the new value.
lista[1] = 'hello world'
print(lista)

#changing the value for a nested list
lista[2] = [True, False]
print(lista)
