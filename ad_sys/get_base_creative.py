from fb_config import APP_ID
from fb_config import APP_SECRET
from fb_config import ACCESS_TOKEN
from fb_config import FB_ACCOUND_ID

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business import adobjects
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.ad import Ad

import datetime

FacebookAdsApi.init(APP_ID, APP_SECRET, ACCESS_TOKEN)
my_account = AdAccount(FB_ACCOUND_ID)

def get_by_name(objs, searched_name, match='full'):
	return get_by_attr(objs, searched_name, 'name', match=match)

def get_by_attr(objs, searched_name, attr, match='full'):
	for obj in objs:
		try:
			obj[attr]
		except Exception as e:
			obj.remote_read(fields=[attr])
			try:
				obj[attr]
			except Exception as e:
				continue

		is_match = False
		if match == 'full':
			is_match = obj[attr] == searched_name
		elif match == 'start':
			is_match = obj[attr].startswith(searched_name)
			# print(obj['name'] + '\n' + searched_name)
			# print('\n')

		if is_match:
			return obj

campaigns = my_account.get_campaigns(fields=['name'])
campaign = get_by_name(campaigns, 'MarciaMello-13092018')

ad_creatives = my_account.get_ad_creatives(fields=['title'])
ad_creative = get_by_attr(ad_creatives, 'Até 70% + Cupom 15% OFF', 'title', match='start')

if not ad_creative:
	raise Exception('creative not found')

print(ad_creative)

BASE_API_ADSET = {
	"daily_budget": "2100",
	"bid_amount": 200,

	# "name": adset_name,
	"start_time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
	"targeting": {
		"facebook_positions": [
			"feed"
		],
		"instagram_positions": [
			"stream",
			# "story"
		],
		"age_max": 65,
		"age_min": 25,
		"genders": [
			2
		],
		"publisher_platforms": [
			"facebook",
			"instagram"
		],
		"targeting_optimization": "expansion_all"
	},

	'campaign_id': campaign['id'],
	"attribution_spec": [
		{
			"event_type": "CLICK_THROUGH",
			"window_days": 7
		},
		{
			"event_type": "VIEW_THROUGH",
			"window_days": 1
		}
	],
	"bid_strategy": "LOWEST_COST_WITH_BID_CAP",
	"billing_event": "IMPRESSIONS",
	"configured_status": "PAUSED",
	"status": "PAUSED",
	"destination_type": "UNDEFINED",
	"effective_status": "PAUSED",
	"is_dynamic_creative": False,
	"lifetime_budget": "0",
	"lifetime_imps": 0,
	"optimization_goal": "OFFSITE_CONVERSIONS",
	"pacing_type": [
	  "standard"
	],
	"promoted_object": {
		"custom_event_type": "ADD_TO_CART",
		"pixel_id": "1908760826085113"
	},
	"recurring_budget_semantics": True,
	"use_new_app_click": False
}

# ADSET_NAME_TEMPLATE = '%(campaign)s_%(device)s_%(audience)s_%(platform)s_%(position)s_%(single_or_carousel)s_%(promo_type)s_%(category)s_%(brand)s'
ADSET_NAME_TEMPLATE = '%(campaign)s_%(device)s_%(audience)s_%(platform)s_%(position)s_%(single_or_carousel)s_%(promo_type)s'

DEVICE_CONFIG = {
	'Desktop': {
		'targeting': {"device_platforms": ["desktop"]},
	},
	'Mobile': {
		'targeting': {"device_platforms": ["mobile"]},
	},
	'All': {
		'targeting': {"device_platforms": ["desktop", "mobile"]},
	},
}

AUDIENCE_CONFIG = {
	'Compradores': {
		"targeting": {
			"custom_audiences": [
				{
					"id": "23843051904060085",
					"name": "Emails-Set2017-Set2018-compradores"
				}
			],
			"geo_locations": {
				"countries": [
					"BR"
				],
				"location_types": [
					"home",
					"recent"
				]
			},
		}
	},
	'LookAlikeCompradores1Perc': {
		"targeting": {
			"custom_audiences": [
				{
					"id": "23843112110960085",
					"name": "Lookalike (BR, 1%) - Emails-Set2017-Set2018-compradores"
				}
			],
			"geo_locations": {
				"countries": [
					"BR"
				],
				"location_types": [
					"home",
					"recent"
				]
			},
		}
	},
	'CidadesComMM': {
		"targeting": {
			"geo_locations": {
	            "cities": [
	                {
	                    "country": "BR",
	                    "distance_unit": "kilometer",
	                    "key": "247071",
	                    "name": "Campinas",
	                    "radius": 40,
	                    "region": "S\u00e3o Paulo (state)",
	                    "region_id": "460"
	                },
	                {
	                    "country": "BR",
	                    "distance_unit": "kilometer",
	                    "key": "257242",
	                    "name": "Jundia\u00ed",
	                    "radius": 40,
	                    "region": "S\u00e3o Paulo (state)",
	                    "region_id": "460"
	                },
	                {
	                    "country": "BR",
	                    "distance_unit": "kilometer",
	                    "key": "264046",
	                    "name": "Piracicaba",
	                    "radius": 40,
	                    "region": "S\u00e3o Paulo (state)",
	                    "region_id": "460"
	                },
	                {
	                    "country": "BR",
	                    "distance_unit": "kilometer",
	                    "key": "266876",
	                    "name": "Ribeir\u00e3o Pr\u00eato",
	                    "radius": 40,
	                    "region": "S\u00e3o Paulo (state)",
	                    "region_id": "460"
	                }
	            ],
	            "location_types": [
	                "home",
	                "recent"
	            ]
	        },
		}
    },
}

