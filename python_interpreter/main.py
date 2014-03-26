# http://jayconrod.com/posts/37/a-simple-interpreter-from-scratch-in-python-part-1

import re
import sys

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
					if tag:
						token = (match.group(0), tag)
						tokens.append(token)
					break;

			if not match:
				# Error, the current character don't match anything
				sys.stderr.write("Illegal character: '%s', position: %d \n" % (self.text[position], position))
				sys.exit(1)
			else:
				# move toward the end of the match (consume)
				position = match.end(0)
				
		return tokens

text = """
# This is a comment
function hello(priority, message) {
	console.log(1.2, 2,  message);
}
"""

tokens = [
	(r"\s+", None), # whitespace (\t, \n, \r, \f, \v)
	(r"#[^\\\n]*", "COMMENT"), # single line comments
	(r"function", "RESEVED"),
	(r"\(", "RESEVED"),
	(r"\)", "RESEVED"),
	(r"\{", "RESEVED"),	
	(r"\}", "RESEVED"),
	(r";", "RESEVED"),
	(r",", "RESERVED"),
	(r"\.", "DOT"),
	(r"\d+\.\d+", "FLOAT"), # float
	(r"\d+", "INT"), # int
	(r"\w+", "STRING") # general string
]

lexer = Lexer(text)
tokens = lexer.process(tokens)

for token in tokens:
	print token