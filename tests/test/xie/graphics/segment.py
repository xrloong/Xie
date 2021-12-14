import unittest
import copy

from xie.graphics.segment import BeelineSegment
from xie.graphics.segment import QCurveSegment
from xie.graphics.segment import SegmentFactory

from xie.graphics.stroke_path import StrokePath

class SegmentTestCase(unittest.TestCase):
	def setUp(self):
		self.segmentFactory = SegmentFactory()
		self.generateTestData()

	def tearDown(self):
		pass

	def generateTestData(self):
		self.beeline_0=BeelineSegment((0, 0))
		self.beeline_1=BeelineSegment((9, 118))
		self.beeline_2=BeelineSegment((-114, 103))
		self.beeline_3=BeelineSegment((123, -24))
		self.beeline_4=BeelineSegment((-11, -27))

		self.qcurve_1=QCurveSegment((33, 21), (57, 97))
		self.qcurve_2=QCurveSegment((80, 66), (-30, 16))
		self.qcurve_3=QCurveSegment((-5, -51), (65, -113))
		self.qcurve_4=QCurveSegment((-123, 71), (-37, -17))
		self.qcurve_5=QCurveSegment((-42, -74), (-25, 5))

		self.stroke_path_1=StrokePath([self.beeline_1])
		self.stroke_path_2=StrokePath([self.beeline_2])
		self.stroke_path_3=StrokePath([self.qcurve_1])
		self.stroke_path_4=StrokePath([self.qcurve_2])
		self.stroke_path_5=StrokePath([self.beeline_1, self.qcurve_1])
		self.stroke_path_6=StrokePath([self.beeline_1, self.qcurve_2])
		self.stroke_path_7=StrokePath([self.beeline_2, self.qcurve_1])

	def testBeelineEquality(self):
		self.assertEqual(self.beeline_1, self.beeline_1)
		self.assertEqual(self.beeline_1, copy.deepcopy(self.beeline_1))
		self.assertNotEqual(self.beeline_1, self.beeline_2)

	def testQCurveEquality(self):
		self.assertEqual(self.qcurve_1, self.qcurve_1)
		self.assertEqual(self.qcurve_1, copy.deepcopy(self.qcurve_1))
		self.assertNotEqual(self.qcurve_1, self.qcurve_2)

	def testStrokePathEquality(self):
		self.assertEqual(self.stroke_path_1, self.stroke_path_1)
		self.assertEqual(self.stroke_path_1, copy.deepcopy(self.stroke_path_1))
		self.assertNotEqual(self.stroke_path_1, self.stroke_path_2)

		self.assertEqual(self.stroke_path_3, self.stroke_path_3)
		self.assertEqual(self.stroke_path_3, copy.deepcopy(self.stroke_path_3))
		self.assertNotEqual(self.stroke_path_3, self.stroke_path_4)

		self.assertEqual(self.stroke_path_5, self.stroke_path_5)
		self.assertEqual(self.stroke_path_5, copy.deepcopy(self.stroke_path_5))
		self.assertNotEqual(self.stroke_path_5, StrokePath(self.stroke_path_6))
		self.assertNotEqual(self.stroke_path_5, StrokePath(self.stroke_path_7))

		self.assertEqual(StrokePath([]), StrokePath([]))

	def testBeeline(self):
		self.assertEqual(self.beeline_1.getEndPoint(), (9, 118))
		self.assertEqual(self.beeline_2.getEndPoint(), (-114, 103))
		self.assertEqual(self.beeline_3.getEndPoint(), (123, -24))
		self.assertEqual(self.beeline_4.getEndPoint(), (-11, -27))

		# specific
		beeline=self.beeline_0
		self.assertEqual(self.beeline_0.getEndPoint(), (0, 0))

	def testBeelineBoundary(self):
		self.assertEqual(self.beeline_1.computeBoundary(), (0, 0, 9, 118))
		self.assertEqual(self.beeline_2.computeBoundary(), (-114, 0, 0, 103))
		self.assertEqual(self.beeline_3.computeBoundary(), (0, -24, 123, 0))
		self.assertEqual(self.beeline_4.computeBoundary(), (-11, -27, 0, 0))

		self.assertEqual(self.beeline_0.computeBoundary(), (0, 0, 0, 0))

	def testQCurve(self):
		self.assertEqual(self.qcurve_1.getControlPoint(), (33, 21))
		self.assertEqual(self.qcurve_1.getEndPoint(), (57, 97))

	def testQCurveBoundary(self):
		self.assertEqual(self.qcurve_1.computeBoundary(), (0, 0, 57, 97))
		self.assertEqual(self.qcurve_2.computeBoundary(), (-30, 0, 34, 38))
		self.assertEqual(self.qcurve_3.computeBoundary(), (-1, -113, 65, 0))
		self.assertEqual(self.qcurve_4.computeBoundary(), (-73, -17, 0, 32))
		self.assertEqual(self.qcurve_5.computeBoundary(), (-30, -36, 0, 5))

