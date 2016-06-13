class DrawingSystem():
	def __init__(self, canvasController):
		self.canvasController=canvasController
		self.lastPoint = None

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

	def startDrawing(self, startPoin):
		self._moveTo(startPoin)

	def endDrawing(self):
		self._clearLastPoint()

	def _convertPoint(self, point):
		startPoint=self.lastPoint
		return (startPoint[0]+point[0], startPoint[1]+point[1])

	def lineTo(self, point):
		canvasController=self.canvasController
		p=self._convertPoint(point)
		canvasController.lineTo(p)
		self.lastPoint=p

	def qCurveTo(self, p1, p2):
		canvasController=self.canvasController
		p1=self._convertPoint(p1)
		p2=self._convertPoint(p2)
		canvasController.qCurveTo(p1, p2)
		self.lastPoint=p2

