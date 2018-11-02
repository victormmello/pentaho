import requests, json, unicodecsv, pyodbc
# import dateutil.relativedelta
from datetime import datetime

api_connection_file = open("api_connection.json", 'rb')
api_connection_config = json.load(api_connection_file)

# database_connection_file = open("database_connection.json", 'rb')
# database_connection_config = json.load(database_connection_file)

# cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s' % (
# 	database_connection_config['server'],
# 	database_connection_config['database'],
# 	database_connection_config['username'],
# 	database_connection_config['password']
# 	))
# cnxn.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
# cnxn.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
# cnxn.setencoding(encoding='utf-8')
# cursor = cnxn.cursor()

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

# url = "https://marciamello.vtexcommercestable.com.br/api/catalog_system/pub/products/search"
# params = {
# 	"O":"OrderByNameASC"
# }

# columns = [
# 	"SKU",
# 	"Ref",
# ]

# with open('skus_p1_l2.csv', 'wb') as f:
# 	csv_file = unicodecsv.DictWriter(f, fieldnames=columns, delimiter=";",encoding='latin-1')
# 	csv_file.writeheader()

# 	list_set = list()

# 	result_range = 50
# 	results_from = 1
# 	results_to = result_range
# 	response_status_code = 206

# 	c=1
# 	while response_status_code == 206:
# 		print(u"iteracao: %d" % c)
# 		c+=1
# 		params["_from"] = results_from
# 		params["_to"] = results_to
# 		response = requests.request("GET", url, headers=api_connection_config, params=params)

# 		response_status_code = response.status_code

# 		print(u"   status code: %d" % response_status_code)

# 		if response_status_code in (200,206):
# 			results_from += result_range
# 			results_to += result_range

# 			json_response = json.loads(response.text)
			
# 			for item in json_response:
# 				row = {
# 					"SKU":item["Id"],
# 					"Ref":item["RefId"],
# 				}

# 				list_set.append(row)
# 	# print(list_set)
# 	csv_file.writerows(list_set)








columns = [
	"SKU",
	"Ref",
]

ref_ids = [
	'32.03.0345',
'22.04.0214',
'22.04.0214',
'35.09.0565',
'23.11.0244',
'23.11.0244',
'22.12.0516',
'23.11.0244',
'35.09.1039',
'22.04.0214',
'22.12.0535',
'35.01.0774',
'23.11.0244',
'23.11.0244',
'23.11.0244',
'23.08.0196',
'22.04.0214',
'32.02.0245',
'32.02.0245',
'22.12.0516',
'23.11.0244',
'22.12.0541',
'22.04.0214',
'34.05.0031',
'22.11.0211',
'31.02.0093',
'23.11.0254',
'23.09.0074',
'34.05.0031',
'34.05.0031',
'34.05.0031',
'35.01.0765',
'35.09.0565',
'34.05.0031',
'34.05.0031',
'34.05.0031',
'35.09.1039',
'35.01.0764',
'32.02.0245',
'22.11.0211',
'23.08.0196',
'22.12.0521',
'35.01.0782',
'23.11.0244',
'23.11.0254',
'23.11.0254',
'32.03.0345',
'34.05.0031',
'22.06.0457',
'22.12.0516',
'22.12.0516',
'22.11.0211',
'22.04.0214',
'22.12.0541',
'23.03.0028',
'33.02.0198',

]

base_url = 'http://marciamello.vtexcommercestable.com.br/api/catalog_system/pvt/products/productgetbyrefid/%s'

errors = []

with open('skus_p1_l2.csv', 'wb') as f:
	csv_file = unicodecsv.DictWriter(f, fieldnames=columns, delimiter=";",encoding='latin-1')
	csv_file.writeheader()

	list_set = list()

	for ref_id in ref_ids:
		try:
			url = base_url % ref_id

			response = requests.request("GET", url, headers=api_connection_config)
			json_response = json.loads(response.text)

			if not json_response:
				# import pdb; pdb.set_trace()
				errors.append('no response :"%s"' % ref_id)
				continue

			url = 'http://marciamello.vtexcommercestable.com.br/api/catalog_system/pvt/sku/stockkeepingunitByProductId/%s' % json_response["Id"]
			response = requests.request("GET", url, headers=api_connection_config)
			json_response = json.loads(response.text)
			json_response = [json_response[0]]

			for x in json_response:
				row = {
					"SKU": x['Id'],
					"Ref": ref_id,
				}
				print(row)

				list_set.append(row)
		except Exception as e:
			errors.append('exception :"%s"' % str(e))

	csv_file.writerows(list_set)

print(errors)