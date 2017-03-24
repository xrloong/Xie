import unittest
import copy

from xie.graphics.segment import BeelineSegment
from xie.graphics.segment import QCurveSegment
from xie.graphics.segment import StrokePath
from xie.graphics.segment import SegmentFactory
from xie.graphics.stroke_info import StrokeInfo

class FactoryTestCase(unittest.TestCase):
	def setUp(self):
		self.segmentFactory = SegmentFactory()
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
		pass

	def tearDown(self):
		pass

	def testStrokeInfo(self):
		strokeInfo = StrokeInfo("空", StrokePath([]))
		self.assertEqual(strokeInfo.getName(), "空")
		self.assertEqual(strokeInfo.getStrokePath(), StrokePath([]))

		segments=[BeelineSegment((37, 41)), QCurveSegment((0, -99), (57, -99))]
		strokeInfo = StrokeInfo("測試", StrokePath(segments))
		self.assertEqual(strokeInfo.getName(), "測試")
		self.assertEqual(strokeInfo.getStrokePath(), StrokePath(segments))

	def testStrokeInfo_點(self):
		pass

	def testStrokeInfo_圈(self):
		pass

	def testStrokeInfo_橫(self):
		pass

	def testStrokeInfo_橫鉤(self):
		pass

	def testStrokeInfo_橫折(self):
		pass

	def testStrokeInfo_橫折折(self):
		pass

	def testStrokeInfo_橫折提(self):
		pass

	def testStrokeInfo_橫折折撇(self):
		pass

	def testStrokeInfo_橫撇彎鉤(self):
		pass

	def testStrokeInfo_橫折鉤(self):
		pass

	def testStrokeInfo_橫折彎(self):
		pass

	def testStrokeInfo_橫撇(self):
		pass

	def testStrokeInfo_橫斜彎鉤(self):
		pass

	def testStrokeInfo_橫折折折鉤(self):
		pass

	def testStrokeInfo_橫斜鉤(self):
		pass

	def testStrokeInfo_橫折折折(self):
		pass

	def testStrokeInfo_豎(self):
		pass

	def testStrokeInfo_豎折(self):
		pass

	def testStrokeInfo_豎彎左(self):
		pass

	def testStrokeInfo_豎提(self):
		pass

	def testStrokeInfo_豎折折(self):
		pass

	def testStrokeInfo_豎折彎鉤(self):
		pass

	def testStrokeInfo_豎彎鉤(self):
		pass

	def testStrokeInfo_豎彎(self):
		pass

	def testStrokeInfo_豎鉤(self):
		pass

	def testStrokeInfo_斜鉤(self):
		pass

	def testStrokeInfo_彎鉤(self):
		pass

	def testStrokeInfo_撇鉤(self):
		pass

	def testStrokeInfo_撇(self):
		pass

	def testStrokeInfo_撇點(self):
		pass

	def testStrokeInfo_撇橫(self):
		pass

	def testStrokeInfo_撇橫撇(self):
		pass

	def testStrokeInfo_豎撇(self):
		pass

	def testStrokeInfo_提(self):
		pass

	def testStrokeInfo_捺(self):
		pass

	def testStrokeInfo_臥捺(self):
		pass

	def testStrokeInfo_提捺(self):
		pass

	def testStrokeInfo_橫捺(self):
		pass

