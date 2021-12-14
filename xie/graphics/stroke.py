from .shape import Shape, Pane
from .stroke_path import StrokePath

from . import DrawingSystem

class StrokeInfo:
	def __init__(self, name, strokePath: StrokePath):
		self.name = name
		self.strokePath = strokePath

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		return isinstance(other, StrokeInfo) and (self.getName()==other.getName() and self.getStrokePath()==other.getStrokePath())

	def getName(self):
		return self.name

	def getStrokePath(self):
		return self.strokePath

	def getPane(self):
		return self.strokePath.pane

class StrokePosition:
	def __init__(self, startPoint, statePane: Pane = None):
		self.startPoint = startPoint
		self.statePane = statePane

	def transform(self, fromPane, toPane):
		newStatePane = fromPane.transformRelativePaneByTargetPane(self.statePane, toPane)
		newStartPoint = fromPane.transformRelativePointByTargetPane(self.startPoint, toPane)
		return StrokePosition(newStartPoint, newStatePane)

class Stroke(Shape):
	def __init__(self, strokeInfo: StrokeInfo, strokePosition: StrokePosition):
		self.strokeInfo = strokeInfo
		self.strokePosition = strokePosition

	def getStartPoint(self):
		return self.strokePosition.startPoint

	def getStrokeInfo(self):
		return self.strokeInfo

	def getName(self):
		return self.getStrokeInfo().getName()

	def getStrokePath(self):
		return self.getStrokeInfo().getStrokePath()

	def getInfoPane(self):
		return self.getStrokeInfo().getPane()

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
		return Stroke(self.strokeInfo, strokePosition)

