# coding=utf8

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
		return isinstance(other, Pane) and (
				self.left == other.left and self.top == other.top
				and self.right == other.right and self.bottom == other.bottom
			)

	def __ne__(self, other):
		return not self.__eq__(other)

	def clone(self):
		return Pane(self.left, self.top, self.right, self.bottom)

	def translateBy(self, offset):
		self.offsetLeftAndRight(offset[0])
		self.offsetTopAndBottom(offset[1])

	def scale(self, pivot, ratio):
		pivotX = pivot[0]
		pivotY = pivot[1]
		self.left = (self.left - pivotX) * ratio + pivotX;
		self.right = (self.right - pivotX) * ratio + pivotX;

		self.top = (self.top - pivotY) * ratio + pivotY;
		self.bottom = (self.bottom - pivotY) * ratio + pivotY;

	def offsetLeftAndRight(self, offset):
		self.left += offset
		self.right += offset

	def offsetTopAndBottom(self, offset):
		self.top += offset
		self.bottom += offset

	@property
	def width(self):
		return self.right-self.left+1

	@property
	def height(self):
		return self.bottom-self.top+1

	def containsPoint(self, point):
		x, y = point
		return (self.left<=x<=self.right) and (self.top<=y<=self.bottom)

	def containsPane(self, pane):
		return self.containsPoint(pane.getLeftTop()) and self.containsPoint(pane.getRightBottom())

	def limitedToPane(self, pane):
		left=max(self.left, pane.left)
		top=max(self.top, pane.top)
		right=min(self.right, pane.right)
		bottom=min(self.bottom, pane.bottom)

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

	def getWidth(self):
		return self.width

	def getHeight(self):
		return self.height

	def getLeftTop(self):
		return (self.left, self.top)

	def getRightBottom(self):
		return (self.right, self.bottom)

	def transformRelativePointByTargetPane(self, point, targetPane):
		(x, y)=point

		newX=int((x-self.getLeft())*targetPane.getWidth()/self.getWidth())+targetPane.getLeft()
		newY=int((y-self.getTop())*targetPane.getHeight()/self.getHeight())+targetPane.getTop()

		return (newX, newY)

	def transformRelativePaneByTargetPane(self, relativePane, targetPane):
		(left, top)=self.transformRelativePointByTargetPane(relativePane.getLeftTop(), targetPane)
		(right, bottom)=self.transformRelativePointByTargetPane(relativePane.getRightBottom(), targetPane)

		return Pane(left, top, right, bottom)


# 字面框（Bounding Box）
Pane.BBOX=Pane(
	Pane.BBOX_X_MIN,
	Pane.BBOX_Y_MIN,
	Pane.BBOX_X_MAX,
	Pane.BBOX_Y_MAX,
	)

class Drawable:
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

def offsetBoundary(boundary, offset):
	return (boundary[0]+offset[0], boundary[1]+offset[1], boundary[2]+offset[0], boundary[3]+offset[1],)

def mergeBoundary(boundaryA, boundaryB):
	return (min(boundaryA[0], boundaryB[0]), min(boundaryA[1], boundaryB[1]),
		max(boundaryA[2], boundaryB[2]), max(boundaryA[3], boundaryB[3]),)

