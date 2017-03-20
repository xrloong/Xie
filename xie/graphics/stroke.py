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
		sTargetPane=self.getStatePane()
		newSTargetPane=sgTargetPane.transformRelativePaneByTargetPane(sTargetPane, newSgTargetPane)

		strokeCopy=Stroke(self.startPoint, self.strokeInfo, newSTargetPane)
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
	def __init__(self, strokeGroupInfo, infoPane):
		self.strokeGroupInfo=strokeGroupInfo

		self.infoPane=infoPane
		self.statePane=infoPane

	def getInfoPane(self):
		return self.infoPane

	def getStrokeList(self):
		return self.strokeGroupInfo.getStrokeList()

	def getCount(self):
		return len(self.getStrokeList())

	def draw(self, drawingSystem):
		strokeList = self.getStrokeList();

		for stroke in strokeList:
			stroke.draw(drawingSystem)

	@classmethod
	def generateInstanceByInfo(cls, strokeGroupInfo, infoPane=None):
		if not infoPane:
			infoPane=strokeGroupInfo.getInfoPane()
		return StrokeGroup(strokeGroupInfo, infoPane)

	@classmethod
	def generateInstanceByStrokeList(cls, strokeList):
		strokeGroupInfo=StrokeGroupInfo(strokeList)
		return StrokeGroup.generateInstanceByInfo(strokeGroupInfo)

	@classmethod
	def generateInstanceByStrokeGroupPane(cls, sg, pane):
		newSgTargetPane=pane
		sgInfoPane=sg.getInfoPane()

		strokeList=[s.generateCopyToApplyNewPane(sgInfoPane, newSgTargetPane) for s in sg.getStrokeList()]

		strokeGroupInfo=StrokeGroupInfo(strokeList)

		infoPane=newSgTargetPane
		strokeGroup=StrokeGroup.generateInstanceByInfo(strokeGroupInfo, infoPane)

		return strokeGroup

	@classmethod
	def generateInstanceByStrokeGroupPanePairList(cls, strokeGroupPanePairList):
		def computeBBox(paneList):
			left=min(map(lambda pane: pane.getLeft(), paneList))
			top=min(map(lambda pane: pane.getTop(), paneList))
			right=max(map(lambda pane: pane.getRight(), paneList))
			bottom=max(map(lambda pane: pane.getBottom(), paneList))
			return Pane(left, top, right, bottom)

		resultStrokeList=[]
		paneList=[]
		for strokeGroup, pane in strokeGroupPanePairList:
			strokeGroup=StrokeGroup.generateInstanceByStrokeGroupPane(strokeGroup, pane)
			resultStrokeList.extend(strokeGroup.getStrokeList())
			paneList.append(strokeGroup.getInfoPane())

		pane=computeBBox(paneList)
		strokeGroupInfo=StrokeGroupInfo(resultStrokeList)
		strokeGroup=StrokeGroup.generateInstanceByInfo(strokeGroupInfo, pane)

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

