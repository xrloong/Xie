from .shape import Shape
from .quadratic import solveMin, solveMax

class Segment(Shape):
	def __init__(self):
		pass

	def __ne__(self, other):
		return not self.__eq__(other)

	def draw(self, drawingSystem):
		pass

	def computeBoundary(self):
		return (0, 0, 0, 0)

class BaseBeelineSegment(Segment):
	def __eq__(self, other):
		return (isinstance(other, self.__class__)
			and self.getEndPoint() == other.getEndPoint())

	def getEndPoint(self):
		return (0, 0)

	def draw(self, drawingSystem):
		drawingSystem.lineTo(self.getEndPoint())

	def computeBoundary(self):
		startPoint=(0, 0)
		endPoint=self.getEndPoint()
		return (min(startPoint[0], endPoint[0]), min(startPoint[1], endPoint[1]),
			max(startPoint[0], endPoint[0]), max(startPoint[1], endPoint[1]))

class BaseQCurveSegment(Segment):
	def __eq__(self, other):
		return (
			isinstance(other, self.__class__)
			and (
				self.getControlPoint() == other.getControlPoint()
				and self.getEndPoint() == other.getEndPoint()
			)
		)

	def getControlPoint(self):
		return (0, 0)

	def getEndPoint(self):
		return (0, 0)

	def draw(self, drawingSystem):
		drawingSystem.qCurveTo(self.getControlPoint(), self.getEndPoint())

	def computeBoundary(self):
		startPoint=(0, 0)
		controlPoint=self.getControlPoint()
		endPoint=self.getEndPoint()
		minX = solveMin(startPoint[0], controlPoint[0], endPoint[0])
		minY = solveMin(startPoint[1], controlPoint[1], endPoint[1])
		maxX = solveMax(startPoint[0], controlPoint[0], endPoint[0])
		maxY = solveMax(startPoint[1], controlPoint[1], endPoint[1])
		return (minX, minY, maxX, maxY)

class BeelineSegment(BaseBeelineSegment):
	def __init__(self, point):
		super().__init__()
		self.point=point

	def __str__(self):
		return "Beeline({0})".format(self.point)

	def __repr__(self):
		return "BeelineSegment({0})".format(self.point)

	def getEndPoint(self):
		return self.point

class QCurveSegment(BaseQCurveSegment):
	def __init__(self, control_point, point):
		super().__init__()
		self.control_point=control_point
		self.point=point

	def __str__(self):
		return "QCurve({0}, {1})".format(self.control_point, self.point)

	def __repr__(self):
		return "QCurveSegment({0}, {1})".format(self.control_point, self.point)

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

