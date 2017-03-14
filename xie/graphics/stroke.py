from .shape import Drawing
from .shape import Shape
from .shape import Pane

from .segment import SegmentFactory

segmentFactory=SegmentFactory()

class StrokePath(Shape):
	def __init__(self, segments):
		self.segments=segments

	def getSegments(self):
		return self.segments

	def draw(self, drawingSystem):
		segments=self.getSegments()

		for segment in segments:
			segment.draw(drawingSystem)

	def getPoints(self, startPoint):
		points = []
		currentPoint = startPoint
		for segment  in self.getSegments():
			points.extend(segment.getPoints(currentPoint))
			endPoint = segment.getEndPoint()
			currentPoint = (currentPoint[0] + endPoint[0], currentPoint[1] + endPoint[1])
		return points

class Character(Shape):
	def __init__(self, strokes=[], name=""):
		self.name = name
		self.strokes = strokes

	def setName(self, name):
		self.name = name

	def setStrokes(self, strokes):
		self.strokes = strokes

	def getStrokes(self):
		return self.strokes

	def draw(self, drawingSystem):
		strokes=self.getStrokes()
		for stroke in strokes:
			stroke.draw(drawingSystem)

class StrokeInfo:
	def __init__(self, name, strokePath):
		self.name=name
		self.strokePath=strokePath

	def getName(self):
		return self.name

	def getStrokePath(self):
		return self.strokePath

class StrokeInfoGenerator:
	def generate(self, name, parameterList):
		strokePath = self.computeStrokePath(parameterList)
		strokeInfo = StrokeInfo(name, strokePath)
		return strokeInfo

	def parseExpression(self, parameterExpressionList):
		return []

	def computeStrokeSegments(self, paramList):
		return []

	def computeStrokePath(self, parameterList):
		strokeSegments=self.computeStrokeSegments(parameterList)
		return StrokePath(strokeSegments)

	@staticmethod
	def computeExtreme(points, extreme, solveExtreme, retrieveValue):
		firstPointPair = points[0]
		prevPoint = firstPointPair[1]
		midPoint = None

		extremeValue = retrieveValue(prevPoint)
		for p in points[1:]:
			isCurve = p[0]
			currPoint = p[1]

			extremeValue = extreme(extremeValue, retrieveValue(currPoint))
			if isCurve:
				midPoint=currPoint
			else:
				if midPoint:
					s0, s1, s2 = retrieveValue(prevPoint), retrieveValue(midPoint), retrieveValue(currPoint)
					tmpExtremeValue = solveExtreme(s0, s1, s2)
					extremeValue = extreme(extremeValue, tmpExtremeValue)

				prevPoint=currPoint
				midPoint=None

		return extremeValue


