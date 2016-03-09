#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from curses import wrapper, curs_set, newwin, doupdate
import curses

#WinMenu, WinContent, MenuElement, WinText, Scene:
from modules.classes.curses import *
from modules.methods import quit, get_want_exit, nothing, change_menu_focus

def main(stdscr):
	# Уровень приложения:
	parenty, parentx = stdscr.getmaxyx()
	if (parenty < 24) or (parentx < 80):
		stdscr.addstr('Размеры консоли слишком малы:\n они должны быть: 80х24,\n а у Вас: ' + str(parentx) + 'x' + str(parenty) + '\nНажмите любую кнопку...')
		stdscr.getch()
		return

	curs_set(False)

	# 	Инициализация цветовых пар:
	# подсветка горячих клавиш
	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
	# выделение ошибок:
	curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
	# 	.

	menu = newwin(parenty - 5, 20)
	output = newwin(parenty - 5, parentx - 20, 0, 20)
	description = newwin(5, parentx, parenty - 5, 0)
	# .
	
	# Уровень сцены:
	scene1 = Scene(
		'Главное меню', 
		'Главное меню игры, а также генерация новой игры'
	)

	scene1.add_content(
		{
			'menu':WinMenu(menu, 'Главное меню', [
					MenuElement('t', nothing, 'Обучение', 'Начать обучение основам игры'),
					MenuElement('n', nothing, 'Новая игра', 'Начать новую игру'),
					MenuElement('q', change_menu_focus, 'Выход', 'Выйти из игры Wanderers', {'self':scene1, 'newfocus':1})
			]),
		'output':WinText(output, 'Описание события'), 
		'description':WinText(description, 'Описание данного действия')
		}
		)
	
	scene1.add_content(
		{
		'menu':WinMenu(
			menu, 
			'Точно выйти?', 
			[
				MenuElement('y', quit, 'Да', 'Выйти из игры'),
				MenuElement('n', change_menu_focus, 'Нет', 'Не выходить пока', {'self':scene1, 'newfocus':0})
			]
		)
		}
		)
	
	while not get_want_exit():
		scene1.step()

wrapper(main)
