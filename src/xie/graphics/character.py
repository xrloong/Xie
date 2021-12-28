from .shape import Shape
from .component import Component
from . import DrawingSystem

class Character(Shape):
	def __init__(self, name, component: Component, tag=None):
		self.name = name
		self.component = component
		self.tag = tag

	def getName(self):
		return self.name

	def getComponent(self):
		return self.component

	def getTag(self):
		return self.tag

	def draw(self, drawingSystem: DrawingSystem):
		character=self

		drawingSystem.clear()
		drawingSystem.onPreDrawCharacter(character)
		drawingSystem.draw(character.getComponent())
		drawingSystem.onPostDrawCharacter(character)

