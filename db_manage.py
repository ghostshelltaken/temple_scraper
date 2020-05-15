import sqlite3

class Database:

	def __init__(self):
		self.conn = None
		self.cursor = None

	def make_connection(self):
		self.conn = sqlite3.connect('temples.db')
		self.cursor = self.conn.cursor()

	def close_connection():
		self.conn.close()

	def execute_query(self, query):
		self.cursor.execute(*query)
		self.conn.commit()