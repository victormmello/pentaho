# https://developers.facebook.com/tools/explorer?method=GET&path=me%3Ffields%3Did%2Cname&version=v3.2

from fb_config import APP_ID
from fb_config import APP_SECRET
from fb_config import ACCESS_TOKEN
from fb_config import FB_ACCOUND_ID

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business import adobjects
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet


FacebookAdsApi.init(APP_ID, APP_SECRET, ACCESS_TOKEN)
my_account = AdAccount(FB_ACCOUND_ID)
campaigns = my_account.get_campaigns()
campaign = campaigns[1].remote_read(fields=['objective', 'name'])
print('connect test OK!')

ad_sets = campaign.get_ad_sets()
ad_set = campaign.get_ad_sets()[0]

# === READ ADSET ===
# ad_set_all_fields = [
# 	'account_id',
# 	'adlabels',
# 	'adset_schedule',
# 	'attribution_spec',
# 	'bid_amount',
# 	'bid_info',
# 	'bid_strategy',
# 	'billing_event',
# 	'budget_remaining',
# 	'campaign',
# 	'campaign_id',
# 	'configured_status',
# 	'created_time',
# 	'creative_sequence',
# 	'daily_budget',
# 	'daily_min_spend_target',
# 	'daily_spend_cap',
# 	'destination_type',
# 	'effective_status',
# 	'end_time',
# 	'frequency_control_specs',
# 	'instagram_actor_id',
# 	'is_dynamic_creative',
# 	'issues_info',
# 	'lifetime_budget',
# 	'lifetime_imps',
# 	'lifetime_min_spend_target',
# 	'lifetime_spend_cap',
# 	'name',
# 	'optimization_goal',
# 	'pacing_type',
# 	'promoted_object',
# 	'recommendations',
# 	'recurring_budget_semantics',
# 	'rf_prediction_id',
# 	'source_adset',
# 	'source_adset_id',
# 	'start_time',
# 	'status',
# 	'targeting',
# 	'time_based_ad_rotation_id_blocks',
# 	'time_based_ad_rotation_intervals',
# 	'updated_time',
# 	'use_new_app_click',
# ]
# yay = ad_set.remote_read(fields=ad_set_all_fields)
# print(yay)

# === CREATE CAMPAIGN ===
# campaign = adobjects.campaign.Campaign(parent_id = my_account.get_id_assured())
# campaign[adobjects.campaign.Campaign.Field.name] = "Potato Campain" # sic
# campaign[adobjects.campaign.Campaign.Field.configured_status] = adobjects.campaign.Campaign.Status.paused
# campaign['objective'] = 'CONVERSIONS'
# campaign.remote_create()

# campaign = Campaign(fbid='23843117418580085')
# print(campaign.remote_read(fields=['name']))

# === CREATE ADSET ===
# new_adset_params = {
# 	'name': 'A CPA Ad Set',
# 	# "name": "DeuaLouca_lookAlike_Conversao_Imagem_Facebook",
# 	'campaign_id': campaign['id'],

#   	"account_id": "1205933616131610",
# 	"attribution_spec": [
# 	  {
# 	      "event_type": "CLICK_THROUGH",
# 	      "window_days": 7
# 	  },
# 	  {
# 	      "event_type": "VIEW_THROUGH",
# 	      "window_days": 1
# 	  }
# 	],
# 	"bid_amount": 650,
# 	"bid_strategy": "LOWEST_COST_WITH_BID_CAP",
# 	"billing_event": "IMPRESSIONS",
# 	"campaign_id": "23843052046520085",
# 	"configured_status": "PAUSED",
# 	"daily_budget": "4000",
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
# 	  "custom_event_type": "ADD_TO_CART",
# 	  "pixel_id": "1908760826085113"
# 	},
# 	"recurring_budget_semantics": True,
# 	"start_time": "2018-09-13T13:17:50-0700",
# 	"status": "PAUSED",
# 	"targeting": {
# 	  "age_max": 65,
# 	  "age_min": 25,
# 	  "custom_audiences": [
# 	      {
# 	          "id": "23843051904060085",
# 	          "name": "Emails-Set2017-Set2018-compradores"
# 	      }
# 	  ],
# 	  "device_platforms": [
# 	      "mobile",
# 	      "desktop"
# 	  ],
# 	  "facebook_positions": [
# 	      "feed"
# 	  ],
# 	  "genders": [
# 	      2
# 	  ],
# 	  "geo_locations": {
# 	      "countries": [
# 	          "BR"
# 	      ],
# 	      "location_types": [
# 	          "home",
# 	          "recent"
# 	      ]
# 	  },
# 	  "instagram_positions": [
# 	      "stream",
# 	      "story"
# 	  ],
# 	  "publisher_platforms": [
# 	      "facebook",
# 	      "instagram"
# 	  ],
# 	  "targeting_optimization": "expansion_all"
# 	},
# 	"use_new_app_click": False
# }
# new_ad_set = my_account.create_ad_set(params=new_adset_params)

