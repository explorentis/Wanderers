# -*- coding:utf-8 -*-
# Элемент меню для WinMenu
from ..baseclass import BaseClass

class MenuElement(BaseClass):
	def __init__(self, hotkey, ptr2func, name, description, param4func={}):
		BaseClass.__init__(self, name, description)
		self.hotkey = hotkey
		self.action_ptr = ptr2func
		self.param4func = param4func
	
	def action(self):
		self.action_ptr(**self.param4func)
