from .shape import Shape, Pane
from .stroke_info import StrokeInfo
from . import DrawingSystem

class Stroke(Shape):
	def __init__(self, startPoint, strokeInfo: StrokeInfo, statePane=None):
		self.startPoint=startPoint
		self.strokeInfo=strokeInfo

		strokePath = strokeInfo.getStrokePath()
		boundary = strokePath.computeBoundary()
		self.infoPane = Pane(*boundary)

		if statePane:
			self.statePane=statePane
		else:
			strokePath=strokeInfo.getStrokePath()
			boundary=strokePath.computeBoundaryWithStartPoint(startPoint)
			self.statePane=Pane(*boundary)

	def getStartPoint(self):
		return self.startPoint

	def getStrokeInfo(self):
		return self.strokeInfo

	def getName(self):
		return self.getStrokeInfo().getName()

	def getStrokePath(self):
		return self.getStrokeInfo().getStrokePath()

	def getInfoPane(self):
		return self.infoPane

	def getStatePane(self):
		return self.statePane

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

		drawingSystem.startDrawing(startPoint)
		drawingSystem.draw(stroke.getStrokePath())
		drawingSystem.endDrawing()
		drawingSystem.restore()
		drawingSystem.onPostDrawStroke(stroke)

	def computeBoundary(self):
		startPoint=self.getStartPoint()
		strokePath=self.getStrokePath()
		return strokePath.computeBoundaryWithStartPoint(startPoint)

