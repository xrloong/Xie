from xie.graphics.stroke import BeelineSegment
from xie.graphics.stroke import QCurveSegment
from xie.graphics.stroke import StrokePath
from xie.graphics.stroke import XieStroke

class StrokeFactory:
	def __init__(self):
		pass

	def _generateSegment_Horizontal(self, length):
		return BeelineSegment((length, 0))

	def _generateSegment_Vertical(self, length):
		return BeelineSegment((0, length))

	def _generateSegment_Slash(self, lengthWidth, lengthHeight):
		return BeelineSegment((lengthWidth, lengthHeight))


	# 如：肅的第六筆畫的最後一段
	def _generateSegment_ToLeft(self, length):
		return self._generateSegment_Horizontal(-length)

	# 如：一
	def _generateSegment_ToRight(self, length):
		return self._generateSegment_Horizontal(length)

	# 如：乚的最後一段
	def _generateSegment_ToUp(self, length):
		return self._generateSegment_Vertical(-length)

	# 如：中的最後一筆畫
	def _generateSegment_ToDown(self, length):
		return self._generateSegment_Vertical(length)

	# 如：了的第二筆的最後一段
	def _generateSegment_ToTopLeft(self, lengthWidth, lengthHeight):
		return self._generateSegment_Slash(-lengthWidth, -lengthHeight)

	# 如：氏的第二筆的最後一段
	def _generateSegment_ToTopRight(self, lengthWidth, lengthHeight):
		return self._generateSegment_Slash(lengthWidth, -lengthHeight)

	# 如：大的第二筆
	def _generateSegment_ToBottomLeft(self, lengthWidth, lengthHeight):
		return self._generateSegment_Slash(-lengthWidth, lengthHeight)

	# 如：大的第三筆
	def _generateSegment_ToBottomRight(self, lengthWidth, lengthHeight):
		return self._generateSegment_Slash(lengthWidth, lengthHeight)


	def _generateStrokePath橫(self, length):
		segment=self._generateSegment_ToRight(length)
		return StrokePath([segment])

	def generateStroke橫(self, startPoint, length):
		strokePath=self._generateStrokePath橫(length)
		return XieStroke(startPoint, strokePath)

	def _generateStrokePath豎(self, length):
		segment=self._generateSegment_ToDown(length)
		return StrokePath([segment])

	def generateStroke豎(self, startPoint, length):
		strokePath=self._generateStrokePath豎(length)
		return XieStroke(startPoint, strokePath)

	def _generateStrokePath撇(self, lengthWidth, lengthHeight):
		segment=self._generateSegment_ToBottomLeft(lengthWidth, lengthHeight)
		return StrokePath([segment])

	def generateStroke撇(self, startPoint, lengthWidth, lengthHeight):
		strokePath=self._generateStrokePath撇(lengthWidth, lengthHeight)
		return XieStroke(startPoint, strokePath)

	def _generateStrokePath捺(self, lengthWidth, lengthHeight):
		segment=self._generateSegment_ToBottomRight(lengthWidth, lengthHeight)
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

