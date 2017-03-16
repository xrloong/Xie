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
		self.testQH()

	def testQH(self):
#		self.testQH_1()
#		self.testQH_2()
#		self.testQH_3()
		self.testQH_4()

	def testQH_1(self):
		from xie.graphics.stroke import generateStroke
		stroke=generateStroke("圈", [126, 40], [77, 79])
		self.dh.draw(stroke)

		stroke=generateStroke("點", [93, 91], [60, 73])
		self.dh.draw(stroke)

		stroke=generateStroke("橫", [20, 123], [202])
		self.dh.draw(stroke)

		stroke=generateStroke("豎", [121, 27], [190])
		self.dh.draw(stroke)

	def testQH_2(self):
		from xie.graphics.stroke import generateStroke
		stroke=generateStroke("提", [80, 177], [85, 53])
		self.dh.draw(stroke)

		stroke=generateStroke("捺", [145, 93], [86, 147])
		self.dh.draw(stroke)

		stroke=generateStroke("豎彎左", [145, 123], [86, 147])
		self.dh.draw(stroke)

		stroke=generateStroke("豎彎鉤", [110, 21], [185, 88, 26, 51])
		self.dh.draw(stroke)

	def testQH_3(self):
		from xie.graphics.stroke import generateStroke
		stroke=generateStroke("豎撇", [58, 26], [45, 204])
		self.dh.draw(stroke)

		stroke=generateStroke("臥捺", [10, 202], [220, 22])
		self.dh.draw(stroke)

		stroke=generateStroke("彎鉤", [124, 41], [-10, 196, 33, 19])
		self.dh.draw(stroke)

		stroke=generateStroke("橫折鉤", [95, 104], [93, 48, 120, 48, 55])
		self.dh.draw(stroke)

	def testQH_4(self):
		from xie.graphics.stroke import generateStroke
		stroke=generateStroke("斜鉤", [107, 20], [121, 227, 62])
		self.dh.draw(stroke)

		stroke=generateStroke("橫斜彎鉤", [35, 46], [124, 166, 151, 32, 48, 50])
		self.dh.draw(stroke)

if __name__ == '__main__':
	app=XieApp()
	app.test()
	app.mainloop()

