import unittest
import copy

from xie.graphics.segment import BeelineSegment
from xie.graphics.segment import QCurveSegment
from xie.graphics.segment import SegmentFactory
from xie.graphics.stroke_path import StrokePath
from xie.graphics.stroke import Stroke
from xie.graphics.stroke import StrokeInfo
from xie.graphics.stroke import StrokePosition
from xie.graphics.factory import ShapeFactory
from xie.graphics.factory import StrokeFactory

from xie.graphics.canvas import EncodedTextCanvasController
from xie.graphics.drawing import DrawingSystem

class FactoryTestCase(unittest.TestCase):
	def setUp(self):
		self.segmentFactory = SegmentFactory()
		self.shapeFactory = ShapeFactory()
		self.generateTestDataSegments()

	def tearDown(self):
		pass

	def generateTestDataSegments(self):
		self.segments_點_1=self.segmentFactory.generateSegments_點(80, 144)
		self.segments_點_2=self.segmentFactory.generateSegments_點(-63, -85)
		self.segments_點_3=self.segmentFactory.generateSegments_點(8, 34)
		self.segments_點_4=self.segmentFactory.generateSegments_點(-66, 110)
		self.segments_點_1_r=[
			BeelineSegment((80, 144))
		]
		self.segments_點_2_r=[
			BeelineSegment((-63, -85))
		]
		self.segments_點_3_r=[
			BeelineSegment((8, 34))
		]
		self.segments_點_4_r=[
			BeelineSegment((-66, 110))
		]

		self.segments_圈_1=self.segmentFactory.generateSegments_圈(90, 63)
		self.segments_圈_2=self.segmentFactory.generateSegments_圈(70, 107)
		self.segments_圈_3=self.segmentFactory.generateSegments_圈(122, 105)
		self.segments_圈_4=self.segmentFactory.generateSegments_圈(57, 99)
		self.segments_圈_1_r=[
			QCurveSegment((90, 0), (90, 63)),
			QCurveSegment((0, 63), (-90, 63)),
			QCurveSegment((-90, 0), (-90, -63)),
			QCurveSegment((0, -63), (90, -63))
		]
		self.segments_圈_2_r=[
			QCurveSegment((70, 0), (70, 107)),
			QCurveSegment((0, 107), (-70, 107)),
			QCurveSegment((-70, 0), (-70, -107)),
			QCurveSegment((0, -107), (70, -107))
		]
		self.segments_圈_3_r=[
			QCurveSegment((122, 0), (122, 105)),
			QCurveSegment((0, 105), (-122, 105)),
			QCurveSegment((-122, 0), (-122, -105)),
			QCurveSegment((0, -105), (122, -105))
		]
		self.segments_圈_4_r=[
			QCurveSegment((57, 0), (57, 99)),
			QCurveSegment((0, 99), (-57, 99)),
			QCurveSegment((-57, 0), (-57, -99)),
			QCurveSegment((0, -99), (57, -99))
		]

		self.segments_橫_1=self.segmentFactory.generateSegments_橫(90)
		self.segments_橫_2=self.segmentFactory.generateSegments_橫(84)
		self.segments_橫_3=self.segmentFactory.generateSegments_橫(127)
		self.segments_橫_4=self.segmentFactory.generateSegments_橫(48)
		self.segments_橫_1_r=[
			BeelineSegment((90, 0))
		]
		self.segments_橫_2_r=[
			BeelineSegment((84, 0))
		]
		self.segments_橫_3_r=[
			BeelineSegment((127, 0))
		]
		self.segments_橫_4_r=[
			BeelineSegment((48, 0))
		]

		self.segments_豎_1=self.segmentFactory.generateSegments_豎(30)
		self.segments_豎_2=self.segmentFactory.generateSegments_豎(88)
		self.segments_豎_3=self.segmentFactory.generateSegments_豎(53)
		self.segments_豎_4=self.segmentFactory.generateSegments_豎(102)
		self.segments_豎_1_r=[
			BeelineSegment((0, 30))
		]
		self.segments_豎_2_r=[
			BeelineSegment((0, 88))
		]
		self.segments_豎_3_r=[
			BeelineSegment((0, 53))
		]
		self.segments_豎_4_r=[
			BeelineSegment((0, 102))
		]

		self.segments_左_1=self.segmentFactory.generateSegments_左(4)
		self.segments_左_2=self.segmentFactory.generateSegments_左(94)
		self.segments_左_3=self.segmentFactory.generateSegments_左(116)
		self.segments_左_4=self.segmentFactory.generateSegments_左(79)
		self.segments_左_1_r=[
			BeelineSegment((-4, 0))
		]
		self.segments_左_2_r=[
			BeelineSegment((-94, 0))
		]
		self.segments_左_3_r=[
			BeelineSegment((-116, 0))
		]
		self.segments_左_4_r=[
			BeelineSegment((-79, 0))
		]

		self.segments_上_1=self.segmentFactory.generateSegments_上(33)
		self.segments_上_2=self.segmentFactory.generateSegments_上(28)
		self.segments_上_3=self.segmentFactory.generateSegments_上(24)
		self.segments_上_4=self.segmentFactory.generateSegments_上(47)
		self.segments_上_1_r=[
			BeelineSegment((0, -33))
		]
		self.segments_上_2_r=[
			BeelineSegment((0, -28))
		]
		self.segments_上_3_r=[
			BeelineSegment((0, -24))
		]
		self.segments_上_4_r=[
			BeelineSegment((0, -47))
		]

		self.segments_提_1=self.segmentFactory.generateSegments_提(33, 103)
		self.segments_提_2=self.segmentFactory.generateSegments_提(46, 78)
		self.segments_提_3=self.segmentFactory.generateSegments_提(73, 127)
		self.segments_提_4=self.segmentFactory.generateSegments_提(120, 74)
		self.segments_提_1_r=[
			BeelineSegment((33, -103))
		]
		self.segments_提_2_r=[
			BeelineSegment((46, -78))
		]
		self.segments_提_3_r=[
			BeelineSegment((73, -127))
		]
		self.segments_提_4_r=[
			BeelineSegment((120, -74))
		]


		self.segments_捺_1=self.segmentFactory.generateSegments_捺(70, 101)
		self.segments_捺_2=self.segmentFactory.generateSegments_捺(115, 122)
		self.segments_捺_3=self.segmentFactory.generateSegments_捺(17, 109)
		self.segments_捺_4=self.segmentFactory.generateSegments_捺(25, 33)
		self.segments_捺_1_r=[
			QCurveSegment((2, 73), (70, 101))
		]
		self.segments_捺_2_r=[
			QCurveSegment((17, 99), (115, 122))
		]
		self.segments_捺_3_r=[
			QCurveSegment((0.0, 55.0), (17, 109))
		]
		self.segments_捺_4_r=[
			QCurveSegment((1, 24), (25, 33))
		]

		self.segments_撇_1=self.segmentFactory.generateSegments_撇(46, 39)
		self.segments_撇_2=self.segmentFactory.generateSegments_撇(46, 13)
		self.segments_撇_3=self.segmentFactory.generateSegments_撇(35, 38)
		self.segments_撇_4=self.segmentFactory.generateSegments_撇(72, 14)
		self.segments_撇_1_r=[
			BeelineSegment((-46, 39))
		]
		self.segments_撇_2_r=[
			BeelineSegment((-46, 13))
		]
		self.segments_撇_3_r=[
			BeelineSegment((-35, 38))
		]
		self.segments_撇_4_r=[
			BeelineSegment((-72, 14))
		]

		self.segments_鉤_1=self.segmentFactory.generateSegments_鉤(29, 118)
		self.segments_鉤_2=self.segmentFactory.generateSegments_鉤(120, 91)
		self.segments_鉤_3=self.segmentFactory.generateSegments_鉤(73, 17)
		self.segments_鉤_4=self.segmentFactory.generateSegments_鉤(44, 50)
		self.segments_鉤_1_r=[
			BeelineSegment((-29, -118))
		]
		self.segments_鉤_2_r=[
			BeelineSegment((-120, -91))
		]
		self.segments_鉤_3_r=[
			BeelineSegment((-73, -17))
		]
		self.segments_鉤_4_r=[
			BeelineSegment((-44, -50))
		]

		self.segments_臥捺_1=self.segmentFactory.generateSegments_臥捺(73, 19)
		self.segments_臥捺_2=self.segmentFactory.generateSegments_臥捺(104, 60)
		self.segments_臥捺_3=self.segmentFactory.generateSegments_臥捺(36, 94)
		self.segments_臥捺_4=self.segmentFactory.generateSegments_臥捺(104, 63)
		self.segments_臥捺_1_r=[
			QCurveSegment((20, -5), (36, 9)),
			QCurveSegment((16, 13), (36, 9))
		]
		self.segments_臥捺_2_r=[
			QCurveSegment((33, 2), (52, 30)),
			QCurveSegment((19, 28), (52, 30))
		]
		self.segments_臥捺_3_r=[
			QCurveSegment((20, 19), (18, 47)),
			QCurveSegment((-2, 27), (18, 47))
		]
		self.segments_臥捺_4_r=[
			QCurveSegment((33, 2), (52, 31)),
			QCurveSegment((19, 28), (52, 31))
		]

		self.segments_豎撇_1=self.segmentFactory.generateSegments_豎撇(17, 69, 17)
		self.segments_豎撇_2=self.segmentFactory.generateSegments_豎撇(83, 108, 28)
		self.segments_豎撇_3=self.segmentFactory.generateSegments_豎撇(25, 42, 121)
		self.segments_豎撇_4=self.segmentFactory.generateSegments_豎撇(26, 43, 118)
		self.segments_豎撇_1_r=[
			BeelineSegment((0, 69)),
			QCurveSegment((0, 17), (-17, 17))
		]
		self.segments_豎撇_2_r=[
			BeelineSegment((0, 108)),
			QCurveSegment((0, 28), (-83, 28))
		]
		self.segments_豎撇_3_r=[
			BeelineSegment((0, 42)),
			QCurveSegment((0, 121), (-25, 121))
		]
		self.segments_豎撇_4_r=[
			BeelineSegment((0, 43)),
			QCurveSegment((0, 118), (-26, 118))
		]

		self.segments_彎鉤之彎_1=self.segmentFactory.generateSegments_彎鉤之彎(51, 22)
		self.segments_彎鉤之彎_2=self.segmentFactory.generateSegments_彎鉤之彎(79, 45)
		self.segments_彎鉤之彎_3=self.segmentFactory.generateSegments_彎鉤之彎(35, 22)
		self.segments_彎鉤之彎_4=self.segmentFactory.generateSegments_彎鉤之彎(52, 74)
		self.segments_彎鉤之彎_1_r=[
			QCurveSegment((36, -14), [51, 22])
		]
		self.segments_彎鉤之彎_2_r=[
			QCurveSegment((61, -17), [79, 45])
		]
		self.segments_彎鉤之彎_3_r=[
			QCurveSegment((28, -6), [35, 22])
		]
		self.segments_彎鉤之彎_4_r=[
			QCurveSegment((63, 11), [52, 74])
		]

		self.segments_撇鉤之撇_1=self.segmentFactory.generateSegments_撇鉤之撇(47, 14)
		self.segments_撇鉤之撇_2=self.segmentFactory.generateSegments_撇鉤之撇(119, 10)
		self.segments_撇鉤之撇_3=self.segmentFactory.generateSegments_撇鉤之撇(40, 47)
		self.segments_撇鉤之撇_4=self.segmentFactory.generateSegments_撇鉤之撇(109, 54)
		self.segments_撇鉤之撇_1_r=[
			QCurveSegment((0, 14), (-47, 14))
		]
		self.segments_撇鉤之撇_2_r=[
			QCurveSegment((0, 10), (-119, 10))
		]
		self.segments_撇鉤之撇_3_r=[
			QCurveSegment((0, 47), (-40, 47))
		]
		self.segments_撇鉤之撇_4_r=[
			QCurveSegment((0, 54), (-109, 54))
		]

		self.segments_斜鉤之斜_1=self.segmentFactory.generateSegments_斜鉤之斜(120, 127)
		self.segments_斜鉤之斜_2=self.segmentFactory.generateSegments_斜鉤之斜(97, 87)
		self.segments_斜鉤之斜_3=self.segmentFactory.generateSegments_斜鉤之斜(57, 85)
		self.segments_斜鉤之斜_4=self.segmentFactory.generateSegments_斜鉤之斜(99, 12)
		self.segments_斜鉤之斜_1_r=[
			QCurveSegment((24, 101), (120, 127))
		]
		self.segments_斜鉤之斜_2_r=[
			QCurveSegment((19, 69), (97, 87))
		]
		self.segments_斜鉤之斜_3_r=[
			QCurveSegment((11, 68), (57, 85))
		]
		self.segments_斜鉤之斜_4_r=[
			QCurveSegment((19, 9), (99, 12))
		]

		self.segments_曲_1=self.segmentFactory.generateSegments_曲(5)
		self.segments_曲_2=self.segmentFactory.generateSegments_曲(42)
		self.segments_曲_3=self.segmentFactory.generateSegments_曲(73)
		self.segments_曲_4=self.segmentFactory.generateSegments_曲(1)
		self.segments_曲_1_r=[
			QCurveSegment([0, 5], [5, 5])
		]
		self.segments_曲_2_r=[
			QCurveSegment([0, 42], [42, 42])
		]
		self.segments_曲_3_r=[
			QCurveSegment([0, 73], [73, 73])
		]
		self.segments_曲_4_r=[
			QCurveSegment([0, 1], [1, 1])
		]

		self.segments_撇曲_1=self.segmentFactory.generateSegments_撇曲(80, 102, 93, 5)
		self.segments_撇曲_2=self.segmentFactory.generateSegments_撇曲(44, 116, 7, 25)
		self.segments_撇曲_3=self.segmentFactory.generateSegments_撇曲(91, 29, 102, 4)
		self.segments_撇曲_4=self.segmentFactory.generateSegments_撇曲(36, 26, 116, 64)
		self.segments_撇曲_1_r=[
			BeelineSegment([-75, 87]),
			QCurveSegment((-5, 6), (0, 6)),
			BeelineSegment((177, 0))
		]
		self.segments_撇曲_2_r=[
			BeelineSegment([-19, 3]),
			QCurveSegment((-25, 4), (0, 4)),
			BeelineSegment((135, 0))
		]
		self.segments_撇曲_3_r=[
			BeelineSegment([-87, 97]),
			QCurveSegment((-4, 5), (0, 5)),
			BeelineSegment((116, 0))
		]
		self.segments_撇曲_4_r=[
			BeelineSegment([28, -91]),
			QCurveSegment((-64, 207), (0, 207)),
			BeelineSegment((-2, 0))
		]

	def testSegments_點(self):
		self.assertEqual(self.segments_點_1, self.segments_點_1_r)
		self.assertEqual(self.segments_點_2, self.segments_點_2_r)
		self.assertEqual(self.segments_點_3, self.segments_點_3_r)
		self.assertEqual(self.segments_點_4, self.segments_點_4_r)

	def testSegments_圈(self):
		self.assertEqual(self.segments_圈_1, self.segments_圈_1_r)
		self.assertEqual(self.segments_圈_2, self.segments_圈_2_r)
		self.assertEqual(self.segments_圈_3, self.segments_圈_3_r)
		self.assertEqual(self.segments_圈_4, self.segments_圈_4_r)

	def testSegments_橫(self):
		self.assertEqual(self.segments_橫_1, self.segments_橫_1_r)
		self.assertEqual(self.segments_橫_2, self.segments_橫_2_r)
		self.assertEqual(self.segments_橫_3, self.segments_橫_3_r)
		self.assertEqual(self.segments_橫_4, self.segments_橫_4_r)

	def testSegments_豎(self):
		self.assertEqual(self.segments_豎_1, self.segments_豎_1_r)
		self.assertEqual(self.segments_豎_2, self.segments_豎_2_r)
		self.assertEqual(self.segments_豎_3, self.segments_豎_3_r)
		self.assertEqual(self.segments_豎_4, self.segments_豎_4_r)

	def testSegments_左(self):
		self.assertEqual(self.segments_左_1, self.segments_左_1_r)
		self.assertEqual(self.segments_左_2, self.segments_左_2_r)
		self.assertEqual(self.segments_左_3, self.segments_左_3_r)
		self.assertEqual(self.segments_左_4, self.segments_左_4_r)

	def testSegments_上(self):
		self.assertEqual(self.segments_上_1, self.segments_上_1_r)
		self.assertEqual(self.segments_上_2, self.segments_上_2_r)
		self.assertEqual(self.segments_上_3, self.segments_上_3_r)
		self.assertEqual(self.segments_上_4, self.segments_上_4_r)

	def testSegments_提(self):
		self.assertEqual(self.segments_提_1, self.segments_提_1_r)
		self.assertEqual(self.segments_提_2, self.segments_提_2_r)
		self.assertEqual(self.segments_提_3, self.segments_提_3_r)
		self.assertEqual(self.segments_提_4, self.segments_提_4_r)

	def testSegments_捺(self):
		self.assertEqual(self.segments_捺_1, self.segments_捺_1_r)
		self.assertEqual(self.segments_捺_2, self.segments_捺_2_r)
		self.assertEqual(self.segments_捺_3, self.segments_捺_3_r)
		self.assertEqual(self.segments_捺_4, self.segments_捺_4_r)

	def testSegments_撇(self):
		self.assertEqual(self.segments_撇_1, self.segments_撇_1_r)
		self.assertEqual(self.segments_撇_2, self.segments_撇_2_r)
		self.assertEqual(self.segments_撇_3, self.segments_撇_3_r)
		self.assertEqual(self.segments_撇_4, self.segments_撇_4_r)

	def testSegments_鉤(self):
		self.assertEqual(self.segments_鉤_1, self.segments_鉤_1_r)
		self.assertEqual(self.segments_鉤_2, self.segments_鉤_2_r)
		self.assertEqual(self.segments_鉤_3, self.segments_鉤_3_r)
		self.assertEqual(self.segments_鉤_4, self.segments_鉤_4_r)

	def testSegments_臥捺(self):
		self.assertEqual(self.segments_臥捺_1, self.segments_臥捺_1_r)
		self.assertEqual(self.segments_臥捺_2, self.segments_臥捺_2_r)
		self.assertEqual(self.segments_臥捺_3, self.segments_臥捺_3_r)
		self.assertEqual(self.segments_臥捺_4, self.segments_臥捺_4_r)

	def testSegments_豎撇(self):
		self.assertEqual(self.segments_豎撇_1, self.segments_豎撇_1_r)
		self.assertEqual(self.segments_豎撇_2, self.segments_豎撇_2_r)
		self.assertEqual(self.segments_豎撇_3, self.segments_豎撇_3_r)
		self.assertEqual(self.segments_豎撇_4, self.segments_豎撇_4_r)

	def testSegments_彎鉤之彎(self):
		self.assertEqual(self.segments_彎鉤之彎_1, self.segments_彎鉤之彎_1_r)
		self.assertEqual(self.segments_彎鉤之彎_2, self.segments_彎鉤之彎_2_r)
		self.assertEqual(self.segments_彎鉤之彎_3, self.segments_彎鉤之彎_3_r)
		self.assertEqual(self.segments_彎鉤之彎_4, self.segments_彎鉤之彎_4_r)

	def testSegments_撇鉤之撇(self):
		self.assertEqual(self.segments_撇鉤之撇_1, self.segments_撇鉤之撇_1_r)
		self.assertEqual(self.segments_撇鉤之撇_2, self.segments_撇鉤之撇_2_r)
		self.assertEqual(self.segments_撇鉤之撇_3, self.segments_撇鉤之撇_3_r)
		self.assertEqual(self.segments_撇鉤之撇_4, self.segments_撇鉤之撇_4_r)

	def testSegments_斜鉤之斜(self):
		self.assertEqual(self.segments_斜鉤之斜_1, self.segments_斜鉤之斜_1_r)
		self.assertEqual(self.segments_斜鉤之斜_2, self.segments_斜鉤之斜_2_r)
		self.assertEqual(self.segments_斜鉤之斜_3, self.segments_斜鉤之斜_3_r)
		self.assertEqual(self.segments_斜鉤之斜_4, self.segments_斜鉤之斜_4_r)

	def testSegments_曲(self):
		self.assertEqual(self.segments_曲_1, self.segments_曲_1_r)
		self.assertEqual(self.segments_曲_2, self.segments_曲_2_r)
		self.assertEqual(self.segments_曲_3, self.segments_曲_3_r)
		self.assertEqual(self.segments_曲_4, self.segments_曲_4_r)

	def testSegments_撇曲(self):
		self.assertEqual(self.segments_撇曲_1, self.segments_撇曲_1_r)
		self.assertEqual(self.segments_撇曲_2, self.segments_撇曲_2_r)
		self.assertEqual(self.segments_撇曲_3, self.segments_撇曲_3_r)
		self.assertEqual(self.segments_撇曲_4, self.segments_撇曲_4_r)

