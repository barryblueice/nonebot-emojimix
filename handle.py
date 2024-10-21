import json
import requests
import os
from nonebot.log import logger
# from jsonpath_ng import jsonpath, parse

local_path = os.path.join(os.getcwd(), 'resources', 'emojimix')

current_directory = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(current_directory,'metadata.json'),'r',encoding='utf-8') as i:
    data = json.load(i)

with open(os.path.join(current_directory,'known.json'),'r',encoding='utf-8') as i:
    emoji_list = json.load(i)

emoji_list = emoji_list

# def mix(a,b):
#     try:
#         if not os.path.exists(local_path):
#             os.makedirs(local_path)
#         url = 'https://www.gstatic.com/android/keyboard/emojikitchen/'
#         a = str(hex(ord(a))).lstrip('0x')
#         b = str(hex(ord(b))).lstrip('0x')
#         logger.info(a)
#         logger.info(b)
#         if a in emoji_list and b in emoji_list:
#             # jsonpath_expression = parse(f"$.data.{b}")
#             # result = [match.value for match in jsonpath_expression.find(data)]
#             # print (result)
#             if f'u{a}_u{b}.png' in (os.listdir(local_path)):
#                 return os.path.join(local_path,f'u{a}_u{b}.png')
#             else:
#                 ready_list = []
#                 for c in range(0,len(data['data'][b]["combinations"]),1):
#                     if data['data'][b]["combinations"][c]['rightEmojiCodepoint'] == b:
#                         if data['data'][b]["combinations"][c]['leftEmojiCodepoint'] == a:
#                             ready_list.append(data['data'][b]["combinations"][c]['date'])

#                 ready_list = (list(set(ready_list)))

#                 ready_list = [int(x) for x in ready_list]

#                 ready = max (ready_list)

#                 url = f'https://www.gstatic.com/android/keyboard/emojikitchen/{ready}/u{b}/u{a}_u{b}.png'

#                 logger.info(url)

#                 result = requests.get(url=url)
                
#                 if result.status_code == 200:
#                     with open(os.path.join(local_path,f'u{a}_u{b}.png'), "wb") as file:
#                         file.write(result.content)
#                     return url
#                 else:
#                     ready_list = []
#                     for c in range(0,len(data['data'][a]["combinations"]),1):
#                         if data['data'][a]["combinations"][c]['rightEmojiCodepoint'] == b:
#                             if data['data'][a]["combinations"][c]['leftEmojiCodepoint'] == a:
#                                 ready_list.append(data['data'][a]["combinations"][c]['date'])

#                     ready_list = (list(set(ready_list)))

#                     ready_list = [int(x) for x in ready_list]

#                     ready = max (ready_list)
#                     url = f'https://www.gstatic.com/android/keyboard/emojikitchen/{ready}/u{a}/u{a}_u{b}.png'
#                     logger.info(url)
#                     result = requests.get(url=url)
#                     if result.status_code == 200:
#                         with open(os.path.join(local_path,f'u{a}_u{b}.png'), "wb") as file:
#                             file.write(result.content)
#                         return url
#                     else:
#                         result = mix_reverse(a,b)
#                         return result
#         else:
#             if not a in emoji_list:
#                 return ('a')
#             else:
#                 return ('b')
#     except:
#         result = mix_reverse(a=b,b=a)
#         return result
    
def mix(a,b):
    # try:
        if not os.path.exists(local_path):
            os.makedirs(local_path)
        a = str(hex(ord(a))).lstrip('0x')
        b = str(hex(ord(b))).lstrip('0x')
        logger.info(a)
        logger.info(b)
        if a in emoji_list and b in emoji_list:
            # jsonpath_expression = parse(f"$.data.{b}")
            # result = [match.value for match in jsonpath_expression.find(data)]
            # print (result)
            if f'u{a}_u{b}.png' in (os.listdir(local_path)) or f'u{b}_u{a}.png' in (os.listdir(local_path)):
                return os.path.join(local_path,f'u{a}_u{b}.png')
            else:
                
                for i in range(0,len(data[a])):
                    if b == data[a][i]['rightEmojiCodepoint'] and a == data[a][i]['leftEmojiCodepoint']:

                        url = data[a][i]['gStaticUrl']

                        logger.info(url)

                        result = requests.get(url=url)
                        
                        if result.status_code == 200:
                            with open(os.path.join(local_path,f'u{a}_u{b}.png'), "wb") as file:
                                file.write(result.content)
                            return url
                    
                    elif b == data[a][i]['leftEmojiCodepoint'] and a == data[a][i]['rightEmojiCodepoint']:

                        url = data[a][i]['gStaticUrl']

                        logger.info(url)

                        result = requests.get(url=url)
                        
                        if result.status_code == 200:
                            with open(os.path.join(local_path,f'u{a}_u{b}.png'), "wb") as file:
                                file.write(result.content)
                            return url
                        
                for i in range(0,len(data[b])):
                        
                    if a == data[b][i]['rightEmojiCodepoint'] and b == data[b][i]['leftEmojiCodepoint']:

                        url = data[b][i]['gStaticUrl']

                        logger.info(url)

                        result = requests.get(url=url)
                        
                        if result.status_code == 200:
                            with open(os.path.join(local_path,f'u{b}_u{a}.png'), "wb") as file:
                                file.write(result.content)
                            return url
                        
                    elif a == data[b][i]['leftEmojiCodepoint'] and b == data[b][i]['rightEmojiCodepoint']:

                        url = data[b][i]['gStaticUrl']

                        logger.info(url)

                        result = requests.get(url=url)
                        
                        if result.status_code == 200:
                            with open(os.path.join(local_path,f'u{b}_u{a}.png'), "wb") as file:
                                file.write(result.content)
                            return url
                    
                    return None

        else:
            if not a in emoji_list:
                return ('a')
            else:
                return ('b')
    # except:
    #     return None


# result = mix('🦄','🦄')
# print (result)