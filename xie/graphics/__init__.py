from .shape import Shape, Pane, Rectangle
from .stroke_info import StrokeInfo
from .drawing import DrawingSystem

from .stroke import Stroke
from .component import Component, ComponentInfo
from .character import Character
from .factory import ShapeFactory
from .segment import SegmentFactory

from .canvas import BaseTextCanvasController
from .canvas import SvgCanvasController, WxCanvasController, TrueTypeGlyphCanvasController

from .utils import TextCodec

if __name__=='__main__':
	pass

