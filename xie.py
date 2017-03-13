#!/usr/bin/env python3

class XieApp:
	def __init__(self):
		self.canvasWidth=512
		self.canvasHeight=512

		import tkinter

		self.root=tkinter.Tk()

		master=self.root
		frame=tkinter.Frame(master)
		frame.pack()

		self.canvas = tkinter.Canvas(master=frame, width=self.canvasWidth, height=self.canvasHeight)
		self.canvas.grid(row=3, columnspan=3)

		from xie.graphics.canvas import TkCanvasController
		canvasController = TkCanvasController(self.canvas, self.canvasWidth, self.canvasHeight)

		from xie.graphics.drawing import DrawingSystem
		self.dh = DrawingSystem(canvasController)

		from xie.graphics.shape import Rectangle

		frame=Rectangle(0, 0, canvasController.getWidth(), canvasController.getHeight())
		self.dh.draw(frame)

		targetRect = Rectangle(0, 0, 512, 512)

	def mainloop(self):
		self.root.mainloop()

	def test(self):
#		self.testXie()
		self.testQH()

	def testXie(self):
		import xie.graphics.stroke_factory as StrokeFactory

		strokeFactory = StrokeFactory.getInstance()
		stroke=strokeFactory.generateStroke橫((70, 30), 200)
		self.dh.draw(stroke)

		stroke=strokeFactory.generateStroke豎((70, 30), 200)
		self.dh.draw(stroke)

		stroke=strokeFactory.generateStroke撇((270, 30), 200, 200)
		self.dh.draw(stroke)

		stroke=strokeFactory.generateStroke捺((170, 130), 200, 200)
		self.dh.draw(stroke)

		stroke=strokeFactory.generateStroke圈((256, 300), 200, 100)
		self.dh.draw(stroke)

	def testQH(self):
#		self.testQH_1()
#		self.testQH_2()
#		self.testQH_3()
		self.testQH_4()

	def testQH_1(self):
		from xie.graphics.stroke import generateStroke
		qhStroke=generateStroke("圈", [126, 40], [77, 79], [49, 40, 203, 198])
		stroke=qhStroke.toXieStroke()
		self.dh.draw(stroke)

		qhStroke=generateStroke("點", [93, 91], [60, 73], [93, 91, 153, 164])
		stroke=qhStroke.toXieStroke()
		self.dh.draw(stroke)

		qhStroke=generateStroke("橫", [20, 123], [202], [20, 123, 222, 123])
		stroke=qhStroke.toXieStroke()
		self.dh.draw(stroke)

		qhStroke=generateStroke("豎", [121, 27], [190], [121, 27, 121, 217])
		stroke=qhStroke.toXieStroke()
		self.dh.draw(stroke)

	def testQH_2(self):
		from xie.graphics.stroke import generateStroke
		qhStroke=generateStroke("提", [80, 177], [85, 53], [80, 124, 165, 177])
		stroke=qhStroke.toXieStroke()
		self.dh.draw(stroke)

		qhStroke=generateStroke("捺", [145, 93], [86, 147], [145, 93, 231, 240])
		stroke=qhStroke.toXieStroke()
		self.dh.draw(stroke)

		qhStroke=generateStroke("豎彎左", [145, 123], [86, 147], [20, 123, 222, 123])
		stroke=qhStroke.toXieStroke()
		self.dh.draw(stroke)

		qhStroke=generateStroke("豎彎鉤", [110, 21], [185, 88, 26, 51], [110, 21, 198, 206])
		stroke=qhStroke.toXieStroke()
		self.dh.draw(stroke)

	def testQH_3(self):
		from xie.graphics.stroke import generateStroke
		qhStroke=generateStroke("豎撇", [58, 26], [45, 204], [13, 26, 58, 230])
		stroke=qhStroke.toXieStroke()
		self.dh.draw(stroke)

		qhStroke=generateStroke("臥捺", [10, 202], [220, 22], [10, 180, 230, 245])
		stroke=qhStroke.toXieStroke()
		self.dh.draw(stroke)

		qhStroke=generateStroke("彎鉤", [124, 41], [-10, 196, 33, 19], [81, 41, 217, 237])
		stroke=qhStroke.toXieStroke()
		self.dh.draw(stroke)

		qhStroke=generateStroke("橫折鉤", [95, 104], [93, 48, 120, 48, 55], [92, 104, 188, 224])
		stroke=qhStroke.toXieStroke()
		self.dh.draw(stroke)

	def testQH_4(self):
		from xie.graphics.stroke import generateStroke
		qhStroke=generateStroke("斜鉤", [107, 20], [121, 227, 62], [107, 20, 228, 247])
		stroke=qhStroke.toXieStroke()
		self.dh.draw(stroke)

		qhStroke=generateStroke("橫斜彎鉤", [35, 46], [124, 166, 151, 32, 48, 50], [8, 46, 191, 212])
		stroke=qhStroke.toXieStroke()
		self.dh.draw(stroke)

if __name__ == '__main__':
	app=XieApp()
	app.test()
	app.mainloop()

