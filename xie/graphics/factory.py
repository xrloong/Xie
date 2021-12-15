from .stroke import Stroke, StrokePosition, StrokeInfo
from .component import Component, ComponentInfo
from .stroke_path import *

from .shape import Pane

class ShapeFactory:
	def __init__(self):
		self.strokeFactory=StrokeFactory()

	def generateStrokeByParameters(self, name, parameters, startPoint = None, strokeBoundPane = None):
		assert startPoint != None or strokeBoundPane != None

		strokePath = self.strokeFactory.generateStrokePathByParameters(name, parameters)

		if startPoint:
			boundary = strokePath.computeBoundaryWithStartPoint(startPoint)
			strokeBoundPane = Pane(*boundary)
		else:
			infoPane = strokePath.pane
			startPoint = infoPane.transformRelativePointByTargetPane((0, 0), strokeBoundPane)

		return self.strokeFactory.generateStroke(name, strokePath, strokeBoundPane)

	def generateStrokeBySegments(self, name, segments, startPoint):
		strokePath = self.strokeFactory.generateStrokePathBySegments(segments)

		boundary = strokePath.computeBoundaryWithStartPoint(startPoint)
		pane = Pane(*boundary)

		return self.strokeFactory.generateStroke(name, strokePath, pane)

	def _generateComponent(self, strokes, pane = None):
		componentInfo = ComponentInfo(strokes)
		if not pane:
			pane = componentInfo.getInfoPane()
		return Component(componentInfo, pane)

	def generateComponentByStrokes(self, strokes):
		return self._generateComponent(strokes)

	def generateComponentByComponentPane(self, component, pane):
		componentStrokes = component.getStrokeList()
		componentStatePane = component.getStatePane()
		strokes = [s.transform(componentStatePane, pane) for s in componentStrokes]

		return self._generateComponent(strokes)

	def generateComponentByComponentPanePairs(self, componentPanePairs):
		from .shape import mergePanes

		strokes = []
		for component, pane in componentPanePairs:
			component=self.generateComponentByComponentPane(component, pane)
			strokes.extend(component.getStrokeList())

		panes = [stroke.getStatePane() for stroke in strokes]
		pane = mergePanes(panes)

		return self._generateComponent(strokes, pane)

class StrokeFactory:
	def __init__(self):
		from .segment import SegmentFactory

		segmentFactory = SegmentFactory()
		self.strokePathMap = {
			"點": StrokePathGenerator_點(segmentFactory),
#			"長頓點": StrokePathGenerator_點(segmentFactory),
			"圈": StrokePathGenerator_圈(segmentFactory),
			"橫": StrokePathGenerator_橫(segmentFactory),
			"橫鉤": StrokePathGenerator_橫鉤(segmentFactory),
			"橫折": StrokePathGenerator_橫折(segmentFactory),
			"橫折折": StrokePathGenerator_橫折折(segmentFactory),
			"橫折提": StrokePathGenerator_橫折提(segmentFactory),
			"橫折折撇": StrokePathGenerator_橫折折撇(segmentFactory),
			"橫撇彎鉤": StrokePathGenerator_橫撇彎鉤(segmentFactory),
			"橫折鉤": StrokePathGenerator_橫折鉤(segmentFactory),
			"橫折彎": StrokePathGenerator_橫折彎(segmentFactory),
			"橫撇": StrokePathGenerator_橫撇(segmentFactory),
			"橫斜彎鉤": StrokePathGenerator_橫斜彎鉤(segmentFactory),
			"橫折折折鉤": StrokePathGenerator_橫折折折鉤(segmentFactory),
			"橫斜鉤": StrokePathGenerator_橫斜鉤(segmentFactory),
			"橫折折折": StrokePathGenerator_橫折折折(segmentFactory),
			"豎": StrokePathGenerator_豎(segmentFactory),
			"豎折": StrokePathGenerator_豎折(segmentFactory),
			"豎彎左": StrokePathGenerator_豎彎左(segmentFactory),
			"豎提": StrokePathGenerator_豎提(segmentFactory),
			"豎折折": StrokePathGenerator_豎折折(segmentFactory),
			"豎折彎鉤": StrokePathGenerator_豎折彎鉤(segmentFactory),
			"豎彎鉤": StrokePathGenerator_豎彎鉤(segmentFactory),
			"豎彎": StrokePathGenerator_豎彎(segmentFactory),
			"豎鉤": StrokePathGenerator_豎鉤(segmentFactory),
			"扁斜鉤": StrokePathGenerator_豎彎鉤(segmentFactory),
			"斜鉤": StrokePathGenerator_斜鉤(segmentFactory),
			"彎鉤": StrokePathGenerator_彎鉤(segmentFactory),
			"撇鉤": StrokePathGenerator_撇鉤(segmentFactory),

			"撇": StrokePathGenerator_撇(segmentFactory),
			"撇點": StrokePathGenerator_撇點(segmentFactory),
			"撇橫": StrokePathGenerator_撇橫(segmentFactory),
			"撇提": StrokePathGenerator_撇橫(segmentFactory),
			"撇折": StrokePathGenerator_撇橫(segmentFactory),
			"撇橫撇": StrokePathGenerator_撇橫撇(segmentFactory),
			"豎撇": StrokePathGenerator_豎撇(segmentFactory),
			"提": StrokePathGenerator_提(segmentFactory),
			"捺": StrokePathGenerator_捺(segmentFactory),
			"臥捺": StrokePathGenerator_臥捺(segmentFactory),
			"提捺": StrokePathGenerator_提捺(segmentFactory),
			"橫捺": StrokePathGenerator_橫捺(segmentFactory),
		}

	# StrokePath
	def generateStrokePathByParameters(self, name, parameters):
		strokePathGenerator = self.strokePathMap.get(name, None)
		assert strokePathGenerator!=None

		strokePath = strokePathGenerator.generate(parameters)
		return strokePath

	def generateStrokePathBySegments(self, segments):
		strokePath = StrokePath(segments)
		return strokePath

	# StrokeInfo
	def generateStrokeInfo(self, name, strokePath):
		return StrokeInfo(name, strokePath)

	def generateStrokeInfoByParameters(self, name, parameters):
		strokePath = self.generateStrokePathByParameters(name, parameters)
		return StrokeInfo(name, strokePath)

	# Stroke
	def generateStroke(self, name, strokePath, strokeBoundPane):
		infoPane = strokePath.pane
		startPoint = infoPane.transformRelativePointByTargetPane((0, 0), strokeBoundPane)

		strokeInfo = self.generateStrokeInfo(name, strokePath)
		strokePosition = StrokePosition(startPoint, strokeBoundPane)
		return Stroke(strokeInfo, strokePosition)

