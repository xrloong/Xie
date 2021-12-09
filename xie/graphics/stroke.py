from .shape import Shape, Pane
from .stroke_info import StrokeInfo
from . import DrawingSystem

class StrokePosition:
	def __init__(self, startPoint, statePane: Pane = None):
		self.startPoint = startPoint
		self.statePane = statePane

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
		drawingSystem.translate(-infoPane.getLeft(), -infoPane.getTop())
		drawingSystem.scale(statePane.getWidth()/infoPane.getWidth(), statePane.getHeight()/infoPane.getHeight())
		drawingSystem.translate(statePane.getLeft(), statePane.getTop())

		drawingSystem.startDrawing()

		drawingSystem.moveTo(startPoint)
		drawingSystem.draw(stroke.getStrokePath())

		drawingSystem.endDrawing()

		drawingSystem.restore()
		drawingSystem.onPostDrawStroke(stroke)

	def computeBoundary(self):
		startPoint=self.getStartPoint()
		strokePath=self.getStrokePath()
		return strokePath.computeBoundaryWithStartPoint(startPoint)

