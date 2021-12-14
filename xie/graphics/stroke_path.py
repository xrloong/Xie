from .shape import Shape
from .shape import mergeBoundary
from .shape import offsetBoundary

class StrokePath(Shape):
	def __init__(self, segments):
		self.segments=segments

	def __eq__(self, other):
		return (isinstance(other, self.__class__)
			and self.getSegments() == other.getSegments())

	def __str__(self):
		return "-".join(map(lambda s: str(s), self.getSegments()))

	def __repr__(self):
		return "StrokePath({0})".format(",".join(map(lambda s: str(s), self.getSegments())))

	def getSegments(self):
		return self.segments

	def draw(self, drawingSystem):
		segments=self.getSegments()

		for segment in segments:
			segment.draw(drawingSystem)

	def computeBoundary(self):
		segments=self.getSegments()

		currentPoint=(0, 0)
		totalBoundary=(0, 0, 0, 0)
		for segment in segments:
			boundary=segment.computeBoundary()
			newBoundary=offsetBoundary(boundary, currentPoint)
			totalBoundary=mergeBoundary(totalBoundary, newBoundary)

			endPoint=segment.getEndPoint()
			currentPoint=(currentPoint[0]+endPoint[0], currentPoint[1]+endPoint[1], )

		return totalBoundary

	def computeBoundaryWithStartPoint(self, startPoint):
		strokePathBoundary = self.computeBoundary()
		return offsetBoundary(strokePathBoundary, startPoint)

