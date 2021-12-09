import numpy

class DrawingSystem():
	def __init__(self, canvasController):
		self.canvasController=canvasController
		self.lastPoint = None

		self.matrix = numpy.eye(3)
		self.matrixStack = []

	def getWidth(self):
		return self.canvasController.getWidth()

	def getHeight(self):
		return self.canvasController.getHeight()

	def _clearLastPoint(self):
		self.lastPoint = (0, 0)

	def _convertPoint(self, point):
		lastPoint=self.lastPoint
		return (lastPoint[0]+point[0], lastPoint[1]+point[1])

	def _convertPointByBoundary(self, point):
		# source boundary
		Bx, By = 0, 0
		BW, BH = 256, 256

		tx, ty = 0, 0
		tW, tH = self.getWidth(), self.getHeight()
		x, y = point

		return (tx + (x-Bx)*tW/BW, ty + (y-By)*tH/BH)


	# Matrix related operation
	def save(self):
		self.matrixStack.append(self.matrix)

	def restore(self):
		self.matrix = self.matrixStack.pop()

	def translate(self, x, y):
		matrix = numpy.array([
				[0, 0, x],
				[0, 0, y],
				[0, 0, 0],
			])
		self.matrix = self.matrix+matrix

	def scale(self, sx, sy):
		matrix = numpy.array([
				[sx, 0, 0],
				[0, sy, 0],
				[0, 0, 1],
			])
		self.matrix = matrix.dot(self.matrix)

	def convertPointByPane(self, p):
		pp = (p[0], p[1], 1)
		result = self.matrix.dot(pp)
		resultList = result.tolist()

		return (resultList[0], resultList[1])

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

		p=self._convertPoint(self._convertPointByBoundary(point))
		canvasController.moveTo(self.convertPointByPane(p))
		self.lastPoint = p

	def lineTo(self, point):
		canvasController=self.canvasController
		p=self._convertPoint(self._convertPointByBoundary(point))
		canvasController.lineTo(self.convertPointByPane(p))
		self.lastPoint=p

	def qCurveTo(self, p1, p2):
		canvasController=self.canvasController
		p1=self._convertPoint(self._convertPointByBoundary(p1))
		p2=self._convertPoint(self._convertPointByBoundary(p2))
		canvasController.qCurveTo(self.convertPointByPane(p1), self.convertPointByPane(p2))
		self.lastPoint=p2

	def clear(self):
		self.canvasController.clear()

	def draw(self, shape):
		shape.draw(self)

