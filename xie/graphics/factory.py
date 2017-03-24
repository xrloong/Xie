from .stroke import Stroke
from .stroke import StrokeGroup
from .stroke import StrokeGroupInfo
from .stroke_info import *

from .shape import Pane

class ShapeFactory:
	def __init__(self):
		self.strokeInfoFactory=StrokeInfoFactory()

	def generateStrokeInfo(self, name, parameterList):
		return self.strokeInfoFactory.generateStrokeInfo(name, parameterList)

	def generateStroke(self, name, startPoint, parameterList):
		strokeInfo = self.generateStrokeInfo(name, parameterList)
		return Stroke(startPoint, strokeInfo)

	def generateStrokeGroupByStrokeList(self, strokeList):
		strokeGroupInfo=StrokeGroupInfo(strokeList)
		return StrokeGroup(strokeGroupInfo)

	def generateStrokeGroupByStrokeGroupPane(self, sg, pane):
		return sg.generateCopyToApplyNewPane(pane)

	def generateStrokeGroupByStrokeGroupPanePairList(self, strokeGroupPanePairList):
		def computeBBox(paneList):
			left=min(map(lambda pane: pane.getLeft(), paneList))
			top=min(map(lambda pane: pane.getTop(), paneList))
			right=max(map(lambda pane: pane.getRight(), paneList))
			bottom=max(map(lambda pane: pane.getBottom(), paneList))
			return Pane(left, top, right, bottom)

		resultStrokeList=[]
		for strokeGroup, pane in strokeGroupPanePairList:
			strokeGroup=self.generateStrokeGroupByStrokeGroupPane(strokeGroup, pane)
			resultStrokeList.extend(strokeGroup.getStrokeList())

		paneList=[stroke.getStatePane() for stroke in resultStrokeList]
		pane=computeBBox(paneList)

		strokeGroupInfo=StrokeGroupInfo(resultStrokeList)
		strokeGroup=StrokeGroup(strokeGroupInfo, pane)

		return strokeGroup

class StrokeInfoFactory:
	def __init__(self):
		from .segment import SegmentFactory

		segmentFactory = SegmentFactory()
		self.strokeInfoMap = {
			"點": StrokeInfoGenerator_點(segmentFactory),
#			"長頓點": StrokeInfoGenerator_點(segmentFactory),
			"圈": StrokeInfoGenerator_圈(segmentFactory),
			"橫": StrokeInfoGenerator_橫(segmentFactory),
			"橫鉤": StrokeInfoGenerator_橫鉤(segmentFactory),
			"橫折": StrokeInfoGenerator_橫折(segmentFactory),
			"橫折折": StrokeInfoGenerator_橫折折(segmentFactory),
			"橫折提": StrokeInfoGenerator_橫折提(segmentFactory),
			"橫折折撇": StrokeInfoGenerator_橫折折撇(segmentFactory),
			"橫撇彎鉤": StrokeInfoGenerator_橫撇彎鉤(segmentFactory),
			"橫折鉤": StrokeInfoGenerator_橫折鉤(segmentFactory),
			"橫折彎": StrokeInfoGenerator_橫折彎(segmentFactory),
			"橫撇": StrokeInfoGenerator_橫撇(segmentFactory),
			"橫斜彎鉤": StrokeInfoGenerator_橫斜彎鉤(segmentFactory),
			"橫折折折鉤": StrokeInfoGenerator_橫折折折鉤(segmentFactory),
			"橫斜鉤": StrokeInfoGenerator_橫斜鉤(segmentFactory),
			"橫折折折": StrokeInfoGenerator_橫折折折(segmentFactory),
			"豎": StrokeInfoGenerator_豎(segmentFactory),
			"豎折": StrokeInfoGenerator_豎折(segmentFactory),
			"豎彎左": StrokeInfoGenerator_豎彎左(segmentFactory),
			"豎提": StrokeInfoGenerator_豎提(segmentFactory),
			"豎折折": StrokeInfoGenerator_豎折折(segmentFactory),
			"豎折彎鉤": StrokeInfoGenerator_豎折彎鉤(segmentFactory),
			"豎彎鉤": StrokeInfoGenerator_豎彎鉤(segmentFactory),
			"豎彎": StrokeInfoGenerator_豎彎(segmentFactory),
			"豎鉤": StrokeInfoGenerator_豎鉤(segmentFactory),
			"扁斜鉤": StrokeInfoGenerator_豎彎鉤(segmentFactory),
			"斜鉤": StrokeInfoGenerator_斜鉤(segmentFactory),
			"彎鉤": StrokeInfoGenerator_彎鉤(segmentFactory),
			"撇鉤": StrokeInfoGenerator_撇鉤(segmentFactory),

			"撇": StrokeInfoGenerator_撇(segmentFactory),
			"撇點": StrokeInfoGenerator_撇點(segmentFactory),
			"撇橫": StrokeInfoGenerator_撇橫(segmentFactory),
			"撇提": StrokeInfoGenerator_撇橫(segmentFactory),
			"撇折": StrokeInfoGenerator_撇橫(segmentFactory),
			"撇橫撇": StrokeInfoGenerator_撇橫撇(segmentFactory),
			"豎撇": StrokeInfoGenerator_豎撇(segmentFactory),
			"提": StrokeInfoGenerator_提(segmentFactory),
			"捺": StrokeInfoGenerator_捺(segmentFactory),
			"臥捺": StrokeInfoGenerator_臥捺(segmentFactory),
			"提捺": StrokeInfoGenerator_提捺(segmentFactory),
			"橫捺": StrokeInfoGenerator_橫捺(segmentFactory),
		}


	def generateStrokeInfo(self, name, parameterList):
		strokeInfoGenerator = self.strokeInfoMap.get(name, None)
		assert strokeInfoGenerator!=None

		parameterList = strokeInfoGenerator.parseExpression(parameterList)
		strokeInfo = strokeInfoGenerator.generate(name, parameterList)
		return strokeInfo


