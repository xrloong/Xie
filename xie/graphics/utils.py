class TextCodec:
	def __init__(self):
		pass

	def encodeStartPoint(self, p):
		return "0{0[0]:02X}{0[1]:02X}".format(p)

	def encodeEndPoint(self, p):
		return "1{0[0]:02X}{0[1]:02X}".format(p)

	def encodeControlPoint(self, p):
		return "2{0[0]:02X}{0[1]:02X}".format(p)

	def encodeStrokeExpression(self, pointExpressionList):
		return ",".join(pointExpressionList)

	def encodeCharacterExpression(self, strokeExpressionList):
		return ";".join(strokeExpressionList)

	def isStartPoint(self, pointExpression):
		return pointExpression[0]=='0'

	def isEndPoint(self, pointExpression):
		return pointExpression[0]=='1'

	def isControlPoint(self, pointExpression):
		return pointExpression[0]=='2'

	def decodePointExpression(self, pointExpression):
		e=pointExpression
		return (int(e[1:3], 16), int(e[3:5], 16))

	def decodeStrokeExpression(self, strokeExpression):
		return strokeExpression.split(",")

	def decodeCharacterExpression(self, characterExpression):
		return characterExpression.split(";")

