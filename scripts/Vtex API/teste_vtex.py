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

# columns = [
# 	"productId",
# 	"productReference",
# 	"link",
# 	"itemId",
# 	"imageUrl",
# ]

product_categories = []
product_info = []
product_images = []
product_items = []

with open('catalog_output.csv', 'wb') as f:
	# csv_file = unicodecsv.DictWriter(f,fieldnames=columns, delimiter=";",encoding='latin-1')
	# csv_file.writeheader()

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
			
			for product in json_response:
				product_id = product["productId"]
				produto = product["productReference"]

				original_price = 0
				sale_price = 0
				for item in product["items"]:
					item_original_price = item["sellers"][0]["commertialOffer"]["ListPrice"]
					item_sale_price = item["sellers"][0]["commertialOffer"]["Price"]
					original_price = max(original_price,item_original_price)
					sale_price = max(sale_price,item_sale_price)

					product_items.append({
						"item_id":item["itemId"],
						"ean":item["ean"],
						"image_url":item["images"][0]["imageUrl"]
					})

				product_info.append({
					"product_id":product_id,
					"produto":produto,
					"link":product["link"],
					"category_id":product["categoryId"],
					"category_name":product["categories"][0],
					"original_price":original_price,
					"sale_price":sale_price
				})

				# Product Categories:
				for i in range(0,len(product["categories"])):
					product_categories.append({
						"product_id":product_id,
						"produto":produto,
						"category_id":product["categoriesIds"][i],
						"category_name":product["categories"][i]
					})

				print(product_items)
				print(product_info)
				print(product_categories)
				raise Exception

				
	# print(list_set)
	# csv_file.writerows(list_set)