import unittest
from xie.graphics.utils import TextCodec

class TextUtilsTestCase(unittest.TestCase):
	def setUp(self):
		self.codec = TextCodec()

	def tearDown(self):
		pass

	def test_encodeStartPoint(self):
		self.assertEqual("0.37.59", self.codec.encodeStartPoint((37, 59)))
		self.assertEqual("0.59.37", self.codec.encodeStartPoint((59, 37)))

		self.assertEqual("0.0.0", self.codec.encodeStartPoint((0, 0)))
		self.assertEqual("0.255.0", self.codec.encodeStartPoint((255, 0)))
		self.assertEqual("0.255.255", self.codec.encodeStartPoint((255, 255)))
		self.assertEqual("0.0.255", self.codec.encodeStartPoint((0, 255)))

		# outside
		self.assertEqual("0.1234.5678", self.codec.encodeStartPoint((1234, 5678)))
		self.assertEqual("0.5678.1234", self.codec.encodeStartPoint((5678, 1234)))

	def test_encodeEndPoint(self):
		self.assertEqual("1.37.59", self.codec.encodeEndPoint((37, 59)))
		self.assertEqual("1.59.37", self.codec.encodeEndPoint((59, 37)))

		self.assertEqual("1.0.0", self.codec.encodeEndPoint((0, 0)))
		self.assertEqual("1.255.0", self.codec.encodeEndPoint((255, 0)))
		self.assertEqual("1.255.255", self.codec.encodeEndPoint((255, 255)))
		self.assertEqual("1.0.255", self.codec.encodeEndPoint((0, 255)))

		# outside
		self.assertEqual("1.1234.5678", self.codec.encodeEndPoint((1234, 5678)))
		self.assertEqual("1.5678.1234", self.codec.encodeEndPoint((5678, 1234)))

	def test_encodeControlPoint(self):
		self.assertEqual("2.37.59", self.codec.encodeControlPoint((37, 59)))
		self.assertEqual("2.59.37", self.codec.encodeControlPoint((59, 37)))

		self.assertEqual("2.0.0", self.codec.encodeControlPoint((0, 0)))
		self.assertEqual("2.255.0", self.codec.encodeControlPoint((255, 0)))
		self.assertEqual("2.255.255", self.codec.encodeControlPoint((255, 255)))
		self.assertEqual("2.0.255", self.codec.encodeControlPoint((0, 255)))

		# outside
		self.assertEqual("2.1234.5678", self.codec.encodeControlPoint((1234, 5678)))
		self.assertEqual("2.5678.1234", self.codec.encodeControlPoint((5678, 1234)))

	def test_isStartPoint(self):
		self.assertTrue(self.codec.isStartPoint("0.37.59"))
		self.assertFalse(self.codec.isStartPoint("1.37.59"))
		self.assertFalse(self.codec.isStartPoint("2.37.59"))

	def test_isEndPoint(self):
		self.assertFalse(self.codec.isEndPoint("0.37.59"))
		self.assertTrue(self.codec.isEndPoint("1.37.59"))
		self.assertFalse(self.codec.isEndPoint("2.37.59"))

	def test_isControlPoint(self):
		self.assertFalse(self.codec.isControlPoint("0.37.59"))
		self.assertFalse(self.codec.isControlPoint("1.37.59"))
		self.assertTrue(self.codec.isControlPoint("2.37.59"))

	def test_decodePointExpression(self):
		self.assertEqual((37, 59), self.codec.decodePointExpression("0.37.59"))
		self.assertEqual((37, 59), self.codec.decodePointExpression("1.37.59"))
		self.assertEqual((37, 59), self.codec.decodePointExpression("2.37.59"))

		self.assertEqual((59, 37), self.codec.decodePointExpression("0.59.37"))
		self.assertEqual((59, 37), self.codec.decodePointExpression("1.59.37"))
		self.assertEqual((59, 37), self.codec.decodePointExpression("2.59.37"))

