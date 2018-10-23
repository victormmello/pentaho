import json
import pyodbc

class DatabaseConnection(object):
	def __init__(self):
		database_connection_file = open("database\database_connection.json", 'rb')
		database_connection_config = json.load(database_connection_file)

		self.cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s' % (
			database_connection_config['server'],
			database_connection_config['database'],
			database_connection_config['username'],
			database_connection_config['password']
			))
		self.cnxn.setdecoding(pyodbc.SQL_CHAR, encoding='latin1')
		self.cnxn.setdecoding(pyodbc.SQL_WCHAR, encoding='latin1')
		self.cnxn.setencoding(encoding='latin1')
		self.cursor = self.cnxn.cursor()

	def select(self,query):
		self.cursor.execute(query)
		return self.cursor.fetchall()
	def execute(self,query):
		self.cursor.execute(query)
		self.cnxn.commit()