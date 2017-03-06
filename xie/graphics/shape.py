# coding=utf8

class Shape:
	pass

class Pane:
	EMBOX_X_MIN=0x00
	EMBOX_Y_MIN=0x00
	EMBOX_X_MAX=0xFF
	EMBOX_Y_MAX=0xFF
	EMBOX_WIDTH=EMBOX_X_MAX-EMBOX_X_MIN+1
	EMBOX_HEIGHT=EMBOX_Y_MAX-EMBOX_Y_MIN+1

	BBOX_X_MIN=0x08
	BBOX_Y_MIN=0x08
	BBOX_X_MAX=0xF7
	BBOX_Y_MAX=0xF7


	EMBOX_REGION=[EMBOX_X_MIN, EMBOX_Y_MIN, EMBOX_X_MAX, EMBOX_Y_MAX]

	def __init__(self, region=EMBOX_REGION):
		[left, top, right, bottom]=region
		self.left=left
		self.top=top
		self.right=right
		self.bottom=bottom

		self.setup()

	def __str__(self):
		return "%s"%([self.left, self.top, self.right, self.bottom])

	def clone(self):
		return Pane(self.getAsList())

	def setup(self):
		self.hScale=self.width*1./Pane.EMBOX_WIDTH
		self.vScale=self.height*1./Pane.EMBOX_HEIGHT

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

		self.setup()

	def getAsList(self):
		return [self.left, self.top, self.right, self.bottom]

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

	def getHScale(self):
		return self.hScale

	def getVScale(self):
		return self.vScale

	def getLeftTop(self):
		return (self.left, self.top)

	def getRightBottom(self):
		return (self.right, self.bottom)

	def transformPoint(self, point):
		[x, y]=point
		left=self.getLeft()
		top=self.getTop()

		hScale=self.getHScale()
		vScale=self.getVScale()

		newX=int(x*hScale)+left
		newY=int(y*vScale)+top

		return (newX, newY)

	def transformPane(self, pane):
		(left, top)=self.transformPoint((pane.left, pane.top))
		(right, bottom)=self.transformPoint((pane.right, pane.bottom))

		pane.left=left
		pane.top=top
		pane.right=right
		pane.bottom=bottom

		pane.setup()

	def transformRelativePointByTargetPane(self, point, targetPane):
		(x, y)=point

		newX=int((x-self.getLeft())*targetPane.getWidth()/self.getWidth())+targetPane.getLeft()
		newY=int((y-self.getTop())*targetPane.getHeight()/self.getHeight())+targetPane.getTop()

		assert newX==max(targetPane.left, min(targetPane.right, newX))
		assert newY==max(targetPane.top, min(targetPane.bottom, newY))

		return (newX, newY)

	def transformRelativePaneByTargetPane(self, relativePane, targetPane):
		(left, top)=self.transformRelativePointByTargetPane(relativePane.getLeftTop(), targetPane)
		(right, bottom)=self.transformRelativePointByTargetPane(relativePane.getRightBottom(), targetPane)

		return Pane((left, top, right, bottom))


# 字身框（Em Box）
Pane.EMBOX=Pane()

# 字面框（Bounding Box）
Pane.BBOX=Pane([
	Pane.BBOX_X_MIN,
	Pane.BBOX_Y_MIN,
	Pane.BBOX_X_MAX,
	Pane.BBOX_Y_MAX,
	])

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

