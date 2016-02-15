#!/usr/bin/python
# -*- coding: utf-8 -*-
# Файл с функциями для menuelement

# Для выхода из игры:
want_exit = False
def get_want_exit():
	global want_exit
	return want_exit

def quit():
	global want_exit
	want_exit = True
#.

# Ничего не делает - заглушка
def nothing():
	pass
