from enum import Enum

class JointOperator(Enum):
	Silkworm = '蚕'
	Goose = '鴻'
	Loop = '回'

	Qi = '起'
	Zhe = '這'
	Liao = '廖'
	Zai = '載'
	Dou = '斗'

	Tong = '同'
	Han = '函'
	Qu = '區'
	Left = '左'

	Mu = '畞'
	Zuo = '㘴'
	You = '幽'
	Liang = '㒳'
	Jia = '夾'

class LayoutSpec:
	def __init__(self, operator, weights = [int],
			containerPane = None, subPanes = []):
		self.operator = operator
		self.weights = weights

		self.containerPane = containerPane
		self.subPanes = subPanes

