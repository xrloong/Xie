from .shape import Drawing
from .shape import Shape
from .shape import Pane

from .stroke_info import StrokeInfoFactory

class Character(Shape):
	def __init__(self, strokes=[], name=""):
		self.name = name
		self.strokes = strokes

	def setName(self, name):
		self.name = name

	def setStrokes(self, strokes):
		self.strokes = strokes

	def getStrokes(self):
		return self.strokes

	def draw(self, drawingSystem):
		strokes=self.getStrokes()
		for stroke in strokes:
			stroke.draw(drawingSystem)

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

		strokePath = stroke.getStrokePath()
		strokePath.draw(drawingSystem)

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
	def __init__(self, strokeList, bBoxPane):
		self.strokeList=strokeList
		self.bBoxPane=bBoxPane

	def getStrokeList(self):
		return self.strokeList

	def getBBoxPane(self):
		return self.bBoxPane

	@classmethod
	def generateInstanceByStrokeList(cls, strokeList):
		def mergeBoundaryList(boundaryList):
			from xie.graphics.shape import mergeBoundary
			r = boundaryList[0]
			for b in boundaryList[1:]:
				r = mergeBoundary(r, b)
			return r

		boundaryList=[stroke.computeBoundary() for stroke in strokeList]
		bBox=mergeBoundaryList(boundaryList)

		return StrokeGroupInfo(strokeList, Pane(*bBox))

	@staticmethod
	def generateInstanceFromComposition(strokeList, bBoxPane):
		return StrokeGroupInfo(strokeList, bBoxPane)

class StrokeGroup(Drawing):
	def __init__(self, strokeGroupInfo, infoPane, statePane):
		super().__init__(infoPane, statePane)
		self.strokeGroupInfo=strokeGroupInfo

	def getStrokeList(self):
		return self.strokeGroupInfo.getStrokeList()

	def getCount(self):
		return len(self.getStrokeList())

	def draw(self, drawingSystem):
		strokeList = self.getStrokeList();

		drawingSystem.clear()
		for stroke in strokeList:
			stroke.draw(drawingSystem)

	@classmethod
	def generateInstanceByInfo(cls, strokeGroupInfo):
		pane=strokeGroupInfo.getBBoxPane()
		infoPane=pane
		statePane=pane
		return StrokeGroup(strokeGroupInfo, infoPane, statePane)

	@classmethod
	def generateInstanceByStrokeGroupPane(cls, sg, pane):
		newSgTargetPane=pane
		sgInfoPane=sg.getInfoPane()

		strokeList=[s.generateCopyToApplyNewPane(sgInfoPane, newSgTargetPane) for s in sg.getStrokeList()]

		strokeGroupInfo=StrokeGroupInfo.generateInstanceByStrokeList(strokeList)

		infoPane=newSgTargetPane
		statePane=newSgTargetPane
		strokeGroup=StrokeGroup(strokeGroupInfo, infoPane, statePane)

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
		strokeGroupInfo=StrokeGroupInfo.generateInstanceFromComposition(resultStrokeList, pane)
		strokeGroup=StrokeGroup.generateInstanceByInfo(strokeGroupInfo)

		return strokeGroup

