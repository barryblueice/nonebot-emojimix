import json

with open('.\\metadata_original.json', 'r', encoding='utf-8') as i:
    data = json.load(i)

new_data = {}

for i in data['data']:
    combinations_dict = data['data'][i]['combinations']
    
    merged_list = []
    for a in combinations_dict:
        combination_list = combinations_dict[a]
        for item in combination_list:
            for key in ['alt', 'leftEmoji', 'rightEmoji', 'date', 'gBoardOrder']:
                if key in item:
                    del item[key]
        filtered_list = [item for item in combination_list if item.get('isLatest') == True]
        for item in filtered_list:
            if 'isLatest' in item:
                del item['isLatest']

        merged_list.extend(filtered_list)

    new_data[i] = merged_list

with open('.\\metadata.json', 'w', encoding='utf-8') as e:
    json.dump(new_data, e, ensure_ascii=False, indent=4)
