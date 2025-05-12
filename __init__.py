from nonebot import on_message
from nonebot.adapters.onebot.v11 import MessageEvent, MessageSegment, Bot
import emoji

from .handle import mix

from nonebot.plugin import PluginMetadata

__plugin_meta__ = PluginMetadata(
    name="Emoji合成器",
    description="合成emoji",
    usage="""😎+😁=？"""
)

emojimix = on_message(priority=5, block=False)

@emojimix.handle()
async def _(event: MessageEvent,bot: Bot):
    text = event.get_plaintext()
    emojis = emoji.emoji_list(text)

    if len(emojis) >= 2:
        a = emojis[0]['emoji']
        b = emojis[1]['emoji']

        result = mix(a,b)
        
        if result == 'a':
            msg = (f'不正确的参数：{a}')
        elif result == 'b':
            msg = (f'不正确的参数：{b}')
        elif result == None:
            msg = '表情不支持，请重新选择'
        else:
            if result.startswith('https://'):
                msg = MessageSegment.reply(event.message_id)+MessageSegment.image(result)
            else:
                msg = MessageSegment.reply(event.message_id)+MessageSegment.image('file://'+result)
        await emojimix.send(msg)
    