#!/usr/bin/python
# -*- coding: utf-8 -*-
# Файл с функциями для menuelement

# Для выхода из игры:
want_exit = False
def get_want_exit(**kwargs):
	global want_exit
	return want_exit

def quit(**kwargs):
	global want_exit
	want_exit = True
#.

# Смена меню
def change_menu_focus(**kwargs):
	kwargs['self'].menu_focus = kwargs['self'].menu_list[kwargs['newfocus']]
	kwargs['self'].draw()
#.

# Ничего не делает - заглушка
def nothing(**kwargs):
	pass
