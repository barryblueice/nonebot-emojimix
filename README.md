# nonebot-emojimix

基于[nonebot-plugin-emojimix](https://github.com/noneplugin/nonebot-plugin-emojimix)重构的emoji合成插件。

理论上适用于基于nonebot2+onebot v11运行的所有bot。

使用方法：

```
emoji+emoji
示例：😎+😁
```
![image](https://github.com/user-attachments/assets/51dbd587-3322-41b7-9942-9c79065c1b22)

## 使用前提醒：
本插件包括以下能治疗各位开发者血压低的内容：

1. 三角稳定：

```python
if:
    if:
        if:
            if:
                if:
                    if:
                    else:
                else:
            else:
        else:
    else:
else:
```

2. 视而不见：

```python
try:
except:
try:
except:
try:
except:
```

3. 热辣炸串：

```python
if:
elif:
elif:
elif:
elif:
else
```

4. 真假李逵：

```python
def mix(a,b):
    ......
def mix_reverse(a,b):
    ......
```

## 运行原理

根据[emoji-kitchen](https://github.com/xsalazar/emoji-kitchen)中获取到的metadata.json进行部分数据提取+增删:

源数据很大，大约有52MB，全部加载显然不现实：

![image](https://github.com/barryblueice/nonebot-emojimix/assets/44601454/159687c3-453a-4ff0-a0ae-54ec43fe8ac2)

分析metadata.json可以得知，里面的数据由可用emoji的unicode编码+emoji合成判断组成。

![image](https://github.com/barryblueice/nonebot-emojimix/assets/44601454/e3d9a77d-bdf9-44c9-8e08-bd0243716067)

emoji图片则遵循这么一个url规则：

```
https://www.gstatic.com/android/keyboard/emojikitchen/{日期}/{表情a}/{表情a}_{表情b}.png
```

或者

```
https://www.gstatic.com/android/keyboard/emojikitchen/{日期}/{表情b}/{表情a}_{表情b}.png
```

蒸馏原metadata.json中对我们无用的大部分数据后，我们得到一个判断是否为可用emoji的known.json，以及获取合成表情相关信息的魔改后metadata.json。

![image](https://github.com/barryblueice/nonebot-emojimix/assets/44601454/d7716f29-5b80-446b-beb3-88f286569638)

接着做一个对比，然后根据url规则实现就可以。

原metadata.json下载地址：[https://raw.githubusercontent.com/xsalazar/emoji-kitchen-backend/main/app/metadata.json](https://raw.githubusercontent.com/xsalazar/emoji-kitchen-backend/main/app/metadata.json)
