import requests, json, dateutil.relativedelta, unicodecsv, pyodbc
from datetime import datetime

api_connection_file = open("api_connection.json", 'rb')
api_connection_config = json.load(api_connection_file)

database_connection_file = open("database_connection.json", 'rb')
database_connection_config = json.load(database_connection_file)

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s' % (
	database_connection_config['server'],
	database_connection_config['database'],
	database_connection_config['username'],
	database_connection_config['password']
	))
cnxn.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
cnxn.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
cnxn.setencoding(encoding='utf-8')
cursor = cnxn.cursor()

# cursor.execute("DROP TABLE #bi_disponivel_vtex_temp;")
# cnxn.commit()


# row = cursor.fetchone()
# while row:
#     print(row[0])
#     row = cursor.fetchone()

# API DOCS > consultar https://documenter.getpostman.com/view/845/vtex-catalog-api/Hs44

# consulta SKU:
# sku_id = "570897"
# url = "https://marciamello.vtexcommercestable.com.br/api/catalog_system/pvt/sku/stockkeepingunitbyid/%s" % sku_id
# url = "https://marciamello.vtexcommercestable.com.br/api/catalog_system/pvt/products/GetProductAndSkuIds"
# params = {
# 	"categoryId":"1",
# 	"_from":"1",
# 	"_to":"10"
# }

# lista de marcas:
# url = "https://marciamello.vtexcommercestable.com.br/api/catalog_system/pvt/brand/list"

# consulta pedido:
# url = "https://marciamello.vtexcommercestable.com.br/api/oms/pvt/orders/?f_invoicedDate=invoicedDate:[%sT00:00:00.000Z TO %sT00:00:00.000Z]" % (
# 	datetime.strftime(datetime.now().replace(day=1) + dateutil.relativedelta.relativedelta(months=-1),'%Y-%m-%d'),
# 	datetime.strftime(datetime.now().replace(day=1),'%Y-%m-%d'),
# )
# url = "https://marciamello.vtexcommercestable.com.br/api/oms/pvt/orders/?f_invoicedDate=invoicedDate:[2018-09-15T00:00:00.000Z TO 2018-09-19T00:00:00.000Z]"

# url = "https://marciamello.vtexcommercestable.com.br/api/catalog_system/pub/category/tree/1/"

url = "https://marciamello.vtexcommercestable.com.br/api/catalog_system/pub/products/search"
params = {
	"O":"OrderByNameASC"
}

columns = [
	"productId",
	"productReference",
	"link",
	"itemId",
	"imageUrl",
]

with open('catalog_output.csv', 'wb') as f:
	csv_file = unicodecsv.DictWriter(f,fieldnames=columns, delimiter=";",encoding='latin-1')
	csv_file.writeheader()

	list_set = list()

	result_range = 50
	results_from = 1
	results_to = result_range
	response_status_code = 206

	c=1
	while response_status_code == 206:
		print(u"iteração: %d" % c)
		c+=1
		params["_from"] = results_from
		params["_to"] = results_to
		response = requests.request("GET", url, headers=api_connection_config, params=params)

		response_status_code = response.status_code

		print(u"   status code: %d" % response_status_code)

		if response_status_code in (200,206):
			results_from += result_range
			results_to += result_range

			json_response = json.loads(response.text)
			
			for item in json_response:
				row = {
					"productId":item["productId"],
					"productReference":item["productReference"],
					"link":item["link"],
					"itemId":item["items"][0]["itemId"],
					"imageUrl":item["items"][0]["images"][0]["imageUrl"],
				}
				list_set.append(row)
	# print(list_set)
	csv_file.writerows(list_set)