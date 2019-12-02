import os, sys


from .src.main import executeMigration

class Runner():
	def __init__(self):
		pass

	def process(self, request_dict):
		print(request_dict, "***** data obtained *****")
		return executeMigration(request_dict)

	def train(self):
		pass