class StrokeFactoryTestCase(unittest.TestCase):
	def setUp(self):
		self.strokeFactory = StrokeFactory()
		self.generateTestDataStrokePaths()

		self.controller = EncodedTextCanvasController()
		self.ds = DrawingSystem(self.controller)

	def tearDown(self):
		pass

	def generateStrokePath(self, name, params):
		return self.strokeFactory.generateStrokePathByParameters(name, params)

	def _generateStroke(self, strokePath):
		strokeInfo = StrokeInfo("測試", strokePath)
		return Stroke(strokeInfo, StrokePosition((0, 0), strokePath.pane))

	def _getDrawResultForStrokePath(self, strokePath):
		stroke = self._generateStroke(strokePath)

		self.ds.draw(stroke)
		return self.controller.getStrokeExpression()

	def generateTestDataStrokePaths(self):
		self.strokePath_點_1 = self.generateStrokePath("點", (5, 95))
		self.strokePath_點_2 = self.generateStrokePath("點", (20, 122))
		self.strokePath_點_3 = self.generateStrokePath("點", (125, 46))
		self.strokePath_點_4 = self.generateStrokePath("點", (14, 16))

		self.strokePath_圈_1 = self.generateStrokePath("圈", (6, 126))
		self.strokePath_圈_2 = self.generateStrokePath("圈", (53, 83))
		self.strokePath_圈_3 = self.generateStrokePath("圈", (21, 72))
		self.strokePath_圈_4 = self.generateStrokePath("圈", (99, 41))

		self.strokePath_橫_1 = self.generateStrokePath("橫", (30,))
		self.strokePath_橫_2 = self.generateStrokePath("橫", (124,))
		self.strokePath_橫_3 = self.generateStrokePath("橫", (13,))
		self.strokePath_橫_4 = self.generateStrokePath("橫", (105,))

		self.strokePath_橫鉤_1 = self.generateStrokePath("橫鉤", (103, 125, 68))
		self.strokePath_橫鉤_2 = self.generateStrokePath("橫鉤", (81, 38, 54))
		self.strokePath_橫鉤_3 = self.generateStrokePath("橫鉤", (72, 3, 124))
		self.strokePath_橫鉤_4 = self.generateStrokePath("橫鉤", (94, 74, 35))

		self.strokePath_橫折_1 = self.generateStrokePath("橫折", (72, 122))
		self.strokePath_橫折_2 = self.generateStrokePath("橫折", (113, 115))
		self.strokePath_橫折_3 = self.generateStrokePath("橫折", (46, 89))
		self.strokePath_橫折_4 = self.generateStrokePath("橫折", (121, 123))

		self.strokePath_橫折折_1 = self.generateStrokePath("橫折折", (94, 34, 33))
		self.strokePath_橫折折_2 = self.generateStrokePath("橫折折", (33, 6, 40))
		self.strokePath_橫折折_3 = self.generateStrokePath("橫折折", (30, 115, 19))
		self.strokePath_橫折折_4 = self.generateStrokePath("橫折折", (105, 43, 53))

		self.strokePath_橫折提_1 = self.generateStrokePath("橫折提", (32, 123, 58, 62))
		self.strokePath_橫折提_2 = self.generateStrokePath("橫折提", (107, 36, 73, 50))
		self.strokePath_橫折提_3 = self.generateStrokePath("橫折提", (86, 122, 46, 90))
		self.strokePath_橫折提_4 = self.generateStrokePath("橫折提", (55, 38, 4, 121))

		self.strokePath_橫折折撇_1 = self.generateStrokePath("橫折折撇", (64, 123, 53, 44, 47, 7))
		self.strokePath_橫折折撇_2 = self.generateStrokePath("橫折折撇", (36, 104, 120, 46, 44, 107))
		self.strokePath_橫折折撇_3 = self.generateStrokePath("橫折折撇", (68, 46, 47, 21, 10, 101))
		self.strokePath_橫折折撇_4 = self.generateStrokePath("橫折折撇", (120, 20, 97, 6, 33, 91))

		self.strokePath_橫撇彎鉤_1 = self.generateStrokePath("橫撇彎鉤", (115, 113, 12, 16, 104, 4, 71))
		self.strokePath_橫撇彎鉤_2 = self.generateStrokePath("橫撇彎鉤", (79, 82, 52, 53, 111, 68, 97))
		self.strokePath_橫撇彎鉤_3 = self.generateStrokePath("橫撇彎鉤", (58, 62, 38, 99, 64, 53, 20))
		self.strokePath_橫撇彎鉤_4 = self.generateStrokePath("橫撇彎鉤", (38, 87, 100, 5, 122, 32, 47))

		self.strokePath_橫折鉤_1 = self.generateStrokePath("橫折鉤", (104, 35, 80, 29, 37))
		self.strokePath_橫折鉤_2 = self.generateStrokePath("橫折鉤", (32, 30, 20, 69, 73))
		self.strokePath_橫折鉤_3 = self.generateStrokePath("橫折鉤", (2, 46, 60, 101, 49))
		self.strokePath_橫折鉤_4 = self.generateStrokePath("橫折鉤", (82, 17, 82, 49, 52))

		self.strokePath_橫折彎_1 = self.generateStrokePath("橫折彎", (114, 84, 108, 5))
		self.strokePath_橫折彎_2 = self.generateStrokePath("橫折彎", (81, 64, 115, 1))
		self.strokePath_橫折彎_3 = self.generateStrokePath("橫折彎", (11, 43, 44, 2))
		self.strokePath_橫折彎_4 = self.generateStrokePath("橫折彎", (94, 94, 93, 60))

		self.strokePath_橫撇_1 = self.generateStrokePath("橫撇", (4, 90, 127))
		self.strokePath_橫撇_2 = self.generateStrokePath("橫撇", (26, 94, 42))
		self.strokePath_橫撇_3 = self.generateStrokePath("橫撇", (99, 124, 44))
		self.strokePath_橫撇_4 = self.generateStrokePath("橫撇", (16, 20, 82))

		self.strokePath_橫斜彎鉤_1 = self.generateStrokePath("橫斜彎鉤", (18, 99, 50, 93, 24, 5))
		self.strokePath_橫斜彎鉤_2 = self.generateStrokePath("橫斜彎鉤", (79, 34, 81, 112, 118, 11))
		self.strokePath_橫斜彎鉤_3 = self.generateStrokePath("橫斜彎鉤", (76, 31, 11, 123, 10, 107))
		self.strokePath_橫斜彎鉤_4 = self.generateStrokePath("橫斜彎鉤", (100, 77, 111, 107, 61, 123))

		self.strokePath_橫折折折鉤_1 = self.generateStrokePath("橫折折折鉤", (97, 67, 67, 41, 14, 69, 91, 2))
		self.strokePath_橫折折折鉤_2 = self.generateStrokePath("橫折折折鉤", (117, 123, 117, 102, 67, 44, 127, 53))
		self.strokePath_橫折折折鉤_3 = self.generateStrokePath("橫折折折鉤", (33, 81, 95, 65, 125, 125, 24, 41))
		self.strokePath_橫折折折鉤_4 = self.generateStrokePath("橫折折折鉤", (115, 111, 93, 99, 47, 76, 111, 43))

		self.strokePath_橫斜鉤_1 = self.generateStrokePath("橫斜鉤", (105, 22, 12, 14))
		self.strokePath_橫斜鉤_2 = self.generateStrokePath("橫斜鉤", (89, 87, 100, 43))
		self.strokePath_橫斜鉤_3 = self.generateStrokePath("橫斜鉤", (95, 30, 79, 106))
		self.strokePath_橫斜鉤_4 = self.generateStrokePath("橫斜鉤", (60, 6, 74, 64))

		self.strokePath_橫折折折_1 = self.generateStrokePath("橫折折折", (14, 97, 45, 63))
		self.strokePath_橫折折折_2 = self.generateStrokePath("橫折折折", (21, 32, 20, 15))
		self.strokePath_橫折折折_3 = self.generateStrokePath("橫折折折", (95, 4, 22, 11))
		self.strokePath_橫折折折_4 = self.generateStrokePath("橫折折折", (16, 29, 29, 101))

		self.strokePath_豎_1 = self.generateStrokePath("豎", (55,))
		self.strokePath_豎_2 = self.generateStrokePath("豎", (112,))
		self.strokePath_豎_3 = self.generateStrokePath("豎", (50,))
		self.strokePath_豎_4 = self.generateStrokePath("豎", (127,))

		self.strokePath_豎折_1 = self.generateStrokePath("豎折", (72, 84))
		self.strokePath_豎折_2 = self.generateStrokePath("豎折", (104, 7))
		self.strokePath_豎折_3 = self.generateStrokePath("豎折", (121, 75))
		self.strokePath_豎折_4 = self.generateStrokePath("豎折", (3, 15))

		self.strokePath_豎彎左_1 = self.generateStrokePath("豎彎左", (81, 25))
		self.strokePath_豎彎左_2 = self.generateStrokePath("豎彎左", (3, 24))
		self.strokePath_豎彎左_3 = self.generateStrokePath("豎彎左", (38, 101))
		self.strokePath_豎彎左_4 = self.generateStrokePath("豎彎左", (114, 76))

		self.strokePath_豎提_1 = self.generateStrokePath("豎提", (66, 65, 114))
		self.strokePath_豎提_2 = self.generateStrokePath("豎提", (27, 4, 54))
		self.strokePath_豎提_3 = self.generateStrokePath("豎提", (14, 72, 9))
		self.strokePath_豎提_4 = self.generateStrokePath("豎提", (25, 87, 99))

		self.strokePath_豎折折_1 = self.generateStrokePath("豎折折", (43, 91, 89))
		self.strokePath_豎折折_2 = self.generateStrokePath("豎折折", (81, 118, 25))
		self.strokePath_豎折折_3 = self.generateStrokePath("豎折折", (85, 59, 104))
		self.strokePath_豎折折_4 = self.generateStrokePath("豎折折", (39, 100, 32))

		self.strokePath_豎折彎鉤_1 = self.generateStrokePath("豎折彎鉤", (54, 96, 34, 73, 89, 53, 88))
		self.strokePath_豎折彎鉤_2 = self.generateStrokePath("豎折彎鉤", (116, 72, 112, 22, 25, 95, 39))
		self.strokePath_豎折彎鉤_3 = self.generateStrokePath("豎折彎鉤", (77, 37, 77, 25, 97, 71, 105))
		self.strokePath_豎折彎鉤_4 = self.generateStrokePath("豎折彎鉤", (75, 107, 78, 73, 35, 115, 102))

		self.strokePath_豎彎鉤_1 = self.generateStrokePath("豎彎鉤", (124, 94, 91, 80))
		self.strokePath_豎彎鉤_2 = self.generateStrokePath("豎彎鉤", (103, 122, 44, 90))
		self.strokePath_豎彎鉤_3 = self.generateStrokePath("豎彎鉤", (122, 124, 102, 49))
		self.strokePath_豎彎鉤_4 = self.generateStrokePath("豎彎鉤", (28, 123, 11, 9))

		self.strokePath_豎彎_1 = self.generateStrokePath("豎彎", (13, 76, 100))
		self.strokePath_豎彎_2 = self.generateStrokePath("豎彎", (56, 93, 3))
		self.strokePath_豎彎_3 = self.generateStrokePath("豎彎", (30, 127, 75))
		self.strokePath_豎彎_4 = self.generateStrokePath("豎彎", (40, 7, 95))

		self.strokePath_豎鉤_1 = self.generateStrokePath("豎鉤", (115, 21, 5))
		self.strokePath_豎鉤_2 = self.generateStrokePath("豎鉤", (110, 27, 10))
		self.strokePath_豎鉤_3 = self.generateStrokePath("豎鉤", (21, 109, 2))
		self.strokePath_豎鉤_4 = self.generateStrokePath("豎鉤", (77, 40, 2))

		self.strokePath_斜鉤_1 = self.generateStrokePath("斜鉤", (121, 18, 56))
		self.strokePath_斜鉤_2 = self.generateStrokePath("斜鉤", (64, 69, 70))
		self.strokePath_斜鉤_3 = self.generateStrokePath("斜鉤", (86, 15, 98))
		self.strokePath_斜鉤_4 = self.generateStrokePath("斜鉤", (68, 116, 68))

		self.strokePath_彎鉤_1 = self.generateStrokePath("彎鉤", (90, 114, 17, 38))
		self.strokePath_彎鉤_2 = self.generateStrokePath("彎鉤", (35, 96, 48, 127))
		self.strokePath_彎鉤_3 = self.generateStrokePath("彎鉤", (115, 55, 75, 110))
		self.strokePath_彎鉤_4 = self.generateStrokePath("彎鉤", (49, 99, 52, 125))

		self.strokePath_撇鉤_1 = self.generateStrokePath("撇鉤", (34, 30, 125, 114))
		self.strokePath_撇鉤_2 = self.generateStrokePath("撇鉤", (12, 83, 87, 59))
		self.strokePath_撇鉤_3 = self.generateStrokePath("撇鉤", (54, 69, 77, 64))
		self.strokePath_撇鉤_4 = self.generateStrokePath("撇鉤", (110, 31, 97, 121))

		self.strokePath_撇_1 = self.generateStrokePath("撇", (64, 100))
		self.strokePath_撇_2 = self.generateStrokePath("撇", (13, 120))
		self.strokePath_撇_3 = self.generateStrokePath("撇", (40, 91))
		self.strokePath_撇_4 = self.generateStrokePath("撇", (64, 68))

		self.strokePath_撇點_1 = self.generateStrokePath("撇點", (104, 96, 86, 60))
		self.strokePath_撇點_2 = self.generateStrokePath("撇點", (51, 18, 126, 64))
		self.strokePath_撇點_3 = self.generateStrokePath("撇點", (127, 93, 43, 11))
		self.strokePath_撇點_4 = self.generateStrokePath("撇點", (119, 121, 86, 120))

		self.strokePath_撇橫_1 = self.generateStrokePath("撇橫", (36, 42, 82, 5))
		self.strokePath_撇橫_2 = self.generateStrokePath("撇橫", (64, 34, 23, 110))
		self.strokePath_撇橫_3 = self.generateStrokePath("撇橫", (30, 121, 67, 75))
		self.strokePath_撇橫_4 = self.generateStrokePath("撇橫", (118, 48, 90, 115))

		self.strokePath_撇橫撇_1 = self.generateStrokePath("撇橫撇", (69, 71, 86, 20, 22))
		self.strokePath_撇橫撇_2 = self.generateStrokePath("撇橫撇", (72, 72, 21, 2, 2))
		self.strokePath_撇橫撇_3 = self.generateStrokePath("撇橫撇", (80, 52, 1, 37, 117))
		self.strokePath_撇橫撇_4 = self.generateStrokePath("撇橫撇", (21, 78, 40, 124, 46))

		self.strokePath_豎撇_1 = self.generateStrokePath("豎撇", (89, 12))
		self.strokePath_豎撇_2 = self.generateStrokePath("豎撇", (74, 10))
		self.strokePath_豎撇_3 = self.generateStrokePath("豎撇", (10, 65))
		self.strokePath_豎撇_4 = self.generateStrokePath("豎撇", (61, 71))

		self.strokePath_提_1 = self.generateStrokePath("提", (7, 17))
		self.strokePath_提_2 = self.generateStrokePath("提", (121, 62))
		self.strokePath_提_3 = self.generateStrokePath("提", (52, 93))
		self.strokePath_提_4 = self.generateStrokePath("提", (118, 3))

		self.strokePath_捺_1 = self.generateStrokePath("捺", (107, 63))
		self.strokePath_捺_2 = self.generateStrokePath("捺", (101, 27))
		self.strokePath_捺_3 = self.generateStrokePath("捺", (109, 55))
		self.strokePath_捺_4 = self.generateStrokePath("捺", (36, 125))

		self.strokePath_臥捺_1 = self.generateStrokePath("臥捺", (8, 53))
		self.strokePath_臥捺_2 = self.generateStrokePath("臥捺", (68, 6))
		self.strokePath_臥捺_3 = self.generateStrokePath("臥捺", (8, 39))
		self.strokePath_臥捺_4 = self.generateStrokePath("臥捺", (4, 15))

		self.strokePath_提捺_1 = self.generateStrokePath("提捺", (14, 43, 46, 43))
		self.strokePath_提捺_2 = self.generateStrokePath("提捺", (2, 26, 41, 66))
		self.strokePath_提捺_3 = self.generateStrokePath("提捺", (93, 18, 120, 6))
		self.strokePath_提捺_4 = self.generateStrokePath("提捺", (114, 10, 122, 61))

		self.strokePath_橫捺_1 = self.generateStrokePath("橫捺", (49, 17, 40))
		self.strokePath_橫捺_2 = self.generateStrokePath("橫捺", (64, 98, 91))
		self.strokePath_橫捺_3 = self.generateStrokePath("橫捺", (12, 26, 12))
		self.strokePath_橫捺_4 = self.generateStrokePath("橫捺", (4, 49, 124))

	def testStrokeInfo(self):
		strokePath = StrokeInfo("空", StrokePath([]))
		self.assertEqual(strokePath.getName(), "空")
		self.assertEqual(strokePath.getStrokePath(), StrokePath([]))

		segments=[BeelineSegment((37, 41)), QCurveSegment((0, -99), (57, -99))]
		strokePath = StrokeInfo("測試", StrokePath(segments))
		self.assertEqual(strokePath.getName(), "測試")
		self.assertEqual(strokePath.getStrokePath(), StrokePath(segments))

	def testStrokePath_點(self):
		self.assertEqual("0.0.0,1.5.95", self._getDrawResultForStrokePath(self.strokePath_點_1))
		self.assertEqual("0.0.0,1.20.122", self._getDrawResultForStrokePath(self.strokePath_點_2))
		self.assertEqual("0.0.0,1.125.46", self._getDrawResultForStrokePath(self.strokePath_點_3))
		self.assertEqual("0.0.0,1.14.16", self._getDrawResultForStrokePath(self.strokePath_點_4))

	def testStrokePath_圈(self):
		self.assertEqual("0.0.0,2.6.0,1.6.126,2.6.252,1.0.252,2.-6.252,1.-6.126,2.-6.0,1.0.0",
				self._getDrawResultForStrokePath(self.strokePath_圈_1))
		self.assertEqual("0.0.0,2.53.0,1.53.83,2.53.166,1.0.166,2.-53.166,1.-53.83,2.-53.0,1.0.0",
				self._getDrawResultForStrokePath(self.strokePath_圈_2))
		self.assertEqual("0.0.0,2.21.0,1.21.72,2.21.144,1.0.144,2.-21.144,1.-21.72,2.-21.0,1.0.0",
				self._getDrawResultForStrokePath(self.strokePath_圈_3))
		self.assertEqual("0.0.0,2.99.0,1.99.41,2.99.82,1.0.82,2.-99.82,1.-99.41,2.-99.0,1.0.0",
				self._getDrawResultForStrokePath(self.strokePath_圈_4))

	def testStrokePath_橫(self):
		self.assertEqual("0.0.0,1.30.0",
				self._getDrawResultForStrokePath(self.strokePath_橫_1))
		self.assertEqual("0.0.0,1.124.0",
				self._getDrawResultForStrokePath(self.strokePath_橫_2))
		self.assertEqual("0.0.0,1.13.0",
				self._getDrawResultForStrokePath(self.strokePath_橫_3))
		self.assertEqual("0.0.0,1.105.0",
				self._getDrawResultForStrokePath(self.strokePath_橫_4))

	def testStrokePath_橫鉤(self):
		self.assertEqual("0.0.0,1.103.0,1.-22.68",
				self._getDrawResultForStrokePath(self.strokePath_橫鉤_1))
		self.assertEqual("0.0.0,1.81.0,1.43.54",
				self._getDrawResultForStrokePath(self.strokePath_橫鉤_2))
		self.assertEqual("0.0.0,1.72.0,1.69.124",
				self._getDrawResultForStrokePath(self.strokePath_橫鉤_3))
		self.assertEqual("0.0.0,1.94.0,1.20.35",
				self._getDrawResultForStrokePath(self.strokePath_橫鉤_4))

	def testStrokePath_橫折(self):
		self.assertEqual("0.0.0,1.72.0,1.72.122",
				self._getDrawResultForStrokePath(self.strokePath_橫折_1))
		self.assertEqual("0.0.0,1.113.0,1.113.115",
				self._getDrawResultForStrokePath(self.strokePath_橫折_2))
		self.assertEqual("0.0.0,1.46.0,1.46.89",
				self._getDrawResultForStrokePath(self.strokePath_橫折_3))
		self.assertEqual("0.0.0,1.121.0,1.121.123",
				self._getDrawResultForStrokePath(self.strokePath_橫折_4))

	def testStrokePath_橫折折(self):
		self.assertEqual("0.0.0,1.94.0,1.94.34,1.127.34",
				self._getDrawResultForStrokePath(self.strokePath_橫折折_1))
		self.assertEqual("0.0.0,1.33.0,1.33.6,1.73.6",
				self._getDrawResultForStrokePath(self.strokePath_橫折折_2))
		self.assertEqual("0.0.0,1.30.0,1.30.115,1.49.115",
				self._getDrawResultForStrokePath(self.strokePath_橫折折_3))
		self.assertEqual("0.0.0,1.105.0,1.105.43,1.158.43",
				self._getDrawResultForStrokePath(self.strokePath_橫折折_4))

	def testStrokePath_橫折提(self):
		self.assertEqual("0.0.0,1.32.0,1.32.123,1.90.61",
				self._getDrawResultForStrokePath(self.strokePath_橫折提_1))
		self.assertEqual("0.0.0,1.107.0,1.107.36,1.180.-14",
				self._getDrawResultForStrokePath(self.strokePath_橫折提_2))
		self.assertEqual("0.0.0,1.86.0,1.86.122,1.132.32",
				self._getDrawResultForStrokePath(self.strokePath_橫折提_3))
		self.assertEqual("0.0.0,1.55.0,1.55.38,1.59.-83",
				self._getDrawResultForStrokePath(self.strokePath_橫折提_4))

	def testStrokePath_橫折折撇(self):
		self.assertEqual("0.0.0,1.64.0,1.-59.53,1.-15.53,1.-62.60",
				self._getDrawResultForStrokePath(self.strokePath_橫折折撇_1))
		self.assertEqual("0.0.0,1.36.0,1.-68.120,1.-22.120,1.-66.227",
				self._getDrawResultForStrokePath(self.strokePath_橫折折撇_2))
		self.assertEqual("0.0.0,1.68.0,1.22.47,1.43.47,1.33.148",
				self._getDrawResultForStrokePath(self.strokePath_橫折折撇_3))
		self.assertEqual("0.0.0,1.120.0,1.100.97,1.106.97,1.73.188",
				self._getDrawResultForStrokePath(self.strokePath_橫折折撇_4))

	def testStrokePath_橫撇彎鉤(self):
		self.assertEqual("0.0.0,1.115.0,1.2.12,2.62.56,1.18.116,1.14.45",
				self._getDrawResultForStrokePath(self.strokePath_橫撇彎鉤_1))
		self.assertEqual("0.0.0,1.79.0,1.-3.52,2.78.81,1.50.163,1.-18.66",
				self._getDrawResultForStrokePath(self.strokePath_橫撇彎鉤_2))
		self.assertEqual("0.0.0,1.58.0,1.-4.38,2.77.21,1.95.102,1.42.82",
				self._getDrawResultForStrokePath(self.strokePath_橫撇彎鉤_3))
		self.assertEqual("0.0.0,1.38.0,1.-49.100,2.14.159,1.-44.222,1.-76.175",
				self._getDrawResultForStrokePath(self.strokePath_橫撇彎鉤_4))

	def testStrokePath_橫折鉤(self):
		self.assertEqual("0.0.0,1.104.0,2.104.80,1.69.80,1.40.43",
				self._getDrawResultForStrokePath(self.strokePath_橫折鉤_1))
		self.assertEqual("0.0.0,1.32.0,2.32.20,1.2.20,1.-67.-53",
				self._getDrawResultForStrokePath(self.strokePath_橫折鉤_2))
		self.assertEqual("0.0.0,1.2.0,2.2.60,1.-44.60,1.-145.11",
				self._getDrawResultForStrokePath(self.strokePath_橫折鉤_3))
		self.assertEqual("0.0.0,1.82.0,2.82.82,1.65.82,1.16.30",
				self._getDrawResultForStrokePath(self.strokePath_橫折鉤_4))

	def testStrokePath_橫折彎(self):
		self.assertEqual("0.0.0,1.104.0,2.104.80,1.69.80,1.40.43",
				self._getDrawResultForStrokePath(self.strokePath_橫折鉤_1))
		self.assertEqual("0.0.0,1.32.0,2.32.20,1.2.20,1.-67.-53",
				self._getDrawResultForStrokePath(self.strokePath_橫折鉤_2))
		self.assertEqual("0.0.0,1.2.0,2.2.60,1.-44.60,1.-145.11",
				self._getDrawResultForStrokePath(self.strokePath_橫折鉤_3))
		self.assertEqual("0.0.0,1.82.0,2.82.82,1.65.82,1.16.30",
				self._getDrawResultForStrokePath(self.strokePath_橫折鉤_4))

	def testStrokePath_橫撇(self):
		self.assertEqual("0.0.0,1.104.0,2.104.80,1.69.80,1.40.43",
				self._getDrawResultForStrokePath(self.strokePath_橫折鉤_1))
		self.assertEqual("0.0.0,1.32.0,2.32.20,1.2.20,1.-67.-53",
				self._getDrawResultForStrokePath(self.strokePath_橫折鉤_2))
		self.assertEqual("0.0.0,1.2.0,2.2.60,1.-44.60,1.-145.11",
				self._getDrawResultForStrokePath(self.strokePath_橫折鉤_3))
		self.assertEqual("0.0.0,1.82.0,2.82.82,1.65.82,1.16.30",
				self._getDrawResultForStrokePath(self.strokePath_橫折鉤_4))

	def testStrokePath_橫斜彎鉤(self):
		self.assertEqual("0.0.0,1.104.0,2.104.80,1.69.80,1.40.43",
				self._getDrawResultForStrokePath(self.strokePath_橫折鉤_1))
		self.assertEqual("0.0.0,1.32.0,2.32.20,1.2.20,1.-67.-53",
				self._getDrawResultForStrokePath(self.strokePath_橫折鉤_2))
		self.assertEqual("0.0.0,1.2.0,2.2.60,1.-44.60,1.-145.11",
				self._getDrawResultForStrokePath(self.strokePath_橫折鉤_3))
		self.assertEqual("0.0.0,1.82.0,2.82.82,1.65.82,1.16.30",
				self._getDrawResultForStrokePath(self.strokePath_橫折鉤_4))

	def testStrokePath_橫折折折鉤(self):
		self.assertEqual("0.0.0,1.97.0,1.30.67,1.71.67,2.71.136,1.57.136,1.-34.134",
				self._getDrawResultForStrokePath(self.strokePath_橫折折折鉤_1))
		self.assertEqual("0.0.0,1.117.0,1.-6.117,1.96.117,2.96.161,1.29.161,1.-98.108",
				self._getDrawResultForStrokePath(self.strokePath_橫折折折鉤_2))
		self.assertEqual("0.0.0,1.33.0,1.-48.95,1.17.95,2.17.220,1.-108.220,1.-132.179",
				self._getDrawResultForStrokePath(self.strokePath_橫折折折鉤_3))
		self.assertEqual("0.0.0,1.115.0,1.4.93,1.103.93,2.103.169,1.56.169,1.-55.126",
				self._getDrawResultForStrokePath(self.strokePath_橫折折折鉤_4))

	def testStrokePath_橫斜鉤(self):
		self.assertEqual("0.0.0,1.105.0,2.109.9,1.127.12,1.127.-2",
				self._getDrawResultForStrokePath(self.strokePath_橫斜鉤_1))
		self.assertEqual("0.0.0,1.89.0,2.106.80,1.176.100,1.176.57",
				self._getDrawResultForStrokePath(self.strokePath_橫斜鉤_2))
		self.assertEqual("0.0.0,1.95.0,2.101.63,1.125.79,1.125.-27",
				self._getDrawResultForStrokePath(self.strokePath_橫斜鉤_3))
		self.assertEqual("0.0.0,1.60.0,2.61.59,1.66.74,1.66.10",
				self._getDrawResultForStrokePath(self.strokePath_橫斜鉤_4))

	def testStrokePath_橫折折折(self):
		self.assertEqual("0.0.0,1.14.0,1.14.97,1.59.97,1.59.160",
				self._getDrawResultForStrokePath(self.strokePath_橫折折折_1))
		self.assertEqual("0.0.0,1.21.0,1.21.32,1.41.32,1.41.47",
				self._getDrawResultForStrokePath(self.strokePath_橫折折折_2))
		self.assertEqual("0.0.0,1.95.0,1.95.4,1.117.4,1.117.15",
				self._getDrawResultForStrokePath(self.strokePath_橫折折折_3))
		self.assertEqual("0.0.0,1.16.0,1.16.29,1.45.29,1.45.130",
				self._getDrawResultForStrokePath(self.strokePath_橫折折折_4))

	def testStrokePath_豎(self):
		self.assertEqual("0.0.0,1.0.55",
				self._getDrawResultForStrokePath(self.strokePath_豎_1))
		self.assertEqual("0.0.0,1.0.112",
				self._getDrawResultForStrokePath(self.strokePath_豎_2))
		self.assertEqual("0.0.0,1.0.50",
				self._getDrawResultForStrokePath(self.strokePath_豎_3))
		self.assertEqual("0.0.0,1.0.127",
				self._getDrawResultForStrokePath(self.strokePath_豎_4))

	def testStrokePath_豎折(self):
		self.assertEqual("0.0.0,1.0.72,1.84.72",
				self._getDrawResultForStrokePath(self.strokePath_豎折_1))
		self.assertEqual("0.0.0,1.0.104,1.7.104",
				self._getDrawResultForStrokePath(self.strokePath_豎折_2))
		self.assertEqual("0.0.0,1.0.121,1.75.121",
				self._getDrawResultForStrokePath(self.strokePath_豎折_3))
		self.assertEqual("0.0.0,1.0.3,1.15.3",
				self._getDrawResultForStrokePath(self.strokePath_豎折_4))

	def testStrokePath_豎彎左(self):
		self.assertEqual("0.0.0,1.0.81,1.-25.81",
				self._getDrawResultForStrokePath(self.strokePath_豎彎左_1))
		self.assertEqual("0.0.0,1.0.3,1.-24.3",
				self._getDrawResultForStrokePath(self.strokePath_豎彎左_2))
		self.assertEqual("0.0.0,1.0.38,1.-101.38",
				self._getDrawResultForStrokePath(self.strokePath_豎彎左_3))
		self.assertEqual("0.0.0,1.0.114,1.-76.114",
				self._getDrawResultForStrokePath(self.strokePath_豎彎左_4))

	def testStrokePath_豎提(self):
		self.assertEqual("0.0.0,1.0.66,1.65.-48",
				self._getDrawResultForStrokePath(self.strokePath_豎提_1))
		self.assertEqual("0.0.0,1.0.27,1.4.-27",
				self._getDrawResultForStrokePath(self.strokePath_豎提_2))
		self.assertEqual("0.0.0,1.0.14,1.72.5",
				self._getDrawResultForStrokePath(self.strokePath_豎提_3))
		self.assertEqual("0.0.0,1.0.25,1.87.-74",
				self._getDrawResultForStrokePath(self.strokePath_豎提_4))

	def testStrokePath_豎折折(self):
		self.assertEqual("0.0.0,1.0.43,1.91.43,1.91.132",
				self._getDrawResultForStrokePath(self.strokePath_豎折折_1))
		self.assertEqual("0.0.0,1.0.81,1.118.81,1.118.106",
				self._getDrawResultForStrokePath(self.strokePath_豎折折_2))
		self.assertEqual("0.0.0,1.0.85,1.59.85,1.59.189",
				self._getDrawResultForStrokePath(self.strokePath_豎折折_3))
		self.assertEqual("0.0.0,1.0.39,1.100.39,1.100.71",
				self._getDrawResultForStrokePath(self.strokePath_豎折折_4))

	def testStrokePath_豎折彎鉤(self):
		self.assertEqual("0.0.0,1.-54.96,1.-20.96,2.-20.185,1.-93.185,1.-146.97",
				self._getDrawResultForStrokePath(self.strokePath_豎折彎鉤_1))
		self.assertEqual("0.0.0,1.-116.72,1.-4.72,2.-4.97,1.-26.97,1.-121.58",
				self._getDrawResultForStrokePath(self.strokePath_豎折彎鉤_2))
		self.assertEqual("0.0.0,1.-77.37,1.0.37,2.0.134,1.-25.134,1.-96.29",
				self._getDrawResultForStrokePath(self.strokePath_豎折彎鉤_3))
		self.assertEqual("0.0.0,1.-75.107,1.3.107,2.3.142,1.-70.142,1.-185.40",
				self._getDrawResultForStrokePath(self.strokePath_豎折彎鉤_4))

	def testStrokePath_豎彎鉤(self):
		self.assertEqual("0.0.0,1.0.33,2.0.124,1.91.124,1.94.124,1.94.44",
				self._getDrawResultForStrokePath(self.strokePath_豎彎鉤_1))
		self.assertEqual("0.0.0,1.0.59,2.0.103,1.44.103,1.122.103,1.122.13",
				self._getDrawResultForStrokePath(self.strokePath_豎彎鉤_2))
		self.assertEqual("0.0.0,1.0.20,2.0.122,1.102.122,1.124.122,1.124.73",
				self._getDrawResultForStrokePath(self.strokePath_豎彎鉤_3))
		self.assertEqual("0.0.0,1.0.17,2.0.28,1.11.28,1.123.28,1.123.19",
				self._getDrawResultForStrokePath(self.strokePath_豎彎鉤_4))

	def testStrokePath_豎彎(self):
		self.assertEqual("0.0.0,1.0.76,2.0.176,1.100.176,1.113.176",
				self._getDrawResultForStrokePath(self.strokePath_豎彎_1))
		self.assertEqual("0.0.0,1.0.93,2.0.96,1.3.96,1.59.96",
				self._getDrawResultForStrokePath(self.strokePath_豎彎_2))
		self.assertEqual("0.0.0,1.0.127,2.0.202,1.75.202,1.105.202",
				self._getDrawResultForStrokePath(self.strokePath_豎彎_3))
		self.assertEqual("0.0.0,1.0.7,2.0.102,1.95.102,1.135.102",
				self._getDrawResultForStrokePath(self.strokePath_豎彎_4))

	def testStrokePath_豎鉤(self):
		self.assertEqual("0.0.0,1.0.100,2.0.115,1.-5.115,1.-15.105",
				self._getDrawResultForStrokePath(self.strokePath_豎鉤_1))
		self.assertEqual("0.0.0,1.0.80,2.0.110,1.-6.110,1.-19.97",
				self._getDrawResultForStrokePath(self.strokePath_豎鉤_2))
		self.assertEqual("0.0.0,1.0.15,2.0.21,1.-27.21,1.-81.-33",
				self._getDrawResultForStrokePath(self.strokePath_豎鉤_3))
		self.assertEqual("0.0.0,1.0.71,2.0.77,1.-10.77,1.-30.57",
				self._getDrawResultForStrokePath(self.strokePath_豎鉤_4))

	def testStrokePath_斜鉤(self):
		self.assertEqual("0.0.0,2.24.14,1.121.18,1.121.-38",
				self._getDrawResultForStrokePath(self.strokePath_斜鉤_1))
		self.assertEqual("0.0.0,2.12.55,1.64.69,1.64.-1",
				self._getDrawResultForStrokePath(self.strokePath_斜鉤_2))
		self.assertEqual("0.0.0,2.17.12,1.86.15,1.86.-83",
				self._getDrawResultForStrokePath(self.strokePath_斜鉤_3))
		self.assertEqual("0.0.0,2.13.92,1.68.116,1.68.48",
				self._getDrawResultForStrokePath(self.strokePath_斜鉤_4))

	def testStrokePath_彎鉤(self):
		self.assertEqual("0.0.0,2.102.12,1.90.114,1.73.76",
				self._getDrawResultForStrokePath(self.strokePath_彎鉤_1))
		self.assertEqual("0.0.0,2.65.31,1.35.96,1.-13.-31",
				self._getDrawResultForStrokePath(self.strokePath_彎鉤_2))
		self.assertEqual("0.0.0,2.84.-30,1.115.55,1.40.-55",
				self._getDrawResultForStrokePath(self.strokePath_彎鉤_3))
		self.assertEqual("0.0.0,2.73.25,1.49.99,1.-3.-26",
				self._getDrawResultForStrokePath(self.strokePath_彎鉤_4))

	def testStrokePath_撇鉤(self):
		self.assertEqual("0.0.0,2.32.-2,1.34.30,1.-91.-84",
				self._getDrawResultForStrokePath(self.strokePath_撇鉤_1))
		self.assertEqual("0.0.0,2.47.35,1.12.83,1.-75.24",
				self._getDrawResultForStrokePath(self.strokePath_撇鉤_2))
		self.assertEqual("0.0.0,2.61.7,1.54.69,1.-23.5",
				self._getDrawResultForStrokePath(self.strokePath_撇鉤_3))
		self.assertEqual("0.0.0,2.70.-40,1.110.31,1.13.-90",
				self._getDrawResultForStrokePath(self.strokePath_撇鉤_4))

	def testStrokePath_撇(self):
		self.assertEqual("0.0.0,1.-64.100",
				self._getDrawResultForStrokePath(self.strokePath_撇_1))
		self.assertEqual("0.0.0,1.-13.120",
				self._getDrawResultForStrokePath(self.strokePath_撇_2))
		self.assertEqual("0.0.0,1.-40.91",
				self._getDrawResultForStrokePath(self.strokePath_撇_3))
		self.assertEqual("0.0.0,1.-64.68",
				self._getDrawResultForStrokePath(self.strokePath_撇_4))

	def testStrokePath_撇點(self):
		self.assertEqual("0.0.0,1.-104.96,1.-18.156",
				self._getDrawResultForStrokePath(self.strokePath_撇點_1))
		self.assertEqual("0.0.0,1.-51.18,1.75.82",
				self._getDrawResultForStrokePath(self.strokePath_撇點_2))
		self.assertEqual("0.0.0,1.-127.93,1.-84.104",
				self._getDrawResultForStrokePath(self.strokePath_撇點_3))
		self.assertEqual("0.0.0,1.-119.121,1.-33.241",
				self._getDrawResultForStrokePath(self.strokePath_撇點_4))

	def testStrokePath_撇橫(self):
		self.assertEqual("0.0.0,1.-36.42,1.46.47",
				self._getDrawResultForStrokePath(self.strokePath_撇橫_1))
		self.assertEqual("0.0.0,1.-64.34,1.-41.144",
				self._getDrawResultForStrokePath(self.strokePath_撇橫_2))
		self.assertEqual("0.0.0,1.-30.121,1.37.196",
				self._getDrawResultForStrokePath(self.strokePath_撇橫_3))
		self.assertEqual("0.0.0,1.-118.48,1.-28.163",
				self._getDrawResultForStrokePath(self.strokePath_撇橫_4))

	def testStrokePath_撇橫撇(self):
		self.assertEqual("0.0.0,1.-69.71,1.17.71,1.-3.93",
				self._getDrawResultForStrokePath(self.strokePath_撇橫撇_1))
		self.assertEqual("0.0.0,1.-72.72,1.-51.72,1.-53.74",
				self._getDrawResultForStrokePath(self.strokePath_撇橫撇_2))
		self.assertEqual("0.0.0,1.-80.52,1.-79.52,1.-116.169",
				self._getDrawResultForStrokePath(self.strokePath_撇橫撇_3))
		self.assertEqual("0.0.0,1.-21.78,1.19.78,1.-105.124",
				self._getDrawResultForStrokePath(self.strokePath_撇橫撇_4))

	def testStrokePath_豎撇(self):
		self.assertEqual("0.0.0,1.0.6,2.0.12,1.-89.12",
				self._getDrawResultForStrokePath(self.strokePath_豎撇_1))
		self.assertEqual("0.0.0,1.0.5,2.0.10,1.-74.10",
				self._getDrawResultForStrokePath(self.strokePath_豎撇_2))
		self.assertEqual("0.0.0,1.0.33,2.0.65,1.-10.65",
				self._getDrawResultForStrokePath(self.strokePath_豎撇_3))
		self.assertEqual("0.0.0,1.0.36,2.0.71,1.-61.71",
				self._getDrawResultForStrokePath(self.strokePath_豎撇_4))

	def testStrokePath_提(self):
		self.assertEqual("0.0.0,1.7.-17",
				self._getDrawResultForStrokePath(self.strokePath_提_1))
		self.assertEqual("0.0.0,1.121.-62",
				self._getDrawResultForStrokePath(self.strokePath_提_2))
		self.assertEqual("0.0.0,1.52.-93",
				self._getDrawResultForStrokePath(self.strokePath_提_3))
		self.assertEqual("0.0.0,1.118.-3",
				self._getDrawResultForStrokePath(self.strokePath_提_4))

	def testStrokePath_捺(self):
		self.assertEqual("0.0.0,2.35.62,1.107.63",
				self._getDrawResultForStrokePath(self.strokePath_捺_1))
		self.assertEqual("0.0.0,2.47.26,1.101.27",
				self._getDrawResultForStrokePath(self.strokePath_捺_2))
		self.assertEqual("0.0.0,2.41.54,1.109.55",
				self._getDrawResultForStrokePath(self.strokePath_捺_3))
		self.assertEqual("0.0.0,2.1.67,1.36.125",
				self._getDrawResultForStrokePath(self.strokePath_捺_4))

	def testStrokePath_臥捺(self):
		self.assertEqual("0.0.0,2.8.12,1.4.26,2.0.40,1.8.52",
				self._getDrawResultForStrokePath(self.strokePath_臥捺_1))
		self.assertEqual("0.0.0,2.17.-7,1.34.3,2.51.12,1.68.6",
				self._getDrawResultForStrokePath(self.strokePath_臥捺_2))
		self.assertEqual("0.0.0,2.6.8,1.4.19,2.2.29,1.8.38",
				self._getDrawResultForStrokePath(self.strokePath_臥捺_3))
		self.assertEqual("0.0.0,2.2.3,1.2.7,2.2.10,1.4.14",
				self._getDrawResultForStrokePath(self.strokePath_臥捺_4))

	def testStrokePath_提捺(self):
		self.assertEqual("0.0.0,1.14.-43,2.23.-7,1.60.0",
				self._getDrawResultForStrokePath(self.strokePath_提捺_1))
		self.assertEqual("0.0.0,1.2.-26,2.2.19,1.43.40",
				self._getDrawResultForStrokePath(self.strokePath_提捺_2))
		self.assertEqual("0.0.0,1.93.-18,2.153.-12,1.213.-12",
				self._getDrawResultForStrokePath(self.strokePath_提捺_3))
		self.assertEqual("0.0.0,1.114.-10,2.160.50,1.236.51",
				self._getDrawResultForStrokePath(self.strokePath_提捺_4))

	def testStrokePath_橫捺(self):
		self.assertEqual("0.0.0,1.49.0,2.49.23,1.66.40",
				self._getDrawResultForStrokePath(self.strokePath_橫捺_1))
		self.assertEqual("0.0.0,1.64.0,2.83.77,1.162.91",
				self._getDrawResultForStrokePath(self.strokePath_橫捺_2))
		self.assertEqual("0.0.0,1.12.0,2.23.12,1.38.12",
				self._getDrawResultForStrokePath(self.strokePath_橫捺_3))
		self.assertEqual("0.0.0,1.4.0,2.4.71,1.53.124",
				self._getDrawResultForStrokePath(self.strokePath_橫捺_4))

