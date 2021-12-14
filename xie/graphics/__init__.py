from .shape import Pane, Rectangle
from .drawing import DrawingSystem

from .stroke import Stroke
from .component import Component
from .character import Character

from .segment import SegmentFactory
from .factory import ShapeFactory
from .factory import StrokeFactory

from .canvas import BaseTextCanvasController
from .canvas import SvgCanvasController, WxCanvasController, TrueTypeGlyphCanvasController

from .utils import TextCodec

from .shape import genVerticalPanes, genHorizontalPanes

if __name__=='__main__':
	pass

