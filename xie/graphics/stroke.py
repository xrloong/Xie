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

class Stroke(Drawing, Shape):
	def __init__(self, startPoint, strokeInfo=None, strokePath=None, infoPane=Pane.BBOX, statePane=Pane.BBOX):
		super().__init__(infoPane, statePane)
		self.startPoint=startPoint

		if strokeInfo:
			self.strokeInfo=strokeInfo
			self.strokePath=strokeInfo.getStrokePath()
			self.name=strokeInfo.getName()
		else:
			self.strokeInfo=None
			self.strokePath=strokePath
			self.name=""

	def clone(self):
		stroke=Stroke(self.startPoint, strokeInfo=self.strokeInfo, strokePath=self.strokePath,
			infoPane=self.getInfoPane(), statePane=self.getStatePane())
		return stroke

	def getName(self):
		return self.name

	def getStartPoint(self):
		return self.startPoint

	def getStrokePath(self):
		return self.strokePath

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


def generateStroke(name, startPoint, parameterList):
	strokeInfo = strokeInfoFactory.generateStrokeInfo(name, parameterList)
	strokePath=strokeInfo.getStrokePath()
	boundary=strokePath.computeBoundaryWithStartPoint(startPoint)

	pane = Pane(*boundary)
	infoPane = pane
	statePane = pane
	return Stroke(startPoint, strokeInfo=strokeInfo, infoPane=infoPane, statePane=statePane)

class StrokeGroupInfo:
	def __init__(self, strokeList, bBoxPane):
		self.strokeList=strokeList
		self.bBoxPane=bBoxPane

	def getStrokeList(self):
		return self.strokeList

	def getBBoxPane(self):
		return self.bBoxPane

	@staticmethod
	def generateInstanceByStrokeList(strokeList, bBox):
		return StrokeGroupInfo(strokeList, Pane(*bBox))

	@staticmethod
	def generateInstanceFromComposition(strokeList, bBoxPane):
		return StrokeGroupInfo(strokeList, bBoxPane)

class StrokeGroup(Drawing):
	def __init__(self, strokeGroupInfo):
		pane=strokeGroupInfo.getBBoxPane()
		super().__init__(pane, pane)
		self.strokeGroupInfo=strokeGroupInfo

	def clone(self):
		strokeList=[s.clone() for s in self.getStrokeList()]
		strokeGroupInfo=StrokeGroupInfo.generateInstanceFromComposition(strokeList, self.getInfoPane())
		strokeGroup=StrokeGroup(strokeGroupInfo)
		strokeGroup.setStatePane(self.getStatePane())
		return strokeGroup

	def getDrawingList(self):
		return self.getStrokeList()

	def getStrokeList(self):
		return self.strokeGroupInfo.getStrokeList()

	def getCount(self):
		return len(self.getStrokeList())

	@staticmethod
	def generateStrokeGroup(sg, pane):
		strokeGroup=sg.clone()

		newSgTargetPane=pane
		sgTargetPane=strokeGroup.getStatePane()
		sgInfoPane=strokeGroup.getInfoPane()
		for drawing in strokeGroup.getDrawingList():
			sTargetPane=drawing.getStatePane()
			sInfoPane=drawing.getInfoPane()
			drawing.transformBy(sgInfoPane, newSgTargetPane)

		strokeGroup.setStatePane(newSgTargetPane)
		strokeGroup.setInfoPane(newSgTargetPane)

		return strokeGroup

	@staticmethod
	def generateStrokeGroupInfo(strokeGroupPanePair):
		def computeBBox(paneList):
			left=min(map(lambda pane: pane.getLeft(), paneList))
			top=min(map(lambda pane: pane.getTop(), paneList))
			right=max(map(lambda pane: pane.getRight(), paneList))
			bottom=max(map(lambda pane: pane.getBottom(), paneList))
			return Pane(left, top, right, bottom)

		resultStrokeList=[]
		paneList=[]
		for strokeGroup, pane in strokeGroupPanePair:
			strokeGroup=StrokeGroup.generateStrokeGroup(strokeGroup, pane)
			resultStrokeList.extend(strokeGroup.getStrokeList())
			paneList.append(strokeGroup.getInfoPane())

		pane=computeBBox(paneList)
		strokeGroupInfo=StrokeGroupInfo.generateInstanceFromComposition(resultStrokeList, pane)

		return strokeGroupInfo