def update_nested_dict(original_dict, update_dict):
	for key in update_dict:
		if key not in original_dict or not isinstance(original_dict[key], dict):
			original_dict[key] = update_dict[key]
		else:
			update_nested_dict(original_dict[key], update_dict[key])


for audience in AUDIENCE_CONFIG: 
	adset_name_params = {
		'campaign': '15OffAcima200',
		'device': 'All',
		'audience': audience,
		'platform': 'All',
		'position': 'Feed',
		'single_or_carousel': 'Single',
		'promo_type': 'XOff',
		# 'category': 'NONE',
		# 'brand': 'NONE',
	}

	adset_name = ADSET_NAME_TEMPLATE % adset_name_params

	import copy
	api_adset = copy.deepcopy(BASE_API_ADSET)

	api_adset['name'] = adset_name

	update_nested_dict(api_adset, DEVICE_CONFIG[adset_name_params['device']])
	update_nested_dict(api_adset, AUDIENCE_CONFIG[adset_name_params['audience']])

	# print(api_adset)
	new_ad_set = my_account.create_ad_set(params=api_adset)

	# === sei lah pq o comentado nao funciona, mas o outro funciona
	# api_ad = {
	# 	'name': adset_name,
	# 	'adset': new_ad_set,
	# 	'creative': ad_creative,
	# 	'status': 'PAUSED',
	# }
	# try:
	# 	new_ad_set.create_ad(params=api_ad)
	# except Exception as e:
	# 	import pdb; pdb.set_trace()
	# 	raise e

	ad = Ad(parent_id=FB_ACCOUND_ID)
	ad[Ad.Field.name] = adset_name
	ad[Ad.Field.adset_id] = new_ad_set['id']
	ad[Ad.Field.creative] = {
		'creative_id': ad_creative['id'],
	}
	ad.remote_create(params={
		'status': Ad.Status.paused,
	})


	# new_adset_params = {
	# 	"daily_budget": "2000",
	# 	"bid_amount": 200,

	# 	"name": adset_name,
	# 	"start_time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
	# 	"targeting": {
	# 		"custom_audiences": [
	# 			{
	# 				"id": "23843051904060085",
	# 				"name": "Emails-Set2017-Set2018-compradores"
	# 			}
	# 		],
	# 		"geo_locations": {
	# 			"countries": [
	# 				"BR"
	# 			],
	# 			"location_types": [
	# 				"home",
	# 				"recent"
	# 			]
	# 		},
	# 		"device_platforms": [
	# 			"mobile",
	# 			"desktop"
	# 		],



	# 		"facebook_positions": [
	# 			"feed"
	# 		],
	# 		"instagram_positions": [
	# 			"stream",
	# 			# "story"
	# 		],
	# 		"age_max": 65,
	# 		"age_min": 25,
	# 		"genders": [
	# 			2
	# 		],
	# 		"publisher_platforms": [
	# 			"facebook",
	# 			"instagram"
	# 		],
	# 		"targeting_optimization": "expansion_all"
	# 	},

	# 	'campaign_id': campaign['id'],
	# 	"attribution_spec": [
	# 		{
	# 			"event_type": "CLICK_THROUGH",
	# 			"window_days": 7
	# 		},
	# 		{
	# 			"event_type": "VIEW_THROUGH",
	# 			"window_days": 1
	# 		}
	# 	],
	# 	"bid_strategy": "LOWEST_COST_WITH_BID_CAP",
	# 	"billing_event": "IMPRESSIONS",
	# 	"configured_status": "PAUSED",
	# 	"status": "PAUSED",
	# 	"destination_type": "UNDEFINED",
	# 	"effective_status": "PAUSED",
	# 	"is_dynamic_creative": False,
	# 	"lifetime_budget": "0",
	# 	"lifetime_imps": 0,
	# 	"optimization_goal": "OFFSITE_CONVERSIONS",
	# 	"pacing_type": [
	# 	  "standard"
	# 	],
	# 	"promoted_object": {
	# 		"custom_event_type": "ADD_TO_CART",
	# 		"pixel_id": "1908760826085113"
	# 	},
	# 	"recurring_budget_semantics": True,
	# 	"use_new_app_click": False
	# }
