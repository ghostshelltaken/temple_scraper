import sqlite3

class Database:

	def __init__(self):
		self.conn = None
		self.cursor = None

	def make_connection(self):
		self.conn = sqlite3.connect('./temples.db')
		self.cursor = self.conn.cursor()

	def close_connection(self):
		self.conn.close()

	def execute_query(self, query):
		self.cursor.execute(*query)
		self.conn.commit()

	def select_query(self, query):
		self.cursor.execute(*query)
		result = self.cursor.fetchall()
		self.conn.commit()
		return result

# a = Database()
# a.make_connection()