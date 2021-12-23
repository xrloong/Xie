from .stroke import Stroke, StrokePosition
from .component import Component, ComponentInfo
from .stroke_path import *

from .shape import Pane

from .layout import JointOperator
from .layout import LayoutSpec

def _splitLengthToList(length, weightList):
	totalWeight=sum(weightList)
	unitLength=length*1./totalWeight

	pointList=[]
	newComponentList=[]
	base=0
	for weight in weightList:
		pointList.append(int(base))
		base=base+unitLength*weight
	pointList.append(int(base))
	return pointList

def genVerticalPanes(weights, containerPane):
	pane = containerPane
	points=_splitLengthToList(pane.height, weights)
	paneList=[]
	offset=pane.top
	for [pointStart, pointEnd] in zip(points[:-1], points[1:]):
		height=pointEnd-pointStart
		targetHeight=int(height*0.90)
		offset=int(height-targetHeight)//2
		tmpPane=Pane(pane.left, pointStart+offset, pane.right, pointEnd-offset)
		tmpPane._offsetTopAndBottom(offset)
		paneList.append(tmpPane)
	return paneList

def genHorizontalPanes(weights, containerPane):
	pane = containerPane
	points=_splitLengthToList(pane.width, weights)
	paneList=[]
	offset=pane.left
	for [pointStart, pointEnd] in zip(points[:-1], points[1:]):
		width=pointEnd-pointStart
		targetWidth=int(width*0.90)
		offset=int(width-targetWidth)//2
		tmpPane=Pane(pointStart+offset, pane.top, pointEnd-offset, pane.bottom)
		tmpPane._offsetLeftAndRight(offset)
		paneList.append(tmpPane)
	return paneList
class ShapeFactory:
	# 字面框（Bounding Box）
	BBOX_X_MIN = 0x08
	BBOX_Y_MIN = 0x08
	BBOX_X_MAX = 0xF7
	BBOX_Y_MAX = 0xF7

	DefaultBox = Pane(
		BBOX_X_MIN,
		BBOX_Y_MIN,
		BBOX_X_MAX,
		BBOX_Y_MAX,
	)

	def __init__(self):
		pass

	def generateLayouts(self, spec: LayoutSpec) -> [Pane]:
		operator = spec.operator
		if operator == JointOperator.Goose:
			return genHorizontalPanes(spec.weights, ShapeFactory.DefaultBox)
		if operator == JointOperator.Silkworm:
			return genVerticalPanes(spec.weights, ShapeFactory.DefaultBox)

		if spec.containerPane and spec.subPanes:
			return [spec.containerPane] + spec.subPanes

		return []

class StrokeSpec:
	def __init__(self, typeName, parameters = None, segments = None,
			splinePointsList = None):
		self.typeName = typeName
		self.parameters = parameters
		self.segments = segments

		if splinePointsList:
			lastEndPoint = (0, 0)
			relativeControlPointsList = []
			for points in splinePointsList:
				newPoints = [(point[0] - lastEndPoint[0], point[1] - lastEndPoint[1]) for point in points]
				relativeControlPointsList.append(newPoints)
				lastEndPoint = points[-1]

			self.relativeControlPointsList = relativeControlPointsList
			self.absoluteControlPointsList = splinePointsList
		else:
			self.relativeControlPointsList = None
			self.absoluteControlPointsList = None

	def isBySegments(self):
		return (self.segments != None)

	def isByControlPoints(self):
		return (self.relativeControlPointsList != None)

class StrokeFactory:
	def __init__(self):
		from .segment import SegmentFactory

		segmentFactory = SegmentFactory()
		self.segmentFactory = segmentFactory
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


			"橫撇彎鉤": StrokePathGenerator_橫撇彎鉤(segmentFactory),
			"豎彎折": StrokePathGenerator_豎彎折(segmentFactory),
		}

	# StrokePath
	def generateStrokePathBySpec(self, spec: StrokeSpec):
		if spec.isBySegments():
			segments = spec.segments
			strokePath = StrokePath(segments)
		elif spec.isByControlPoints():
			segmentFactory = self.segmentFactory

			# Start at (0, 0)
			# Format:
			# [
			#     [(x, y)],
			#     [(x, y), (x,y)],
			# ]
			controlPointsList = spec.relativeControlPointsList

			segments = []
			controlPoint = None
			for points in controlPointsList:
				segmentCount = len(points)
				if segmentCount == 2:
					# 二次貝茲曲線
					segment = segmentFactory.generateSegment_QCurve(points[0], points[1])
				elif segmentCount == 1:
					# 一次貝茲曲線、線性
					segment = segmentFactory.generateSegment_Beeline(points[0])
				else:
					assert False
				segments.append(segment)
			strokePath = StrokePath(segments)
		else:
			strokeTypeName = spec.typeName
			parameters = spec.parameters

			strokePathGenerator = self.strokePathMap.get(strokeTypeName, None)
			assert strokePathGenerator!=None

			strokePath = strokePathGenerator.generate(parameters)
		return strokePath

	# Stroke
	def _generateStroke(self, name, strokePath, strokeBoundPane):
		infoPane = strokePath.pane
		startPoint = infoPane.transformRelativePointByTargetPane((0, 0), strokeBoundPane)

		strokePosition = StrokePosition(startPoint, strokeBoundPane)
		return Stroke(name, strokePath, strokePosition)

	def generateStrokeBySpec(self, spec: StrokeSpec, startPoint = None, strokeBoundPane = None):
		strokeTypeName = spec.typeName
		strokePath = self.generateStrokePathBySpec(spec)
		if spec.isBySegments():
			boundary = strokePath.computeBoundaryWithStartPoint(startPoint)
			pane = Pane(*boundary)

			return self._generateStroke(strokeTypeName, strokePath, pane)
		else:
			assert startPoint != None or strokeBoundPane != None

			if startPoint:
				boundary = strokePath.computeBoundaryWithStartPoint(startPoint)
				strokeBoundPane = Pane(*boundary)
			else:
				infoPane = strokePath.pane
				startPoint = infoPane.transformRelativePointByTargetPane((0, 0), strokeBoundPane)

			return self._generateStroke(strokeTypeName, strokePath, strokeBoundPane)

class ComponentFactory:
	def __init__(self):
		pass

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

