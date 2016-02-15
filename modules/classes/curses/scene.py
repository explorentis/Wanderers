#!/usr/bin/python
# -*- coding: utf-8 -*-
# Класс, позволяющий взаимодействовать контенту друг с другом
from ..baseclass import BaseClass
from curses import doupdate
class Scene(BaseClass):
	def __init__(self, name, description='', content_list={}):
		BaseClass.__init__(self, name, description)
		self.conlist = {}
		self.add_content(content_list)
		self.conlist['description'].new_text(
				self.conlist['menu'].menu[self.conlist['menu'].choice].description
		)
		for content in self.conlist:
			self.conlist[content].draw()
		doupdate()

	
	def add_content(self, content_list):
		self.conlist = content_list
		for element in content_list.values():
			element.current_scene = self

	def step(self):
		self.conlist['menu'].proc_presskey()
		doupdate()

