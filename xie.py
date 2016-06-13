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
		frame.draw(self.dh)

		targetRect = Rectangle(0, 0, 512, 512)

	def mainloop(self):
		self.root.mainloop()

if __name__ == '__main__':
	app=XieApp()
	app.mainloop()

