# coding: utf-8
 
"""definition: 一个观测序列代表一个事件。一个事件由不定长的多个senz组成
本次伪造的数据集均采用长度为10的senz作为观测序列"""

import random
import json

__all__ = ['generate_studying_senz_list', 'generate_working_senz_list', 'generate_shopping_senz_list', 'generate_dining_senz_list']

motion_type = ("sitting", "walking", "running", "riding", "driving")

# sound_level1_type  = ("quiet", "lowish", "noisy")

sound_type = (
    "keyboard", "bird", "tree", "car_crash", "music", "turning_page", "gun", "talking", "quarrel", "mouse_click",
    "writing", "car_whistle", "school_bell", "wind", "car_driving_by", "stair", "tableware", "laugh", "others",
    "scream", "subway", "boom", "flowing", "speech", "step", "sea", "car_brakes"
)

location_type = ("dining", "shopping", "life_service", "entertainment", "auto_related", "healthcare", "hotel", "scenic_spot", "exhibition", "education", "finance", "infrastructure", "estate")

'''
location_type = (
    "hospital", "bath_sauna", "drugstore", "vegetarian_diet", "talent_market", "business_building",
    "comprehensive_market", "motel", "stationer", "high_school", "insurance_company", "home", "resort",
    "digital_store", "cigarette_store", "pawnshop", "auto_sale", "japan_korea_restaurant", "toll_station",
    "salvage_station", "newstand", "western_restaurant", "car_maintenance", "scenic_spot", "barbershop",
    "chafing_dish", "buffet", "convenience_store", "odeum", "pet_service", "traffic", "cinema", "coffee",
    "auto_repair", "bar", "hostel", "video_store", "others", "game_room", "laundry", "photographic_studio", "ktv",
    "exhibition_hall", "bank", "night_club", "bike_store", "furniture_store", "travel_agency", "technical_school",
    "welfare_house", "intermediary", "security_company", "gift_store", "muslim", "lottery_station",
    "photography_store", "science_museum", "sports_store", "gas_station", "university", "primary_school", "outdoor",
    "motorcycle", "electricity_office", "library", "conventioncenter", "kinder_garten", "ticket_agent",
    "snack_bar", "hotel", "cosmetics_store", "adult_education", "telecom_offices", "pet_market", "housekeeping",
    "antique_store", "work_office", "seafood", "gallery", "bbq", "water_supply_office", "other_infrastructure",
    "residence", "clinic", "internet_bar", "commodity_market", "guest_house", "clothing_store", "farmers_market",
    "flea_market", "jewelry_store", "training_institutions", "post_office", "mother_store", "supermarket",
    "economy_hotel", "glass_store", "public_utilities", "dessert", "cooler", "emergency_center", "car_wash",
    "parking_plot", "chinese_restaurant", "atm", "museum"
)
'''

 
def _generate_dining_senz():
    """dining 规则 
         location: 60%以上的 "dining" ;
         motion: 80% "sitting", 15% "walking", 5% "running",不可能出现"riding" or "driving"
         sound: 出现概率稍大的是"tableware", "talking", "laugh"
    """
    random_num = random.random() # 假设三个状态变量是相关的

    # location
    dining_location_type = set(location_type)
    dining_location_type.remove('dining')
    dining_location_type = tuple(location_type)
    if random_num <= 0.6:
        location = 'dining'
    else:
        location = random.choice(dining_location_type)

    # motion
    if random_num <= 0.8:
        motion = 'sitting'
    elif random_num <= 0.95:
        motion = 'walking'
    else:
        motion = 'running'

    # sound
    dining_sound_type = set(sound_type)
    dining_sound_type.remove('tableware')
    dining_sound_type.remove('talking')
    dining_sound_type.remove('laugh')
    dining_sound_type = tuple(dining_sound_type)
    if random_num <= 0.55:
        sound = random.choice(["tableware", "talking", "laugh", "music", "others"])
    else:
        sound = random.choice(dining_sound_type)

    return {'location':location, 'sound':sound, 'motion':motion}

 
def _generate_shopping_senz():
    """ shopping 规则
          location: 80%以上的 "shopping"
          motion: 绝大部分"walking", 少量"sitting", 其他出现概率极低
          sound: 出现概率稍大的是"music", "talking", "laugh", "others"
    """
    random_num = random.random() # 假设三个状态变量是相关的

    # location
    shopping_location_type = set(location_type)
    shopping_location_type.remove('shopping')
    shopping_location_type = tuple(location_type)
    if random_num <= 0.6:
        location = 'shopping'
    else:
        location = random.choice(shopping_location_type)

    # motion
    shopping_motion_type = set(motion_type)
    shopping_motion_type.remove('walking')
    shopping_motion_type.remove('sitting')
    shopping_motion_type = tuple(motion_type)
    if random_num <= 0.8:
        motion = 'walking'
    elif random_num <= 0.95:
        motion = 'sitting'
    else:
        motion = random.choice(shopping_motion_type)

    # sound
    shopping_sound_type = set(sound_type)
    shopping_sound_type.remove('music')
    shopping_sound_type.remove('talking')
    shopping_sound_type.remove('laugh')
    shopping_sound_type.remove('others')
    shopping_sound_type = tuple(shopping_sound_type)
    if random_num <= 0.55:
        sound = random.choice(["music", "talking", "laugh", "others"])
    else:
        sound = random.choice(shopping_sound_type)

    return {'location':location, 'sound':sound, 'motion':motion}

 
