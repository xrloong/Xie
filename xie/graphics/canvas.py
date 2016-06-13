class CanvasController:
	def __init__(self, width=1000, height=1000):
		self.width=width
		self.height=height

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

class TkCanvasController(CanvasController):
	def __init__(self, tkcanvas, width, height):
		super().__init__(width, height)

		self.canvas=tkcanvas
		self.clear()
		self.point_list=[]
		self.lastp=None

		import tkinter
		self.drawoption={'smooth':True, 'width':20, 'capstyle':tkinter.ROUND,}

	def clear(self):
		self.canvas.delete("all")

	def moveTo(self, p):
		self.setLastPoint(p)

	def lineTo(self, p, drawoption=None):
		if drawoption==None:
			drawoption=self.drawoption
		self.canvas.create_line(self.lastp[0], self.lastp[1], p[0], p[1], drawoption)
		self.lastp=p

	def qCurveTo(self, cp, p):
		self.canvas.create_line(self.lastp[0], self.lastp[1], cp[0], cp[1], p[0], p[1], self.drawoption)
		self.setLastPoint(p)

	def setLastPoint(self, p):
		self.lastp=p

class TrueTypeGlyphCanvasController(CanvasController):
	def __init__(self, width, height):
		super().__init__(width, height)

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
		self.glyphPen.moveTo(self.converCoordinate(p))
		self.hasDraw=True

	def lineTo(self, p):
		self.glyphPen.lineTo(self.converCoordinate(p))

	def qCurveTo(self, cp, p):
		self.glyphPen.qCurveTo(self.converCoordinate(cp), self.converCoordinate(p))

	def converCoordinate(self, p):
		return (p[0], self.height-p[1])

class SvgCanvasController(CanvasController):
	def __init__(self, width, height):
		super().__init__(width, height)
		self.expression=""

	def clear(self):
		self.expression=""
		pass

	def moveTo(self, p):
		self.expression +="M %s %s"%(p[0], p[1])
		pass

	def lineTo(self, p, drawoption=None):
		self.expression +="L %s %s"%(p[0], p[1])
		pass

	def qCurveTo(self, cp, p):
		self.expression +="Q %s %s %s %s"%(cp[0], cp[1], p[0], p[1])

	def getExpression(self):
		return self.expression

