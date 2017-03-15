class TextCodec:
	def __init__(self):
		pass

	def encodeStartPoint(self, p):
		return "0000{0[0]:02X}{0[1]:02X}".format(p)

	def encodeEndPoint(self, p):
		return "0001{0[0]:02X}{0[1]:02X}".format(p)

	def encodeControlPoint(self, p):
		return "0002{0[0]:02X}{0[1]:02X}".format(p)

	def encodeStrokeExpression(self, pointExpressionList):
		return ",".join(pointExpressionList)

	def encodeCharacterExpression(self, strokeExpressionList):
		return ";".join(strokeExpressionList)

	def isStartPoint(self, pointExpression):
		return pointExpression[3]=='0'

	def isEndPoint(self, pointExpression):
		return pointExpression[3]=='1'

	def isControlPoint(self, pointExpression):
		return pointExpression[3]=='2'

	def decodePointExpression(self, pointExpression):
		e=pointExpression
		return (int(e[4:6], 16), int(e[6:8], 16))

	def decodeStrokeExpression(self, strokeExpression):
		return strokeExpression.split(",")

	def decodeCharacterExpression(self, characterExpression):
		return characterExpression.split(";")

