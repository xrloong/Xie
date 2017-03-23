import unittest
import copy

from xie.graphics.segment import BeelineSegment
from xie.graphics.segment import QCurveSegment
from xie.graphics.segment import StrokePath
from xie.graphics.segment import SegmentFactory
from xie.graphics.stroke_info import StrokeInfo
from xie.graphics.factory import ShapeFactory

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

class StrokeInfoFactoryTestCase(unittest.TestCase):
	def setUp(self):
		self.segmentFactory = SegmentFactory()
		self.shapeFactory = ShapeFactory()
		self.generateTestDataStrokeInfos()

	def tearDown(self):
		pass

	def generateStrokeInfo(self, name, paramList):
		return self.shapeFactory.generateStrokeInfo(name, paramList)

	def generateTestDataStrokeInfos(self):
		self.strokeInfo_點_1=self.generateStrokeInfo("點", (5, 95))
		self.strokeInfo_點_2=self.generateStrokeInfo("點", (20, 122))
		self.strokeInfo_點_3=self.generateStrokeInfo("點", (125, 46))
		self.strokeInfo_點_4=self.generateStrokeInfo("點", (14, 16))
		self.strokeInfo_點_1_r=StrokeInfo("點", StrokePath([
			BeelineSegment((5, 95))
		]))
		self.strokeInfo_點_2_r=StrokeInfo("點", StrokePath([
			BeelineSegment((20, 122))
		]))
		self.strokeInfo_點_3_r=StrokeInfo("點", StrokePath([
			BeelineSegment((125, 46))]
		))
		self.strokeInfo_點_4_r=StrokeInfo("點", StrokePath([
			BeelineSegment((14, 16))]
		))

		self.strokeInfo_圈_1=self.generateStrokeInfo("圈", (6, 126))
		self.strokeInfo_圈_2=self.generateStrokeInfo("圈", (53, 83))
		self.strokeInfo_圈_3=self.generateStrokeInfo("圈", (21, 72))
		self.strokeInfo_圈_4=self.generateStrokeInfo("圈", (99, 41))
		self.strokeInfo_圈_1_r=StrokeInfo("圈", StrokePath([
			QCurveSegment((6, 0), (6, 126)),
			QCurveSegment((0, 126), (-6, 126)),
			QCurveSegment((-6, 0), (-6, -126)),
			QCurveSegment((0, -126), (6, -126))
			]))
		self.strokeInfo_圈_2_r=StrokeInfo("圈", StrokePath([
			QCurveSegment((53, 0), (53, 83)),
			QCurveSegment((0, 83), (-53, 83)),
			QCurveSegment((-53, 0), (-53, -83)),
			QCurveSegment((0, -83), (53, -83))
			]))
		self.strokeInfo_圈_3_r=StrokeInfo("圈", StrokePath([
			QCurveSegment((21, 0), (21, 72)),
			QCurveSegment((0, 72), (-21, 72)),
			QCurveSegment((-21, 0), (-21, -72)),
			QCurveSegment((0, -72), (21, -72))
			]))
		self.strokeInfo_圈_4_r=StrokeInfo("圈", StrokePath([
			QCurveSegment((99, 0), (99, 41)),
			QCurveSegment((0, 41), (-99, 41)),
			QCurveSegment((-99, 0), (-99, -41)),
			QCurveSegment((0, -41), (99, -41))
			]))

		self.strokeInfo_橫_1=self.generateStrokeInfo("橫", (30,))
		self.strokeInfo_橫_2=self.generateStrokeInfo("橫", (124,))
		self.strokeInfo_橫_3=self.generateStrokeInfo("橫", (13,))
		self.strokeInfo_橫_4=self.generateStrokeInfo("橫", (105,))
		self.strokeInfo_橫_1_r=StrokeInfo("橫", StrokePath([
			BeelineSegment((30, 0))
			]))
		self.strokeInfo_橫_2_r=StrokeInfo("橫", StrokePath([
			BeelineSegment((124, 0))
			]))
		self.strokeInfo_橫_3_r=StrokeInfo("橫", StrokePath([
			BeelineSegment((13, 0))
			]))
		self.strokeInfo_橫_4_r=StrokeInfo("橫", StrokePath([
			BeelineSegment((105, 0))
			]))

		self.strokeInfo_橫鉤_1=self.generateStrokeInfo("橫鉤", (103, 125, 68))
		self.strokeInfo_橫鉤_2=self.generateStrokeInfo("橫鉤", (81, 38, 54))
		self.strokeInfo_橫鉤_3=self.generateStrokeInfo("橫鉤", (72, 3, 124))
		self.strokeInfo_橫鉤_4=self.generateStrokeInfo("橫鉤", (94, 74, 35))
		self.strokeInfo_橫鉤_1_r=StrokeInfo("橫鉤", StrokePath([
			BeelineSegment((103, 0)),
			BeelineSegment((-125, 68))
			]))
		self.strokeInfo_橫鉤_2_r=StrokeInfo("橫鉤", StrokePath([
			BeelineSegment((81, 0)),
			BeelineSegment((-38, 54))
			]))
		self.strokeInfo_橫鉤_3_r=StrokeInfo("橫鉤", StrokePath([
			BeelineSegment((72, 0)),
			BeelineSegment((-3, 124))
			]))
		self.strokeInfo_橫鉤_4_r=StrokeInfo("橫鉤", StrokePath([
			BeelineSegment((94, 0)),
			BeelineSegment((-74, 35))
			]))

		self.strokeInfo_橫折_1=self.generateStrokeInfo("橫折", (72, 122))
		self.strokeInfo_橫折_2=self.generateStrokeInfo("橫折", (113, 115))
		self.strokeInfo_橫折_3=self.generateStrokeInfo("橫折", (46, 89))
		self.strokeInfo_橫折_4=self.generateStrokeInfo("橫折", (121, 123))
		self.strokeInfo_橫折_1_r=StrokeInfo("橫折", StrokePath([
			BeelineSegment((72, 0)),
			BeelineSegment((0, 122))
			]))
		self.strokeInfo_橫折_2_r=StrokeInfo("橫折", StrokePath([
			BeelineSegment((113, 0)),
			BeelineSegment((0, 115))
			]))
		self.strokeInfo_橫折_3_r=StrokeInfo("橫折", StrokePath([
			BeelineSegment((46, 0)),
			BeelineSegment((0, 89))
			]))
		self.strokeInfo_橫折_4_r=StrokeInfo("橫折", StrokePath([
			BeelineSegment((121, 0)),
			BeelineSegment((0, 123))
			]))

		self.strokeInfo_橫折折_1=self.generateStrokeInfo("橫折折", (94, 34, 33))
		self.strokeInfo_橫折折_2=self.generateStrokeInfo("橫折折", (33, 6, 40))
		self.strokeInfo_橫折折_3=self.generateStrokeInfo("橫折折", (30, 115, 19))
		self.strokeInfo_橫折折_4=self.generateStrokeInfo("橫折折", (105, 43, 53))
		self.strokeInfo_橫折折_1_r=StrokeInfo("橫折折", StrokePath([
				BeelineSegment((94, 0)),
				BeelineSegment((0, 34)),
				BeelineSegment((33, 0))
			]))
		self.strokeInfo_橫折折_2_r=StrokeInfo("橫折折", StrokePath([
				BeelineSegment((33, 0)),
				BeelineSegment((0, 6)),
				BeelineSegment((40, 0))
			]))
		self.strokeInfo_橫折折_3_r=StrokeInfo("橫折折", StrokePath([
				BeelineSegment((30, 0)),
				BeelineSegment((0, 115)),
				BeelineSegment((19, 0))
			]))
		self.strokeInfo_橫折折_4_r=StrokeInfo("橫折折", StrokePath([
				BeelineSegment((105, 0)),
				BeelineSegment((0, 43)),
				BeelineSegment((53, 0))
			]))

		self.strokeInfo_橫折提_1=self.generateStrokeInfo("橫折提", (32, 123, 58, 62))
		self.strokeInfo_橫折提_2=self.generateStrokeInfo("橫折提", (107, 36, 73, 50))
		self.strokeInfo_橫折提_3=self.generateStrokeInfo("橫折提", (86, 122, 46, 90))
		self.strokeInfo_橫折提_4=self.generateStrokeInfo("橫折提", (55, 38, 4, 121))
		self.strokeInfo_橫折提_1_r=StrokeInfo("橫折提", StrokePath([
				BeelineSegment((32, 0)),
				BeelineSegment((0, 123)),
				BeelineSegment((58, -62))
			]))
		self.strokeInfo_橫折提_2_r=StrokeInfo("橫折提", StrokePath([
				BeelineSegment((107, 0)),
				BeelineSegment((0, 36)),
				BeelineSegment((73, -50))
			]))
		self.strokeInfo_橫折提_3_r=StrokeInfo("橫折提", StrokePath([
				BeelineSegment((86, 0)),
				BeelineSegment((0, 122)),
				BeelineSegment((46, -90))
			]))
		self.strokeInfo_橫折提_4_r=StrokeInfo("橫折提", StrokePath([
				BeelineSegment((55, 0)),
				BeelineSegment((0, 38)),
				BeelineSegment((4, -121))
			]))

		self.strokeInfo_橫折折撇_1=self.generateStrokeInfo("橫折折撇", (64, 123, 53, 44, 47, 7))
		self.strokeInfo_橫折折撇_2=self.generateStrokeInfo("橫折折撇", (36, 104, 120, 46, 44, 107))
		self.strokeInfo_橫折折撇_3=self.generateStrokeInfo("橫折折撇", (68, 46, 47, 21, 10, 101))
		self.strokeInfo_橫折折撇_4=self.generateStrokeInfo("橫折折撇", (120, 20, 97, 6, 33, 91))
		self.strokeInfo_橫折折撇_1_r=StrokeInfo("橫折折撇", StrokePath([
				BeelineSegment((64, 0)),
				BeelineSegment((-123, 53)),
				BeelineSegment((44, 0)),
				BeelineSegment((-47, 7))
			]))
		self.strokeInfo_橫折折撇_2_r=StrokeInfo("橫折折撇", StrokePath([
				BeelineSegment((36, 0)),
				BeelineSegment((-104, 120)),
				BeelineSegment((46, 0)),
				BeelineSegment((-44, 107))
			]))
		self.strokeInfo_橫折折撇_3_r=StrokeInfo("橫折折撇", StrokePath([
				BeelineSegment((68, 0)),
				BeelineSegment((-46, 47)),
				BeelineSegment((21, 0)),
				BeelineSegment((-10, 101))
			]))
		self.strokeInfo_橫折折撇_4_r=StrokeInfo("橫折折撇", StrokePath([
				BeelineSegment((120, 0)),
				BeelineSegment((-20, 97)),
				BeelineSegment((6, 0)),
				BeelineSegment((-33, 91))
			]))

		self.strokeInfo_橫撇彎鉤_1=self.generateStrokeInfo("橫撇彎鉤", (115, 113, 12, 16, 104, 4, 71))
		self.strokeInfo_橫撇彎鉤_2=self.generateStrokeInfo("橫撇彎鉤", (79, 82, 52, 53, 111, 68, 97))
		self.strokeInfo_橫撇彎鉤_3=self.generateStrokeInfo("橫撇彎鉤", (58, 62, 38, 99, 64, 53, 20))
		self.strokeInfo_橫撇彎鉤_4=self.generateStrokeInfo("橫撇彎鉤", (38, 87, 100, 5, 122, 32, 47))
		self.strokeInfo_橫撇彎鉤_1_r=StrokeInfo("橫撇彎鉤", StrokePath([
				BeelineSegment((115, 0)),
				BeelineSegment((-113, 12)),
				QCurveSegment((60, 44), [16, 104]),
				BeelineSegment((-4, -71))
			]))
		self.strokeInfo_橫撇彎鉤_2_r=StrokeInfo("橫撇彎鉤", StrokePath([
				BeelineSegment((79, 0)),
				BeelineSegment((-82, 52)),
				QCurveSegment((81, 29), [53, 111]),
				BeelineSegment((-68, -97))
			]))
		self.strokeInfo_橫撇彎鉤_3_r=StrokeInfo("橫撇彎鉤", StrokePath([
				BeelineSegment((58, 0)),
				BeelineSegment((-62, 38)),
				QCurveSegment((81, -17), [99, 64]),
				BeelineSegment((-53, -20))
			]))
		self.strokeInfo_橫撇彎鉤_4_r=StrokeInfo("橫撇彎鉤", StrokePath([
				BeelineSegment((38, 0)),
				BeelineSegment((-87, 100)),
				QCurveSegment((63, 59), [5, 122]),
				BeelineSegment((-32, -47))
			]))

		self.strokeInfo_橫折鉤_1=self.generateStrokeInfo("橫折鉤", (104, 35, 80, 29, 37))
		self.strokeInfo_橫折鉤_2=self.generateStrokeInfo("橫折鉤", (32, 30, 20, 69, 73))
		self.strokeInfo_橫折鉤_3=self.generateStrokeInfo("橫折鉤", (2, 46, 60, 101, 49))
		self.strokeInfo_橫折鉤_4=self.generateStrokeInfo("橫折鉤", (82, 17, 82, 49, 52))
		self.strokeInfo_橫折鉤_1_r=StrokeInfo("橫折鉤", StrokePath([
				BeelineSegment((104, 0)),
				QCurveSegment((0, 80), (-35, 80)),
				BeelineSegment((-29, -37))
			]))
		self.strokeInfo_橫折鉤_2_r=StrokeInfo("橫折鉤", StrokePath([
				BeelineSegment((32, 0)),
				QCurveSegment((0, 20), (-30, 20)),
				BeelineSegment((-69, -73))
			]))
		self.strokeInfo_橫折鉤_3_r=StrokeInfo("橫折鉤", StrokePath([
				BeelineSegment((2, 0)),
				QCurveSegment((0, 60), (-46, 60)),
				BeelineSegment((-101, -49))
			]))
		self.strokeInfo_橫折鉤_4_r=StrokeInfo("橫折鉤", StrokePath([
				BeelineSegment((82, 0)),
				QCurveSegment((0, 82), (-17, 82)),
				BeelineSegment((-49, -52))
			]))

		self.strokeInfo_橫折彎_1=self.generateStrokeInfo("橫折彎", (114, 84, 108, 5))
		self.strokeInfo_橫折彎_2=self.generateStrokeInfo("橫折彎", (81, 64, 115, 1))
		self.strokeInfo_橫折彎_3=self.generateStrokeInfo("橫折彎", (11, 43, 44, 2))
		self.strokeInfo_橫折彎_4=self.generateStrokeInfo("橫折彎", (94, 94, 93, 60))
		self.strokeInfo_橫折彎_1_r=StrokeInfo("橫折彎", StrokePath([
				BeelineSegment((114, 0)),
				BeelineSegment((0, 79)),
				QCurveSegment([0, 5], [5, 5]),
				BeelineSegment((103, 0))
			]))
		self.strokeInfo_橫折彎_2_r=StrokeInfo("橫折彎", StrokePath([
				BeelineSegment((81, 0)),
				BeelineSegment((0, 63)),
				QCurveSegment([0, 1], [1, 1]),
				BeelineSegment((114, 0))
			]))
		self.strokeInfo_橫折彎_3_r=StrokeInfo("橫折彎", StrokePath([
				BeelineSegment((11, 0)),
				BeelineSegment((0, 41)),
				QCurveSegment([0, 2], [2, 2]),
				BeelineSegment((42, 0))
			]))
		self.strokeInfo_橫折彎_4_r=StrokeInfo("橫折彎", StrokePath([
				BeelineSegment((94, 0)),
				BeelineSegment((0, 34)),
				QCurveSegment([0, 60], [60, 60]),
				BeelineSegment((33, 0))
			]))

		self.strokeInfo_橫撇_1=self.generateStrokeInfo("橫撇", (4, 90, 127))
		self.strokeInfo_橫撇_2=self.generateStrokeInfo("橫撇", (26, 94, 42))
		self.strokeInfo_橫撇_3=self.generateStrokeInfo("橫撇", (99, 124, 44))
		self.strokeInfo_橫撇_4=self.generateStrokeInfo("橫撇", (16, 20, 82))
		self.strokeInfo_橫撇_1_r=StrokeInfo("橫撇", StrokePath([
				BeelineSegment((4, 0)),
				BeelineSegment((-90, 127))
			]))
		self.strokeInfo_橫撇_2_r=StrokeInfo("橫撇", StrokePath([
				BeelineSegment((26, 0)),
				BeelineSegment((-94, 42))
			]))
		self.strokeInfo_橫撇_3_r=StrokeInfo("橫撇", StrokePath([
				BeelineSegment((99, 0)),
				BeelineSegment((-124, 44))
			]))
		self.strokeInfo_橫撇_4_r=StrokeInfo("橫撇", StrokePath([
				BeelineSegment((16, 0)),
				BeelineSegment((-20, 82))
			]))

		self.strokeInfo_橫斜彎鉤_1=self.generateStrokeInfo("橫斜彎鉤", (18, 99, 50, 93, 24, 5))
		self.strokeInfo_橫斜彎鉤_2=self.generateStrokeInfo("橫斜彎鉤", (79, 34, 81, 112, 118, 11))
		self.strokeInfo_橫斜彎鉤_3=self.generateStrokeInfo("橫斜彎鉤", (76, 31, 11, 123, 10, 107))
		self.strokeInfo_橫斜彎鉤_4=self.generateStrokeInfo("橫斜彎鉤", (100, 77, 111, 107, 61, 123))
		self.strokeInfo_橫斜彎鉤_1_r=StrokeInfo("橫斜彎鉤", StrokePath([
				BeelineSegment((18, 0)),
				BeelineSegment([-26, 51]),
				QCurveSegment((-24, 48), (0, 48)),
				BeelineSegment((119, 0)),
				BeelineSegment((0, -5))
			]))
		self.strokeInfo_橫斜彎鉤_2_r=StrokeInfo("橫斜彎鉤", StrokePath([
				BeelineSegment((79, 0)),
				BeelineSegment([37, -16]),
				QCurveSegment((-118, 50), (0, 50)),
				BeelineSegment((75, 0)),
				BeelineSegment((0, -11))
			]))
		self.strokeInfo_橫斜彎鉤_3_r=StrokeInfo("橫斜彎鉤", StrokePath([
				BeelineSegment((76, 0)),
				BeelineSegment([-1, 2]),
				QCurveSegment((-10, 29), (0, 29)),
				BeelineSegment((124, 0)),
				BeelineSegment((0, -107))
			]))
		self.strokeInfo_橫斜彎鉤_4_r=StrokeInfo("橫斜彎鉤", StrokePath([
				BeelineSegment((100, 0)),
				BeelineSegment([-50, 34]),
				QCurveSegment((-61, 43), (0, 43)),
				BeelineSegment((157, 0)),
				BeelineSegment((0, -123))
			]))

		self.strokeInfo_橫折折折鉤_1=self.generateStrokeInfo("橫折折折鉤", (97, 67, 67, 41, 14, 69, 91, 2))
		self.strokeInfo_橫折折折鉤_2=self.generateStrokeInfo("橫折折折鉤", (117, 123, 117, 102, 67, 44, 127, 53))
		self.strokeInfo_橫折折折鉤_3=self.generateStrokeInfo("橫折折折鉤", (33, 81, 95, 65, 125, 125, 24, 41))
		self.strokeInfo_橫折折折鉤_4=self.generateStrokeInfo("橫折折折鉤", (115, 111, 93, 99, 47, 76, 111, 43))
		self.strokeInfo_橫折折折鉤_1_r=StrokeInfo("橫折折折鉤", StrokePath([
				BeelineSegment((97, 0)),
				BeelineSegment((-67, 67)),
				BeelineSegment((41, 0)),
				QCurveSegment((0, 69), (-14, 69)),
				BeelineSegment((-91, -2))
			]))
		self.strokeInfo_橫折折折鉤_2_r=StrokeInfo("橫折折折鉤", StrokePath([
				BeelineSegment((117, 0)),
				BeelineSegment((-123, 117)),
				BeelineSegment((102, 0)),
				QCurveSegment((0, 44), (-67, 44)),
				BeelineSegment((-127, -53))
			]))
		self.strokeInfo_橫折折折鉤_3_r=StrokeInfo("橫折折折鉤", StrokePath([
				BeelineSegment((33, 0)),
				BeelineSegment((-81, 95)),
				BeelineSegment((65, 0)),
				QCurveSegment((0, 125), (-125, 125)),
				BeelineSegment((-24, -41))
			]))
		self.strokeInfo_橫折折折鉤_4_r=StrokeInfo("橫折折折鉤", StrokePath([
				BeelineSegment((115, 0)),
				BeelineSegment((-111, 93)),
				BeelineSegment((99, 0)),
				QCurveSegment((0, 76), (-47, 76)),
				BeelineSegment((-111, -43))
			]))

		self.strokeInfo_橫斜鉤_1=self.generateStrokeInfo("橫斜鉤", (105, 22, 12, 14))
		self.strokeInfo_橫斜鉤_2=self.generateStrokeInfo("橫斜鉤", (89, 87, 100, 43))
		self.strokeInfo_橫斜鉤_3=self.generateStrokeInfo("橫斜鉤", (95, 30, 79, 106))
		self.strokeInfo_橫斜鉤_4=self.generateStrokeInfo("橫斜鉤", (60, 6, 74, 64))
		self.strokeInfo_橫斜鉤_1_r=StrokeInfo("橫斜鉤", StrokePath([
				BeelineSegment((105, 0)),
				QCurveSegment((4, 9), (22, 12)),
				BeelineSegment((0, -14))
			]))
		self.strokeInfo_橫斜鉤_2_r=StrokeInfo("橫斜鉤", StrokePath([
				BeelineSegment((89, 0)),
				QCurveSegment((17, 80), (87, 100)),
				BeelineSegment((0, -43))
			]))
		self.strokeInfo_橫斜鉤_3_r=StrokeInfo("橫斜鉤", StrokePath([
				BeelineSegment((95, 0)),
				QCurveSegment((6, 63), (30, 79)),
				BeelineSegment((0, -106))
			]))
		self.strokeInfo_橫斜鉤_4_r=StrokeInfo("橫斜鉤", StrokePath([
				BeelineSegment((60, 0)),
				QCurveSegment((1, 59), (6, 74)),
				BeelineSegment((0, -64))
			]))

		self.strokeInfo_橫折折折_1=self.generateStrokeInfo("橫折折折", (14, 97, 45, 63))
		self.strokeInfo_橫折折折_2=self.generateStrokeInfo("橫折折折", (21, 32, 20, 15))
		self.strokeInfo_橫折折折_3=self.generateStrokeInfo("橫折折折", (95, 4, 22, 11))
		self.strokeInfo_橫折折折_4=self.generateStrokeInfo("橫折折折", (16, 29, 29, 101))
		self.strokeInfo_橫折折折_1_r=StrokeInfo("橫折折折", StrokePath([
				BeelineSegment((14, 0)),
				BeelineSegment((0, 97)),
				BeelineSegment((45, 0)),
				BeelineSegment((0, 63))
			]))
		self.strokeInfo_橫折折折_2_r=StrokeInfo("橫折折折", StrokePath([
				BeelineSegment((21, 0)),
				BeelineSegment((0, 32)),
				BeelineSegment((20, 0)),
				BeelineSegment((0, 15))
			]))
		self.strokeInfo_橫折折折_3_r=StrokeInfo("橫折折折", StrokePath([
				BeelineSegment((95, 0)),
				BeelineSegment((0, 4)),
				BeelineSegment((22, 0)),
				BeelineSegment((0, 11))
			]))
		self.strokeInfo_橫折折折_4_r=StrokeInfo("橫折折折", StrokePath([
				BeelineSegment((16, 0)),
				BeelineSegment((0, 29)),
				BeelineSegment((29, 0)),
				BeelineSegment((0, 101))
			]))

		self.strokeInfo_豎_1=self.generateStrokeInfo("豎", (55,))
		self.strokeInfo_豎_2=self.generateStrokeInfo("豎", (112,))
		self.strokeInfo_豎_3=self.generateStrokeInfo("豎", (50,))
		self.strokeInfo_豎_4=self.generateStrokeInfo("豎", (127,))
		self.strokeInfo_豎_1_r=StrokeInfo("豎", StrokePath([
				BeelineSegment((0, 55))
			]))
		self.strokeInfo_豎_2_r=StrokeInfo("豎", StrokePath([
				BeelineSegment((0, 112))
			]))
		self.strokeInfo_豎_3_r=StrokeInfo("豎", StrokePath([
				BeelineSegment((0, 50))
			]))
		self.strokeInfo_豎_4_r=StrokeInfo("豎", StrokePath([
				BeelineSegment((0, 127))
			]))

		self.strokeInfo_豎折_1=self.generateStrokeInfo("豎折", (72, 84))
		self.strokeInfo_豎折_2=self.generateStrokeInfo("豎折", (104, 7))
		self.strokeInfo_豎折_3=self.generateStrokeInfo("豎折", (121, 75))
		self.strokeInfo_豎折_4=self.generateStrokeInfo("豎折", (3, 15))
		self.strokeInfo_豎折_1_r=StrokeInfo("豎折", StrokePath([
				BeelineSegment((0, 72)),
				BeelineSegment((84, 0))
			]))
		self.strokeInfo_豎折_2_r=StrokeInfo("豎折", StrokePath([
				BeelineSegment((0, 104)),
				BeelineSegment((7, 0))
			]))
		self.strokeInfo_豎折_3_r=StrokeInfo("豎折", StrokePath([
				BeelineSegment((0, 121)),
				BeelineSegment((75, 0))
			]))
		self.strokeInfo_豎折_4_r=StrokeInfo("豎折", StrokePath([
				BeelineSegment((0, 3)),
				BeelineSegment((15, 0))
			]))

		self.strokeInfo_豎彎左_1=self.generateStrokeInfo("豎彎左", (81, 25))
		self.strokeInfo_豎彎左_2=self.generateStrokeInfo("豎彎左", (3, 24))
		self.strokeInfo_豎彎左_3=self.generateStrokeInfo("豎彎左", (38, 101))
		self.strokeInfo_豎彎左_4=self.generateStrokeInfo("豎彎左", (114, 76))
		self.strokeInfo_豎彎左_1_r=StrokeInfo("豎彎左", StrokePath([
			BeelineSegment((0, 81)),
			BeelineSegment((-25, 0))
			]))
		self.strokeInfo_豎彎左_2_r=StrokeInfo("豎彎左", StrokePath([
			BeelineSegment((0, 3)),
			BeelineSegment((-24, 0))
			]))
		self.strokeInfo_豎彎左_3_r=StrokeInfo("豎彎左", StrokePath([
			BeelineSegment((0, 38)),
			BeelineSegment((-101, 0))
			]))
		self.strokeInfo_豎彎左_4_r=StrokeInfo("豎彎左", StrokePath([
			BeelineSegment((0, 114)),
			BeelineSegment((-76, 0))
			]))

		self.strokeInfo_豎提_1=self.generateStrokeInfo("豎提", (66, 65, 114))
		self.strokeInfo_豎提_2=self.generateStrokeInfo("豎提", (27, 4, 54))
		self.strokeInfo_豎提_3=self.generateStrokeInfo("豎提", (14, 72, 9))
		self.strokeInfo_豎提_4=self.generateStrokeInfo("豎提", (25, 87, 99))
		self.strokeInfo_豎提_1_r=StrokeInfo("豎提", StrokePath([
				BeelineSegment((0, 66)),
				BeelineSegment((65, -114))
			]))
		self.strokeInfo_豎提_2_r=StrokeInfo("豎提", StrokePath([
				BeelineSegment((0, 27)),
				BeelineSegment((4, -54))
			]))
		self.strokeInfo_豎提_3_r=StrokeInfo("豎提", StrokePath([
				BeelineSegment((0, 14)),
				BeelineSegment((72, -9))
			]))
		self.strokeInfo_豎提_4_r=StrokeInfo("豎提", StrokePath([
				BeelineSegment((0, 25)),
				BeelineSegment((87, -99))
			]))

		self.strokeInfo_豎折折_1=self.generateStrokeInfo("豎折折", (43, 91, 89))
		self.strokeInfo_豎折折_2=self.generateStrokeInfo("豎折折", (81, 118, 25))
		self.strokeInfo_豎折折_3=self.generateStrokeInfo("豎折折", (85, 59, 104))
		self.strokeInfo_豎折折_4=self.generateStrokeInfo("豎折折", (39, 100, 32))
		self.strokeInfo_豎折折_1_r=StrokeInfo("豎折折", StrokePath([
				BeelineSegment((0, 43)),
				BeelineSegment((91, 0)),
				BeelineSegment((0, 89))
			]))
		self.strokeInfo_豎折折_2_r=StrokeInfo("豎折折", StrokePath([
				BeelineSegment((0, 81)),
				BeelineSegment((118, 0)),
				BeelineSegment((0, 25))
			]))
		self.strokeInfo_豎折折_3_r=StrokeInfo("豎折折", StrokePath([
				BeelineSegment((0, 85)),
				BeelineSegment((59, 0)),
				BeelineSegment((0, 104))
			]))
		self.strokeInfo_豎折折_4_r=StrokeInfo("豎折折", StrokePath([
				BeelineSegment((0, 39)),
				BeelineSegment((100, 0)),
				BeelineSegment((0, 32))
			]))

		self.strokeInfo_豎折彎鉤_1=self.generateStrokeInfo("豎折彎鉤", (54, 96, 34, 73, 89, 53, 88))
		self.strokeInfo_豎折彎鉤_2=self.generateStrokeInfo("豎折彎鉤", (116, 72, 112, 22, 25, 95, 39))
		self.strokeInfo_豎折彎鉤_3=self.generateStrokeInfo("豎折彎鉤", (77, 37, 77, 25, 97, 71, 105))
		self.strokeInfo_豎折彎鉤_4=self.generateStrokeInfo("豎折彎鉤", (75, 107, 78, 73, 35, 115, 102))
		self.strokeInfo_豎折彎鉤_1_r=StrokeInfo("豎折彎鉤", StrokePath([
				BeelineSegment((-54, 96)),
				BeelineSegment((34, 0)),
				QCurveSegment((0, 89), (-73, 89)),
				BeelineSegment((-53, -88))
			]))
		self.strokeInfo_豎折彎鉤_2_r=StrokeInfo("豎折彎鉤", StrokePath([
				BeelineSegment((-116, 72)),
				BeelineSegment((112, 0)),
				QCurveSegment((0, 25), (-22, 25)),
				BeelineSegment((-95, -39))
			]))
		self.strokeInfo_豎折彎鉤_3_r=StrokeInfo("豎折彎鉤", StrokePath([
				BeelineSegment((-77, 37)),
				BeelineSegment((77, 0)),
				QCurveSegment((0, 97), (-25, 97)),
				BeelineSegment((-71, -105))
			]))
		self.strokeInfo_豎折彎鉤_4_r=StrokeInfo("豎折彎鉤", StrokePath([
				BeelineSegment((-75, 107)),
				BeelineSegment((78, 0)),
				QCurveSegment((0, 35), (-73, 35)),
				BeelineSegment((-115, -102))
			]))

		self.strokeInfo_豎彎鉤_1=self.generateStrokeInfo("豎彎鉤", (124, 94, 91, 80))
		self.strokeInfo_豎彎鉤_2=self.generateStrokeInfo("豎彎鉤", (103, 122, 44, 90))
		self.strokeInfo_豎彎鉤_3=self.generateStrokeInfo("豎彎鉤", (122, 124, 102, 49))
		self.strokeInfo_豎彎鉤_4=self.generateStrokeInfo("豎彎鉤", (28, 123, 11, 9))
		self.strokeInfo_豎彎鉤_1_r=StrokeInfo("豎彎鉤", StrokePath([
				BeelineSegment((0, 33)),
				QCurveSegment([0, 91], [91, 91]),
				BeelineSegment((3, 0)),
				BeelineSegment((0, -80))
			]))
		self.strokeInfo_豎彎鉤_2_r=StrokeInfo("豎彎鉤", StrokePath([
				BeelineSegment((0, 59)),
				QCurveSegment([0, 44], [44, 44]),
				BeelineSegment((78, 0)),
				BeelineSegment((0, -90))
			]))
		self.strokeInfo_豎彎鉤_3_r=StrokeInfo("豎彎鉤", StrokePath([
				BeelineSegment((0, 20)),
				QCurveSegment([0, 102], [102, 102]),
				BeelineSegment((22, 0)),
				BeelineSegment((0, -49))
			]))
		self.strokeInfo_豎彎鉤_4_r=StrokeInfo("豎彎鉤", StrokePath([
				BeelineSegment((0, 17)),
				QCurveSegment([0, 11], [11, 11]),
				BeelineSegment((112, 0)),
				BeelineSegment((0, -9))
			]))

		self.strokeInfo_豎彎_1=self.generateStrokeInfo("豎彎", (13, 76, 100))
		self.strokeInfo_豎彎_2=self.generateStrokeInfo("豎彎", (56, 93, 3))
		self.strokeInfo_豎彎_3=self.generateStrokeInfo("豎彎", (30, 127, 75))
		self.strokeInfo_豎彎_4=self.generateStrokeInfo("豎彎", (40, 7, 95))
		self.strokeInfo_豎彎_1_r=StrokeInfo("豎彎", StrokePath([
				BeelineSegment((0, 76)),
				QCurveSegment([0, 100], [100, 100]),
				BeelineSegment((13, 0))
			]))
		self.strokeInfo_豎彎_2_r=StrokeInfo("豎彎", StrokePath([
				BeelineSegment((0, 93)),
				QCurveSegment([0, 3], [3, 3]),
				BeelineSegment((56, 0))
			]))
		self.strokeInfo_豎彎_3_r=StrokeInfo("豎彎", StrokePath([
				BeelineSegment((0, 127)),
				QCurveSegment([0, 75], [75, 75]),
				BeelineSegment((30, 0))
			]))
		self.strokeInfo_豎彎_4_r=StrokeInfo("豎彎", StrokePath([
				BeelineSegment((0, 7)),
				QCurveSegment([0, 95], [95, 95]),
				BeelineSegment((40, 0))
			]))

		self.strokeInfo_豎鉤_1=self.generateStrokeInfo("豎鉤", (115, 21, 5))
		self.strokeInfo_豎鉤_2=self.generateStrokeInfo("豎鉤", (110, 27, 10))
		self.strokeInfo_豎鉤_3=self.generateStrokeInfo("豎鉤", (21, 109, 2))
		self.strokeInfo_豎鉤_4=self.generateStrokeInfo("豎鉤", (77, 40, 2))
		self.strokeInfo_豎鉤_1_r=StrokeInfo("豎鉤", StrokePath([
				BeelineSegment((0, 100)),
				QCurveSegment((0, 15), (-5, 15)),
				BeelineSegment((-10, -10))
			]))
		self.strokeInfo_豎鉤_2_r=StrokeInfo("豎鉤", StrokePath([
				BeelineSegment((0, 80)),
				QCurveSegment((0, 30), (-6, 30)),
				BeelineSegment((-13, -13))
			]))
		self.strokeInfo_豎鉤_3_r=StrokeInfo("豎鉤", StrokePath([
				BeelineSegment((0, 15)),
				QCurveSegment((0, 6), (-27, 6)),
				BeelineSegment((-54, -54))
			]))
		self.strokeInfo_豎鉤_4_r=StrokeInfo("豎鉤", StrokePath([
				BeelineSegment((0, 71)),
				QCurveSegment((0, 6), (-10, 6)),
				BeelineSegment((-20, -20))
			]))

		self.strokeInfo_斜鉤_1=self.generateStrokeInfo("斜鉤", (121, 18, 56))
		self.strokeInfo_斜鉤_2=self.generateStrokeInfo("斜鉤", (64, 69, 70))
		self.strokeInfo_斜鉤_3=self.generateStrokeInfo("斜鉤", (86, 15, 98))
		self.strokeInfo_斜鉤_4=self.generateStrokeInfo("斜鉤", (68, 116, 68))
		self.strokeInfo_斜鉤_1_r=StrokeInfo("斜鉤", StrokePath([
				QCurveSegment((24, 14), (121, 18)),
				BeelineSegment((0, -56))
			]))
		self.strokeInfo_斜鉤_2_r=StrokeInfo("斜鉤", StrokePath([
				QCurveSegment((12, 55), (64, 69)),
				BeelineSegment((0, -70))
			]))
		self.strokeInfo_斜鉤_3_r=StrokeInfo("斜鉤", StrokePath([
				QCurveSegment((17, 12), (86, 15)),
				BeelineSegment((0, -98))
			]))
		self.strokeInfo_斜鉤_4_r=StrokeInfo("斜鉤", StrokePath([
				QCurveSegment((13, 92), (68, 116)),
				BeelineSegment((0, -68))
			]))

		self.strokeInfo_彎鉤_1=self.generateStrokeInfo("彎鉤", (90, 114, 17, 38))
		self.strokeInfo_彎鉤_2=self.generateStrokeInfo("彎鉤", (35, 96, 48, 127))
		self.strokeInfo_彎鉤_3=self.generateStrokeInfo("彎鉤", (115, 55, 75, 110))
		self.strokeInfo_彎鉤_4=self.generateStrokeInfo("彎鉤", (49, 99, 52, 125))
		self.strokeInfo_彎鉤_1_r=StrokeInfo("彎鉤", StrokePath([
				QCurveSegment((102, 12), [90, 114]),
				BeelineSegment((-17, -38))
			]))
		self.strokeInfo_彎鉤_2_r=StrokeInfo("彎鉤", StrokePath([
				QCurveSegment((65, 31), [35, 96]),
				BeelineSegment((-48, -127))
			]))
		self.strokeInfo_彎鉤_3_r=StrokeInfo("彎鉤", StrokePath([
				QCurveSegment((84, -30), [115, 55]),
				BeelineSegment((-75, -110))
			]))
		self.strokeInfo_彎鉤_4_r=StrokeInfo("彎鉤", StrokePath([
				QCurveSegment((73, 25), [49, 99]),
				BeelineSegment((-52, -125))
			]))

		self.strokeInfo_撇鉤_1=self.generateStrokeInfo("撇鉤", (34, 30, 125, 114))
		self.strokeInfo_撇鉤_2=self.generateStrokeInfo("撇鉤", (12, 83, 87, 59))
		self.strokeInfo_撇鉤_3=self.generateStrokeInfo("撇鉤", (54, 69, 77, 64))
		self.strokeInfo_撇鉤_4=self.generateStrokeInfo("撇鉤", (110, 31, 97, 121))
		self.strokeInfo_撇鉤_1_r=StrokeInfo("撇鉤", StrokePath([
				QCurveSegment((32, -2), [34, 30]),
				BeelineSegment((-125, -114))
			]))
		self.strokeInfo_撇鉤_2_r=StrokeInfo("撇鉤", StrokePath([
				QCurveSegment((47, 35), [12, 83]),
				BeelineSegment((-87, -59))
			]))
		self.strokeInfo_撇鉤_3_r=StrokeInfo("撇鉤", StrokePath([
				QCurveSegment((61, 7), [54, 69]),
				BeelineSegment((-77, -64))
			]))
		self.strokeInfo_撇鉤_4_r=StrokeInfo("撇鉤", StrokePath([
				QCurveSegment((70, -40), [110, 31]),
				BeelineSegment((-97, -121))
			]))

		self.strokeInfo_撇_1=self.generateStrokeInfo("撇", (64, 100))
		self.strokeInfo_撇_2=self.generateStrokeInfo("撇", (13, 120))
		self.strokeInfo_撇_3=self.generateStrokeInfo("撇", (40, 91))
		self.strokeInfo_撇_4=self.generateStrokeInfo("撇", (64, 68))
		self.strokeInfo_撇_1_r=StrokeInfo("撇", StrokePath([
				BeelineSegment((-64, 100))
			]))
		self.strokeInfo_撇_2_r=StrokeInfo("撇", StrokePath([
				BeelineSegment((-13, 120))
			]))
		self.strokeInfo_撇_3_r=StrokeInfo("撇", StrokePath([
				BeelineSegment((-40, 91))
			]))
		self.strokeInfo_撇_4_r=StrokeInfo("撇", StrokePath([
				BeelineSegment((-64, 68))
			]))

		self.strokeInfo_撇點_1=self.generateStrokeInfo("撇點", (104, 96, 86, 60))
		self.strokeInfo_撇點_2=self.generateStrokeInfo("撇點", (51, 18, 126, 64))
		self.strokeInfo_撇點_3=self.generateStrokeInfo("撇點", (127, 93, 43, 11))
		self.strokeInfo_撇點_4=self.generateStrokeInfo("撇點", (119, 121, 86, 120))
		self.strokeInfo_撇點_1_r=StrokeInfo("撇點", StrokePath([
				BeelineSegment((-104, 96)),
				BeelineSegment((86, 60))
			]))
		self.strokeInfo_撇點_2_r=StrokeInfo("撇點", StrokePath([
				BeelineSegment((-51, 18)),
				BeelineSegment((126, 64))
			]))
		self.strokeInfo_撇點_3_r=StrokeInfo("撇點", StrokePath([
				BeelineSegment((-127, 93)),
				BeelineSegment((43, 11))
			]))
		self.strokeInfo_撇點_4_r=StrokeInfo("撇點", StrokePath([
				BeelineSegment((-119, 121)),
				BeelineSegment((86, 120))
			]))

		self.strokeInfo_撇橫_1=self.generateStrokeInfo("撇橫", (36, 42, 82, 5))
		self.strokeInfo_撇橫_2=self.generateStrokeInfo("撇橫", (64, 34, 23, 110))
		self.strokeInfo_撇橫_3=self.generateStrokeInfo("撇橫", (30, 121, 67, 75))
		self.strokeInfo_撇橫_4=self.generateStrokeInfo("撇橫", (118, 48, 90, 115))
		self.strokeInfo_撇橫_1_r=StrokeInfo("撇橫", StrokePath([
				BeelineSegment((-36, 42)),
				BeelineSegment((82, 5))
			]))
		self.strokeInfo_撇橫_2_r=StrokeInfo("撇橫", StrokePath([
				BeelineSegment((-64, 34)),
				BeelineSegment((23, 110))
			]))
		self.strokeInfo_撇橫_3_r=StrokeInfo("撇橫", StrokePath([
				BeelineSegment((-30, 121)),
				BeelineSegment((67, 75))
			]))
		self.strokeInfo_撇橫_4_r=StrokeInfo("撇橫", StrokePath([
				BeelineSegment((-118, 48)),
				BeelineSegment((90, 115))
			]))

		self.strokeInfo_撇橫撇_1=self.generateStrokeInfo("撇橫撇", (69, 71, 86, 20, 22))
		self.strokeInfo_撇橫撇_2=self.generateStrokeInfo("撇橫撇", (72, 72, 21, 2, 2))
		self.strokeInfo_撇橫撇_3=self.generateStrokeInfo("撇橫撇", (80, 52, 1, 37, 117))
		self.strokeInfo_撇橫撇_4=self.generateStrokeInfo("撇橫撇", (21, 78, 40, 124, 46))
		self.strokeInfo_撇橫撇_1_r=StrokeInfo("撇橫撇", StrokePath([
				BeelineSegment((-69, 71)),
				BeelineSegment((86, 0)),
				BeelineSegment((-20, 22))
			]))
		self.strokeInfo_撇橫撇_2_r=StrokeInfo("撇橫撇", StrokePath([
				BeelineSegment((-72, 72)),
				BeelineSegment((21, 0)),
				BeelineSegment((-2, 2))
			]))
		self.strokeInfo_撇橫撇_3_r=StrokeInfo("撇橫撇", StrokePath([
				BeelineSegment((-80, 52)),
				BeelineSegment((1, 0)),
				BeelineSegment((-37, 117))
			]))
		self.strokeInfo_撇橫撇_4_r=StrokeInfo("撇橫撇", StrokePath([
				BeelineSegment((-21, 78)),
				BeelineSegment((40, 0)),
				BeelineSegment((-124, 46))
			]))

		self.strokeInfo_豎撇_1=self.generateStrokeInfo("豎撇", (89, 12))
		self.strokeInfo_豎撇_2=self.generateStrokeInfo("豎撇", (74, 10))
		self.strokeInfo_豎撇_3=self.generateStrokeInfo("豎撇", (10, 65))
		self.strokeInfo_豎撇_4=self.generateStrokeInfo("豎撇", (61, 71))
		self.strokeInfo_豎撇_1_r=StrokeInfo("豎撇", StrokePath([
				BeelineSegment((0, 6)),
				QCurveSegment((0, 6), (-89, 6))
			]))
		self.strokeInfo_豎撇_2_r=StrokeInfo("豎撇", StrokePath([
				BeelineSegment((0, 5)),
				QCurveSegment((0, 5), (-74, 5))
			]))
		self.strokeInfo_豎撇_3_r=StrokeInfo("豎撇", StrokePath([
				BeelineSegment((0, 33)),
				QCurveSegment((0, 32), (-10, 32))
			]))
		self.strokeInfo_豎撇_4_r=StrokeInfo("豎撇", StrokePath([
				BeelineSegment((0, 36)),
				QCurveSegment((0, 35), (-61, 35))
			]))

		self.strokeInfo_提_1=self.generateStrokeInfo("提", (7, 17))
		self.strokeInfo_提_2=self.generateStrokeInfo("提", (121, 62))
		self.strokeInfo_提_3=self.generateStrokeInfo("提", (52, 93))
		self.strokeInfo_提_4=self.generateStrokeInfo("提", (118, 3))
		self.strokeInfo_提_1_r=StrokeInfo("提", StrokePath([
				BeelineSegment((7, -17))
			]))
		self.strokeInfo_提_2_r=StrokeInfo("提", StrokePath([
				BeelineSegment((121, -62))
			]))
		self.strokeInfo_提_3_r=StrokeInfo("提", StrokePath([
				BeelineSegment((52, -93))
			]))
		self.strokeInfo_提_4_r=StrokeInfo("提", StrokePath([
				BeelineSegment((118, -3))
			]))

		self.strokeInfo_捺_1=self.generateStrokeInfo("捺", (107, 63))
		self.strokeInfo_捺_2=self.generateStrokeInfo("捺", (101, 27))
		self.strokeInfo_捺_3=self.generateStrokeInfo("捺", (109, 55))
		self.strokeInfo_捺_4=self.generateStrokeInfo("捺", (36, 125))
		self.strokeInfo_捺_1_r=StrokeInfo("捺", StrokePath([
				QCurveSegment((35.0, 62.0), (107, 63))
			]))
		self.strokeInfo_捺_2_r=StrokeInfo("捺", StrokePath([
				QCurveSegment((47.0, 26.0), (101, 27))
			]))
		self.strokeInfo_捺_3_r=StrokeInfo("捺", StrokePath([
				QCurveSegment((41.0, 54.0), (109, 55))
			]))
		self.strokeInfo_捺_4_r=StrokeInfo("捺", StrokePath([
				QCurveSegment((1.0, 67.0), (36, 125))
			]))

		self.strokeInfo_臥捺_1=self.generateStrokeInfo("臥捺", (8, 53))
		self.strokeInfo_臥捺_2=self.generateStrokeInfo("臥捺", (68, 6))
		self.strokeInfo_臥捺_3=self.generateStrokeInfo("臥捺", (8, 39))
		self.strokeInfo_臥捺_4=self.generateStrokeInfo("臥捺", (4, 15))
		self.strokeInfo_臥捺_1_r=StrokeInfo("臥捺", StrokePath([
				QCurveSegment((8, 12), (4, 26)),
				QCurveSegment((-4, 14), (4, 26))
			]))
		self.strokeInfo_臥捺_2_r=StrokeInfo("臥捺", StrokePath([
				QCurveSegment((17, -7), (34, 3)),
				QCurveSegment((17, 9), (34, 3))
			]))
		self.strokeInfo_臥捺_3_r=StrokeInfo("臥捺", StrokePath([
				QCurveSegment((6, 8), (4, 19)),
				QCurveSegment((-2, 10), (4, 19))
			]))
		self.strokeInfo_臥捺_4_r=StrokeInfo("臥捺", StrokePath([
				QCurveSegment((2, 3), (2, 7)),
				QCurveSegment((0, 3), (2, 7))
			]))

		self.strokeInfo_提捺_1=self.generateStrokeInfo("提捺", (14, 43, 46, 43))
		self.strokeInfo_提捺_2=self.generateStrokeInfo("提捺", (2, 26, 41, 66))
		self.strokeInfo_提捺_3=self.generateStrokeInfo("提捺", (93, 18, 120, 6))
		self.strokeInfo_提捺_4=self.generateStrokeInfo("提捺", (114, 10, 122, 61))
		self.strokeInfo_提捺_1_r=StrokeInfo("提捺", StrokePath([
				BeelineSegment((14, -43)),
				QCurveSegment((9, 36), (46, 43))
			]))
		self.strokeInfo_提捺_2_r=StrokeInfo("提捺", StrokePath([
				BeelineSegment((2, -26)),
				QCurveSegment((0.0, 45.0), (41, 66))
			]))
		self.strokeInfo_提捺_3_r=StrokeInfo("提捺", StrokePath([
				BeelineSegment((93, -18)),
				QCurveSegment((60.0, 6.0), (120, 6))
			]))
		self.strokeInfo_提捺_4_r=StrokeInfo("提捺", StrokePath([
				BeelineSegment((114, -10)),
				QCurveSegment((46.0, 60.0), (122, 61))
			]))

		self.strokeInfo_橫捺_1=self.generateStrokeInfo("橫捺", (49, 17, 40))
		self.strokeInfo_橫捺_2=self.generateStrokeInfo("橫捺", (64, 98, 91))
		self.strokeInfo_橫捺_3=self.generateStrokeInfo("橫捺", (12, 26, 12))
		self.strokeInfo_橫捺_4=self.generateStrokeInfo("橫捺", (4, 49, 124))
		self.strokeInfo_橫捺_1_r=StrokeInfo("橫捺", StrokePath([
				BeelineSegment((49, 0)),
				QCurveSegment((0.0, 23.0), (17, 40))
			]))
		self.strokeInfo_橫捺_2_r=StrokeInfo("橫捺", StrokePath([
				BeelineSegment((64, 0)),
				QCurveSegment((19, 77), (98, 91))
			]))
		self.strokeInfo_橫捺_3_r=StrokeInfo("橫捺", StrokePath([
				BeelineSegment((12, 0)),
				QCurveSegment((11.0, 12.0), (26, 12))
			]))
		self.strokeInfo_橫捺_4_r=StrokeInfo("橫捺", StrokePath([
				BeelineSegment((4, 0)),QCurveSegment((0.0, 71.0), (49, 124))
			]))

	def testStrokeInfo(self):
		strokeInfo = StrokeInfo("空", StrokePath([]))
		self.assertEqual(strokeInfo.getName(), "空")
		self.assertEqual(strokeInfo.getStrokePath(), StrokePath([]))

		segments=[BeelineSegment((37, 41)), QCurveSegment((0, -99), (57, -99))]
		strokeInfo = StrokeInfo("測試", StrokePath(segments))
		self.assertEqual(strokeInfo.getName(), "測試")
		self.assertEqual(strokeInfo.getStrokePath(), StrokePath(segments))

	def testStrokeInfo_點(self):
		self.assertEqual(self.strokeInfo_點_1, self.strokeInfo_點_1_r)
		self.assertEqual(self.strokeInfo_點_2, self.strokeInfo_點_2_r)
		self.assertEqual(self.strokeInfo_點_3, self.strokeInfo_點_3_r)
		self.assertEqual(self.strokeInfo_點_4, self.strokeInfo_點_4_r)

	def testStrokeInfo_圈(self):
		self.assertEqual(self.strokeInfo_圈_1, self.strokeInfo_圈_1_r)
		self.assertEqual(self.strokeInfo_圈_2, self.strokeInfo_圈_2_r)
		self.assertEqual(self.strokeInfo_圈_3, self.strokeInfo_圈_3_r)
		self.assertEqual(self.strokeInfo_圈_4, self.strokeInfo_圈_4_r)

	def testStrokeInfo_橫(self):
		self.assertEqual(self.strokeInfo_橫_1, self.strokeInfo_橫_1_r)
		self.assertEqual(self.strokeInfo_橫_2, self.strokeInfo_橫_2_r)
		self.assertEqual(self.strokeInfo_橫_3, self.strokeInfo_橫_3_r)
		self.assertEqual(self.strokeInfo_橫_4, self.strokeInfo_橫_4_r)

	def testStrokeInfo_橫鉤(self):
		self.assertEqual(self.strokeInfo_橫鉤_1, self.strokeInfo_橫鉤_1_r)
		self.assertEqual(self.strokeInfo_橫鉤_2, self.strokeInfo_橫鉤_2_r)
		self.assertEqual(self.strokeInfo_橫鉤_3, self.strokeInfo_橫鉤_3_r)
		self.assertEqual(self.strokeInfo_橫鉤_4, self.strokeInfo_橫鉤_4_r)

	def testStrokeInfo_橫折(self):
		self.assertEqual(self.strokeInfo_橫折_1, self.strokeInfo_橫折_1_r)
		self.assertEqual(self.strokeInfo_橫折_2, self.strokeInfo_橫折_2_r)
		self.assertEqual(self.strokeInfo_橫折_3, self.strokeInfo_橫折_3_r)
		self.assertEqual(self.strokeInfo_橫折_4, self.strokeInfo_橫折_4_r)

	def testStrokeInfo_橫折折(self):
		self.assertEqual(self.strokeInfo_橫折折_1, self.strokeInfo_橫折折_1_r)
		self.assertEqual(self.strokeInfo_橫折折_2, self.strokeInfo_橫折折_2_r)
		self.assertEqual(self.strokeInfo_橫折折_3, self.strokeInfo_橫折折_3_r)
		self.assertEqual(self.strokeInfo_橫折折_4, self.strokeInfo_橫折折_4_r)

	def testStrokeInfo_橫折提(self):
		self.assertEqual(self.strokeInfo_橫折提_1, self.strokeInfo_橫折提_1_r)
		self.assertEqual(self.strokeInfo_橫折提_2, self.strokeInfo_橫折提_2_r)
		self.assertEqual(self.strokeInfo_橫折提_3, self.strokeInfo_橫折提_3_r)
		self.assertEqual(self.strokeInfo_橫折提_4, self.strokeInfo_橫折提_4_r)

	def testStrokeInfo_橫折折撇(self):
		self.assertEqual(self.strokeInfo_橫折折撇_1, self.strokeInfo_橫折折撇_1_r)
		self.assertEqual(self.strokeInfo_橫折折撇_2, self.strokeInfo_橫折折撇_2_r)
		self.assertEqual(self.strokeInfo_橫折折撇_3, self.strokeInfo_橫折折撇_3_r)
		self.assertEqual(self.strokeInfo_橫折折撇_4, self.strokeInfo_橫折折撇_4_r)

	def testStrokeInfo_橫撇彎鉤(self):
		self.assertEqual(self.strokeInfo_橫撇彎鉤_1, self.strokeInfo_橫撇彎鉤_1_r)
		self.assertEqual(self.strokeInfo_橫撇彎鉤_2, self.strokeInfo_橫撇彎鉤_2_r)
		self.assertEqual(self.strokeInfo_橫撇彎鉤_3, self.strokeInfo_橫撇彎鉤_3_r)
		self.assertEqual(self.strokeInfo_橫撇彎鉤_4, self.strokeInfo_橫撇彎鉤_4_r)

	def testStrokeInfo_橫折鉤(self):
		self.assertEqual(self.strokeInfo_橫折鉤_1, self.strokeInfo_橫折鉤_1_r)
		self.assertEqual(self.strokeInfo_橫折鉤_2, self.strokeInfo_橫折鉤_2_r)
		self.assertEqual(self.strokeInfo_橫折鉤_3, self.strokeInfo_橫折鉤_3_r)
		self.assertEqual(self.strokeInfo_橫折鉤_4, self.strokeInfo_橫折鉤_4_r)

	def testStrokeInfo_橫折彎(self):
		self.assertEqual(self.strokeInfo_橫折彎_1, self.strokeInfo_橫折彎_1_r)
		self.assertEqual(self.strokeInfo_橫折彎_2, self.strokeInfo_橫折彎_2_r)
		self.assertEqual(self.strokeInfo_橫折彎_3, self.strokeInfo_橫折彎_3_r)
		self.assertEqual(self.strokeInfo_橫折彎_4, self.strokeInfo_橫折彎_4_r)

	def testStrokeInfo_橫撇(self):
		self.assertEqual(self.strokeInfo_橫撇_1, self.strokeInfo_橫撇_1_r)
		self.assertEqual(self.strokeInfo_橫撇_2, self.strokeInfo_橫撇_2_r)
		self.assertEqual(self.strokeInfo_橫撇_3, self.strokeInfo_橫撇_3_r)
		self.assertEqual(self.strokeInfo_橫撇_4, self.strokeInfo_橫撇_4_r)

	def testStrokeInfo_橫斜彎鉤(self):
		self.assertEqual(self.strokeInfo_橫斜彎鉤_1, self.strokeInfo_橫斜彎鉤_1_r)
		self.assertEqual(self.strokeInfo_橫斜彎鉤_2, self.strokeInfo_橫斜彎鉤_2_r)
		self.assertEqual(self.strokeInfo_橫斜彎鉤_3, self.strokeInfo_橫斜彎鉤_3_r)
		self.assertEqual(self.strokeInfo_橫斜彎鉤_4, self.strokeInfo_橫斜彎鉤_4_r)

	def testStrokeInfo_橫折折折鉤(self):
		self.assertEqual(self.strokeInfo_橫折折折鉤_1, self.strokeInfo_橫折折折鉤_1_r)
		self.assertEqual(self.strokeInfo_橫折折折鉤_2, self.strokeInfo_橫折折折鉤_2_r)
		self.assertEqual(self.strokeInfo_橫折折折鉤_3, self.strokeInfo_橫折折折鉤_3_r)
		self.assertEqual(self.strokeInfo_橫折折折鉤_4, self.strokeInfo_橫折折折鉤_4_r)

	def testStrokeInfo_橫斜鉤(self):
		self.assertEqual(self.strokeInfo_橫斜鉤_1, self.strokeInfo_橫斜鉤_1_r)
		self.assertEqual(self.strokeInfo_橫斜鉤_2, self.strokeInfo_橫斜鉤_2_r)
		self.assertEqual(self.strokeInfo_橫斜鉤_3, self.strokeInfo_橫斜鉤_3_r)
		self.assertEqual(self.strokeInfo_橫斜鉤_4, self.strokeInfo_橫斜鉤_4_r)

	def testStrokeInfo_橫折折折(self):
		self.assertEqual(self.strokeInfo_橫折折折_1, self.strokeInfo_橫折折折_1_r)
		self.assertEqual(self.strokeInfo_橫折折折_2, self.strokeInfo_橫折折折_2_r)
		self.assertEqual(self.strokeInfo_橫折折折_3, self.strokeInfo_橫折折折_3_r)
		self.assertEqual(self.strokeInfo_橫折折折_4, self.strokeInfo_橫折折折_4_r)

	def testStrokeInfo_豎(self):
		self.assertEqual(self.strokeInfo_豎_1, self.strokeInfo_豎_1_r)
		self.assertEqual(self.strokeInfo_豎_2, self.strokeInfo_豎_2_r)
		self.assertEqual(self.strokeInfo_豎_3, self.strokeInfo_豎_3_r)
		self.assertEqual(self.strokeInfo_豎_4, self.strokeInfo_豎_4_r)

	def testStrokeInfo_豎折(self):
		self.assertEqual(self.strokeInfo_豎折_1, self.strokeInfo_豎折_1_r)
		self.assertEqual(self.strokeInfo_豎折_2, self.strokeInfo_豎折_2_r)
		self.assertEqual(self.strokeInfo_豎折_3, self.strokeInfo_豎折_3_r)
		self.assertEqual(self.strokeInfo_豎折_4, self.strokeInfo_豎折_4_r)

	def testStrokeInfo_豎彎左(self):
		self.assertEqual(self.strokeInfo_豎彎左_1, self.strokeInfo_豎彎左_1_r)
		self.assertEqual(self.strokeInfo_豎彎左_2, self.strokeInfo_豎彎左_2_r)
		self.assertEqual(self.strokeInfo_豎彎左_3, self.strokeInfo_豎彎左_3_r)
		self.assertEqual(self.strokeInfo_豎彎左_4, self.strokeInfo_豎彎左_4_r)

	def testStrokeInfo_豎提(self):
		self.assertEqual(self.strokeInfo_豎提_1, self.strokeInfo_豎提_1_r)
		self.assertEqual(self.strokeInfo_豎提_2, self.strokeInfo_豎提_2_r)
		self.assertEqual(self.strokeInfo_豎提_3, self.strokeInfo_豎提_3_r)
		self.assertEqual(self.strokeInfo_豎提_4, self.strokeInfo_豎提_4_r)

	def testStrokeInfo_豎折折(self):
		self.assertEqual(self.strokeInfo_豎折折_1, self.strokeInfo_豎折折_1_r)
		self.assertEqual(self.strokeInfo_豎折折_2, self.strokeInfo_豎折折_2_r)
		self.assertEqual(self.strokeInfo_豎折折_3, self.strokeInfo_豎折折_3_r)
		self.assertEqual(self.strokeInfo_豎折折_4, self.strokeInfo_豎折折_4_r)

	def testStrokeInfo_豎折彎鉤(self):
		self.assertEqual(self.strokeInfo_豎折彎鉤_1, self.strokeInfo_豎折彎鉤_1_r)
		self.assertEqual(self.strokeInfo_豎折彎鉤_2, self.strokeInfo_豎折彎鉤_2_r)
		self.assertEqual(self.strokeInfo_豎折彎鉤_3, self.strokeInfo_豎折彎鉤_3_r)
		self.assertEqual(self.strokeInfo_豎折彎鉤_4, self.strokeInfo_豎折彎鉤_4_r)

	def testStrokeInfo_豎彎鉤(self):
		self.assertEqual(self.strokeInfo_豎彎鉤_1, self.strokeInfo_豎彎鉤_1_r)
		self.assertEqual(self.strokeInfo_豎彎鉤_2, self.strokeInfo_豎彎鉤_2_r)
		self.assertEqual(self.strokeInfo_豎彎鉤_3, self.strokeInfo_豎彎鉤_3_r)
		self.assertEqual(self.strokeInfo_豎彎鉤_4, self.strokeInfo_豎彎鉤_4_r)

	def testStrokeInfo_豎彎(self):
		self.assertEqual(self.strokeInfo_豎彎_1, self.strokeInfo_豎彎_1_r)
		self.assertEqual(self.strokeInfo_豎彎_2, self.strokeInfo_豎彎_2_r)
		self.assertEqual(self.strokeInfo_豎彎_3, self.strokeInfo_豎彎_3_r)
		self.assertEqual(self.strokeInfo_豎彎_4, self.strokeInfo_豎彎_4_r)

	def testStrokeInfo_豎鉤(self):
		self.assertEqual(self.strokeInfo_豎鉤_1, self.strokeInfo_豎鉤_1_r)
		self.assertEqual(self.strokeInfo_豎鉤_2, self.strokeInfo_豎鉤_2_r)
		self.assertEqual(self.strokeInfo_豎鉤_3, self.strokeInfo_豎鉤_3_r)
		self.assertEqual(self.strokeInfo_豎鉤_4, self.strokeInfo_豎鉤_4_r)

	def testStrokeInfo_斜鉤(self):
		self.assertEqual(self.strokeInfo_斜鉤_1, self.strokeInfo_斜鉤_1_r)
		self.assertEqual(self.strokeInfo_斜鉤_2, self.strokeInfo_斜鉤_2_r)
		self.assertEqual(self.strokeInfo_斜鉤_3, self.strokeInfo_斜鉤_3_r)
		self.assertEqual(self.strokeInfo_斜鉤_4, self.strokeInfo_斜鉤_4_r)

	def testStrokeInfo_彎鉤(self):
		self.assertEqual(self.strokeInfo_彎鉤_1, self.strokeInfo_彎鉤_1_r)
		self.assertEqual(self.strokeInfo_彎鉤_2, self.strokeInfo_彎鉤_2_r)
		self.assertEqual(self.strokeInfo_彎鉤_3, self.strokeInfo_彎鉤_3_r)
		self.assertEqual(self.strokeInfo_彎鉤_4, self.strokeInfo_彎鉤_4_r)

	def testStrokeInfo_撇鉤(self):
		self.assertEqual(self.strokeInfo_撇鉤_1, self.strokeInfo_撇鉤_1_r)
		self.assertEqual(self.strokeInfo_撇鉤_2, self.strokeInfo_撇鉤_2_r)
		self.assertEqual(self.strokeInfo_撇鉤_3, self.strokeInfo_撇鉤_3_r)
		self.assertEqual(self.strokeInfo_撇鉤_4, self.strokeInfo_撇鉤_4_r)

	def testStrokeInfo_撇(self):
		self.assertEqual(self.strokeInfo_撇_1, self.strokeInfo_撇_1_r)
		self.assertEqual(self.strokeInfo_撇_2, self.strokeInfo_撇_2_r)
		self.assertEqual(self.strokeInfo_撇_3, self.strokeInfo_撇_3_r)
		self.assertEqual(self.strokeInfo_撇_4, self.strokeInfo_撇_4_r)

	def testStrokeInfo_撇點(self):
		self.assertEqual(self.strokeInfo_撇點_1, self.strokeInfo_撇點_1_r)
		self.assertEqual(self.strokeInfo_撇點_2, self.strokeInfo_撇點_2_r)
		self.assertEqual(self.strokeInfo_撇點_3, self.strokeInfo_撇點_3_r)
		self.assertEqual(self.strokeInfo_撇點_4, self.strokeInfo_撇點_4_r)

	def testStrokeInfo_撇橫(self):
		self.assertEqual(self.strokeInfo_撇橫_1, self.strokeInfo_撇橫_1_r)
		self.assertEqual(self.strokeInfo_撇橫_2, self.strokeInfo_撇橫_2_r)
		self.assertEqual(self.strokeInfo_撇橫_3, self.strokeInfo_撇橫_3_r)
		self.assertEqual(self.strokeInfo_撇橫_4, self.strokeInfo_撇橫_4_r)

	def testStrokeInfo_撇橫撇(self):
		self.assertEqual(self.strokeInfo_撇橫撇_1, self.strokeInfo_撇橫撇_1_r)
		self.assertEqual(self.strokeInfo_撇橫撇_2, self.strokeInfo_撇橫撇_2_r)
		self.assertEqual(self.strokeInfo_撇橫撇_3, self.strokeInfo_撇橫撇_3_r)
		self.assertEqual(self.strokeInfo_撇橫撇_4, self.strokeInfo_撇橫撇_4_r)

	def testStrokeInfo_豎撇(self):
		self.assertEqual(self.strokeInfo_豎撇_1, self.strokeInfo_豎撇_1_r)
		self.assertEqual(self.strokeInfo_豎撇_2, self.strokeInfo_豎撇_2_r)
		self.assertEqual(self.strokeInfo_豎撇_3, self.strokeInfo_豎撇_3_r)
		self.assertEqual(self.strokeInfo_豎撇_4, self.strokeInfo_豎撇_4_r)

	def testStrokeInfo_提(self):
		self.assertEqual(self.strokeInfo_提_1, self.strokeInfo_提_1_r)
		self.assertEqual(self.strokeInfo_提_2, self.strokeInfo_提_2_r)
		self.assertEqual(self.strokeInfo_提_3, self.strokeInfo_提_3_r)
		self.assertEqual(self.strokeInfo_提_4, self.strokeInfo_提_4_r)

	def testStrokeInfo_捺(self):
		self.assertEqual(self.strokeInfo_捺_1, self.strokeInfo_捺_1_r)
		self.assertEqual(self.strokeInfo_捺_2, self.strokeInfo_捺_2_r)
		self.assertEqual(self.strokeInfo_捺_3, self.strokeInfo_捺_3_r)
		self.assertEqual(self.strokeInfo_捺_4, self.strokeInfo_捺_4_r)

	def testStrokeInfo_臥捺(self):
		self.assertEqual(self.strokeInfo_臥捺_1, self.strokeInfo_臥捺_1_r)
		self.assertEqual(self.strokeInfo_臥捺_2, self.strokeInfo_臥捺_2_r)
		self.assertEqual(self.strokeInfo_臥捺_3, self.strokeInfo_臥捺_3_r)
		self.assertEqual(self.strokeInfo_臥捺_4, self.strokeInfo_臥捺_4_r)

	def testStrokeInfo_提捺(self):
		self.assertEqual(self.strokeInfo_提捺_1, self.strokeInfo_提捺_1_r)
		self.assertEqual(self.strokeInfo_提捺_2, self.strokeInfo_提捺_2_r)
		self.assertEqual(self.strokeInfo_提捺_3, self.strokeInfo_提捺_3_r)
		self.assertEqual(self.strokeInfo_提捺_4, self.strokeInfo_提捺_4_r)

	def testStrokeInfo_橫捺(self):
		self.assertEqual(self.strokeInfo_橫捺_1, self.strokeInfo_橫捺_1_r)
		self.assertEqual(self.strokeInfo_橫捺_2, self.strokeInfo_橫捺_2_r)
		self.assertEqual(self.strokeInfo_橫捺_3, self.strokeInfo_橫捺_3_r)
		self.assertEqual(self.strokeInfo_橫捺_4, self.strokeInfo_橫捺_4_r)

