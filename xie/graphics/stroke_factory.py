from xie.graphics.stroke import BeelineSegment
from xie.graphics.stroke import StrokePath
from xie.graphics.stroke import Stroke

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
		return Stroke(startPoint, strokePath)

	def _generateStrokePath豎(self, length):
		segment=self._generateSegment_ToDown(length)
		return StrokePath([segment])

	def generateStroke豎(self, startPoint, length):
		strokePath=self._generateStrokePath豎(length)
		return Stroke(startPoint, strokePath)

_StrokeFactory=StrokeFactory()

def getInstance():
	return _StrokeFactory

