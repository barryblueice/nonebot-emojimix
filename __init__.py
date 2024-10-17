from nonebot import on_regex
from nonebot.params import RegexDict
from nonebot.adapters.onebot.v11 import MessageSegment,MessageEvent,Bot

from .handle import mix

from nonebot.plugin import PluginMetadata

__plugin_meta__ = PluginMetadata(
    name="Emoji合成器",
    description="合成emoji",
    usage="""😎+😁=？"""
)

pattern = "[\U0001F300-\U0001F9FF]"
emojimix = on_regex(rf"^(?P<left>{pattern})\s*\+\s*(?P<right>{pattern})$", block=True, priority=5)

@emojimix.handle()
async def _(event: MessageEvent,bot: Bot,msg: dict = RegexDict()):
    a = msg["left"]
    b = msg["right"]

    result = mix(a,b)
    
    if result == 'a':
        msg = (f'不正确的参数：{a}')
    elif result == 'b':
        msg = (f'不正确的参数：{b}')
    elif result == None:
        msg = '表情不支持，请重新选择'
    else:
        if result.startswith('https://'):
            msg = MessageSegment.image(result)
        else:
            msg = MessageSegment.image('file://'+result)
    await emojimix.send(msg)

