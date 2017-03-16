class TextCodec:
	STROKE_SEPERATOR = "/"
	POINT_SEPERATOR = ","
	PARAMETER_SEPERATOR = "."

	START_POINT_PATTERN="0" + PARAMETER_SEPERATOR + "{0[0]}" + PARAMETER_SEPERATOR + "{0[1]}"
	END_POINT_PATTERN="1" + PARAMETER_SEPERATOR + "{0[0]}" + PARAMETER_SEPERATOR + "{0[1]}"
	CONTROL_POINT_PATTERN="2" + PARAMETER_SEPERATOR + "{0[0]}" + PARAMETER_SEPERATOR + "{0[1]}"

	def __init__(self):
		pass

	def encodeStartPoint(self, p):
		return TextCodec.START_POINT_PATTERN.format(p)

	def encodeEndPoint(self, p):
		return TextCodec.END_POINT_PATTERN.format(p)

	def encodeControlPoint(self, p):
		return TextCodec.CONTROL_POINT_PATTERN.format(p)

	def encodeStrokeExpression(self, pointExpressionList):
		return TextCodec.POINT_SEPERATOR.join(pointExpressionList)

	def encodeCharacterExpression(self, strokeExpressionList):
		return TextCodec.STROKE_SEPERATOR.join(strokeExpressionList)

	def isStartPoint(self, pointExpression):
		return pointExpression[0]=='0'

	def isEndPoint(self, pointExpression):
		return pointExpression[0]=='1'

	def isControlPoint(self, pointExpression):
		return pointExpression[0]=='2'

	def decodePointExpression(self, pointExpression):
		param=pointExpression.split(TextCodec.PARAMETER_SEPERATOR)
		return (int(param[1]), int(param[2]))

	def decodeStrokeExpression(self, strokeExpression):
		return strokeExpression.split(TextCodec.POINT_SEPERATOR)

	def decodeCharacterExpression(self, characterExpression):
		return characterExpression.split(TextCodec.STROKE_SEPERATOR)

