class Boundary():
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

class DrawingSystem():
	def __init__(self, canvasController):
		self.canvasController=canvasController
		self.lastPoint = None
		self.sourceBoundary = Boundary.Default

		self.infoPane=None
		self.statePane=None

	def getWidth(self):
		return self.canvasController.getWidth()

	def getHeight(self):
		return self.canvasController.getHeight()

	def _moveTo(self, point):
		assert point is not None
		self.lastPoint = point

		canvasController=self.canvasController
		canvasController.moveTo(point)

	def _clearLastPoint(self):
		self.lastPoint = None

	def _convertPoint(self, point):
		startPoint=self.lastPoint
		return (startPoint[0]+point[0], startPoint[1]+point[1])

	def _convertPointByBoundary(self, point):
		if self.sourceBoundary:
			tx, ty = 0, 0
			tW, tH = self.getWidth(), self.getHeight()
			sx, sy = self.sourceBoundary.getLeft(), self.sourceBoundary.getTop()
			sW, sH = self.sourceBoundary.getWidth(), self.sourceBoundary.getHeight()
			x, y = point

			return (tx + (x-sx)*tW/sW, ty + (y-sy)*tH/sH)
		else:
			return point

	def setPane(self, infoPane, statePane):
		self.canvasController.setPane(infoPane, statePane)

	def onPreDrawCharacter(self, character):
		self.canvasController.onPreDrawCharacter(character)

	def onPostDrawCharacter(self, character):
		self.canvasController.onPostDrawCharacter(character)

	def onPreDrawStroke(self, stroke):
		self.canvasController.onPreDrawStroke(stroke)

	def onPostDrawStroke(self, stroke):
		self.canvasController.onPostDrawStroke(stroke)

	def startDrawing(self, startPoint):
		self._moveTo(self._convertPointByBoundary(startPoint))

	def endDrawing(self):
		self._clearLastPoint()

	def lineTo(self, point):
		canvasController=self.canvasController
		p=self._convertPoint(self._convertPointByBoundary(point))
		canvasController.lineTo(p)
		self.lastPoint=p

	def qCurveTo(self, p1, p2):
		canvasController=self.canvasController
		p1=self._convertPoint(self._convertPointByBoundary(p1))
		p2=self._convertPoint(self._convertPointByBoundary(p2))
		canvasController.qCurveTo(p1, p2)
		self.lastPoint=p2

	def clear(self):
		self.canvasController.clear()

	def draw(self, shape):
		shape.draw(self)

