# -*- coding: utf-8 -*-
# Реализация вывода текста на окна
from curses import color_pair

from .wincontent import WinContent

class WinText(WinContent):
	def __init__(self, targeted_window, name, description=''):
		WinContent.__init__(self, targeted_window, name, description)
		self.text = ''

	def new_text(self, text):
		self.text = text

	def draw(self):
		WinContent.draw(self)
		line_total = int(len(self.text) / (self.winwidth - 2))
		if line_total > (self.winheight - 3):
			line_total = self.winheight - 3
			self.window.addstr(self.winheight - 1, 1, 'весь текст не ушел', color_pair(2))
		for line_num in range(0, line_total + 1):
			self.window.addstr(1 + line_num, 1, self.text[line_num * (self.winwidth - 2):(line_num + 1) * (self.winwidth - 2)])
		self.window.noutrefresh()
