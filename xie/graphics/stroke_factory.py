from xie.graphics.stroke import BeelineSegment
from xie.graphics.stroke import QCurveSegment
from xie.graphics.stroke import StrokePath
from xie.graphics.stroke import XieStroke

class StrokeFactory:
	def __init__(self):
		from xie.graphics.stroke import SegmentFactory
		self.segmentFactory = SegmentFactory()


	def _generateStrokePath橫(self, length):
		segment=self.segmentFactory.generateSegment_右(length)
		return StrokePath([segment])

	def generateStroke橫(self, startPoint, length):
		strokePath=self._generateStrokePath橫(length)
		return XieStroke(startPoint, strokePath)

	def _generateStrokePath豎(self, length):
		segment=self._generateSegment_ToDown(length)
		return StrokePath([segment])

	def generateStroke豎(self, startPoint, length):
		strokePath=self.segmentFactory.generateSegment_下(length)
		return XieStroke(startPoint, strokePath)

	def _generateStrokePath撇(self, lengthWidth, lengthHeight):
		segment=self.segmentFactory.generateSegment_左下(lengthWidth, lengthHeight)
		return StrokePath([segment])

	def generateStroke撇(self, startPoint, lengthWidth, lengthHeight):
		strokePath=self._generateStrokePath撇(lengthWidth, lengthHeight)
		return XieStroke(startPoint, strokePath)

	def _generateStrokePath捺(self, lengthWidth, lengthHeight):
		segment=self.segmentFactory.generateSegment_右下(lengthWidth, lengthHeight)
		return StrokePath([segment])

	def generateStroke捺(self, startPoint, lengthWidth, lengthHeight):
		strokePath=self._generateStrokePath捺(lengthWidth, lengthHeight)
		return XieStroke(startPoint, strokePath)

	def _generateStrokePath圈(self, width, height):
		halfWidth=width/2
		halfHeight=height/2
		center=(0, halfHeight)

		segment1=QCurveSegment((halfWidth, 0), (halfWidth, halfHeight))
		segment2=QCurveSegment((0, halfHeight), (-halfWidth, halfHeight))
		segment3=QCurveSegment((-halfWidth, 0), (-halfWidth, -halfHeight))
		segment4=QCurveSegment((0, -halfHeight), (halfWidth, -halfHeight))
		return StrokePath([segment1, segment2, segment3, segment4])

	def generateStroke圈(self, startPoint, width, height):
		strokePath=self._generateStrokePath圈(width, height)
		return XieStroke(startPoint, strokePath)

_StrokeFactory=StrokeFactory()

def getInstance():
	return _StrokeFactory

