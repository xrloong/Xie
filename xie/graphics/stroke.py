from .shape import Shape

class Segment(Shape):
	def __init__(self):
		pass

	def draw(self, drawingSystem):
		pass

class BeelineSegment(Segment):
	def __init__(self, point):
		super().__init__()
		self.point=point

	def draw(self, drawingSystem):
		drawingSystem.lineTo(self.point)

class QCurveSegment(Segment):
	def __init__(self, control_point, point):
		super().__init__()
		self.control_point=control_point
		self.point=point

	def draw(self, drawingSystem):
		drawingSystem.qCurveTo(self.control_point, self.point)

class StrokePath(Shape):
	def __init__(self, segments):
		self.segments=segments

	def getSegments(self):
		return self.segments

	def draw(self, drawingSystem):
		segments=self.getSegments()

		for segment in segments:
			segment.draw(drawingSystem)

class Stroke(Shape):
	def __init__(self, startPoint, strokePath):
		self.startPoint=startPoint
		self.strokePath=strokePath

	def getStartPoint(self):
		return self.startPoint

	def getStrokePath(self):
		return self.strokePath

	def draw(self, drawingSystem):
		startPoint = self.getStartPoint()
		drawingSystem.startDrawing(startPoint)

		strokePath = self.getStrokePath()
		strokePath.draw(drawingSystem)

		drawingSystem.endDrawing()

class Character(Shape):
	def __init__(self, name, strokes):
		self.name = name
		self.strokes = strokes

	def getStrokes(self):
		return self.strokes

	def draw(self, drawingSystem):
		strokes=self.getStrokes()
		for stroke in strokes:
			stroke.draw(drawingSystem)

