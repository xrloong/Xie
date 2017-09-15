from .shape import Shape
from .shape import Pane

class Stroke(Shape):
	def __init__(self, startPoint, strokeInfo, statePane=None):
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

	def draw(self, drawingSystem):
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

	def generateCopyToApplyNewPane(self, sgTargetPane, newSgTargetPane):
		newSTargetPane=sgTargetPane.transformRelativePaneByTargetPane(self.getStatePane(), newSgTargetPane)
		newStartPoint=sgTargetPane.transformRelativePointByTargetPane(self.getStartPoint(), newSgTargetPane)

		strokeCopy=Stroke(newStartPoint, self.strokeInfo, newSTargetPane)
		return strokeCopy

class StrokeGroupInfo:
	def __init__(self, strokeList):
		self.strokeList=strokeList
		self.infoPane=None

	def getStrokeList(self):
		return self.strokeList

	def getInfoPane(self):
		if not self.infoPane:
			def mergeBoundaryList(boundaryList):
				from xie.graphics.shape import mergeBoundary
				r = boundaryList[0]
				for b in boundaryList[1:]:
					r = mergeBoundary(r, b)
				return r

			strokeList=self.getStrokeList()
			boundaryList=[stroke.computeBoundary() for stroke in strokeList]
			bBox=mergeBoundaryList(boundaryList)
			self.infoPane=Pane(*bBox)

		return self.infoPane

class StrokeGroup(Shape):
	def __init__(self, strokeGroupInfo, statePane=None):
		self.strokeGroupInfo=strokeGroupInfo

		if not statePane:
			statePane=strokeGroupInfo.getInfoPane()
		self.statePane=statePane

	def getStatePane(self):
		return self.statePane

	def getStrokeList(self):
		return self.strokeGroupInfo.getStrokeList()

	def getCount(self):
		return len(self.getStrokeList())

	def getStroke(self, index):
		return self.getStrokeList()[index]

	def draw(self, drawingSystem):
		strokeList = self.getStrokeList();

		for stroke in strokeList:
			stroke.draw(drawingSystem)

	def generateCopyToApplyNewPane(self, newSgTargetPane):
		sgStatePane=self.getStatePane()
		strokeList=[s.generateCopyToApplyNewPane(sgStatePane, newSgTargetPane) for s in self.getStrokeList()]
		strokeGroupInfo=StrokeGroupInfo(strokeList)

		strokeGroup=StrokeGroup(strokeGroupInfo)
		return strokeGroup

class Character(Shape):
	def __init__(self, name, strokeGroup, tag=None):
		self.name = name
		self.strokeGroup = strokeGroup
		self.tag = tag

	def getName(self):
		return self.name

	def getStrokeGroup(self):
		return self.strokeGroup

	def getTag(self):
		return self.tag

	def draw(self, drawingSystem):
		character=self

		drawingSystem.clear()
		drawingSystem.onPreDrawCharacter(character)
		drawingSystem.draw(character.getStrokeGroup())
		drawingSystem.onPostDrawCharacter(character)

