# -*- coding: utf-8 -*-
# Этот класс контролирует показываемое на экране содержимое, это базовый класс для всех классов, относящихся к окнам
from ..baseclass import BaseClass

class WinContent(BaseClass):
	def __init__(self, targeted_window, name, description=''):
		BaseClass.__init__(self, name, description)
		self.window = targeted_window
		self.current_scene = None
		self.winheight, self.winwidth = targeted_window.getmaxyx()

	def draw(self):
		self.window.erase()
		self.window.border()
		self.window.addstr(0, 1, self.name)
		self.window.noutrefresh()

