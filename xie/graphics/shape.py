# coding=utf8
import numpy

class Shape:
	def draw(self, drawSystem):
		pass

class Pane:
	BBOX_X_MIN=0x08
	BBOX_Y_MIN=0x08
	BBOX_X_MAX=0xF7
	BBOX_Y_MAX=0xF7

	def __init__(self, left, top, right, bottom):
		self.left=left
		self.top=top
		self.right=right
		self.bottom=bottom

	def __str__(self):
		return "%s"%([self.left, self.top, self.right, self.bottom])

	def __eq__(self, other):
		return isinstance(other, Pane) and all(numpy.isclose(self.boundary, other.boundary))

	def __ne__(self, other):
		return not self.__eq__(other)

	def clone(self):
		return Pane(self.left, self.top, self.right, self.bottom)

	def offsetLeftAndRight(self, offset):
		self.left += offset
		self.right += offset

	def offsetTopAndBottom(self, offset):
		self.top += offset
		self.bottom += offset

	@property
	def boundary(self):
		return (self.left, self.top, self.right, self.bottom)

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


# 字面框（Bounding Box）
Pane.BBOX=Pane(
	Pane.BBOX_X_MIN,
	Pane.BBOX_Y_MIN,
	Pane.BBOX_X_MAX,
	Pane.BBOX_Y_MAX,
	)

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

def _splitLengthToList(length, weightList):
	totalWeight=sum(weightList)
	unitLength=length*1./totalWeight

	pointList=[]
	newComponentList=[]
	base=0
	for weight in weightList:
		pointList.append(int(base))
		base=base+unitLength*weight
	pointList.append(int(base))
	return pointList

def genVerticalPanes(weights):
	pane=Pane.BBOX
	points=_splitLengthToList(pane.height, weights)
	paneList=[]
	offset=pane.top
	for [pointStart, pointEnd] in zip(points[:-1], points[1:]):
		height=pointEnd-pointStart
		targetHeight=int(height*0.90)
		offset=int(height-targetHeight)//2
		tmpPane=Pane(pane.left, pointStart+offset, pane.right, pointEnd-offset)
		tmpPane.offsetTopAndBottom(offset)
		paneList.append(tmpPane)
	return paneList

def genHorizontalPanes(weights):
	pane=Pane.BBOX
	points=_splitLengthToList(pane.width, weights)
	paneList=[]
	offset=pane.left
	for [pointStart, pointEnd] in zip(points[:-1], points[1:]):
		width=pointEnd-pointStart
		targetWidth=int(width*0.90)
		offset=int(width-targetWidth)//2
		tmpPane=Pane(pointStart+offset, pane.top, pointEnd-offset, pane.bottom)
		tmpPane.offsetLeftAndRight(offset)
		paneList.append(tmpPane)
	return paneList
