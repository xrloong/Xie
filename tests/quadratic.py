import unittest

from xie.graphics.quadratic import solveMin
from xie.graphics.quadratic import solveMax

class QuadraticTestCase(unittest.TestCase):
	def setUp(self):
		self.testDataSet=[
			((13, 67, 99), 13, 99),
			((13, 99, 67), 13, 76),
			((67, 13, 99), 46, 99),
			((67, 99, 13), 13, 76),
			((99, 13, 67), 46, 99),
			((99, 67, 13), 13, 99),

			((67, 13, 0), 0, 67),
			((67, 0, 13), 10, 67),

			((67, 13, 13), 13, 67),
			((13, 67, 13), 13, 40),
			((67, 13, 67), 40, 67),

			((67, 67, 67), 67, 67),
			((13, 13, 13), 13, 13),

			((-68, 14, -42), -68, -19),
			((-82, -89, 73), -83, 73),
			((0, 0, 0), 0, 0),
			((11, 11, 11), 11, 11),
			((-11, -11, -11), -11, -11),
			((11, 0, 0), 0, 11),
			((0, 13, 13), 0, 13),
		]

	def tearDown(self):
		pass

	def test_solveMin(self):
		for testDataPair in self.testDataSet:
			testData=testDataPair[0]
			testResult=testDataPair[1]
			realResult=solveMin(*testData)
			self.assertEqual(realResult, testResult, "solveMin(*{0}) = {1}".format(testData, realResult))

	def test_solveMax(self):
		for testDataPair in self.testDataSet:
			testData=testDataPair[0]
			testResult=testDataPair[2]
			realResult=solveMax(*testData)
			self.assertEqual(realResult, testResult, "solveMax(*{0}) = {1}".format(testData, realResult))


