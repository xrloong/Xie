class DrawingSystem():
	def __init__(self, canvasController):
		self.canvasController=canvasController
		self.lastPoint = None

	def getWidth(self):
		return self.canvasController.getWidth()

	def getHeight(self):
		return self.canvasController.getHeight()

	def _clearLastPoint(self):
		self.lastPoint = None

	def _convertPoint(self, point):
		startPoint=self.lastPoint
		return (startPoint[0]+point[0], startPoint[1]+point[1])

	def _convertPointByBoundary(self, point):
		# source boundary
		Bx, By = 0, 0
		BW, BH = 256, 256

		tx, ty = 0, 0
		tW, tH = self.getWidth(), self.getHeight()
		x, y = point

		return (tx + (x-Bx)*tW/BW, ty + (y-By)*tH/BH)

	def save(self):
		self.canvasController.save()

	def restore(self):
		self.canvasController.restore()

	def translate(self, x, y):
		self.canvasController.translate(x, y)

	def scale(self, sx, sy):
		self.canvasController.scale(sx, sy)

	def onPreDrawCharacter(self, character):
		self.canvasController.onPreDrawCharacter(character)

	def onPostDrawCharacter(self, character):
		self.canvasController.onPostDrawCharacter(character)

	def onPreDrawStroke(self, stroke):
		self.canvasController.onPreDrawStroke(stroke)

	def onPostDrawStroke(self, stroke):
		self.canvasController.onPostDrawStroke(stroke)

	def startDrawing(self):
		self._clearLastPoint()

	def endDrawing(self):
		self._clearLastPoint()

	def moveTo(self, point):
		canvasController=self.canvasController

		canvasController.moveTo(point)
		self.lastPoint = point

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

