# coding=utf8

class Shape:
	pass

class Boundary:
	def __init__(self, left, top, right, bottom):
		assert left <= right and top <= bottom
		self.left=left
		self.top=top
		self.right=right
		self.bottom=bottom

	def getLeft(self):
		return self.left

	def getTop(self):
		return self.top

	def getRight(self):
		return self.right

	def getBottom(self):
		return self.bottom

	def getTopLeft(self):
		return (self.left, self.top)

	def getTopRight(self):
		return (self.right, self.top)

	def getBottomLeft(self):
		return (self.left, self.bottom)

	def getBottomRight(self):
		return (self.right, self.bottom)

	def getWidth(self):
		return self.right - self.left

	def getHeight(self):
		return self.bottom - self.top

Boundary.Default = Boundary(0, 0, 256, 256)
#	def getBoundary(self):
#		return (self.left, self.top, self.right, self.bottom)

class Drawable:
	def __init__(self, boundary = Boundary.Default):
		self.boundary = boundary

	def getBoundary(self):
		return self.boundary

	def draw(self, drawSystem):
		pass

class Rectangle(Drawable):
	def __init__(self, x=0, y=0, w=0, h=0):
		super().__init__()
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