def _generate_working_senz():
    """ working 规则
          location: 60%以上的 "finance"
          motion: 绝大部分"sitting", 少量"walking"或极少量"running",不可能出现"riding" or "driving"
          sound: 出现概率稍大的是"keyboard", "mouse_click", "turning_page", "writing", "talking"
    """
    random_num = random.random() # 假设三个状态变量是相关的

    # location
    working_location_type = set(location_type)
    working_location_type.remove('finance')
    working_location_type = tuple(location_type)
    if random_num <= 0.6:
        location = 'finance'
    else:
        location = random.choice(working_location_type)

    # motion
    if random_num <= 0.8:
        motion = 'sitting'
    elif random_num <= 0.95:
        motion = 'walking'
    else:
        motion = 'running'

    # sound
    working_sound_type = set(sound_type)
    working_sound_type.remove('keyboard')
    working_sound_type.remove('mouse_click')
    working_sound_type.remove('turning_page')
    working_sound_type.remove('writing')
    working_sound_type.remove('talking')
    working_sound_type = tuple(working_sound_type)
    if random_num <= 0.75:
        sound = random.choice(["keyboard", "mouse_click", "turning_page", "writing", "talking"])
    else:
        sound = random.choice(working_sound_type)

    return {'location':location, 'sound':sound, 'motion':motion}

 
def _generate_studying_senz():
    """ studying 规则
         location: 60%以上的 "education"
         motion: 绝大部分"sitting", 少量"walking"或极少量"running",不可能出现"riding" or "driving"
         sound: 出现概率稍大的是"keyboard", "mouse_click", "turning_page", "writing", "talking"
    """
    random_num = random.random() # 假设三个状态变量是相关的

    # location
    studying_location_type = set(location_type)
    studying_location_type.remove('education')
    studying_location_type = tuple(location_type)
    if random_num <= 0.6:
        location = 'education'
    else:
        location = random.choice(studying_location_type)

    # motion
    if random_num <= 0.8:
        motion = 'sitting'
    elif random_num <= 0.95:
        motion = 'walking'
    else:
        motion = 'running'

    # sound
    studying_sound_type = set(sound_type)
    studying_sound_type.remove('keyboard')
    studying_sound_type.remove('mouse_click')
    studying_sound_type.remove('turning_page')
    studying_sound_type.remove('writing')
    studying_sound_type.remove('talking')
    studying_sound_type = tuple(studying_sound_type)
    if random_num <= 0.75:
        sound = random.choice(["keyboard", "mouse_click", "turning_page", "writing", "talking"])
    else:
        sound = random.choice(studying_sound_type)

    return {'location':location, 'sound':sound, 'motion':motion}


def generate_dining_senz_list(list_len=10, list_count=1, store_file=''):
    """生成dining senz list, 长度为list_len, 个数为list_count
    """
    result = []
    for i in xrange(list_count):
        senz_list = []
        for j in xrange(list_len):
            senz_list.append(_generate_dining_senz())
        result.append(senz_list)

    if store_file:
        with open(store_file, 'w') as fw:
            json.dump(result, fw)

    return result


def generate_shopping_senz_list(list_len=10, list_count=1, store_file=''):
    """生成shopping senz list, 长度为list_len, 个数为list_count
    """
    result = []
    for i in xrange(list_count):
        senz_list = []
        for j in xrange(list_len):
            senz_list.append(_generate_shopping_senz())
        result.append(senz_list)

    if store_file:
        with open(store_file, 'w') as fw:
            json.dump(result, fw)

    return result


def generate_working_senz_list(list_len=10, list_count=1, store_file=''):
    """生成working senz list, 长度为list_len, 个数为list_count
    """
    result = []
    for i in xrange(list_count):
        senz_list = []
        for j in xrange(list_len):
            senz_list.append(_generate_working_senz())
        result.append(senz_list)

    if store_file:
        with open(store_file, 'w') as fw:
            json.dump(result, fw)

    return result


def generate_studying_senz_list(list_len=10, list_count=1, store_file=''):
    """生成studying senz list, 长度为list_len, 个数为list_count
    """
    result = []
    for i in xrange(list_count):
        senz_list = []
        for j in xrange(list_len):
            senz_list.append(_generate_studying_senz())
        result.append(senz_list)

    if store_file:
        with open(store_file, 'w') as fw:
            json.dump(result, fw)

    return result
