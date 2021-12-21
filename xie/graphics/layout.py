from enum import Enum

class JointOperator(Enum):
	Silkworm = '蚕'
	Goose = '鴻'

class LayoutSpec:
	def __init__(self, operator, weights = [int]):
		self.operator = operator
		self.weights = weights

