from .shape import Shape
from .shape import Pane

from .stroke_info import StrokeInfoFactory

strokeInfoFactory=StrokeInfoFactory()

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

def generateStroke(name, startPoint, parameterList):
	strokeInfo = strokeInfoFactory.generateStrokeInfo(name, parameterList)
	return Stroke(startPoint, strokeInfo)

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

	@classmethod
	def generateInstanceByStrokeList(cls, strokeList):
		strokeGroupInfo=StrokeGroupInfo(strokeList)
		return StrokeGroup(strokeGroupInfo)

	@classmethod
	def generateInstanceByStrokeGroupPane(cls, sg, pane):
		return sg.generateCopyToApplyNewPane(pane)

	@classmethod
	def generateInstanceByStrokeGroupPanePairList(cls, strokeGroupPanePairList):
		def computeBBox(paneList):
			left=min(map(lambda pane: pane.getLeft(), paneList))
			top=min(map(lambda pane: pane.getTop(), paneList))
			right=max(map(lambda pane: pane.getRight(), paneList))
			bottom=max(map(lambda pane: pane.getBottom(), paneList))
			return Pane(left, top, right, bottom)

		resultStrokeList=[]
		for strokeGroup, pane in strokeGroupPanePairList:
			strokeGroup=StrokeGroup.generateInstanceByStrokeGroupPane(strokeGroup, pane)
			resultStrokeList.extend(strokeGroup.getStrokeList())

		paneList=[stroke.getStatePane() for stroke in resultStrokeList]
		pane=computeBBox(paneList)

		strokeGroupInfo=StrokeGroupInfo(resultStrokeList)
		strokeGroup=StrokeGroup(strokeGroupInfo, pane)

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

