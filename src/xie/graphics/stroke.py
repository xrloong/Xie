from .shape import Shape, Pane
from .stroke_path import StrokePath

from . import DrawingSystem

class StrokePosition:
	def __init__(self, startPoint, statePane: Pane = None):
		self.startPoint = startPoint
		self.statePane = statePane

	def transform(self, fromPane, toPane):
		newStatePane = fromPane.transformRelativePaneByTargetPane(self.statePane, toPane)
		newStartPoint = fromPane.transformRelativePointByTargetPane(self.startPoint, toPane)
		return StrokePosition(newStartPoint, newStatePane)

class Stroke(Shape):
	def __init__(self, typeName, path: StrokePath, strokePosition: StrokePosition):
		self.typeName = typeName
		self.path = path
		self.strokePosition = strokePosition

	def getStartPoint(self):
		return self.strokePosition.startPoint

	def getTypeName(self):
		return self.typeName

	def getName(self):
		return self.getTypeName()

	def getStrokePath(self):
		return self.path

	def getInfoPane(self):
		return self.path.getPane()

	def getStatePane(self):
		return self.strokePosition.statePane

	def draw(self, drawingSystem: DrawingSystem):
		startPoint = self.getStartPoint()

		stroke=self
		drawingSystem.onPreDrawStroke(stroke)
		drawingSystem.save()

		infoPane = stroke.getInfoPane()
		statePane = stroke.getStatePane()
		drawingSystem.translate(-startPoint[0], -startPoint[1])
		drawingSystem.translate(-infoPane.centerX, -infoPane.centerY)
		if infoPane.width != 0:
			drawingSystem.scale(statePane.width/infoPane.width, 1)
		if infoPane.height != 0:
			drawingSystem.scale(1, statePane.height/infoPane.height)
		drawingSystem.translate(statePane.centerX, statePane.centerY)

		drawingSystem.startDrawing()

		drawingSystem.moveTo(startPoint)
		drawingSystem.draw(stroke.getStrokePath())

		drawingSystem.endDrawing()

		drawingSystem.restore()
		drawingSystem.onPostDrawStroke(stroke)

	def transform(self, fromComponentPane, toComponentPane):
		strokePosition = self.strokePosition.transform(fromComponentPane, toComponentPane)
		return Stroke(self.typeName, self.path, strokePosition)

