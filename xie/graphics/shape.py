# coding=utf8
import numpy

class Shape:
	def draw(self, drawSystem):
		pass

class Pane:
	def __init__(self, left, top, right, bottom):
		self.left=left
		self.top=top
		self.right=right
		self.bottom=bottom

	def __str__(self):
		return "%s"%(self.left, self.top, self.right, self.bottom)

	def __eq__(self, other):
		return isinstance(other, Pane) and all(numpy.isclose(self.boundary, other.boundary))

	def __ne__(self, other):
		return not self.__eq__(other)

	def clone(self):
		return Pane(self.left, self.top, self.right, self.bottom)

	@property
	def width(self):
		return self.right-self.left

	@property
	def height(self):
		return self.bottom-self.top

	@property
	def centerX(self):
		return self.left + self.width / 2

	@property
	def centerY(self):
		return self.top + self.height / 2

	@property
	def center(self):
		return (self.centerX, self.centerY)

	@property
	def leftTop(self):
		return (self.left, self.top)

	@property
	def rightBottom(self):
		return (self.right, self.bottom)

	@property
	def boundary(self):
		return (self.left, self.top, self.right, self.bottom)

	def _offsetLeftAndRight(self, offset):
		self.left += offset
		self.right += offset

	def _offsetTopAndBottom(self, offset):
		self.top += offset
		self.bottom += offset

	def transformRelativePointByTargetPane(self, point, targetPane):
		(x, y)=point

		newX = x-self.centerX
		newY = y-self.centerY
		if self.width != 0:
			newX *= targetPane.width / self.width
		if self.height != 0:
			newY *= targetPane.height / self.height
		newX += targetPane.centerX
		newY += targetPane.centerY

		return (newX, newY)

	def transformRelativePaneByTargetPane(self, relativePane, targetPane):
		(left, top)=self.transformRelativePointByTargetPane(relativePane.leftTop, targetPane)
		(right, bottom)=self.transformRelativePointByTargetPane(relativePane.rightBottom, targetPane)

		return Pane(left, top, right, bottom)

class Rectangle(Shape):
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
		drawSystem.startDrawing()

		drawSystem.moveTo((0, 0))
		drawSystem.lineTo((self.w, 0))
		drawSystem.lineTo((0, self.h))
		drawSystem.lineTo((-self.w, 0))
		drawSystem.lineTo((0, -self.h))

		drawSystem.endDrawing()

def offsetBoundary(boundary, offset):
	return (boundary[0]+offset[0], boundary[1]+offset[1], boundary[2]+offset[0], boundary[3]+offset[1],)

def mergeBoundary(boundaryA, boundaryB):
	return (min(boundaryA[0], boundaryB[0]), min(boundaryA[1], boundaryB[1]),
		max(boundaryA[2], boundaryB[2]), max(boundaryA[3], boundaryB[3]),)

def mergePanes(panes):
	boxes = map(lambda pane: pane.boundary, panes)

	mergedBox = next(boxes)
	for box in boxes:
		mergedBox = mergeBoundary(mergedBox, box)
	return Pane(*mergedBox)

