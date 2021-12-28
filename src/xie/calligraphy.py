class Parameter:
	def __init__(self, name):
		self.name = name

	def getName(self):
		return self.name

class Argument:
	def __init__(self, value):
		self.value = value

	def getValue(self):
		return self.value

class SegmentInfo:
	def __init__(self, parameters):
		self.parameters = parameters

class Segment:
	def __init__(self, parameters, arguments):
		self.parameters = parameters
		self.arguments = arguments

class Stroke:
	def __init__(self):
		self.startPoint = (0, 0)
		self.segments = []

