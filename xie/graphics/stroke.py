from . import Shape, Pane
from . import StrokeInfo
from . import DrawingSystem

class Stroke(Shape):
	def __init__(self, startPoint, strokeInfo: StrokeInfo, statePane=None):
		self.startPoint=startPoint
		self.strokeInfo=strokeInfo

		strokePath=strokeInfo.getStrokePath()
		boundary=strokePath.computeBoundaryWithStartPoint(startPoint)

		self.infoPane = Pane(*boundary)
		if statePane:
			self.statePane=statePane
		else:
			self.statePane=self.infoPane

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
		drawingSystem.setPane(stroke.getInfoPane(), stroke.getStatePane())

		drawingSystem.startDrawing(startPoint)
		drawingSystem.draw(stroke.getStrokePath())
		drawingSystem.endDrawing()
		drawingSystem.onPostDrawStroke(stroke)

	def computeBoundary(self):
		startPoint=self.getStartPoint()
		strokePath=self.getStrokePath()
		return strokePath.computeBoundaryWithStartPoint(startPoint)

	def generateCopyToApplyNewPane(self, sgTargetPane: Pane, newSgTargetPane: Pane):
		newSTargetPane=sgTargetPane.transformRelativePaneByTargetPane(self.getStatePane(), newSgTargetPane)
		newStartPoint=sgTargetPane.transformRelativePointByTargetPane(self.getStartPoint(), newSgTargetPane)

		strokeCopy=Stroke(newStartPoint, self.strokeInfo, newSTargetPane)
		return strokeCopy

