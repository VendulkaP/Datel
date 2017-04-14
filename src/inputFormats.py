import dataFormats

class InputSource():
	def executeQuery(query):
		# TODO throw unsupported op exception
		pass

class OracleDbInputSource(InputSource):
	def __init__(t, url, port, dbName, userName, passw):
		# TODO construct connection object
		t.connectionObject = None
	def executeQuery(t, query):
		# TODO connect to database
		# TODO return query results in the standard format
		df = dataFormats.tabularData([])
		return df
	def close(t):
		# TODO close connection object
		# TODO implement autoclosable interface
		pass
