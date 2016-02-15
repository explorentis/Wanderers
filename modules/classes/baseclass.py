# -*- coding: utf-8 -*-
# Самый базовый класс, от которого будет наследоваться все остальное
class BaseClass:
	def __init__(self, name, description=''):
		self.name = name
		self.description = description
