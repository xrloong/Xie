import unittest
from xie.graphics.drawing import DrawingSystem
from xie.graphics.canvas import EncodedTextCanvasController

from xie.graphics.factory import ShapeFactory

class DrawingSystemTestCase(unittest.TestCase):
	def setUp(self):
		self.controller = EncodedTextCanvasController()
		self.ds = DrawingSystem(self.controller)
		self.shapeFactory = ShapeFactory()

	def tearDown(self):
		pass

	def test_draw_stroke_1(self):
		stroke = self.shapeFactory.generateStrokeByParameters("橫", [222], startPoint=(20, 123))
		self.ds.draw(stroke)
		self.assertEqual("0.20.123,1.242.123", self.controller.getStrokeExpression())

	def test_draw_stroke_2(self):
		stroke = self.shapeFactory.generateStrokeByParameters("豎", [211], startPoint=(124, 27))
		self.ds.draw(stroke)
		self.assertEqual("0.124.27,1.124.238", self.controller.getStrokeExpression())

	def test_draw_stroke_3(self):
		stroke = self.shapeFactory.generateStrokeByParameters("豎彎", [146, 126, 32], startPoint=(43, 54))
		self.ds.draw(stroke)
		self.assertEqual("0.43.54,1.43.180,2.43.212,1.75.212,1.221.212", self.controller.getStrokeExpression())


	def test_translate(self):
		stroke = self.shapeFactory.generateStrokeByParameters("橫", [222], startPoint=(20, 123))
		self.ds.translate(29, 105)
		self.ds.draw(stroke)
		self.assertEqual("0.49.228,1.271.228", self.controller.getStrokeExpression())

	def test_scale(self):
		stroke = self.shapeFactory.generateStrokeByParameters("橫", [222], startPoint=(20, 123))
		self.ds.scale(0.5, 1.2)
		self.ds.draw(stroke)
		self.assertEqual("0.10.148,1.121.148", self.controller.getStrokeExpression())

	def test_complex_transform(self):
		stroke = self.shapeFactory.generateStrokeByParameters("橫", [222], startPoint=(20, 123))
		self.ds.translate(-10, -110)
		self.ds.scale(0.5, 1.2)
		self.ds.translate(26, 80)
		self.ds.draw(stroke)
		self.assertEqual("0.31.96,1.142.96", self.controller.getStrokeExpression())

