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

if __name__ == '__main__':
	app=XieApp()
	app.test()
	app.mainloop()

