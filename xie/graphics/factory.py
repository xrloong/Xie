from .stroke import Stroke, StrokePosition
from .component import Component, ComponentInfo
from .stroke_info import *

from .shape import Pane

class ShapeFactory:
	def __init__(self):
		self.strokeInfoFactory=StrokeInfoFactory()

	def _generateStroke(self, startPoint, strokeInfo, pane = None):
		if not pane:
			strokePath = strokeInfo.getStrokePath()
			boundary = strokePath.computeBoundaryWithStartPoint(startPoint)
			statePane = Pane(*boundary)
		else:
			infoPane = strokeInfo.pane
			statePane = pane
			startPoint = infoPane.transformRelativePointByTargetPane((0, 0), statePane)

		strokePosition = StrokePosition(startPoint, statePane)
		return Stroke(strokeInfo, strokePosition)

	def generateParameterBasedStroke(self, name, parameterList, startPoint):
		strokeInfo = self.strokeInfoFactory.generateStrokeInfo(name, parameterList)
		return self._generateStroke(startPoint, strokeInfo)

	def generateSegmentBasedStroke(self, name, segments, startPoint):
		strokePath = StrokePath(segments)
		strokeInfo = StrokeInfo(name, strokePath)
		return self._generateStroke(startPoint, strokeInfo)

	def _generateStrokeByStrokeAndNewPane(self, stroke, sgTargetPane: Pane, newSgTargetPane: Pane):
		newSTargetPane=sgTargetPane.transformRelativePaneByTargetPane(stroke.getStatePane(), newSgTargetPane)
		newStartPoint=sgTargetPane.transformRelativePointByTargetPane(stroke.getStartPoint(), newSgTargetPane)

		return self._generateStroke(newStartPoint, stroke.strokeInfo, newSTargetPane)

	def _generateComponent(self, strokes, pane = None):
		componentInfo = ComponentInfo(strokes)
		if not pane:
			pane = componentInfo.getInfoPane()
		return Component(componentInfo, pane)

	def generateComponentByStrokes(self, strokes):
		return self._generateComponent(strokes)

	def generateComponentByComponentPane(self, component, pane):
		componentStatePane=component.getStatePane()
		strokes=[self._generateStrokeByStrokeAndNewPane(s, componentStatePane, pane) for s in component.getStrokeList()]

		return self._generateComponent(strokes)

	def generateComponentByComponentPanePairs(self, componentPanePairs):
		def computeBBox(panes):
			left=min(map(lambda pane: pane.getLeft(), panes))
			top=min(map(lambda pane: pane.getTop(), panes))
			right=max(map(lambda pane: pane.getRight(), panes))
			bottom=max(map(lambda pane: pane.getBottom(), panes))
			return Pane(left, top, right, bottom)

		strokes = []
		for component, pane in componentPanePairs:
			component=self.generateComponentByComponentPane(component, pane)
			strokes.extend(component.getStrokeList())

		panes = [stroke.getStatePane() for stroke in strokes]
		pane = computeBBox(panes)

		return self._generateComponent(strokes, pane)

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


