from .shape import Drawing
from .shape import Shape
from .shape import Pane


class Segment(Shape):
	def __init__(self):
		pass

	def draw(self, drawingSystem):
		pass

class BaseBeelineSegment(Segment):
	def getEndPoint(self):
		return (0, 0)

	def draw(self, drawingSystem):
		drawingSystem.lineTo(self.getEndPoint())

	def getPoints(self, startPoint):
		endPoint = self.getEndPoint()
		return [(False, (startPoint[0] + endPoint[0], startPoint[1] + endPoint[1])), ]

class BaseQCurveSegment(Segment):
	def getControlPoint(self):
		return (0, 0)

	def getEndPoint(self):
		return (0, 0)

	def draw(self, drawingSystem):
		drawingSystem.qCurveTo(self.getControlPoint(), self.getEndPoint())

	def getPoints(self, startPoint):
		endPoint = self.getEndPoint()
		controlPoint = self.getControlPoint()
		return [(True, (startPoint[0] + controlPoint[0], startPoint[1] + controlPoint[1])),
			(False, (startPoint[0] + endPoint[0], startPoint[1] + endPoint[1])), ]

class BeelineSegment(BaseBeelineSegment):
	def __init__(self, point):
		super().__init__()
		self.point=point

	def getEndPoint(self):
		return self.point

class QCurveSegment(BaseQCurveSegment):
	def __init__(self, control_point, point):
		super().__init__()
		self.control_point=control_point
		self.point=point

	def getControlPoint(self):
		return self.control_point

	def getEndPoint(self):
		return self.point

