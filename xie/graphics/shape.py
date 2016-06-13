# coding=utf8

class Shape:
	def draw(self, drawSystem):
		pass

class Rectangle(Shape):
	def __init__(self, x=0, y=0, w=0, h=0):
		self.x=x
		self.y=y
		self.w=w
		self.h=h

	def setGeometry(self, x, y, w, h):
		[self.x, self.y, self.w, self.h,]=[x, y, w, h,]

	def getGeometry(self):
		return [self.x, self.y, self.w, self.h,]

	def __str__(self):
		return "(%s, %s, %s, %s)"%(self.x, self.y, self.w, self.h,)

	def draw(self, drawSystem):
		drawSystem.startDrawing((0, 0))
		drawSystem.lineTo((self.w, 0))
		drawSystem.lineTo((0, self.h))
		drawSystem.lineTo((-self.w, 0))
		drawSystem.lineTo((0, -self.h))
		drawSystem.endDrawing()

