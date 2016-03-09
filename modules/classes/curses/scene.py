#!/usr/bin/python
# -*- coding: utf-8 -*-
# Класс, позволяющий взаимодействовать контенту друг с другом
from ..baseclass import BaseClass
from curses import doupdate
class Scene(BaseClass):
	def __init__(self, name, description='', content_list={}):
		BaseClass.__init__(self, name, description)
		self.menu_list = []
		self.description = None
		self.output_list = []
		self.menu_focus = None
		self.output_focus = None
		self.add_content(content_list)
		doupdate()

	
	def add_content(self, content_list):
		if 'menu' in content_list:
			self.menu_list.append(content_list['menu'])
			if self.menu_focus is None:
				self.menu_focus = self.menu_list[0]
			self.menu_focus.draw()
		if 'output' in content_list:
			self.output_list.append(content_list['output'])
			if self.output_focus is None:
				self.output_focus = self.output_list[0]
			self.output_focus.draw()
		if 'description' in content_list:
			self.description = content_list['description']
			self.description.new_text(
				self.menu_focus.menu[self.menu_focus.choice].descr
			)
			self.description.draw()

		for element in content_list.values():
			element.current_scene = self

	def draw(self):
		self.menu_focus.draw()
		self.output_focus.draw()
		self.description.draw()
		doupdate()
	
	def step(self):
		self.menu_focus.proc_presskey()
		doupdate()

