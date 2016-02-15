# -*- coding:utf-8 -*-
# Элемент меню для WinMenu
from ..baseclass import BaseClass

class MenuElement(BaseClass):
	def __init__(self, hotkey, ptr2func, name, description):
		BaseClass.__init__(self, name, description)
		self.hotkey = hotkey
		self.action = ptr2func
