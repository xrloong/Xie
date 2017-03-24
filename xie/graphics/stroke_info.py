from .segment import StrokePath

class StrokeInfo:
	def __init__(self, name, strokePath):
		self.name=name
		self.strokePath=strokePath

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		return isinstance(other, StrokeInfo) and (self.getName()==other.getName() and self.getStrokePath()==other.getStrokePath())

	def getName(self):
		return self.name

	def getStrokePath(self):
		return self.strokePath

class StrokeInfoGenerator:
	def __init__(self, segmentFactory):
		self.segmentFactory = segmentFactory

	def getSegmentFactory(self):
		return self.segmentFactory

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


class StrokeInfoGenerator_點(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==2
		assert int(l[1])>0
		return [int(l[0]), int(l[1])]

	def computeStrokeSegments(self, paramList):
		w=paramList[0]
		h=paramList[1]

		return self.getSegmentFactory().generateSegments_點(w, h)

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

		return self.getSegmentFactory().generateSegments_圈(w, h)

class StrokeInfoGenerator_橫(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==1
		assert int(l[0])>0
		return [int(l[0])]

	def computeStrokeSegments(self, paramList):
		w1=paramList[0]

		return self.getSegmentFactory().generateSegments_橫(w1)

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
		segments.extend(self.getSegmentFactory().generateSegments_橫(w1))
		segments.extend(self.getSegmentFactory().generateSegments_撇(w2, h2))
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
		segments.extend(self.getSegmentFactory().generateSegments_橫(w1))
		segments.extend(self.getSegmentFactory().generateSegments_豎(h2))
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
		segments.extend(self.getSegmentFactory().generateSegments_橫(w1))
		segments.extend(self.getSegmentFactory().generateSegments_豎(h2))
		segments.extend(self.getSegmentFactory().generateSegments_橫(w3))
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
		segments.extend(self.getSegmentFactory().generateSegments_橫(w1))
		segments.extend(self.getSegmentFactory().generateSegments_豎(h2))
		segments.extend(self.getSegmentFactory().generateSegments_提(w3, h3))
		return segments

class StrokeInfoGenerator_橫折折撇(StrokeInfoGenerator):
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
		w2=paramList[1]
		h2=paramList[2]
		w3=paramList[3]
		w4=paramList[4]
		h4=paramList[5]

		segments=[]
		segments.extend(self.getSegmentFactory().generateSegments_橫(w1))
		segments.extend(self.getSegmentFactory().generateSegments_撇(w2, h2))
		segments.extend(self.getSegmentFactory().generateSegments_橫(w3))
		segments.extend(self.getSegmentFactory().generateSegments_撇(w4, h4))
		return segments

class StrokeInfoGenerator_橫撇彎鉤(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==7
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
		segments.extend(self.getSegmentFactory().generateSegments_橫(w1))
		segments.extend(self.getSegmentFactory().generateSegments_撇(w2, h2))
		segments.extend(self.getSegmentFactory().generateSegments_彎鉤之彎(w3, h3))
		segments.extend(self.getSegmentFactory().generateSegments_鉤(w4, h4))
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
		segments.extend(self.getSegmentFactory().generateSegments_橫(w1))
		segments.extend(self.getSegmentFactory().generateSegments_撇鉤之撇(w2, h2))
		segments.extend(self.getSegmentFactory().generateSegments_鉤(w3, h3))
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
		segments.extend(self.getSegmentFactory().generateSegments_橫(w1))
		segments.extend(self.getSegmentFactory().generateSegments_豎(h2 - cr))
		segments.extend(self.getSegmentFactory().generateSegments_曲(cr))
		segments.extend(self.getSegmentFactory().generateSegments_橫(w2 - cr))
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
		segments.extend(self.getSegmentFactory().generateSegments_橫(w1))
		segments.extend(self.getSegmentFactory().generateSegments_撇(w2, h2))
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
		segments.extend(self.getSegmentFactory().generateSegments_橫(w1))
		segments.extend(self.getSegmentFactory().generateSegments_撇曲(w2l, w2r, h2, cr))
		segments.extend(self.getSegmentFactory().generateSegments_上(h3))
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
		segments.extend(self.getSegmentFactory().generateSegments_橫(w1))
		segments.extend(self.getSegmentFactory().generateSegments_撇(w2, h2))
		segments.extend(self.getSegmentFactory().generateSegments_橫(w3))
		segments.extend(self.getSegmentFactory().generateSegments_撇鉤之撇(w4, h4))
		segments.extend(self.getSegmentFactory().generateSegments_鉤(w5, h5))
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
		segments.extend(self.getSegmentFactory().generateSegments_橫(w1))
		segments.extend(self.getSegmentFactory().generateSegments_斜鉤之斜(w2, h2))
		segments.extend(self.getSegmentFactory().generateSegments_上(h3))
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
		segments.extend(self.getSegmentFactory().generateSegments_橫(w1))
		segments.extend(self.getSegmentFactory().generateSegments_豎(h2))
		segments.extend(self.getSegmentFactory().generateSegments_橫(w3))
		segments.extend(self.getSegmentFactory().generateSegments_豎(h4))
		return segments

class StrokeInfoGenerator_豎(StrokeInfoGenerator):
	def parseExpression(self, parameterExpressionList):
		l=parameterExpressionList
		assert len(l)==1
		assert int(l[0])>0
		return [int(l[0]), ]

	def computeStrokeSegments(self, paramList):
		h1=paramList[0]

		return self.getSegmentFactory().generateSegments_豎(h1)

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
		segments.extend(self.getSegmentFactory().generateSegments_豎(h1))
		segments.extend(self.getSegmentFactory().generateSegments_橫(w2))
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
		segments.extend(self.getSegmentFactory().generateSegments_豎(h1))
		segments.extend(self.getSegmentFactory().generateSegments_左(w2))
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
		segments.extend(self.getSegmentFactory().generateSegments_豎(h1))
		segments.extend(self.getSegmentFactory().generateSegments_提(w2, h2))
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
		segments.extend(self.getSegmentFactory().generateSegments_豎(h1))
		segments.extend(self.getSegmentFactory().generateSegments_橫(w2))
		segments.extend(self.getSegmentFactory().generateSegments_豎(h3))
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
			segments.extend(self.getSegmentFactory().generateSegments_撇(w1, h1))
		elif w1<0:
			assert False
		else:
			segments.extend(self.getSegmentFactory().generateSegments_豎(h1))
		segments.extend(self.getSegmentFactory().generateSegments_橫(w2))
		segments.extend(self.getSegmentFactory().generateSegments_撇鉤之撇(w3, h3))
		segments.extend(self.getSegmentFactory().generateSegments_鉤(w4, h4))
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
		segments.extend(self.getSegmentFactory().generateSegments_豎(h1-cr))
		segments.extend(self.getSegmentFactory().generateSegments_曲(cr))
		segments.extend(self.getSegmentFactory().generateSegments_橫(w1-cr))
		segments.extend(self.getSegmentFactory().generateSegments_上(h2))
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
		segments.extend(self.getSegmentFactory().generateSegments_豎(h1))
		segments.extend(self.getSegmentFactory().generateSegments_曲(cr))
		segments.extend(self.getSegmentFactory().generateSegments_橫(w1))
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
		segments.extend(self.getSegmentFactory().generateSegments_豎撇(wp, hs, hp))
		segments.extend(self.getSegmentFactory().generateSegments_鉤(wg, hg))
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
		segments.extend(self.getSegmentFactory().generateSegments_斜鉤之斜(w1, h1))
		segments.extend(self.getSegmentFactory().generateSegments_上(h2))
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
		segments.extend(self.getSegmentFactory().generateSegments_彎鉤之彎(w1, h1))
		segments.extend(self.getSegmentFactory().generateSegments_鉤(w2, h2))
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
		segments.extend(self.getSegmentFactory().generateSegments_彎鉤之彎(w1, h1))
		segments.extend(self.getSegmentFactory().generateSegments_鉤(w2, h2))
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
		segments.extend(self.getSegmentFactory().generateSegments_撇(w1, h1))
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
		segments.extend(self.getSegmentFactory().generateSegments_撇(w1, h1))
		segments.extend(self.getSegmentFactory().generateSegments_點(w2, h2))
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
		segments.extend(self.getSegmentFactory().generateSegments_撇(w1, h1))
		if h2>0:
			segments.extend(self.getSegmentFactory().generateSegments_點(w2, h2))
		elif h2<0:
			segments.extend(self.getSegmentFactory().generateSegments_提(w2, -h2))
		else:
			segments.extend(self.getSegmentFactory().generateSegments_橫(w2))
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
		segments.extend(self.getSegmentFactory().generateSegments_撇(w1, h1))
		segments.extend(self.getSegmentFactory().generateSegments_橫(w2))
		segments.extend(self.getSegmentFactory().generateSegments_撇(w3, h3))
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
		segments.extend(self.getSegmentFactory().generateSegments_豎撇(w1, hs, hp))
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

		return self.getSegmentFactory().generateSegments_提(w1, h1)

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

		return self.getSegmentFactory().generateSegments_捺(w1, h1)

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

		return self.getSegmentFactory().generateSegments_臥捺(w1, h1)

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
		segments.extend(self.getSegmentFactory().generateSegments_提(w1, h1))
		segments.extend(self.getSegmentFactory().generateSegments_捺(w2, h2))
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
		segments.extend(self.getSegmentFactory().generateSegments_橫(w1))
		segments.extend(self.getSegmentFactory().generateSegments_捺(w2, h2))
		return segments

class StrokeInfoFactory:
	def __init__(self):
		from .segment import SegmentFactory

		segmentFactory = SegmentFactory()
		self.strokeInfoMap = {
			"點": StrokeInfoGenerator_點(segmentFactory),
#			"長頓點": StrokeInfoGenerator_點(segmentFactory),
			"圈": StrokeInfoGenerator_圈(segmentFactory),
			"橫": StrokeInfoGenerator_橫(segmentFactory),
			"橫鉤": StrokeInfoGenerator_橫鉤(segmentFactory),
			"橫折": StrokeInfoGenerator_橫折(segmentFactory),
			"橫折折": StrokeInfoGenerator_橫折折(segmentFactory),
			"橫折提": StrokeInfoGenerator_橫折提(segmentFactory),
			"橫折折撇": StrokeInfoGenerator_橫折折撇(segmentFactory),
			"橫撇彎鉤": StrokeInfoGenerator_橫撇彎鉤(segmentFactory),
			"橫折鉤": StrokeInfoGenerator_橫折鉤(segmentFactory),
			"橫折彎": StrokeInfoGenerator_橫折彎(segmentFactory),
			"橫撇": StrokeInfoGenerator_橫撇(segmentFactory),
			"橫斜彎鉤": StrokeInfoGenerator_橫斜彎鉤(segmentFactory),
			"橫折折折鉤": StrokeInfoGenerator_橫折折折鉤(segmentFactory),
			"橫斜鉤": StrokeInfoGenerator_橫斜鉤(segmentFactory),
			"橫折折折": StrokeInfoGenerator_橫折折折(segmentFactory),
			"豎": StrokeInfoGenerator_豎(segmentFactory),
			"豎折": StrokeInfoGenerator_豎折(segmentFactory),
			"豎彎左": StrokeInfoGenerator_豎彎左(segmentFactory),
			"豎提": StrokeInfoGenerator_豎提(segmentFactory),
			"豎折折": StrokeInfoGenerator_豎折折(segmentFactory),
			"豎折彎鉤": StrokeInfoGenerator_豎折彎鉤(segmentFactory),
			"豎彎鉤": StrokeInfoGenerator_豎彎鉤(segmentFactory),
			"豎彎": StrokeInfoGenerator_豎彎(segmentFactory),
			"豎鉤": StrokeInfoGenerator_豎鉤(segmentFactory),
			"扁斜鉤": StrokeInfoGenerator_豎彎鉤(segmentFactory),
			"斜鉤": StrokeInfoGenerator_斜鉤(segmentFactory),
			"彎鉤": StrokeInfoGenerator_彎鉤(segmentFactory),
			"撇鉤": StrokeInfoGenerator_撇鉤(segmentFactory),

			"撇": StrokeInfoGenerator_撇(segmentFactory),
			"撇點": StrokeInfoGenerator_撇點(segmentFactory),
			"撇橫": StrokeInfoGenerator_撇橫(segmentFactory),
			"撇提": StrokeInfoGenerator_撇橫(segmentFactory),
			"撇折": StrokeInfoGenerator_撇橫(segmentFactory),
			"撇橫撇": StrokeInfoGenerator_撇橫撇(segmentFactory),
			"豎撇": StrokeInfoGenerator_豎撇(segmentFactory),
			"提": StrokeInfoGenerator_提(segmentFactory),
			"捺": StrokeInfoGenerator_捺(segmentFactory),
			"臥捺": StrokeInfoGenerator_臥捺(segmentFactory),
			"提捺": StrokeInfoGenerator_提捺(segmentFactory),
			"橫捺": StrokeInfoGenerator_橫捺(segmentFactory),
		}


	def generateStrokeInfo(self, name, parameterList):
		strokeInfoGenerator = self.strokeInfoMap.get(name, None)
		assert strokeInfoGenerator!=None

		parameterList = strokeInfoGenerator.parseExpression(parameterList)
		strokeInfo = strokeInfoGenerator.generate(name, parameterList)
		return strokeInfo


