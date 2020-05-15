import sqlite3

class Database:

	def __init__(self):
		self.conn = None
		self.cursor = None