class StrokeInfoGenerator_點(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==2
		assert int(l[1])>0
		return [int(l[0]), int(l[1])]

	def computeStrokeSegments(self, paramList):
		w=paramList[0]
		h=paramList[1]

		return segmentFactory.generateSegments_點(w, h)

class StrokeInfoGenerator_圈(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==2
		assert int(l[0])>0
		assert int(l[1])>0
		return [int(l[0]), int(l[1])]

	def computeStrokeSegments(self, paramList):
		w=paramList[0]
		h=paramList[1]

		return segmentFactory.generateSegments_圈(w, h)

class StrokeInfoGenerator_橫(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==1
		assert int(l[0])>0
		return [int(l[0])]

	def computeStrokeSegments(self, paramList):
		w1=paramList[0]

		return segmentFactory.generateSegments_橫(w1)

class StrokeInfoGenerator_橫鉤(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==3
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		return [int(l[0]), int(l[1]), int(l[2]), ]

	def computeStrokeSegments(self, paramList):
		w1=paramList[0]
		w2=paramList[1]
		h2=paramList[2]

		segments=[]
		segments.extend(segmentFactory.generateSegments_橫(w1))
		segments.extend(segmentFactory.generateSegments_撇(w2, h2))
		return segments

class StrokeInfoGenerator_橫折(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==2
		assert int(l[0])>0
		assert int(l[1])>0
		return [int(l[0]), int(l[1]), ]

	def computeStrokeSegments(self, paramList):
		w1=paramList[0]
		h2=paramList[1]

		segments=[]
		segments.extend(segmentFactory.generateSegments_橫(w1))
		segments.extend(segmentFactory.generateSegments_豎(h2))
		return segments

class StrokeInfoGenerator_橫折折(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==3
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		return [int(l[0]), int(l[1]), int(l[2]), ]

	def computeStrokeSegments(self, paramList):
		w1=paramList[0]
		h2=paramList[1]
		w3=paramList[2]

		segments=[]
		segments.extend(segmentFactory.generateSegments_橫(w1))
		segments.extend(segmentFactory.generateSegments_豎(h2))
		segments.extend(segmentFactory.generateSegments_橫(w3))
		return segments

class StrokeInfoGenerator_橫折提(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==4
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		assert int(l[3])>0
		return [int(l[0]), int(l[1]), int(l[2]), int(l[3]), ]

	def computeStrokeSegments(self, paramList):
		w1=paramList[0]
		h2=paramList[1]
		w3=paramList[2]
		h3=paramList[3]

		segments=[]
		segments.extend(segmentFactory.generateSegments_橫(w1))
		segments.extend(segmentFactory.generateSegments_豎(h2))
		segments.extend(segmentFactory.generateSegments_提(w3, h3))
		return segments

class StrokeInfoGenerator_橫折折撇(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==4
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		assert int(l[3])>0
		assert int(l[4])>0
		assert int(l[5])>0
		return [int(l[0]), int(l[1]), int(l[2]), int(l[3]), int(l[4]), int(l[5]), ]

	def computeStrokeSegments(self, paramList):
		w1=paramList[0]
		w2=paramList[1]
		h2=paramList[2]
		w3=paramList[3]
		w4=paramList[4]
		h4=paramList[5]

		segments=[]
		segments.extend(segmentFactory.generateSegments_橫(w1))
		segments.extend(segmentFactory.generateSegments_撇(w2, h2))
		segments.extend(segmentFactory.generateSegments_橫(w3))
		segments.extend(segmentFactory.generateSegments_撇(w4, h4))
		return segments

class StrokeInfoGenerator_橫撇彎鉤(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==4
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		assert int(l[3])>0
		assert int(l[4])>0
		assert int(l[5])>0
		assert int(l[6])>0
		return [int(l[0]), int(l[1]), int(l[2]), int(l[3]), int(l[4]), int(l[5]), int(l[6]), ]

	def computeStrokeSegments(self, paramList):
		w1=paramList[0]
		w2=paramList[1]
		h2=paramList[2]
		w3=paramList[3]
		h3=paramList[4]
		w4=paramList[5]
		h4=paramList[6]

		segments=[]
		segments.extend(segmentFactory.generateSegments_橫(w1))
		segments.extend(segmentFactory.generateSegments_撇(w2, h2))
		segments.extend(segmentFactory.generateSegments_彎鉤之彎(w3, h3))
		segments.extend(segmentFactory.generateSegments_鉤(w4, h4))
		return segments

class StrokeInfoGenerator_橫折鉤(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==5
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		assert int(l[3])>0
		assert int(l[4])>0
		return [int(l[0]), int(l[1]), int(l[2]), int(l[3]), int(l[4]), ]

	def computeStrokeSegments(self, paramList):
		w1=paramList[0]
		w2=paramList[1]
		h2=paramList[2]
		w3=paramList[3]
		h3=paramList[4]

		segments=[]
		segments.extend(segmentFactory.generateSegments_橫(w1))
		segments.extend(segmentFactory.generateSegments_撇鉤之撇(w2, h2))
		segments.extend(segmentFactory.generateSegments_鉤(w3, h3))
		return segments

class StrokeInfoGenerator_橫折彎(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==4
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		assert int(l[3])>0
		return [int(l[0]), int(l[1]), int(l[2]), int(l[3]), ]

	def computeStrokeSegments(self, paramList):
		w1=paramList[0]
		h2=paramList[1]
		w2=paramList[2]
		cr=paramList[3]

		segments=[]
		segments.extend(segmentFactory.generateSegments_橫(w1))
		segments.extend(segmentFactory.generateSegments_豎(h2 - cr))
		segments.extend(segmentFactory.generateSegments_曲(cr))
		segments.extend(segmentFactory.generateSegments_橫(w2 - cr))
		return segments

class StrokeInfoGenerator_橫撇(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==3
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		return [int(l[0]), int(l[1]), int(l[2]), ]

	def computeStrokeSegments(self, paramList):
		w1=paramList[0]
		w2=paramList[1]
		h2=paramList[2]

		segments=[]
		segments.extend(segmentFactory.generateSegments_橫(w1))
		segments.extend(segmentFactory.generateSegments_撇(w2, h2))
		return segments

class StrokeInfoGenerator_橫斜彎鉤(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==6
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		assert int(l[3])>0
		assert int(l[4])>0
		assert int(l[5])>0
		return [int(l[0]), int(l[1]), int(l[2]), int(l[3]), int(l[4]), int(l[5]), ]

	def computeStrokeSegments(self, paramList):
		w1=paramList[0]
		h2=paramList[1]
		w2l=paramList[2]
		w2r=paramList[3]
		cr=paramList[4]
		h3=paramList[5]

		segments=[]
		segments.extend(segmentFactory.generateSegments_橫(w1))
		segments.extend(segmentFactory.generateSegments_撇曲(w2l, w2r, h2, cr))
		segments.extend(segmentFactory.generateSegments_上(h3))
		return segments

class StrokeInfoGenerator_橫折折折鉤(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==8
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		assert int(l[3])>0
		assert int(l[4])>0
		assert int(l[5])>0
		assert int(l[6])>0
		assert int(l[7])>0
		return [int(l[0]), int(l[1]), int(l[2]), int(l[3]), int(l[4]), int(l[5]), int(l[6]), int(l[7]), ]

	def computeStrokeSegments(self, paramList):
		w1=paramList[0]
		w2=paramList[1]
		h2=paramList[2]
		w3=paramList[3]
		w4=paramList[4]
		h4=paramList[5]
		w5=paramList[6]
		h5=paramList[7]

		segments=[]
		segments.extend(segmentFactory.generateSegments_橫(w1))
		segments.extend(segmentFactory.generateSegments_撇(w2, h2))
		segments.extend(segmentFactory.generateSegments_橫(w3))
		segments.extend(segmentFactory.generateSegments_撇鉤之撇(w4, h4))
		segments.extend(segmentFactory.generateSegments_鉤(w5, h5))
		return segments

class StrokeInfoGenerator_橫斜鉤(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==4
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		assert int(l[3])>0
		return [int(l[0]), int(l[1]), int(l[2]), int(l[3]), ]

	def computeStrokeSegments(self, paramList):
		w1=paramList[0]
		w2=paramList[1]
		h2=paramList[2]
		h3=paramList[3]

		segments=[]
		segments.extend(segmentFactory.generateSegments_橫(w1))
		segments.extend(segmentFactory.generateSegments_斜鉤之斜(w2, h2))
		segments.extend(segmentFactory.generateSegments_上(h3))
		return segments

class StrokeInfoGenerator_橫折折折(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		assert int(l[3])>0
		assert len(l)==4
		return [int(l[0]), int(l[1]), int(l[2]), int(l[3]), ]

	def computeStrokeSegments(self, paramList):
		w1=paramList[0]
		h2=paramList[1]
		w3=paramList[2]
		h4=paramList[3]

		segments=[]
		segments.extend(segmentFactory.generateSegments_橫(w1))
		segments.extend(segmentFactory.generateSegments_豎(h2))
		segments.extend(segmentFactory.generateSegments_橫(w3))
		segments.extend(segmentFactory.generateSegments_豎(h4))
		return segments

class StrokeInfoGenerator_豎(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==1
		assert int(l[0])>0
		return [int(l[0]), ]

	def computeStrokeSegments(self, paramList):
		h1=paramList[0]

		return segmentFactory.generateSegments_豎(h1)

class StrokeInfoGenerator_豎折(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==2
		assert int(l[0])>0
		assert int(l[1])>0
		return [int(l[0]), int(l[1]), ]

	def computeStrokeSegments(self, paramList):
		h1=paramList[0]
		w2=paramList[1]

		segments=[]
		segments.extend(segmentFactory.generateSegments_豎(h1))
		segments.extend(segmentFactory.generateSegments_橫(w2))
		return segments

class StrokeInfoGenerator_豎彎左(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==2
		assert int(l[0])>0
		assert int(l[1])>0
		return [int(l[0]), int(l[1]), ]

	def computeStrokeSegments(self, paramList):
		h1=paramList[0]
		w2=paramList[1]

		segments=[]
		segments.extend(segmentFactory.generateSegments_豎(h1))
		segments.extend(segmentFactory.generateSegments_左(w2))
		return segments

class StrokeInfoGenerator_豎提(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==3
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		return [int(l[0]), int(l[1]), int(l[2]), ]

	def computeStrokeSegments(self, paramList):
		h1=paramList[0]
		w2=paramList[1]
		h2=paramList[2]

		segments=[]
		segments.extend(segmentFactory.generateSegments_豎(h1))
		segments.extend(segmentFactory.generateSegments_提(w2, h2))
		return segments

class StrokeInfoGenerator_豎折折(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==3
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		return [int(l[0]), int(l[1]), int(l[2]), ]

	def computeStrokeSegments(self, paramList):
		h1=paramList[0]
		w2=paramList[1]
		h3=paramList[2]

		segments=[]
		segments.extend(segmentFactory.generateSegments_豎(h1))
		segments.extend(segmentFactory.generateSegments_橫(w2))
		segments.extend(segmentFactory.generateSegments_豎(h3))
		return segments

class StrokeInfoGenerator_豎折彎鉤(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==7
		assert int(l[0])>=0
		assert int(l[1])>0
		assert int(l[2])>0
		assert int(l[3])>0
		assert int(l[4])>0
		assert int(l[5])>0
		assert int(l[6])>0
		return [int(l[0]), int(l[1]), int(l[2]), int(l[3]), int(l[4]), int(l[5]), int(l[6]), ]

	def computeStrokeSegments(self, paramList):
		w1=paramList[0]
		h1=paramList[1]
		w2=paramList[2]
		w3=paramList[3]
		h3=paramList[4]
		w4=paramList[5]
		h4=paramList[6]

		segments=[]
		if w1>0:
			segments.extend(segmentFactory.generateSegments_撇(w1, h1))
		elif w1<0:
			assert False
		else:
			segments.extend(segmentFactory.generateSegments_豎(h1))
		segments.extend(segmentFactory.generateSegments_橫(w2))
		segments.extend(segmentFactory.generateSegments_撇鉤之撇(w3, h3))
		segments.extend(segmentFactory.generateSegments_鉤(w4, h4))
		return segments

class StrokeInfoGenerator_豎彎鉤(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==4
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		assert int(l[3])>0
		return [int(l[0]), int(l[1]), int(l[2]), int(l[3]), ]

	def computeStrokeSegments(self, paramList):
		h1=paramList[0]
		w1=paramList[1]
		cr=paramList[2]
		h2=paramList[3]

		segments=[]
		segments.extend(segmentFactory.generateSegments_豎(h1-cr))
		segments.extend(segmentFactory.generateSegments_曲(cr))
		segments.extend(segmentFactory.generateSegments_橫(w1-cr))
		segments.extend(segmentFactory.generateSegments_上(h2))
		return segments

class StrokeInfoGenerator_豎彎(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==3
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		return [int(l[0]), int(l[1]), int(l[2]), ]

	def computeStrokeSegments(self, paramList):
		w1=paramList[0]
		h1=paramList[1]
		cr=paramList[2]

		segments=[]
		segments.extend(segmentFactory.generateSegments_豎(h1))
		segments.extend(segmentFactory.generateSegments_曲(cr))
		segments.extend(segmentFactory.generateSegments_橫(w1))
		return segments

class StrokeInfoGenerator_豎鉤(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==3
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		return [int(l[0]), int(l[1]), int(l[2]), ]

	def computeStrokeSegments(self, paramList):
		h1=paramList[0]
		w2=paramList[1]
		h2=paramList[2]

		hs = h1 - h2*3
		hp = h2*3
		wp = w2//4

		wg=w2//2
		hg=wg

		segments=[]
		segments.extend(segmentFactory.generateSegments_豎撇(wp, hs, hp))
		segments.extend(segmentFactory.generateSegments_鉤(wg, hg))
		return segments

class StrokeInfoGenerator_斜鉤(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==3
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		return [int(l[0]), int(l[1]), int(l[2]), ]

	def computeStrokeSegments(self, paramList):
		w1=paramList[0]
		h1=paramList[1]
		h2=paramList[2]

		segments=[]
		segments.extend(segmentFactory.generateSegments_斜鉤之斜(w1, h1))
		segments.extend(segmentFactory.generateSegments_上(h2))
		return segments

class StrokeInfoGenerator_彎鉤(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==4
#		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		assert int(l[3])>0
		return [int(l[0]), int(l[1]), int(l[2]), int(l[3]), ]

	def computeStrokeSegments(self, paramList):
		w1=paramList[0]
		h1=paramList[1]
		w2=paramList[2]
		h2=paramList[3]

		segments=[]
		segments.extend(segmentFactory.generateSegments_彎鉤之彎(w1, h1))
		segments.extend(segmentFactory.generateSegments_鉤(w2, h2))
		return segments

class StrokeInfoGenerator_撇鉤(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==4
#		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		assert int(l[3])>0
		return [int(l[0]), int(l[1]), int(l[2]), int(l[3]), ]

	def computeStrokeSegments(self, paramList):
		w1=paramList[0]
		h1=paramList[1]
		w2=paramList[2]
		h2=paramList[3]

		segments=[]
		segments.extend(segmentFactory.generateSegments_彎鉤之彎(w1, h1))
		segments.extend(segmentFactory.generateSegments_鉤(w2, h2))
		return segments

class StrokeInfoGenerator_撇(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==2
		assert int(l[0])>0
		assert int(l[1])>0
		return [int(l[0]), int(l[1]), ]

	def computeStrokeSegments(self, paramList):
		w1=paramList[0]
		h1=paramList[1]

		segments=[]
		segments.extend(segmentFactory.generateSegments_撇(w1, h1))
		return segments

class StrokeInfoGenerator_撇點(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==4
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		assert int(l[3])>0
		return [int(l[0]), int(l[1]), int(l[2]), int(l[3]), ]

	def computeStrokeSegments(self, paramList):
		w1=paramList[0]
		h1=paramList[1]
		w2=paramList[2]
		h2=paramList[3]

		segments=[]
		segments.extend(segmentFactory.generateSegments_撇(w1, h1))
		segments.extend(segmentFactory.generateSegments_點(w2, h2))
		return segments

class StrokeInfoGenerator_撇橫(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==4
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
#		assert int(l[3])>0
		return [int(l[0]), int(l[1]), int(l[2]), int(l[3]), ]

	def computeStrokeSegments(self, paramList):
		w1=paramList[0]
		h1=paramList[1]
		w2=paramList[2]
		h2=paramList[3]

		segments=[]
		segments.extend(segmentFactory.generateSegments_撇(w1, h1))
		if h2>0:
			segments.extend(segmentFactory.generateSegments_點(w2, h2))
		elif h2<0:
			segments.extend(segmentFactory.generateSegments_提(w2, -h2))
		else:
			segments.extend(segmentFactory.generateSegments_橫(w2))
		return segments

class StrokeInfoGenerator_撇橫撇(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==5
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		assert int(l[3])>0
		assert int(l[4])>0
		return [int(l[0]), int(l[1]), int(l[2]), int(l[3]), int(l[4]), ]

	def computeStrokeSegments(self, paramList):
		w1=paramList[0]
		h1=paramList[1]
		w2=paramList[2]
		w3=paramList[3]
		h3=paramList[4]

		segments=[]
		segments.extend(segmentFactory.generateSegments_撇(w1, h1))
		segments.extend(segmentFactory.generateSegments_橫(w2))
		segments.extend(segmentFactory.generateSegments_撇(w3, h3))
		return segments

class StrokeInfoGenerator_豎撇(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==2
		assert int(l[0])>0
		assert int(l[1])>0
		return [int(l[0]), int(l[1]), ]

	def computeStrokeSegments(self, paramList):
		w1=paramList[0]
		h1=paramList[1]

		hs = h1 - h1//2
		hp = h1 - (hs)
		wp = w1

		segments=[]
		segments.extend(segmentFactory.generateSegments_豎撇(w1, hs, hp))
		return segments

class StrokeInfoGenerator_提(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==2
		assert int(l[0])>0
		assert int(l[1])>0
		return [int(l[0]), int(l[1]), ]

	def computeStrokeSegments(self, paramList):
		w1=paramList[0]
		h1=paramList[1]

		return segmentFactory.generateSegments_提(w1, h1)

class StrokeInfoGenerator_捺(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==2
		assert int(l[0])>0
		assert int(l[1])>0
		return [int(l[0]), int(l[1]), ]

	def computeStrokeSegments(self, paramList):
		w1=paramList[0]
		h1=paramList[1]

		return segmentFactory.generateSegments_捺(w1, h1)

class StrokeInfoGenerator_臥捺(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==2
		assert int(l[0])>0
		assert int(l[1])>0
		return [int(l[0]), int(l[1]), ]

	def computeStrokeSegments(self, paramList):
		w1=paramList[0]
		h1=paramList[1]

		return segmentFactory.generateSegments_臥捺(w1, h1)

class StrokeInfoGenerator_提捺(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==4
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		assert int(l[3])>0
		return [int(l[0]), int(l[1]), int(l[2]), int(l[3]), ]

	def computeStrokeSegments(self, paramList):
		w1=paramList[0]
		h1=paramList[1]
		w2=paramList[2]
		h2=paramList[3]

		segments=[]
		segments.extend(segmentFactory.generateSegments_提(w1, h1))
		segments.extend(segmentFactory.generateSegments_捺(w2, h2))
		return segments

class StrokeInfoGenerator_橫捺(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==3
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		return [int(l[0]), int(l[1]), int(l[2]), ]

	def computeStrokeSegments(self, paramList):
		w1=paramList[0]
		w2=paramList[1]
		h2=paramList[2]

		segments=[]
		segments.extend(segmentFactory.generateSegments_橫(w1))
		segments.extend(segmentFactory.generateSegments_捺(w2, h2))
		return segments

class StrokeInfoFactory:
	def __init__(self):
		self.strokeInfoMap = {
			"點": StrokeInfoGenerator_點(),
#			"長頓點": StrokeInfoGenerator_點(),
			"圈": StrokeInfoGenerator_圈(),
			"橫": StrokeInfoGenerator_橫(),
			"橫鉤": StrokeInfoGenerator_橫鉤(),
			"橫折": StrokeInfoGenerator_橫折(),
			"橫折折": StrokeInfoGenerator_橫折折(),
			"橫折提": StrokeInfoGenerator_橫折提(),
			"橫折折撇": StrokeInfoGenerator_橫折折撇(),
			"橫撇彎鉤": StrokeInfoGenerator_橫撇彎鉤(),
			"橫折鉤": StrokeInfoGenerator_橫折鉤(),
			"橫折彎": StrokeInfoGenerator_橫折彎(),
			"橫撇": StrokeInfoGenerator_橫撇(),
			"橫斜彎鉤": StrokeInfoGenerator_橫斜彎鉤(),
			"橫折折折鉤": StrokeInfoGenerator_橫折折折鉤(),
			"橫斜鉤": StrokeInfoGenerator_橫斜鉤(),
			"橫折折折": StrokeInfoGenerator_橫折折折(),
			"豎": StrokeInfoGenerator_豎(),
			"豎折": StrokeInfoGenerator_豎折(),
			"豎彎左": StrokeInfoGenerator_豎彎左(),
			"豎提": StrokeInfoGenerator_豎提(),
			"豎折折": StrokeInfoGenerator_豎折折(),
			"豎折彎鉤": StrokeInfoGenerator_豎折彎鉤(),
			"豎彎鉤": StrokeInfoGenerator_豎彎鉤(),
			"豎彎": StrokeInfoGenerator_豎彎(),
			"豎鉤": StrokeInfoGenerator_豎鉤(),
			"扁斜鉤": StrokeInfoGenerator_豎彎鉤(),
			"斜鉤": StrokeInfoGenerator_斜鉤(),
			"彎鉤": StrokeInfoGenerator_彎鉤(),
			"撇鉤": StrokeInfoGenerator_撇鉤(),

			"撇": StrokeInfoGenerator_撇(),
			"撇點": StrokeInfoGenerator_撇點(),
			"撇橫": StrokeInfoGenerator_撇橫(),
			"撇提": StrokeInfoGenerator_撇橫(),
			"撇折": StrokeInfoGenerator_撇橫(),
			"撇橫撇": StrokeInfoGenerator_撇橫撇(),
			"豎撇": StrokeInfoGenerator_豎撇(),
			"提": StrokeInfoGenerator_提(),
			"捺": StrokeInfoGenerator_捺(),
			"臥捺": StrokeInfoGenerator_臥捺(),
			"提捺": StrokeInfoGenerator_提捺(),
			"橫捺": StrokeInfoGenerator_橫捺(),
		}


	def generateStrokeInfo(self, name, parameterList):
		strokeInfoGenerator = self.strokeInfoMap.get(name, None)
		assert strokeInfoGenerator!=None

		parameterList = strokeInfoGenerator.parseExpression(parameterList)
		strokeInfo = strokeInfoGenerator.generate(name, parameterList)
		return strokeInfo

strokeInfoFactory=StrokeInfoFactory()

class Stroke(Drawing, Shape):
	def __init__(self, startPoint, strokeInfo=None, strokePath=None, infoPane=Pane.BBOX, statePane=Pane.BBOX):
		super().__init__(infoPane, statePane)
		self.startPoint=startPoint

		if strokeInfo:
			self.strokeInfo=strokeInfo
			self.strokePath=strokeInfo.getStrokePath()
			self.name=strokeInfo.getName()
		else:
			self.strokeInfo=None
			self.strokePath=strokePath
			self.name=""

	def clone(self):
		stroke=Stroke(self.startPoint, strokeInfo=self.strokeInfo, strokePath=self.strokePath,
			infoPane=self.getInfoPane(), statePane=self.getStatePane())
		return stroke

	def getName(self):
		return self.name

	def getExpression(self):
		def encodeStroke(stroke):
			points=stroke.getPoints()
			point = points[0]
			isCurve = point[0]
			assert isCurve is False
			pointExpressionList = ["0000{0[0]:02X}{0[1]:02X}".format(point[1]), ]

			for point in points[1:]:
				isCurve = point[0]
				if isCurve:
					pointExpressionList.append("0002{0[0]:02X}{0[1]:02X}".format(point[1]))
				else:
					pointExpressionList.append("0001{0[0]:02X}{0[1]:02X}".format(point[1]))
			return ",".join(pointExpressionList)
		return encodeStroke(self)


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

	def getPoints(self):
		startPoint=self.getStartPoint()
		strokePath=self.getStrokePath()

		points = [(False, startPoint)]
		points.extend(strokePath.getPoints(startPoint))

		pane=self.getStatePane()
		bBoxPane=self.getInfoPane()
		newPoints = [(isCurve, bBoxPane.transformRelativePointByTargetPane(point, pane)) for (isCurve, point) in points]
		return newPoints


def generateStroke(name, startPoint, parameterList, bBox):
	strokeInfo = strokeInfoFactory.generateStrokeInfo(name, parameterList)

	pane = Pane(*bBox)
	infoPane = pane
	statePane = pane
	return Stroke(startPoint, strokeInfo=strokeInfo, infoPane=infoPane, statePane=statePane)

class StrokeGroupInfo:
	def __init__(self, strokeList, bBoxPane):
		self.strokeList=strokeList
		self.bBoxPane=bBoxPane

	def getStrokeList(self):
		return self.strokeList

	def getBBoxPane(self):
		return self.bBoxPane

class StrokeGroup(Drawing):
	def __init__(self, strokeGroupInfo):
		pane=strokeGroupInfo.getBBoxPane()
		super().__init__(pane, pane)
		self.strokeGroupInfo=strokeGroupInfo

	def clone(self):
		strokeList=[s.clone() for s in self.getStrokeList()]
		strokeGroupInfo=StrokeGroupInfo(strokeList, self.getInfoPane())
		strokeGroup=StrokeGroup(strokeGroupInfo)
		strokeGroup.setStatePane(self.getStatePane())
		return strokeGroup

	def getDrawingList(self):
		return self.getStrokeList()

	def getStrokeList(self):
		return self.strokeGroupInfo.getStrokeList()

	def getCount(self):
		return len(self.getStrokeList())

	@staticmethod
	def generateStrokeGroup(sg, pane):
		strokeGroup=sg.clone()

		newSgTargetPane=pane
		sgTargetPane=strokeGroup.getStatePane()
		sgInfoPane=strokeGroup.getInfoPane()
		for drawing in strokeGroup.getDrawingList():
			sTargetPane=drawing.getStatePane()
			sInfoPane=drawing.getInfoPane()
			drawing.transformBy(sgInfoPane, newSgTargetPane)

		strokeGroup.setStatePane(newSgTargetPane)
		strokeGroup.setInfoPane(newSgTargetPane)

		return strokeGroup

	@staticmethod
	def generateStrokeGroupInfo(strokeGroupPanePair):
		def computeBBox(paneList):
			left=min(map(lambda pane: pane.getLeft(), paneList))
			top=min(map(lambda pane: pane.getTop(), paneList))
			right=max(map(lambda pane: pane.getRight(), paneList))
			bottom=max(map(lambda pane: pane.getBottom(), paneList))
			return Pane(left, top, right, bottom)

		resultStrokeList=[]
		paneList=[]
		for strokeGroup, pane in strokeGroupPanePair:
			strokeGroup=StrokeGroup.generateStrokeGroup(strokeGroup, pane)
			resultStrokeList.extend(strokeGroup.getStrokeList())
			paneList.append(strokeGroup.getInfoPane())

		pane=computeBBox(paneList)
		strokeGroupInfo=StrokeGroupInfo(resultStrokeList, pane)

		return strokeGroupInfo

