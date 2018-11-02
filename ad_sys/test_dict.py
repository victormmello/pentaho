def update_nested_dict(original_dict, update_dict):
	for key in update_dict:
		if key not in original_dict or not isinstance(original_dict[key], dict):
			original_dict[key] = update_dict[key]
		else:
			update_nested_dict(original_dict[key], update_dict[key])

BASE_API_ADSET = {
	"daily_budget": "2000",
	"bid_amount": 200,

	# "name": adset_name,
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
}

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


update_nested_dict(BASE_API_ADSET, DEVICE_CONFIG['All'])
print(BASE_API_ADSET)
import pdb; pdb.set_trace()


update_nested_dict(BASE_API_ADSET, AUDIENCE_CONFIG['Compradores'])
print(BASE_API_ADSET)
import pdb; pdb.set_trace()