# print(new_ad_set)

# === READ CREATIVE ===
# ad_creative_all_fields = [
# 	'account_id',
# 	'actor_id',
# 	'adlabels',
# 	'applink_treatment',
# 	'asset_feed_spec',
# 	'body',
# 	'branded_content_sponsor_page_id',
# 	'call_to_action_type',
# 	'effective_instagram_story_id',
# 	'effective_object_story_id',
# 	'image_crops',
# 	'image_hash',
# 	'image_url',
# 	'instagram_actor_id',
# 	'instagram_permalink_url',
# 	'instagram_story_id',
# 	'link_og_id',
# 	'link_url',
# 	'messenger_sponsored_message',
# 	'name',
# 	'object_id',
# 	'object_story_id',
# 	'object_story_spec',
# 	'object_type',
# 	'object_url',
# 	'platform_customizations',
# 	'product_set_id',
# 	'recommender_settings',
# 	'status',
# 	'template_url',
# 	'template_url_spec',
# 	'thumbnail_url',
# 	'title',
# 	'url_tags',
# 	'use_page_actor_override',
# 	'video_id',
# ]

# ad_creatives = ad_set.get_ad_creatives()
# ad_creative = ad_creatives[0].remote_read(fields=ad_creative_all_fields)

# print(ad_creative)

# === CREATE AD CREATIVE ===
new_ad_creative_params = {
	"body": "teste body",
	"name": "teste name",

	"call_to_action_type": "SHOP_NOW",
	# "effective_instagram_story_id": "1798787056904659",
	"effective_object_story_id": "128223323902650_2014473898610907",
	# "instagram_actor_id": "516353265072236",
	# "instagram_permalink_url": "https://www.instagram.com/p/BnzwZP5jnkg/",
	"object_story_spec": {
	    # "instagram_actor_id": "516353265072236",
	    "link_data": {
	        "attachment_style": "link",
	        "call_to_action": {
	            "type": "SHOP_NOW",
	            "value": {
	                "link": "https://www.marciamello.com.br/roupas?PS=33&O=OrderByTopSaleDESC&utm_medium=social&utm_source=facebook&utm_campaign=DeuaLouca_LookAlike_Conversao_Imagem_Facebook"
	            }
	        },
	        "description": "teste description",
	        "image_hash": "71616e724c458fa2a991bb17231a82a7",
	        "link": "https://www.marciamello.com.br/roupas?PS=33&O=OrderByTopSaleDESC&utm_medium=social&utm_source=facebook&utm_campaign=DeuaLouca_LookAlike_Conversao_Imagem_Facebook",
	        "message": "teste message",
	        "name": "teste name dentro object story spec"
	    },
	    "page_id": "128223323902650"
	},
	"object_type": "SHARE",
	"status": "PAUSED",
	"thumbnail_url": "https://external.xx.fbcdn.net/safe_image.php?d=AQDY3WMWmN4HTSIV&w=64&h=64&url=https%3A%2F%2Fwww.facebook.com%2Fads%2Fimage%2F%3Fd%3DAQKxaAWGCSBL1bz82d9Tn4jbVm8POBNfNrqIyll2kMKKbGotjhC7z-_BZi75AQd8D7BzTL_p2eXUk46grbRX4UFMS3eE0vKhqMocP6qBVcH_FT0jugaKpUbs0v5fwdA3kZ0b8AwPlYj-htGN0Qp68rIG&cfs=1&_nc_hash=AQCK5bNt6ClO4LVm",
	"title": "teste title",
	"use_page_actor_override": False
}

new_ad_creative_params = {
	'name': 'Sample Creative',
	'object_story_spec': {
		'page_id':'128223323902650',
		'link_data': {
			'image_hash':'71616e724c458fa2a991bb17231a82a7',
			'link':'https://www.marciamello.com.br/roupas?PS=33&O=OrderByTopSaleDESC&utm_medium=social&utm_source=facebook&utm_campaign=DeuaLouca_LookAlike_Conversao_Imagem_Facebook',
			'message':'try it out'
		}
	},
}

my_account.create_ad_creative(params=new_ad_creative_params)

import pdb; pdb.set_trace()
