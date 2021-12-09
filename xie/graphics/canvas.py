import numpy

class CanvasController:
	def __init__(self, size=(1000, 1000)):
		self.size = size
		self.width = size[0]
		self.height = size[1]

		self.matrix = numpy.eye(3)
		self.matrixStack = []

	def getWidth(self):
		return self.width

	def getHeight(self):
		return self.height

	def clear(self):
		pass

	def moveTo(self, point):
		pass

	def lineTo(self, point):
		pass

	def qCurveTo(self, cp, p):
		pass

	def onPreDrawCharacter(self, character):
		pass

	def onPostDrawCharacter(self, character):
		pass

	def onPreDrawStroke(self, stroke):
		pass

	def onPostDrawStroke(self, stroke):
		pass

	def save(self):
		self.matrixStack.append(self.matrix)

	def restore(self):
		self.matrix = self.matrixStack.pop()

	def translate(self, x, y):
		matrix = numpy.array([
				[0, 0, x],
				[0, 0, y],
				[0, 0, 0],
			])
		self.matrix = self.matrix+matrix

	def scale(self, sx, sy):
		matrix = numpy.array([
				[sx, 0, 0],
				[0, sy, 0],
				[0, 0, 1],
			])
		self.matrix = matrix.dot(self.matrix)

	def convertPointByPane(self, p):
		pp = (p[0], p[1], 1)
		result = self.matrix.dot(pp)
		resultList = result.tolist()
		return (round(resultList[0]), round(resultList[1]))

class TkCanvasController(CanvasController):
	def __init__(self, parent, size):
		super().__init__(size)

		import tkinter
		self.canvas = tkinter.Canvas(parent, width=self.width, height=self.height)
		self.drawoption = {'smooth':True, 'width':20, 'capstyle':tkinter.ROUND,}

		self.clear()
		self.point_list=[]
		self.lastp=None

	def clear(self):
		self.canvas.delete("all")

	def moveTo(self, p):
		self.setLastPoint(p)

	def lineTo(self, p):
		self.canvas.create_line(self.lastp[0], self.lastp[1], p[0], p[1], self.drawoption)
		self.lastp=p

	def qCurveTo(self, cp, p):
		self.canvas.create_line(self.lastp[0], self.lastp[1], cp[0], cp[1], p[0], p[1], self.drawoption)
		self.setLastPoint(p)

	def setLastPoint(self, p):
		self.lastp=p

class WxCanvasController(CanvasController):
	def __init__(self, parent, size):
		super().__init__(size)

		import wx
		self.canvas = wx.lib.floatcanvas.FloatCanvas.FloatCanvas(parent,
				ProjectionFun = lambda x: (1, -1),
				size = size)

		self.clear()
		self.point_list = []
		self.lastp = None

		self.pathOptions = {"LineWidth": 20, "LineColor": "Black"}

	def clear(self):
		self.canvas.ClearAll()
		self.canvas.ZoomToBB()

	def moveTo(self, p):
		self.setLastPoint(p)

	def lineTo(self, p):
		points = (self.lastp, p)
		self.canvas.AddLine(points, **self.pathOptions)
		self.canvas.ZoomToBB()

		self.setLastPoint(p)

	def qCurveTo(self, cp, p):
		points = (self.lastp, cp, p)
		self.canvas.AddSpline(points, **self.pathOptions)
		self.canvas.ZoomToBB()

		self.setLastPoint(p)

	def setLastPoint(self, p):
		self.lastp=p


class TrueTypeGlyphCanvasController(CanvasController):
	def __init__(self, size):
		super().__init__(size)

	def changeGlyph(self, glyph):
		self.glyph=glyph
		self.glyphPen=glyph.glyphPen()
		self.clear()

	def clear(self):
		self.hasDraw=False
		self.glyph.clear()

	def moveTo(self, p):
		if self.hasDraw:
			self.glyphPen.endPath()
		self.glyphPen.moveTo(self.convertCoordinate(p))
		self.hasDraw=True

	def lineTo(self, p):
		self.glyphPen.lineTo(self.convertCoordinate(p))

	def qCurveTo(self, cp, p):
		self.glyphPen.qCurveTo(self.convertCoordinate(cp), self.convertCoordinate(p))

	def convertCoordinate(self, p):
		return (p[0], self.height-p[1])

class SvgCanvasController(CanvasController):
	def __init__(self, size):
		super().__init__(size)
		self.expression=""

	def clear(self):
		self.expression=""

	def moveTo(self, p):
		self.expression +="M %s %s"%(p[0], p[1])

	def lineTo(self, p):
		self.expression +="L %s %s"%(p[0], p[1])

	def qCurveTo(self, cp, p):
		self.expression +="Q %s %s %s %s"%(cp[0], cp[1], p[0], p[1])

	def getExpression(self):
		return self.expression

class HexTextCanvasController(CanvasController):
	def __init__(self, size=(256, 256)):
		super().__init__(size)
		self.clear()
		from .utils import TextCodec
		self.textCodec=TextCodec()

	def clearStrokeExpression(self):
		self.pointExpressionList=[]

	def getStrokeExpression(self):
		return self.encodeStrokeExpression(self.pointExpressionList)

	def encodeStartPoint(self, p):
		ip=(round(p[0]), round(p[1]))
		return self.textCodec.encodeStartPoint(ip)

	def encodeEndPoint(self, p):
		ip=(round(p[0]), round(p[1]))
		return self.textCodec.encodeEndPoint(ip)

	def encodeControlPoint(self, p):
		ip=(round(p[0]), round(p[1]))
		return self.textCodec.encodeControlPoint(ip)

	def encodeStrokeExpression(self, pointExpressionList):
		return self.textCodec.encodeStrokeExpression(pointExpressionList)

	def encodeCharacterExpression(self, strokeExpressionList):
		return self.textCodec.encodeCharacterExpression(strokeExpressionList)

	def clear(self):
		self.clearStrokeExpression()

	def moveTo(self, p):
		self.pointExpressionList=[self.encodeStartPoint(self.convertPointByPane(p))]

	def lineTo(self, p):
		self.pointExpressionList.append(self.encodeEndPoint(self.convertPointByPane(p)))

	def qCurveTo(self, cp, p):
		self.pointExpressionList.append(self.encodeControlPoint(self.convertPointByPane(cp)))
		self.pointExpressionList.append(self.encodeEndPoint(self.convertPointByPane(p)))


class BaseTextCanvasController(HexTextCanvasController):
	def __init__(self):
		super().__init__()

	def clear(self):
		super().clear()
		self.expressionList=[]

	def onPreDrawStroke(self, stroke):
		self.clearStrokeExpression()

	def onPostDrawStroke(self, stroke):
		e=self.getStrokeExpression()
		if e:
			self.expressionList.append(e)
			self.clearStrokeExpression()

	def getCharacterExpression(self):
		return self.encodeCharacterExpression(self.expressionList)

