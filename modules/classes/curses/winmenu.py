# -*- coding: utf-8 -*-
# Это класс реализующий меню в curses
from .wincontent import WinContent

import curses

class WinMenu(WinContent):
	def __init__(self, targeted_window, name, menu_elements=[], description=''):
		WinContent.__init__(self, targeted_window, name, description)
		targeted_window.keypad(True)
		self.choice = 0
		self.page = int(self.choice / self.winheight) + 1
		self.menu = []
		self.add_menu(menu_elements)
	
	# menu_elements - список элементов MenuElement
	def add_menu(self, menu_elements):
		for element in menu_elements:
			self.menu.append(element)
		self.hotkey_assign = {}
		for element in menu_elements:
			self.hotkey_assign[element.hotkey] = element

	def draw_element(self, line, element, is_selected=False):
		self.window.hline(line, 1, ' ', self.winwidth - 3)
		if is_selected:
			self.window.addstr(line, 1, element.name, curses.A_REVERSE)
			self.window.addstr(line, self.winwidth - 2, element.hotkey, curses.A_REVERSE | curses.color_pair(1))
		else:
			self.window.addstr(line, 1, element.name)
			self.window.addstr(line, self.winwidth - 2, element.hotkey, curses.color_pair(1))

	def draw_page(self, first_element_num, last_element_num, selected_num):
		line = 0
		if last_element_num > len(self.menu):
			last_element_num = len(self.menu)
		for i in range(first_element_num, last_element_num):
			line += 1
			if selected_num == i:
				self.draw_element(line, self.menu[i], True)
			else:
				self.draw_element(line, self.menu[i], False)

	# Сначала была отрисовка только изменившихся элементов, но это сильно усложнило восприятие мной кода, так что нафиг. Заниматься, если только покоя мне это давать не будет
	def draw(self):
		WinContent.draw(self)
		if len(self.menu) > (self.winheight - 3):
			self.window.addstr(self.winheight - 1, self.winwidth - 4, 'Ещё', curses.A_BOLD)
		self.draw_page(
						int(self.choice / (self.winwidth - 3)) * (self.winwidth - 3),
						(1 + int(self.choice / (self.winwidth - 3))) * (self.winwidth - 3),
						self.choice
		)

	def proc_presskey(self):
		key = self.window.getch()
		if key == curses.KEY_DOWN:
			self.choice += 1
			if self.choice > len(self.menu) - 1:
				self.choice = 0
			self.draw()
			self.current_scene.description.new_text(self.menu[self.choice].descr)
			self.current_scene.description.draw()

		elif key == curses.KEY_UP:
			self.choice -= 1
			if self.choice == -1:
				self.choice = len(self.menu) - 1
			self.draw()
			self.current_scene.description.new_text(self.menu[self.choice].descr)
			self.current_scene.description.draw()

		elif key == 10:
			# нажатие клавиши ENTER, т.к. curses'овское определение не сработало
			self.menu[self.choice].action()

		elif curses.keyname(key).decode('utf-8') in self.hotkey_assign:
			self.hotkey_assign[curses.keyname(key).decode('utf-8')].action()
