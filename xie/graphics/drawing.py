class DrawingSystem():
	def __init__(self, canvasController):
		self.canvasController=canvasController
		self.lastPoint = None
		self.sourceBoundary = None
		self.sourceBoundaryState = []

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

	def setSourceBoundary(self, sourceBoundary):
		self.sourceBoundary = sourceBoundary

	def save(self):
		self.sourceBoundaryState.append(self.sourceBoundary)

	def restore(self):
		self.sourceBoundary = self.sourceBoundaryState.pop()

	def startDrawing(self, startPoin):
		self._moveTo(self._convertPointByBoundary(startPoin))

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

