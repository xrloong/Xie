import unittest
from xie.graphics.canvas import CanvasController
from xie.graphics.canvas import EncodedTextCanvasController

class CanvasControllerTestCase(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_size(self):
		canvasController = CanvasController()
		self.assertEqual(1000, canvasController.getWidth())
		self.assertEqual(1000, canvasController.getHeight())

		canvasController = CanvasController((800, 640))
		self.assertEqual(800, canvasController.getWidth())
		self.assertEqual(640, canvasController.getHeight())

class EncodedTextCanvasControllerTestCase(unittest.TestCase):
	def setUp(self):
		self.canvasController = EncodedTextCanvasController()

	def tearDown(self):
		pass

	def test_size(self):
		self.assertEqual(256, self.canvasController.getWidth())
		self.assertEqual(256, self.canvasController.getHeight())

	def test_init_getStrokeExpression(self):
		self.assertEqual("", self.canvasController.getStrokeExpression())

	def test_moveTo(self):
		self.canvasController.moveTo((20, 123))
		self.assertEqual("0.20.123", self.canvasController.getStrokeExpression())

		self.canvasController.moveTo((77, 169))
		self.assertEqual("0.77.169", self.canvasController.getStrokeExpression())

	def test_lineTo(self):
		self.canvasController.moveTo((20, 123))
		self.canvasController.lineTo((77, 169))
		self.assertEqual("0.20.123,1.77.169", self.canvasController.getStrokeExpression())

		self.canvasController.lineTo((153, 81))
		self.assertEqual("0.20.123,1.77.169,1.153.81", self.canvasController.getStrokeExpression())

	def test_qCurveTo(self):
		self.canvasController.moveTo((20, 123))
		self.canvasController.qCurveTo((77, 169), (243, 98))
		self.assertEqual("0.20.123,2.77.169,1.243.98", self.canvasController.getStrokeExpression())

		self.canvasController.qCurveTo((154, 77), (169, 88))
		self.assertEqual("0.20.123,2.77.169,1.243.98,2.154.77,1.169.88", self.canvasController.getStrokeExpression())

	def test_draw_stroke_1(self):
        # 橫
		self.canvasController.moveTo((20, 123))
		self.canvasController.lineTo((222, 123))
		self.assertEqual("0.20.123,1.222.123", self.canvasController.getStrokeExpression())

	def test_draw_stroke_2(self):
        # 豎
		self.canvasController.moveTo((124, 27))
		self.canvasController.lineTo((124, 238))
		self.assertEqual("0.124.27,1.124.238", self.canvasController.getStrokeExpression())

	def test_draw_stroke_3(self):
        # 豎彎
		self.canvasController.moveTo([43, 54])
		self.canvasController.lineTo([43, 200])
		self.canvasController.qCurveTo([75, 232], (195, 232))
		self.assertEqual("0.43.54,1.43.200,2.75.232,1.195.232", self.canvasController.getStrokeExpression())
