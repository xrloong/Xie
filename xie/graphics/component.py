from .shape import Shape, Pane

class ComponentInfo:
	def __init__(self, strokeList):
		self.strokeList=strokeList
		self.infoPane=None

	def getStrokeList(self):
		return self.strokeList

	def getInfoPane(self):
		if not self.infoPane:
			def mergeBoundaryList(boundaryList):
				from xie.graphics.shape import mergeBoundary
				r = boundaryList[0]
				for b in boundaryList[1:]:
					r = mergeBoundary(r, b)
				return r

			strokeList=self.getStrokeList()
			boundaryList=[stroke.computeBoundary() for stroke in strokeList]
			bBox=mergeBoundaryList(boundaryList)
			self.infoPane=Pane(*bBox)

		return self.infoPane

class Component(Shape):
	def __init__(self, componentInfo: ComponentInfo, statePane: Pane=None):
		self.componentInfo=componentInfo

		if not statePane:
			statePane=componentInfo.getInfoPane()
		self.statePane=statePane

	def getStatePane(self):
		return self.statePane

	def getStrokeList(self):
		return self.componentInfo.getStrokeList()

	def getCount(self):
		return len(self.getStrokeList())

	def getStroke(self, index):
		return self.getStrokeList()[index]

	def draw(self, drawingSystem):
		strokeList = self.getStrokeList();

		for stroke in strokeList:
			stroke.draw(drawingSystem)

