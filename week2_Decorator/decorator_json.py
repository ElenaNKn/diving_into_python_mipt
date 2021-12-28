import json
import functools

def to_json(func):  # decorator

	@functools.wraps(func)   # decorated function should keep its name
	# decorated function can be with any arguments

	def wrapped(*args, **kwargs): 
		# a result of the decorated function will be converted to json
		result = json.dumps(func(*args, **kwargs))
		return result
		
	return wrapped