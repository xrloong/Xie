import unittest
import copy
import numpy

from xie.graphics.shape import Pane

class PaneTestCase(unittest.TestCase):
	def setUp(self):
		self.generateTestData()

	def tearDown(self):
		pass

	def generateTestData(self):
		self.pane_1=Pane(38, 32, 101, 50)
		self.pane_2=Pane(22, 50, 122, 89)
		self.pane_3=Pane(5, 20, 31, 32)
		self.pane_4=Pane(2, 1, 5, 88)

		self.point_1=(47, 51)
		self.point_2=(77, 43)

	def testPaneEquality(self):
		self.assertEqual(self.pane_1, copy.deepcopy(self.pane_1))
		self.assertEqual(self.pane_2, copy.deepcopy(self.pane_2))
		self.assertEqual(self.pane_3, copy.deepcopy(self.pane_3))
		self.assertEqual(self.pane_4, copy.deepcopy(self.pane_4))

	def test_transformRelativePointByTargetPane(self):
		transformedPoint_1=self.pane_1.transformRelativePointByTargetPane(self.point_1, self.pane_4)
		self.assertTrue(all(numpy.isclose(transformedPoint_1, (2.4285714285714284, 92.83333333333333))))

		transformedPoint_2=self.pane_1.transformRelativePointByTargetPane(self.point_2, self.pane_4)
		self.assertTrue(all(numpy.isclose(transformedPoint_2, (3.8571428571428568, 54.166666666666664))))

	def test_transformRelativePaneByTargetPane(self):
		transformedPane_1=self.pane_1.transformRelativePaneByTargetPane(self.pane_2, self.pane_4)
		self.assertEqual(transformedPane_1, Pane(1.2380952380952381, 88.0, 6.0, 276.5))

		transformedPane_2=self.pane_1.transformRelativePaneByTargetPane(self.pane_3, self.pane_4)
		self.assertEqual(transformedPane_2, Pane(0.4285714285714286, -57.0, 1.6666666666666667, 1.0))