class SegmentFactory:
	def __init__(self):
		pass

	# 單個 Segment
	def generateSegment_Horizontal(self, w):
		return BeelineSegment((w, 0))

	def generateSegment_Vertical(self, h):
		return BeelineSegment((0, h))

	def generateSegment_Beeline(self, endPoint):
		return BeelineSegment(endPoint)

	def generateSegment_QCurve(self, controlPoint, endPoint):
		return QCurveSegment(controlPoint, endPoint)

	def generateSegment_Slash(self, w, h):
		return self.generateSegment_Beeline((w, h))


	# 單個方向 Segment
	def generateSegment_右(self, w):
		assert w>0
		return self.generateSegment_Horizontal(w)

	def generateSegment_下(self, h):
		assert h>0
		return self.generateSegment_Vertical(h)

	def generateSegment_左(self, w):
		assert w>0
		return self.generateSegment_Horizontal(-w)

	def generateSegment_上(self, h):
		assert h>0
		return self.generateSegment_Vertical(-h)

	def generateSegment_左上(self, w, h):
		assert w>0 and h>0
		return self.generateSegment_Slash(-w, -h)

	def generateSegment_左下(self, w, h):
		assert w>0 and h>0
		return self.generateSegment_Slash(-w, h)

	def generateSegment_右上(self, w, h):
		assert w>0 and h>0
		return self.generateSegment_Slash(w, -h)

	def generateSegment_右下(self, w, h):
		assert w>0 and h>0
		return self.generateSegment_Slash(w, h)


	# 單個筆畫 Segment
	def generateSegment_橫(self, w):
		return self.generateSegment_右(w)

	def generateSegment_豎(self, h):
		return self.generateSegment_下(h)

	# 多個 Segment
	def generateSegments_點(self, w, h):
		return [self.generateSegment_Beeline((w, h))]

	def generateSegments_圈(self, a, b):
		assert a>0 and b>0
		segment1=QCurveSegment((a, 0), (a, b))
		segment2=QCurveSegment((0, b), (-a, b))
		segment3=QCurveSegment((-a, 0), (-a, -b))
		segment4=QCurveSegment((0, -b), (a, -b))
		return [segment1, segment2, segment3, segment4]

	def generateSegments_橫(self, w):
		assert w>0
		return [self.generateSegment_橫(w)]

	def generateSegments_豎(self, h):
		assert h>0
		return [self.generateSegment_豎(h)]

	def generateSegments_左(self, w):
		return [self.generateSegment_左(w), ]

	def generateSegments_上(self, h):
		return [self.generateSegment_上(h), ]

	def generateSegments_提(self, w, h):
		return [self.generateSegment_右上(w, h), ]

	def generateSegments_捺(self, w, h):
		assert w>0 and h>0
		scale = max(3, w/h*2, h/w*2)
		midPoint = (w//2 - h//scale, h//2 + w//scale)
		endPoint = (w, h)
		return [self.generateSegment_QCurve(midPoint, endPoint), ]

	def generateSegments_撇(self, w, h):
		return [self.generateSegment_左下(w, h), ]

	def generateSegments_鉤(self, w, h):
		return [self.generateSegment_左上(w, h), ]

	def generateSegments_臥捺(self, w, h):
		assert w>0 and h>0
		halfW = w//2
		halfH = h//2

		return [self.generateSegment_QCurve((halfW//2+halfH//4, halfH//2-halfW//4), (halfW, halfH)),
			self.generateSegment_QCurve((halfW//2-halfH//4, halfH//2+halfW//4), (halfW, halfH)), ]

	def generateSegments_豎撇(self, w, hs, hp):
		assert w>0 and hs>0 and hp>0
		return self.generateSegments_豎(hs) + [self.generateSegment_QCurve((0, hp), (-w, hp)), ]

	def generateSegments_彎鉤之彎(self, w1, h1):
		assert h1>0
		cPoint = [w1//2, h1//2]
		midPoint1 = [cPoint[0] + h1//2, cPoint[1] - w1//2]
		midPoint2 = [w1, h1]
		return [self.generateSegment_QCurve((w1//2 + h1//2, h1//2 - w1//2), midPoint2), ]

	def generateSegments_撇鉤之撇(self, w, h):
		assert w>0 and h>0
		return [self.generateSegment_QCurve((0, h), (-w, h)), ]

	def generateSegments_斜鉤之斜(self, w, h):
		assert w>0 and h>0
		return [self.generateSegment_QCurve((w//5, h*4//5), (w, h)), ]

	def generateSegments_曲(self, cr):
		assert cr>0
		return [self.generateSegment_QCurve([0, cr], [cr, cr]), ]

	def generateSegments_撇曲(self, wl, wr, h, cr):
		assert wl>0 and wr>0 and h>0
		midPoint1 = [-wl + cr, (wl - cr) * h // wl]
		tmpY = h - (wl - cr) * h // wl
		return [ self.generateSegment_Beeline(midPoint1),
			self.generateSegment_QCurve((-cr, tmpY), (0, tmpY)),
			self.generateSegment_Beeline((wr + wl - cr, 0)), ]

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

class XieStroke(Shape):
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

	def getPoints(self):
		points = [(False, self.getStartPoint())]
		points.extend(self.getStrokePath().getPoints(self.getStartPoint()))
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
	def __init__(self, name, parameterList, bBoxPane):
		self.name=name
		self.parameterList=parameterList
		self.bBoxPane=bBoxPane

	def isValid(self):
		return false

	def getName(self):
		return self.name

	def getBBoxPane(self):
		return self.bBoxPane

	@classmethod
	def parseExpression(cls, parameterExpressionList):
		return []

	def computeStrokeSegments(self):
		return []

	def toStrokePath(self):
		strokeSegments=self.computeStrokeSegments()
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


class StrokeInfo_點(StrokeInfo):
	@classmethod
	def parseExpression(cls, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==2
		assert int(l[1])>0
		return [int(l[0]), int(l[1])]

	def isValid(self):
		paramList=self.parameterList
		w=paramList[0]
		h=paramList[1]
		return h>0
#		return w>0 and h>0

	def computeStrokeSegments(self):
		paramList=self.parameterList
		w=paramList[0]
		h=paramList[1]

		return segmentFactory.generateSegments_點(w, h)

class StrokeInfo_圈(StrokeInfo):
	@classmethod
	def parseExpression(cls, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==2
		assert int(l[0])>0
		assert int(l[1])>0
		return [int(l[0]), int(l[1])]

	def isValid(self):
		paramList=self.parameterList
		a=paramList[0]
		b=paramList[1]
		return a>0 and b>0

	def computeStrokeSegments(self):
		paramList=self.parameterList
		w=paramList[0]
		h=paramList[1]

		return segmentFactory.generateSegments_圈(w, h)

class StrokeInfo_橫(StrokeInfo):
	@classmethod
	def parseExpression(cls, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==1
		assert int(l[0])>0
		return [int(l[0])]

	def isValid(self):
		paramList=self.parameterList
		w1=paramList[0]
		return w1>0

	def computeStrokeSegments(self):
		paramList=self.parameterList
		w1=paramList[0]

		return segmentFactory.generateSegments_橫(w1)

class StrokeInfo_橫鉤(StrokeInfo):
	@classmethod
	def parseExpression(cls, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==3
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		return [int(l[0]), int(l[1]), int(l[2]), ]

	def isValid(self):
		paramList=self.parameterList
		w1=paramList[0]
		w2=paramList[1]
		h2=paramList[2]
		return w1>0 and w2>0 and h2>0

	def computeStrokeSegments(self):
		paramList=self.parameterList
		w1=paramList[0]
		w2=paramList[1]
		h2=paramList[2]

		segments=[]
		segments.extend(segmentFactory.generateSegments_橫(w1))
		segments.extend(segmentFactory.generateSegments_撇(w2, h2))
		return segments

class StrokeInfo_橫折(StrokeInfo):
	@classmethod
	def parseExpression(cls, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==2
		assert int(l[0])>0
		assert int(l[1])>0
		return [int(l[0]), int(l[1]), ]

	def isValid(self):
		paramList=self.parameterList
		w1=paramList[0]
		h2=paramList[1]
		return w1>0 and h2>0

	def computeStrokeSegments(self):
		paramList=self.parameterList
		w1=paramList[0]
		h2=paramList[1]

		segments=[]
		segments.extend(segmentFactory.generateSegments_橫(w1))
		segments.extend(segmentFactory.generateSegments_豎(h2))
		return segments

class StrokeInfo_橫折折(StrokeInfo):
	@classmethod
	def parseExpression(cls, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==3
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		return [int(l[0]), int(l[1]), int(l[2]), ]

	def isValid(self):
		paramList=self.parameterList
		w1=paramList[0]
		h2=paramList[1]
		w3=paramList[2]
		return w1>0 and h2>0 and w3>0

	def computeStrokeSegments(self):
		paramList=self.parameterList
		w1=paramList[0]
		h2=paramList[1]
		w3=paramList[2]

		segments=[]
		segments.extend(segmentFactory.generateSegments_橫(w1))
		segments.extend(segmentFactory.generateSegments_豎(h2))
		segments.extend(segmentFactory.generateSegments_橫(w3))
		return segments

class StrokeInfo_橫折提(StrokeInfo):
	@classmethod
	def parseExpression(cls, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==4
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		assert int(l[3])>0
		return [int(l[0]), int(l[1]), int(l[2]), int(l[3]), ]

	def isValid(self):
		paramList=self.parameterList
		w1=paramList[0]
		h2=paramList[1]
		w3=paramList[2]
		h3=paramList[3]
		return w1>0 and h2>0 and w3>0 and h3>0

	def computeStrokeSegments(self):
		paramList=self.parameterList
		w1=paramList[0]
		h2=paramList[1]
		w3=paramList[2]
		h3=paramList[3]

		segments=[]
		segments.extend(segmentFactory.generateSegments_橫(w1))
		segments.extend(segmentFactory.generateSegments_豎(h2))
		segments.extend(segmentFactory.generateSegments_提(w3, h3))
		return segments

class StrokeInfo_橫折折撇(StrokeInfo):
	@classmethod
	def parseExpression(cls, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==4
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		assert int(l[3])>0
		assert int(l[4])>0
		assert int(l[5])>0
		return [int(l[0]), int(l[1]), int(l[2]), int(l[3]), int(l[4]), int(l[5]), ]

	def isValid(self):
		paramList=self.parameterList
		w1=paramList[0]
		w2=paramList[1]
		h2=paramList[2]
		w3=paramList[3]
		w4=paramList[4]
		h4=paramList[5]
		return w1>0 and w2>0 and h2>0 and w3>0 and w4>0 and h4>0

	def computeStrokeSegments(self):
		paramList=self.parameterList
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

class StrokeInfo_橫撇彎鉤(StrokeInfo):
	@classmethod
	def parseExpression(cls, parameterExpressionList):
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

	def isValid(self):
		paramList=self.parameterList
		w1=paramList[0]
		w2=paramList[1]
		h2=paramList[2]
		w3=paramList[3]
		h3=paramList[4]
		w4=paramList[5]
		h4=paramList[6]
		return w1>0 and w2>0 and h2>0 and w3>0 and h3>0 and w4>0 and h4>0

	def computeStrokeSegments(self):
		paramList=self.parameterList
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

class StrokeInfo_橫折鉤(StrokeInfo):
	@classmethod
	def parseExpression(cls, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==5
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		assert int(l[3])>0
		assert int(l[4])>0
		return [int(l[0]), int(l[1]), int(l[2]), int(l[3]), int(l[4]), ]

	def isValid(self):
		paramList=self.parameterList
		w1=paramList[0]
		w2=paramList[1]
		h2=paramList[2]
		w3=paramList[3]
		h3=paramList[4]
		return w1>0 and w2>0 and h2>0 and w3>0 and h3>0

	def computeStrokeSegments(self):
		paramList=self.parameterList
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

class StrokeInfo_橫折彎(StrokeInfo):
	@classmethod
	def parseExpression(cls, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==4
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		assert int(l[3])>0
		return [int(l[0]), int(l[1]), int(l[2]), int(l[3]), ]

	def isValid(self):
		paramList=self.parameterList
		w1=paramList[0]
		h2=paramList[1]
		w2=paramList[2]
		cr=paramList[3]
		return w1>0 and h2>0 and w2>0 and cr>0 and(h2-cr)>0 and (w2-cr)>0

	def computeStrokeSegments(self):
		paramList=self.parameterList
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

class StrokeInfo_橫撇(StrokeInfo):
	@classmethod
	def parseExpression(cls, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==3
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		return [int(l[0]), int(l[1]), int(l[2]), ]

	def isValid(self):
		paramList=self.parameterList
		w1=paramList[0]
		w2=paramList[1]
		h2=paramList[2]
		return w1>0 and w2>0 and h2>0

	def computeStrokeSegments(self):
		paramList=self.parameterList
		w1=paramList[0]
		w2=paramList[1]
		h2=paramList[2]

		segments=[]
		segments.extend(segmentFactory.generateSegments_橫(w1))
		segments.extend(segmentFactory.generateSegments_撇(w2, h2))
		return segments

class StrokeInfo_橫斜彎鉤(StrokeInfo):
	@classmethod
	def parseExpression(cls, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==6
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		assert int(l[3])>0
		assert int(l[4])>0
		assert int(l[5])>0
		return [int(l[0]), int(l[1]), int(l[2]), int(l[3]), int(l[4]), int(l[5]), ]

	def isValid(self):
		paramList=self.parameterList
		w1=paramList[0]
		h2=paramList[1]
		w2l=paramList[2]
		w2r=paramList[3]
		cr=paramList[4]
		h3=paramList[5]
		return w1>0 and h2>0 and w2l>0 and w2r>0 and cr>0 and h3>0

	def computeStrokeSegments(self):
		paramList=self.parameterList
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

class StrokeInfo_橫折折折鉤(StrokeInfo):
	@classmethod
	def parseExpression(cls, parameterExpressionList):
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

	def isValid(self):
		paramList=self.parameterList
		w1=paramList[0]
		w2=paramList[1]
		h2=paramList[2]
		w3=paramList[3]
		w4=paramList[4]
		h4=paramList[5]
		w5=paramList[6]
		h5=paramList[7]
		return w1>0 and w2>0 and h2>0 and w3>0 and w4>0 and h4>0 and w5>0 and h5>0

	def computeStrokeSegments(self):
		paramList=self.parameterList
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

class StrokeInfo_橫斜鉤(StrokeInfo):
	@classmethod
	def parseExpression(cls, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==4
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		assert int(l[3])>0
		return [int(l[0]), int(l[1]), int(l[2]), int(l[3]), ]

	def isValid(self):
		paramList=self.parameterList
		w1=paramList[0]
		w2=paramList[1]
		h2=paramList[2]
		h3=paramList[3]
		return w1>0 and w2>0 and h2>0 and h3>0

	def computeStrokeSegments(self):
		paramList=self.parameterList
		w1=paramList[0]
		w2=paramList[1]
		h2=paramList[2]
		h3=paramList[3]

		segments=[]
		segments.extend(segmentFactory.generateSegments_橫(w1))
		segments.extend(segmentFactory.generateSegments_斜鉤之斜(w2, h2))
		segments.extend(segmentFactory.generateSegments_上(h3))
		return segments

class StrokeInfo_橫折折折(StrokeInfo):
	@classmethod
	def parseExpression(cls, parameterExpressionList):
		l=parameterExpressionList
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		assert int(l[3])>0
		assert len(l)==4
		return [int(l[0]), int(l[1]), int(l[2]), int(l[3]), ]

	def isValid(self):
		paramList=self.parameterList
		w1=paramList[0]
		h2=paramList[1]
		w3=paramList[2]
		h4=paramList[3]
		return w1>0 and h2>0 and w3>0 and h4>0

	def computeStrokeSegments(self):
		paramList=self.parameterList
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

class StrokeInfo_豎(StrokeInfo):
	@classmethod
	def parseExpression(cls, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==1
		assert int(l[0])>0
		return [int(l[0]), ]

	def isValid(self):
		paramList=self.parameterList
		h1=paramList[0]
		return h1>0

	def computeStrokeSegments(self):
		paramList=self.parameterList
		h1=paramList[0]

		return segmentFactory.generateSegments_豎(h1)

class StrokeInfo_豎折(StrokeInfo):
	@classmethod
	def parseExpression(cls, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==2
		assert int(l[0])>0
		assert int(l[1])>0
		return [int(l[0]), int(l[1]), ]

	def isValid(self):
		paramList=self.parameterList
		h1=paramList[0]
		w2=paramList[1]
		return h1>0 and w2>0

	def computeStrokeSegments(self):
		paramList=self.parameterList
		h1=paramList[0]
		w2=paramList[1]

		segments=[]
		segments.extend(segmentFactory.generateSegments_豎(h1))
		segments.extend(segmentFactory.generateSegments_橫(w2))
		return segments

class StrokeInfo_豎彎左(StrokeInfo):
	@classmethod
	def parseExpression(cls, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==2
		assert int(l[0])>0
		assert int(l[1])>0
		return [int(l[0]), int(l[1]), ]

	def isValid(self):
		paramList=self.parameterList
		h1=paramList[0]
		w2=paramList[1]
		return h1>0 and w2>0

	def computeStrokeSegments(self):
		paramList=self.parameterList
		h1=paramList[0]
		w2=paramList[1]

		segments=[]
		segments.extend(segmentFactory.generateSegments_豎(h1))
		segments.extend(segmentFactory.generateSegments_左(w2))
		return segments

class StrokeInfo_豎提(StrokeInfo):
	@classmethod
	def parseExpression(cls, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==3
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		return [int(l[0]), int(l[1]), int(l[2]), ]

	def isValid(self):
		paramList=self.parameterList
		h1=paramList[0]
		w2=paramList[1]
		h2=paramList[2]
		return h1>0 and w2>0 and h2>0

	def computeStrokeSegments(self):
		paramList=self.parameterList
		h1=paramList[0]
		w2=paramList[1]
		h2=paramList[2]

		segments=[]
		segments.extend(segmentFactory.generateSegments_豎(h1))
		segments.extend(segmentFactory.generateSegments_提(w2, h2))
		return segments

class StrokeInfo_豎折折(StrokeInfo):
	@classmethod
	def parseExpression(cls, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==3
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		return [int(l[0]), int(l[1]), int(l[2]), ]

	def isValid(self):
		paramList=self.parameterList
		h1=paramList[0]
		w2=paramList[1]
		h3=paramList[2]
		return h1>0 and w2>0 and h3>0

	def computeStrokeSegments(self):
		paramList=self.parameterList
		h1=paramList[0]
		w2=paramList[1]
		h3=paramList[2]

		segments=[]
		segments.extend(segmentFactory.generateSegments_豎(h1))
		segments.extend(segmentFactory.generateSegments_橫(w2))
		segments.extend(segmentFactory.generateSegments_豎(h3))
		return segments

class StrokeInfo_豎折彎鉤(StrokeInfo):
	@classmethod
	def parseExpression(cls, parameterExpressionList):
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

	def isValid(self):
		paramList=self.parameterList
		w1=paramList[0]
		h1=paramList[1]
		w2=paramList[2]
		w3=paramList[3]
		h3=paramList[4]
		w4=paramList[5]
		h4=paramList[6]
		return w1>=0 and h1>0 and w2>0 and w3>0 and h3>0 and w4>0 and h4>0
#		return w1>0 and h1>0 and w2>0 and w3>0 and h3>0 and w4>0 and h4>0

	def computeStrokeSegments(self):
		paramList=self.parameterList
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

class StrokeInfo_豎彎鉤(StrokeInfo):
	@classmethod
	def parseExpression(cls, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==4
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		assert int(l[3])>0
		return [int(l[0]), int(l[1]), int(l[2]), int(l[3]), ]

	def isValid(self):
		paramList=self.parameterList
		h1=paramList[0]
		w1=paramList[1]
		cr=paramList[2]
		h2=paramList[3]
		return h1>0 and w1>0 and cr>0 and h2>0 and(h1-cr)>0 and (w1-cr)>0

	def computeStrokeSegments(self):
		paramList=self.parameterList
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

class StrokeInfo_豎彎(StrokeInfo):
	@classmethod
	def parseExpression(cls, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==3
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		return [int(l[0]), int(l[1]), int(l[2]), ]

	def isValid(self):
		paramList=self.parameterList
		w1=paramList[0]
		h1=paramList[1]
		cr=paramList[2]
		return w1>0 and h1>0 and cr>0

	def computeStrokeSegments(self):
		paramList=self.parameterList
		w1=paramList[0]
		h1=paramList[1]
		cr=paramList[2]

		segments=[]
		segments.extend(segmentFactory.generateSegments_豎(h1))
		segments.extend(segmentFactory.generateSegments_曲(cr))
		segments.extend(segmentFactory.generateSegments_橫(w1))
		return segments

class StrokeInfo_豎鉤(StrokeInfo):
	@classmethod
	def parseExpression(cls, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==3
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		return [int(l[0]), int(l[1]), int(l[2]), ]

	def isValid(self):
		paramList=self.parameterList
		h1=paramList[0]
		w2=paramList[1]
		h2=paramList[2]
		return h1>0 and w2>0 and h2>0

	def computeStrokeSegments(self):
		paramList=self.parameterList
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

class StrokeInfo_斜鉤(StrokeInfo):
	@classmethod
	def parseExpression(cls, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==3
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		return [int(l[0]), int(l[1]), int(l[2]), ]

	def isValid(self):
		paramList=self.parameterList
		w1=paramList[0]
		h1=paramList[1]
		h2=paramList[2]
		return w1>0 and h1>0 and h2>0

	def computeStrokeSegments(self):
		paramList=self.parameterList
		w1=paramList[0]
		h1=paramList[1]
		h2=paramList[2]

		segments=[]
		segments.extend(segmentFactory.generateSegments_斜鉤之斜(w1, h1))
		segments.extend(segmentFactory.generateSegments_上(h2))
		return segments

class StrokeInfo_彎鉤(StrokeInfo):
	@classmethod
	def parseExpression(cls, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==4
#		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		assert int(l[3])>0
		return [int(l[0]), int(l[1]), int(l[2]), int(l[3]), ]

	def isValid(self):
		paramList=self.parameterList
		w1=paramList[0]
		h1=paramList[1]
		w2=paramList[2]
		h2=paramList[3]
		return h1>0 and w2>0 and h2>0
#		return w1>0 and h1>0 and w2>0 and h2>0

	def computeStrokeSegments(self):
		paramList=self.parameterList
		w1=paramList[0]
		h1=paramList[1]
		w2=paramList[2]
		h2=paramList[3]

		segments=[]
		segments.extend(segmentFactory.generateSegments_彎鉤之彎(w1, h1))
		segments.extend(segmentFactory.generateSegments_鉤(w2, h2))
		return segments

class StrokeInfo_撇鉤(StrokeInfo):
	@classmethod
	def parseExpression(cls, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==4
#		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		assert int(l[3])>0
		return [int(l[0]), int(l[1]), int(l[2]), int(l[3]), ]

	def isValid(self):
		paramList=self.parameterList
		w1=paramList[0]
		h1=paramList[1]
		w2=paramList[2]
		h2=paramList[3]
		return h1>0 and w2>0 and h2>0
#		return w1>0 and h1>0 and w2>0 and h2>0

	def computeStrokeSegments(self):
		paramList=self.parameterList
		w1=paramList[0]
		h1=paramList[1]
		w2=paramList[2]
		h2=paramList[3]

		segments=[]
		segments.extend(segmentFactory.generateSegments_彎鉤之彎(w1, h1))
		segments.extend(segmentFactory.generateSegments_鉤(w2, h2))
		return segments

class StrokeInfo_撇(StrokeInfo):
	@classmethod
	def parseExpression(cls, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==2
		assert int(l[0])>0
		assert int(l[1])>0
		return [int(l[0]), int(l[1]), ]

	def isValid(self):
		paramList=self.parameterList
		w1=paramList[0]
		h1=paramList[1]
		return w1>0 and h1>0

	def computeStrokeSegments(self):
		paramList=self.parameterList
		w1=paramList[0]
		h1=paramList[1]

		segments=[]
		segments.extend(segmentFactory.generateSegments_撇(w1, h1))
		return segments

class StrokeInfo_撇點(StrokeInfo):
	@classmethod
	def parseExpression(cls, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==4
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		assert int(l[3])>0
		return [int(l[0]), int(l[1]), int(l[2]), int(l[3]), ]

	def isValid(self):
		paramList=self.parameterList
		w1=paramList[0]
		h1=paramList[1]
		w2=paramList[2]
		h2=paramList[3]
		return w1>0 and h1>0 and w2>0 and h2>0

	def computeStrokeSegments(self):
		paramList=self.parameterList
		w1=paramList[0]
		h1=paramList[1]
		w2=paramList[2]
		h2=paramList[3]

		segments=[]
		segments.extend(segmentFactory.generateSegments_撇(w1, h1))
		segments.extend(segmentFactory.generateSegments_點(w2, h2))
		return segments

class StrokeInfo_撇橫(StrokeInfo):
	@classmethod
	def parseExpression(cls, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==4
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
#		assert int(l[3])>0
		return [int(l[0]), int(l[1]), int(l[2]), int(l[3]), ]

	def isValid(self):
		paramList=self.parameterList
		w1=paramList[0]
		h1=paramList[1]
		w2=paramList[2]
		h2=paramList[3]
		return w1>0 and h1>0 and w2>0
#		return w1>0 and h1>0 and w2>0 and h2>0

	def computeStrokeSegments(self):
		paramList=self.parameterList
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

class StrokeInfo_撇橫撇(StrokeInfo):
	@classmethod
	def parseExpression(cls, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==5
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		assert int(l[3])>0
		assert int(l[4])>0
		return [int(l[0]), int(l[1]), int(l[2]), int(l[3]), int(l[4]), ]

	def isValid(self):
		paramList=self.parameterList
		w1=paramList[0]
		h1=paramList[1]
		w2=paramList[2]
		w3=paramList[3]
		h3=paramList[4]
		return w1>0 and h1>0 and w2>0 and w3>0 and h3>0

	def computeStrokeSegments(self):
		paramList=self.parameterList
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

class StrokeInfo_豎撇(StrokeInfo):
	@classmethod
	def parseExpression(cls, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==2
		assert int(l[0])>0
		assert int(l[1])>0
		return [int(l[0]), int(l[1]), ]

	def isValid(self):
		paramList=self.parameterList
		w1=paramList[0]
		h1=paramList[1]
		return w1>0 and h1>0

	def computeStrokeSegments(self):
		paramList=self.parameterList
		w1=paramList[0]
		h1=paramList[1]

		hs = h1 - h1//2
		hp = h1 - (hs)
		wp = w1

		segments=[]
		segments.extend(segmentFactory.generateSegments_豎撇(w1, hs, hp))
		return segments

class StrokeInfo_提(StrokeInfo):
	@classmethod
	def parseExpression(cls, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==2
		assert int(l[0])>0
		assert int(l[1])>0
		return [int(l[0]), int(l[1]), ]

	def isValid(self):
		paramList=self.parameterList
		w1=paramList[0]
		h1=paramList[1]
		return w1>0 and h1>0

	def computeStrokeSegments(self):
		paramList=self.parameterList
		w1=paramList[0]
		h1=paramList[1]

		return segmentFactory.generateSegments_提(w1, h1)

class StrokeInfo_捺(StrokeInfo):
	@classmethod
	def parseExpression(cls, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==2
		assert int(l[0])>0
		assert int(l[1])>0
		return [int(l[0]), int(l[1]), ]

	def isValid(self):
		paramList=self.parameterList
		w1=paramList[0]
		h1=paramList[1]
		return w1>0 and h1>0

	def computeStrokeSegments(self):
		paramList=self.parameterList
		w1=paramList[0]
		h1=paramList[1]

		return segmentFactory.generateSegments_捺(w1, h1)

class StrokeInfo_臥捺(StrokeInfo):
	@classmethod
	def parseExpression(cls, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==2
		assert int(l[0])>0
		assert int(l[1])>0
		return [int(l[0]), int(l[1]), ]

	def isValid(self):
		paramList=self.parameterList
		w1=paramList[0]
		h1=paramList[1]
		return w1>0 and h1>0

	def computeStrokeSegments(self):
		paramList=self.parameterList
		w1=paramList[0]
		h1=paramList[1]

		return segmentFactory.generateSegments_臥捺(w1, h1)

class StrokeInfo_提捺(StrokeInfo):
	@classmethod
	def parseExpression(cls, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==4
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		assert int(l[3])>0
		return [int(l[0]), int(l[1]), int(l[2]), int(l[3]), ]

	def isValid(self):
		paramList=self.parameterList
		w1=paramList[0]
		h1=paramList[1]
		w2=paramList[2]
		h2=paramList[3]
		return w1>0 and h1>0 and w2>0 and h2>0

	def computeStrokeSegments(self):
		paramList=self.parameterList
		w1=paramList[0]
		h1=paramList[1]
		w2=paramList[2]
		h2=paramList[3]

		segments=[]
		segments.extend(segmentFactory.generateSegments_提(w1, h1))
		segments.extend(segmentFactory.generateSegments_捺(w2, h2))
		return segments

class StrokeInfo_橫捺(StrokeInfo):
	@classmethod
	def parseExpression(cls, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==3
		assert int(l[0])>0
		assert int(l[1])>0
		assert int(l[2])>0
		return [int(l[0]), int(l[1]), int(l[2]), ]

	def isValid(self):
		paramList=self.parameterList
		w1=paramList[0]
		w2=paramList[1]
		h2=paramList[2]
		return w1>0 and w2>0 and h2>0

	def computeStrokeSegments(self):
		paramList=self.parameterList
		w1=paramList[0]
		w2=paramList[1]
		h2=paramList[2]

		segments=[]
		segments.extend(segmentFactory.generateSegments_橫(w1))
		segments.extend(segmentFactory.generateSegments_捺(w2, h2))
		return segments

StrokeInfoMap = {
	"點": StrokeInfo_點,
#	"長頓點": StrokeInfo_點,
	"圈": StrokeInfo_圈,
	"橫": StrokeInfo_橫,
	"橫鉤": StrokeInfo_橫鉤,
	"橫折": StrokeInfo_橫折,
	"橫折折": StrokeInfo_橫折折,
	"橫折提": StrokeInfo_橫折提,
	"橫折折撇": StrokeInfo_橫折折撇,
	"橫撇彎鉤": StrokeInfo_橫撇彎鉤,
	"橫折鉤": StrokeInfo_橫折鉤,
	"橫折彎": StrokeInfo_橫折彎,
	"橫撇": StrokeInfo_橫撇,
	"橫斜彎鉤": StrokeInfo_橫斜彎鉤,
	"橫折折折鉤": StrokeInfo_橫折折折鉤,
	"橫斜鉤": StrokeInfo_橫斜鉤,
	"橫折折折": StrokeInfo_橫折折折,
	"豎": StrokeInfo_豎,
	"豎折": StrokeInfo_豎折,
	"豎彎左": StrokeInfo_豎彎左,
	"豎提": StrokeInfo_豎提,
	"豎折折": StrokeInfo_豎折折,
	"豎折彎鉤": StrokeInfo_豎折彎鉤,
	"豎彎鉤": StrokeInfo_豎彎鉤,
	"豎彎": StrokeInfo_豎彎,
	"豎鉤": StrokeInfo_豎鉤,
	"扁斜鉤": StrokeInfo_豎彎鉤,
	"斜鉤": StrokeInfo_斜鉤,
	"彎鉤": StrokeInfo_彎鉤,
	"撇鉤": StrokeInfo_撇鉤,

	"撇": StrokeInfo_撇,
	"撇點": StrokeInfo_撇點,
	"撇橫": StrokeInfo_撇橫,
	"撇提": StrokeInfo_撇橫,
	"撇折": StrokeInfo_撇橫,
	"撇橫撇": StrokeInfo_撇橫撇,
	"豎撇": StrokeInfo_豎撇,
	"提": StrokeInfo_提,
	"捺": StrokeInfo_捺,
	"臥捺": StrokeInfo_臥捺,
	"提捺": StrokeInfo_提捺,
	"橫捺": StrokeInfo_橫捺,
}

def _generateStrokeInfo(name, parameterList, bBox):
	clsStrokeInfo = StrokeInfoMap.get(name, None)
	assert clsStrokeInfo!=None

	parameterList = clsStrokeInfo.parseExpression(parameterList)
	strokeInfo = clsStrokeInfo(name, parameterList, Pane(*bBox))
	return strokeInfo

class QHStroke(Drawing):
	def __init__(self, startPoint, strokeInfo):
		pane=strokeInfo.getBBoxPane()
		super().__init__(pane)
		self.strokeInfo=strokeInfo
		self.startPoint=startPoint
		self.strokePath=strokeInfo.toStrokePath()

	def clone(self):
		stroke=QHStroke(self.startPoint, self.strokeInfo)
		stroke.setStatePane(self.getStatePane())
		return stroke

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


	def getName(self):
		return self.getStrokeInfo().getName()

	def getStartPoint(self):
		return self.startPoint

	def getStrokePath(self):
		return self.strokePath

	def getStrokeInfo(self):
		return self.strokeInfo

	def getPoints(self):
		startPoint=self.getStartPoint()
		strokePath=self.getStrokePath()

		points = [(False, startPoint)]
		points.extend(strokePath.getPoints(startPoint))

		pane=self.getStatePane()
		bBoxPane=self.getInfoPane()
		newPoints = [(isCurve, bBoxPane.transformRelativePointByTargetPane(point, pane)) for (isCurve, point) in points]
		return newPoints

class Stroke(QHStroke):
	def __init__(self, startPoint, strokeInfo, pane):
		super().__init__(startPoint, strokeInfo)
		super().setStatePane(pane)

	def clone(self):
		return Stroke(self.startPoint, self.strokeInfo, self.getStatePane())


def generateStroke(name, startPoint, parameterList, bBox):
	strokeInfo = _generateStrokeInfo(name, parameterList, bBox)
	return Stroke(startPoint, strokeInfo, strokeInfo.getBBoxPane())

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
		super().__init__(pane)
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

