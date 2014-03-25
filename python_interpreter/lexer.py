# http://jayconrod.com/posts/37/a-simple-interpreter-from-scratch-in-python-part-1

import re

class Lexer:
	def __init__(self, text):
		self.text = text

	def process(self, expressions):
		position = 0
		tokens = []
		while position < len(self.text):
			for expression in expressions:
				pattern, tag = expression
				regex = re.compile(pattern)
				match = regex.match(self.text, position)
				if match:
					token = (match.group(0), tag)
					tokens.append(token)
					position = match.end(0) # move toward the end of the match (consume)

			if not match:
				position += 1
				

		return tokens


text = """
function hello(message) {
	console.log(12);
	console.log(message);
}
"""

lexer = Lexer(text)

tokens = lexer.process([
	(r"[ \\n\\t]+", None),
	(r"#[^\\n]*", None),

	(r"function", "FUNCTION"),
	(r"\(", "OPEN_PARENTHESIS"),
	(r"\)", "CLOSE_PARENTHESIS"),
	(r"\{", "OPEN_BRACKET"),
	(r"\}", "CLOSE_BRACKET"),
	(r"\.", "DOT"),
	(r";", "END_LINE"),
	(r"\d+", "INT"),
	(r"[A-Za-z]+", "STRING")
])

for token in tokens:
	print token[0], token[1]