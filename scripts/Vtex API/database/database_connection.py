import json
import pyodbc

# Create a function called "chunks" with two arguments, l and n:
def chunks(l, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(l), n):
        # Create an index range for l of n items:
        yield l[i:i+n]

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

	def select(self, query, trim=False):
		self.cursor.execute(query)
		columns = [column[0] for column in self.cursor.description]
		results = self.cursor.fetchall()

		result_dicts = []
		for result in results:
			result_dict = {}

			for i, value in enumerate(result):
				if trim and isinstance(value, str):
					value = value.strip()

				result_dict[columns[i]] = value

			result_dicts.append(result_dict)

		return result_dicts
	
	def execute(self,query):
		self.cursor.execute(query)
		self.cnxn.commit()

	def sanitize(self,s):
		return str(s).replace("'","''")

	def insert(self,table,values):
		
		for query_values_list in chunks(values,999):
			insert_list = []
			for value in query_values_list:
				query_row = '(%s)' % ','.join('\'%s\'' % self.sanitize(cell) for cell in value)
				insert_list.append(query_row)
			query = """INSERT INTO %s VALUES
			%s
			""" % (table,'\n,'.join(insert_list))
			# print(query)
			self.execute(query)

			