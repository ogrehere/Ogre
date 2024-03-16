import time
import os, logging, asyncio, random
from telethon import Button
from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.types import ChannelParticipantCreator
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError

from config import BOT_TOKEN as bot_token, API_ID as api_id, API_HASH as api_hash

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)


spam_chats = []


@client.on(events.NewMessage(pattern="^/htag ?(.*)"))
async def mention_all(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond(
            "__This command can be used in groups and channels!__"
        )

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧 𝐂𝐚𝐧 𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐓𝐨 𝐀𝐥𝐥 𝐁𝐚𝐛𝐲...")
    
    if event.pattern_match.group(1):
        return await event.respond("/htag  👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 𝐎𝐤 𝐅𝐨𝐫 𝐓𝐚𝐠𝐠𝐢𝐧𝐠..")
    else:
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
        if msg is None:
            return await event.respond(
                "/htag 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 𝐎𝐫 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞..."
            )

    spam_chats.append(chat_id)
    async for usr in client.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        user_id = usr.id
        mention_text = f"[{usr.first_name}](tg://user?id={user_id}) {random.choice(TAGMES)}"
        await client.send_message(chat_id, mention_text)
        time.sleep(5)
        
    try:
        spam_chats.remove(chat_id)
    except:
        pass
        



EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]
  
@client.on(events.NewMessage(pattern="^/etag ?(.*)"))
async def mention_all(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond(
            "__This command can be used in groups and channels!__"
        )

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧 𝐂𝐚𝐧 𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐓𝐨 𝐀𝐥𝐥 𝐁𝐚𝐛𝐲...")
    
    if event.pattern_match.group(1):
        return await event.respond("/etag 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 𝐎𝐤 𝐅𝐨𝐫 𝐓𝐚𝐠𝐠𝐢𝐧𝐠..")
    else:
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
        if msg is None:
            return await event.respond(
                "/etag 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 𝐎𝐫 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞..."
            )

    spam_chats.append(chat_id)
    async for usr in client.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        user_id = usr.id
        mention_text = f"[ {random.choice(EMOJI)} ](tg://user?id={usr.id})"
        await client.send_message(chat_id, mention_text)
        time.sleep(5)
        
    try:
        spam_chats.remove(chat_id)
    except:
        pass
         
 
                   
                          
TAGMES = [ " **𝐇𝐞𝐲 𝐁𝐚𝐛𝐲 𝐊𝐚𝐡𝐚 𝐇𝐨🥱** ",
           " **𝐎𝐲𝐞 𝐒𝐨 𝐆𝐲𝐞 𝐊𝐲𝐚 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐚𝐨😊** ",
           " **𝐕𝐜 𝐂𝐡𝐚𝐥𝐨 𝐁𝐚𝐭𝐞𝐧 𝐊𝐚𝐫𝐭𝐞 𝐇𝐚𝐢𝐧 𝐊𝐮𝐜𝐡 𝐊𝐮𝐜𝐡😃** ",
           " **𝐊𝐡𝐚𝐧𝐚 𝐊𝐡𝐚 𝐋𝐢𝐲𝐞 𝐉𝐢..??🥲** ",
           " **𝐆𝐡𝐚𝐫 𝐌𝐞 𝐒𝐚𝐛 𝐊𝐚𝐢𝐬𝐞 𝐇𝐚𝐢𝐧 𝐉𝐢🥺** ",
           " **𝐏𝐭𝐚 𝐇𝐚𝐢 𝐁𝐨𝐡𝐨𝐭 𝐌𝐢𝐬𝐬 𝐊𝐚𝐫 𝐑𝐡𝐢 𝐓𝐡𝐢 𝐀𝐚𝐩𝐤𝐨🤭** ",
           " **𝐎𝐲𝐞 𝐇𝐚𝐥 𝐂𝐡𝐚𝐥 𝐊𝐞𝐬𝐚 𝐇𝐚𝐢..??🤨** ",
           " **𝐌𝐞𝐫𝐢 𝐁𝐡𝐢 𝐒𝐞𝐭𝐭𝐢𝐧𝐠 𝐊𝐚𝐫𝐛𝐚 𝐃𝐨𝐠𝐞..??🙂** ",
           " **𝐀𝐚𝐩𝐤𝐚 𝐍𝐚𝐦𝐞 𝐊𝐲𝐚 𝐡𝐚𝐢..??🥲** ",
           " **𝐍𝐚𝐬𝐭𝐚 𝐇𝐮𝐚 𝐀𝐚𝐩𝐤𝐚..??😋** ",
           " **𝐌𝐞𝐫𝐞 𝐊𝐨 𝐀𝐩𝐧𝐞 𝐆𝐫𝐨𝐮𝐩 𝐌𝐞 𝐊𝐢𝐝𝐧𝐚𝐩 𝐊𝐫 𝐋𝐨😍** ",
           " **𝐀𝐚𝐩𝐤𝐢 𝐏𝐚𝐫𝐭𝐧𝐞𝐫 𝐀𝐚𝐩𝐤𝐨 𝐃𝐡𝐮𝐧𝐝 𝐑𝐡𝐞 𝐇𝐚𝐢𝐧 𝐉𝐥𝐝𝐢 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐲𝐢𝐚𝐞😅😅** ",
           " **𝐌𝐞𝐫𝐞 𝐒𝐞 𝐃𝐨𝐬𝐭𝐢 𝐊𝐫𝐨𝐠𝐞..??🤔** ",
           " **𝐒𝐨𝐧𝐞 𝐂𝐡𝐚𝐥 𝐆𝐲𝐞 𝐊𝐲𝐚🙄🙄** ",
           " **𝐄𝐤 𝐒𝐨𝐧𝐠 𝐏𝐥𝐚𝐲 𝐊𝐫𝐨 𝐍𝐚 𝐏𝐥𝐬𝐬😕** ",
           " **𝐀𝐚𝐩 𝐊𝐚𝐡𝐚 𝐒𝐞 𝐇𝐨..??🙃** ",
           " **𝐇𝐞𝐥𝐥𝐨 𝐉𝐢 𝐍𝐚𝐦𝐚𝐬𝐭𝐞😛** ",
           " **𝐇𝐞𝐥𝐥𝐨 𝐁𝐚𝐛𝐲 𝐊𝐤𝐫𝐡..?🤔** ",
           " **𝐃𝐨 𝐘𝐨𝐮 𝐊𝐧𝐨𝐰 𝐖𝐡𝐨 𝐈𝐬 𝐌𝐲 𝐎𝐰𝐧𝐞𝐫.?** ",
           " **𝐂𝐡𝐥𝐨 𝐊𝐮𝐜𝐡 𝐆𝐚𝐦𝐞 𝐊𝐡𝐞𝐥𝐭𝐞 𝐇𝐚𝐢𝐧.🤗** ",
           " **𝐀𝐮𝐫 𝐁𝐚𝐭𝐚𝐨 𝐊𝐚𝐢𝐬𝐞 𝐇𝐨 𝐁𝐚𝐛𝐲😇** ",
           " **𝐓𝐮𝐦𝐡𝐚𝐫𝐢 𝐌𝐮𝐦𝐦𝐲 𝐊𝐲𝐚 𝐊𝐚𝐫 𝐑𝐚𝐡𝐢 𝐇𝐚𝐢🤭** ",
           " **𝐌𝐞𝐫𝐞 𝐒𝐞 𝐁𝐚𝐭 𝐍𝐨𝐢 𝐊𝐫𝐨𝐠𝐞🥺🥺** ",
           " **𝐎𝐲𝐞 𝐏𝐚𝐠𝐚𝐥 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐚 𝐉𝐚😶** ",
           " **𝐀𝐚𝐣 𝐇𝐨𝐥𝐢𝐝𝐚𝐲 𝐇𝐚𝐢 𝐊𝐲𝐚 𝐒𝐜𝐡𝐨𝐨𝐥 𝐌𝐞..??🤔** ",
           " **𝐎𝐲𝐞 𝐆𝐨𝐨𝐝 𝐌𝐨𝐫𝐧𝐢𝐧𝐠😜** ",
           " **𝐒𝐮𝐧𝐨 𝐄𝐤 𝐊𝐚𝐦 𝐇𝐚𝐢 𝐓𝐮𝐦𝐬𝐞🙂** ",
           " **𝐊𝐨𝐢 𝐒𝐨𝐧𝐠 𝐏𝐥𝐚𝐲 𝐊𝐫𝐨 𝐍𝐚😪** ",
           " **𝐍𝐢𝐜𝐞 𝐓𝐨 𝐌𝐞𝐞𝐭 𝐔𝐡☺** ",
           " **𝐇𝐞𝐥𝐥𝐨🙊** ",
           " **𝐒𝐭𝐮𝐝𝐲 𝐂𝐨𝐦𝐥𝐞𝐭𝐞 𝐇𝐮𝐚??😺** ",
           " **𝐁𝐨𝐥𝐨 𝐍𝐚 𝐊𝐮𝐜𝐡 𝐘𝐫𝐫🥲** ",
           " **𝐒𝐨𝐧𝐚𝐥𝐢 𝐊𝐨𝐧 𝐇𝐚𝐢...??😅** ",
           " **𝐓𝐮𝐦𝐡𝐚𝐫𝐢 𝐄𝐤 𝐏𝐢𝐜 𝐌𝐢𝐥𝐞𝐠𝐢..?😅** ",
           " **𝐌𝐮𝐦𝐦𝐲 𝐀𝐚 𝐆𝐲𝐢 𝐊𝐲𝐚😆😆😆** ",
           " **𝐎𝐫 𝐁𝐚𝐭𝐚𝐨 𝐁𝐡𝐚𝐛𝐡𝐢 𝐊𝐚𝐢𝐬𝐢 𝐇𝐚𝐢😉** ",
           " **𝐈 𝐋𝐨𝐯𝐞 𝐘𝐨𝐮🙈🙈🙈** ",
           " **𝐃𝐨 𝐘𝐨𝐮 𝐋𝐨𝐯𝐞 𝐌𝐞..?👀** ",
           " **𝐑𝐚𝐤𝐡𝐢 𝐊𝐚𝐛 𝐁𝐚𝐧𝐝 𝐑𝐚𝐡𝐢 𝐇𝐨.??🙉** ",
           " **𝐄𝐤 𝐒𝐨𝐧𝐠 𝐒𝐮𝐧𝐚𝐮..?😹** ",
           " **𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐚 𝐉𝐚 𝐑𝐞 𝐒𝐨𝐧𝐠 𝐒𝐮𝐧𝐚 𝐑𝐚𝐡𝐢 𝐇𝐮😻** ",
           " **𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦 𝐂𝐡𝐚𝐥𝐚𝐭𝐞 𝐇𝐨..??🙃** ",
           " **𝐖𝐡𝐚𝐭𝐬𝐚𝐩𝐩 𝐍𝐮𝐦𝐛𝐞𝐫 𝐃𝐨𝐠𝐞 𝐀𝐩𝐧𝐚 𝐓𝐮𝐦..?😕** ",
           " **𝐓𝐮𝐦𝐡𝐞 𝐊𝐨𝐧 𝐒𝐚 𝐌𝐮𝐬𝐢𝐜 𝐒𝐮𝐧𝐧𝐚 𝐏𝐚𝐬𝐚𝐧𝐝 𝐇𝐚𝐢..?🙃** ",
           " **𝐒𝐚𝐫𝐚 𝐊𝐚𝐦 𝐊𝐡𝐚𝐭𝐚𝐦 𝐇𝐨 𝐆𝐲𝐚 𝐀𝐚𝐩𝐤𝐚..?🙃** ",
           " **𝐊𝐚𝐡𝐚 𝐒𝐞 𝐇𝐨 𝐀𝐚𝐩😊** ",
           " **𝐒𝐮𝐧𝐨 𝐍𝐚🧐** ",
           " **𝐌𝐞𝐫𝐚 𝐄𝐤 𝐊𝐚𝐚𝐦 𝐊𝐚𝐫 𝐃𝐨𝐠𝐞..?** ",
           " **𝐁𝐲 𝐓𝐚𝐭𝐚 𝐌𝐚𝐭 𝐁𝐚𝐭 𝐊𝐚𝐫𝐧𝐚 𝐀𝐚𝐣 𝐊𝐞 𝐁𝐚𝐝😠** ",
           " **𝐌𝐨𝐦 𝐃𝐚𝐝 𝐊𝐚𝐢𝐬𝐞 𝐇𝐚𝐢𝐧..?❤** ",
           " **𝐊𝐲𝐚 𝐇𝐮𝐚..?👱** ",
           " **𝐁𝐨𝐡𝐨𝐭 𝐘𝐚𝐚𝐝 𝐀𝐚 𝐑𝐡𝐢 𝐇𝐚𝐢 🤧❣️** ",
           " **𝐁𝐡𝐮𝐥 𝐆𝐲𝐞 𝐌𝐮𝐣𝐡𝐞😏😏** ",
           " **𝐉𝐮𝐭𝐡 𝐍𝐡𝐢 𝐁𝐨𝐥𝐧𝐚 𝐂𝐡𝐚𝐡𝐢𝐲𝐞🤐** ",
           " **𝐊𝐡𝐚 𝐋𝐨 𝐁𝐡𝐚𝐰 𝐌𝐚𝐭 𝐊𝐫𝐨 𝐁𝐚𝐚𝐭😒** ",
           " **𝐊𝐲𝐚 𝐇𝐮𝐚😮😮** "
           " **𝐇𝐢𝐢👀** ",
           " **𝐀𝐚𝐩𝐤𝐞 𝐉𝐚𝐢𝐬𝐚 𝐃𝐨𝐬𝐭 𝐇𝐨 𝐒𝐚𝐭𝐡 𝐌𝐞 𝐅𝐢𝐫 𝐆𝐮𝐦 𝐊𝐢𝐬 𝐁𝐚𝐭 𝐊𝐚 🙈** ",
           " **𝐀𝐚𝐣 𝐌𝐚𝐢 𝐒𝐚𝐝 𝐇𝐮 ☹️** ",
           " **𝐌𝐮𝐬𝐣𝐡𝐬𝐞 𝐁𝐡𝐢 𝐁𝐚𝐭 𝐊𝐚𝐫 𝐋𝐨 𝐍𝐚 🥺🥺** ",
           " **𝐊𝐲𝐚 𝐊𝐚𝐫 𝐑𝐚𝐡𝐞 𝐇𝐨👀** ",
           " **𝐊𝐲𝐚 𝐇𝐚𝐥 𝐂𝐡𝐚𝐥 𝐇𝐚𝐢 🙂** ",
           " **𝐊𝐚𝐡𝐚 𝐒𝐞 𝐇𝐨 𝐀𝐚𝐩..?🤔** ",
           " **𝐂𝐡𝐚𝐭𝐭𝐢𝐧𝐠 𝐊𝐚𝐫 𝐋𝐨 𝐍𝐚..🥺** ",
           " **𝐌𝐞 𝐌𝐚𝐬𝐨𝐨𝐦 𝐇𝐮 𝐍𝐚🥺🥺** ",
           " **𝐊𝐚𝐥 𝐌𝐚𝐣𝐚 𝐀𝐲𝐚 𝐓𝐡𝐚 𝐍𝐚🤭😅** ",
           " **𝐆𝐫𝐨𝐮𝐩 𝐌𝐞 𝐁𝐚𝐭 𝐊𝐲𝐮 𝐍𝐚𝐡𝐢 𝐊𝐚𝐫𝐭𝐞 𝐇𝐨😕** ",
           " **𝐀𝐚𝐩 𝐑𝐞𝐥𝐚𝐭𝐢𝐨𝐦𝐬𝐡𝐢𝐩 𝐌𝐞 𝐇𝐨..?👀** ",
           " **𝐊𝐢𝐭𝐧𝐚 𝐂𝐡𝐮𝐩 𝐑𝐚𝐡𝐭𝐞 𝐇𝐨 𝐘𝐫𝐫😼** ",
           " **𝐀𝐚𝐩𝐤𝐨 𝐆𝐚𝐧𝐚 𝐆𝐚𝐧𝐞 𝐀𝐚𝐭𝐚 𝐇𝐚𝐢..?😸** ",
           " **𝐆𝐡𝐮𝐦𝐧𝐞 𝐂𝐡𝐚𝐥𝐨𝐠𝐞..??🙈** ",
           " **𝐊𝐡𝐮𝐬 𝐑𝐚𝐡𝐚 𝐊𝐚𝐫𝐨 ✌️🤞** ",
           " **𝐇𝐚𝐦 𝐃𝐨𝐬𝐭 𝐁𝐚𝐧 𝐒𝐚𝐤𝐭𝐞 𝐇𝐚𝐢...?🥰** ",
           " **𝐊𝐮𝐜𝐡 𝐁𝐨𝐥 𝐊𝐲𝐮 𝐍𝐡𝐢 𝐑𝐚𝐡𝐞 𝐇𝐨..🥺🥺** ",
           " **𝐊𝐮𝐜𝐡 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 𝐀𝐝𝐝 𝐊𝐚𝐫 𝐃𝐨 🥲** ",
           " **𝐒𝐢𝐧𝐠𝐥𝐞 𝐇𝐨 𝐘𝐚 𝐌𝐢𝐧𝐠𝐥𝐞 😉** ",
           " **𝐀𝐚𝐨 𝐏𝐚𝐫𝐭𝐲 𝐊𝐚𝐫𝐭𝐞 𝐇𝐚𝐢𝐧😋🥳** ",
           " **𝐇𝐞𝐦𝐥𝐨𝐨🧐** ",
           " **𝐌𝐮𝐣𝐡𝐞 𝐁𝐡𝐮𝐥 𝐆𝐲𝐞 𝐊𝐲𝐚🥺** ",
           " **𝐘𝐚𝐡𝐚 𝐀𝐚 𝐉𝐚𝐨:- [ @NOxDISCUSSION] 𝐌𝐚𝐬𝐭𝐢 𝐊𝐚𝐫𝐞𝐧𝐠𝐞 🤭🤭** ",
           " **𝐓𝐫𝐮𝐭𝐡 𝐀𝐧𝐝 𝐃𝐚𝐫𝐞 𝐊𝐡𝐞𝐥𝐨𝐠𝐞..? 😊** ",
           " **𝐀𝐚𝐣 𝐌𝐮𝐦𝐦𝐲 𝐍𝐞 𝐃𝐚𝐭𝐚 𝐘𝐫🥺🥺** ",
           " **𝐉𝐨𝐢𝐧 𝐊𝐚𝐫 𝐋𝐨:- [ @NOxDISCUSSION ] 🤗** ",
           " **𝐄𝐤 𝐃𝐢𝐥 𝐇𝐚𝐢 𝐄𝐤 𝐃𝐢𝐥 𝐇𝐢 𝐓𝐨 𝐇𝐚𝐢😗😗** ",
           " **𝐓𝐮𝐦𝐡𝐚𝐫𝐞 𝐃𝐨𝐬𝐭 𝐊𝐚𝐡𝐚 𝐆𝐲𝐞🥺** ",
           " **𝐌𝐲 𝐂𝐮𝐭𝐞 𝐎𝐰𝐧𝐞𝐫 [ @FENIXsSLAYER ]🥰** ",
           " **𝐊𝐚𝐡𝐚 𝐊𝐡𝐨𝐲𝐞 𝐇𝐨 𝐉𝐚𝐚𝐧😜** ",
           " **𝐆𝐨𝐨𝐝 𝐍8 𝐉𝐢 𝐁𝐡𝐮𝐭 𝐑𝐚𝐭 𝐇𝐨 𝐠𝐲𝐢🥰** ",
           ]

@client.on(events.NewMessage(pattern="^/tagall ?(.*)"))
@client.on(events.NewMessage(pattern="^@all ?(.*)"))
@client.on(events.NewMessage(pattern="^/utag ?(.*)"))
@client.on(events.NewMessage(pattern="^@utag ?(.*)"))
@client.on(events.NewMessage(pattern="^/all ?(.*)"))
@client.on(events.NewMessage(pattern="^#all ?(.*)"))
@client.on(events.NewMessage(pattern="^@tagall ?(.*)"))
@client.on(events.NewMessage(pattern="^/mentionall?(.*)"))
@client.on(events.NewMessage(pattern="^@mentionall ?(.*)"))
@client.on(events.NewMessage(pattern="^#mentionall ?(.*)"))
@client.on(events.NewMessage(pattern="^/mention ?(.*)"))
@client.on(events.NewMessage(pattern="^@mention ?(.*)"))
@client.on(events.NewMessage(pattern="^#mention ?(.*)"))
@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
@client.on(events.NewMessage(pattern="^#tag ?(.*)"))
@client.on(events.NewMessage(pattern="^@tag ?(.*)"))
@client.on(events.NewMessage(pattern="^#utag ?(.*)"))
@client.on(events.NewMessage(pattern="^#tagall ?(.*)"))
async def mentionall(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond(
            "__This command can be use in groups and channels!__"
        )

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("__Only admins can mention all!__")

    if event.pattern_match.group(1) and event.is_reply:
        return await event.respond("__Give me one argument!__")
    elif event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.is_reply:
        mode = "text_on_reply"
        msg = await event.get_reply_message()
        if msg == None:
            return await event.respond(
                "__I can't mention members for older messages! (messages which are sent before I'm added to group)__"
            )
    else:
        return await event.respond(
            "__Reply to a message or give me some text to mention others!__"
        )

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}), "
        if usrnum == 5:
            if mode == "text_on_cmd":
                txt = f"{msg}\n{usrtxt}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(usrtxt)
            await asyncio.sleep(3)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass
        
        
        
MUSIC = [
    " **Tere naalo challiye haseen koyi NA 😁😁** ",
    " **Taare chann ambar zameen koyi nA** ",
    " **Main Jado Tere Mode Utte Sir Rakheya🧐🧐** ",
    " **Eh Ton Sachi Sama Vi Haseen Koi Na😖😖** ",
    " **Sohniyan Vi Laggan Giyan Fer Walian😍😍** ",
    " **Galan Nal Jado Takraiyan Waliyan🥰🥰** ",
    " **Tare Dekhi Labh Labh Kiven Harde😁😁** ",
    " **Tu Bala Ch Lakoiyan Jado Ratan Kaliyan😒😒** ",
    " **Main Sab Kuj Har Tere Utton De’unga😌😌** ",
    " **Sab Kuj War Tere Utton De’unga😉😉** ",
    " **Akhir Ch Jan Tainu De’un Apni😎😎** ",
    " **Chala Tainu Bhavein Pehli War De’unga😚😚** ",
    " **Han Main Cheti Cheti Lawan😫😫** ",
    " **Tere Nal Laini an😣😣** ",
    " **Samay Da Tan Bhora Vi Yakeen Koi Na🥺🥺** ",
    " **Tere Nalo Jhaliye Haseen Koi Na🥰🥰** ",
    " **Tare Chann Ambar Zameen Koi Na😘😘** ",
    " **Tere Nalo Jhaliye Haseen Koi Na😍😍** ",
    " **Tare Chann Ambar Zameen Koi Na🥰🥰** ",
    " **Main Jado Tere Mode Utte Sir Rakheya😁😁** ",
    " **Eh Ton Sachi Sama Vi Haseen Koi Na😒😒** ",
    " **Tu Yar Mera Tu Hi Ae Sahara AdiyE** ",
    " **Main Pani Tera Mera Tu Kinara Adiye** ",
    " **Phul Ban Jai Main Khushboo Bann Ju** ",
    " **Deevan Bani Mera Teri Lau Ban Ju** ",
    " **Haye Ujadiyan Thawan Te Banate Bag Ne** ",
    " **Teriyan Ankhan Ne Kitte Jadu Yad Ne** ",
    " **Jado Wang Kolon Phadi Vi Ni KassKe** ",
    " **Totte Sambh Rakhe Tutte Hoye Kach De** ",
    " **Han Ki Dil Yadan Rakhda Ae, Sambh Sambh Ke** ",
    " **Hor Dil Sajjna Machine Koi Na** ",
    " **Tere Nalo Jhaliye Haseen Koi Na** ",
    " **Tare Chann Ambar Zameen Koi Na** ",
    " **Tere Nalo Jhaliye Haseen Koi Na** ",
    " **Tare Chann Ambar Zameen Koi Na** ",
    " **Main Jado Tere Mode Utte Sir Rakheya** ",
    " **Eh Ton Sachi Sama Vi Haseen Koi Na** ",
    " **Kine Din Hogye Meri Akh Soi Na** ",
    " **Tere Ton Bagair Mera Aithe Koi Na** ",
    " **Tu Bhukh Vi Ae Tu Hi Ae Guzara Adiye** ",
    " **Mannu Sab Kari Tu Ishara Adiye** ",
    " **Ho Khaure Kinni War Seene Vich Khubiyan** ",
    " **Surme De Vich Dovein Ankhan Dubbiyan** ",
    " **Kini Sohni Lagge Jadon Chup Kar Je** ",
    " **Jandi Jandi Shaman Nu Vi Dhup Kar Je** ",
    " **Haye Main Paun Farmaishi Rang Tere Sohniye** ",
    " **Unj Bahotan Gifty Shaukeen Koi Na** ",
    " **Tere Nalo Jhaliye Haseen Koi Na😍😍** ",
    " **Tare Chann Ambar Zameen Koi Na🥰🥰**",
    " **Tere Nalo Jhaliye Haseen Koi Na😍😍** ",
    " **Tare Chann Ambar Zameen Koi Na🥰🥰** ",
    " **Main Jado Tere Mode Utte Sir Rakheya😁😁** ",
    " **Eh Ton Sachi Sama Vi Haseen Koi Na😒😒** ",
    " **Kanna Wich Jhumka👀👀** ",
    " **Akhan Wich Surma🙈🙈** ",
    " **Ho Jaise Strawberry Candy😋😋** ",
    " **Nakk Utte Koka🤨🤨** ",
    " **Jeena Kare Aukha🤭🤭** ",
    " **Haye Meri Jaan Kadd Laindi😌😌** ",
    " **Tere Nakhre Haye Tauba Sanu Maarde🤫🤫** ",
    " **Ho Gaya Hai Mera Baby Bura HaaL😊😊** ",
    " **Sachi Lut Gaye Hum Tere Is Pyar Mein😏😏** ",
    " **Jeeni Zindagi Hai Bas Tere Naal😚😚** ",
    " **cause I Love You 😘😘** ",
    " **I Love YoU SO MUCH 😍😍** ",
    " **cause I Love You 😘😘** ",
    " **I Love YoU SO MUCH 😍😍** ",
    " **Sapno Mein Mere AayI😝😝** ",
    " **Uff Oh Phir Neendein Hi Churayi😜😜** ",
    " **Oh No! Tera Husan Nazara🥰🥰** ",
    " **Baby! Lage Sohna Kitna PyarA😚😚** ",
    " **Sapno Mein Mere Aayi😝😝** ",
    " **Uff Oh Phir Neendein Hi Churayi😜😜** ",
    " **Oh No! Tera Husan Nazara🥰🥰** ",
    " **Baby! Lage Sohna Kitna PyarA😚😚** ",
    " **Tainu Diamond Mundri Pehnawa😎😎** ",
    " **Naale Duniya Sari Ghumawa🙈🙈** ",
    " **Chhoti-Chhoti Gallan Utte Main Hasavaan💙💙** ",
    " **Yaara Kade Vi Na Tainu Main Rulawaan🙊🙊** ",
    " **cause I Love You🙈🙈** ",
    " **I Love You ❤️❤️** ",
    " **cause I Love You🙈🙈** ",
    " **I Love You ❤️❤️** ",
    " **Yaari Laawan Sachi YaarI💫💫** ",
    " **Tu Jaan Ton Vi Pyari😁😁** ",
    " **Will Love You To The Moon And Back😆😆** ",
    " **Hogi Saza Na Koyi Hogi😙😙** ",
    " **Chahe Karun Chori Chaand Taare😉😉** ",
    " **Imma Give You Them😅😅** ",
    " **Yaari Laavan Sachi YaarI😘😘** ",
    " **Tu Jaan Ton Vi PyarI😆😆** ",
    " **Will Love You To The Moon And Back💕💕** ",
    " **Hogee Sazaa Na Koyi Hogi💓💓** ",
    " **Chahe Karun Chori Chaand Taare🥺🥺** ",
    " **Imma Give You Them🥵🥵** ",
    " **Puri Karunga Main Teri Sari Khahishein😁😁** ",
    " **Tera Rakhanga Main ajj Ke Khayal😘😘** ",
    " **Kitni Khoobiyan Hai Tere Is Yaar Mein🥰🥰** ",
    " **Aaja Bahon Mein Tu Bahein Bas Daal😂😂** ",
    " **Aur Hota Nahi Ab Intezar🤩🤩** ",
    " **Aur Hota Nahee Ab Intezaar😘😘** ",
    " **cause I Love You 😍😍** ",
    " **I Love YoU 😙😙** ",
    " **cause I Love You** ",
    " **I Love YoU SOOOOOOOOOOOOOOOOOO MUCHHHHHHHHHHHHHHHHHHHHH 😘😘** ",
    " **WILL U BE MINE FOREVER??🤔🤔** ",
    " **Je tu akh te main aan kaajal ve😌😌** ",
    " **Tu baarish te main baadal ve🤫🤫** ",
    " **Tu deewana main aan paagal ve🤪🤪** ",
    " **Sohneya sohneya☺️☺️** ",
    " **Je tu chann te main aan taara ve🤗🤗** ",
    " **Main lehar te tu kinara ve😶😶** ",
    " **Main aadha te tu saara ve🤗🤗"" ",
    " **Sohneya sohneya😗😗** ",
    " **Tu jahan hai main wahan😘😘** ",
    " **Tere bin main hoon hi kya🥲🥲** ",
    " **Tere bin chehre se mere🤔🤔** ",
    " **Udd jaaye rang ve😅😅** ",
    " **Tujhko paane ke liye huM😁😁** ",
    " **Roz mangein mannat ve🙈🙈** ",
    " **Duniya to kya cheez hai yaara🙉🙉** ",
    " **Thukra denge jannat ve😌😌** ",
    " **Tujhko paane ke liye hum😌😌** ",
    " **Roz mangein mannat ve🤫🤫** ",
    " **Duniya to kya cheez hai yaara🤔🤔** ",
    " **Thukra denge jannat ve😌😌** ",
    " **Na parwah mainu apni aa😁😁** ",
    " **Na parwah mainu duniya di👅👅** ",
    " **Na parwah mainu apni aa😅😅** ",
    " **Na parwah mainu duniya di👅👅** ",
    " **Tere ton juda nahi kar sakdi🤬🤬** ",
    " **Koyi taakat mainu duniya di😈😈** ",
    " **Dooron aa jaave teri khushbu😎😎** ",
    " **Akhan hun band taan vi vekh lawan😍😍** ",
    " **Teri gali vich mera auna har roz😋😋** ",
    " **Tera ghar jadon aave matha tek lawan😌😌** ",
    " **Nirmaan tujhko dekh ke😏😏** ",
    " **Aa jaave himmat ve😉😉** ",
    " **Tujhko paane ke liye hum😊😊** ",
    " **Roz mangein mannat ve😉😉** ",
    " **Duniya to kya cheez hai yaara😌😌** ",
    " **Thukra denge jannat ve😍😍** ",
    " **Tujhko paane ke liye hum🤫🤫** ",
    " **Roz mangein mannat ve😁😁** ",
    " **Duniya to kya cheez hai yaara😏😏** ",
    " **Thukra denge jannat ve😌😌** ",
    " **SO MISS 😶😶** ",
    " **KYA SOCHA APNE BAARE MAIN😆😆** ",
    " **BADI MUSHKIL SE YEH SAB KARA H RE🥵🥵** ",
    " **PAHLE PURA BOT HI KANG MAAR DIYA BUT🤫🤫** ",
    " **WAHI ERROR AAYE JO AATE THE🥲🥲** ",
    " **BUT TUMHARA HO CHUKA WALA BF😎😎** ",
    " **AND FUTURE HUSBAND JO BANNE WALA THA WO BHOT SMART H RE😌😌** ",
    " **ISS BAAR BOT BANAYA AND CHOTA SA EDIT KARA BAS😁😁** ",
    " **AUR DEKO ABHI TUM USSI BOT SE YEH PADH PAA RHI😂😂** ",
    " **HEHE BTW YEH CHORO MEKO NA TUMSE😶😶** ",
    " **KUCH PUCHNA THA KI ME🤔🤔** ",
    " **TUMHARE KABIL HU YA** ",
    " **TUMHARE KABIL NHI😂💓** ",
    " **AND EK AUR BAAT BOLNI THI KI😙😙** ",
    " **I REALLY REALLY DEEPLY😙😙** ",
    " **LOVE YOU FROM MY HEART TO YOUR HEAT AND MY SOUL ATTACHED BY YOUR SOUL CAN YOU BE MINE FOREVER😌😌❤️** ",
]         


@client.on(events.NewMessage(pattern="^/mtag ?(.*)"))
async def mention_all(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond(
            "__This command can be used in groups and channels!__"
        )

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧 𝐂𝐚𝐧 𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐓𝐨 𝐀𝐥𝐥 𝐁𝐚𝐛𝐲...")
    
    if event.pattern_match.group(1):
        return await event.respond("/mtag 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 𝐎𝐤 𝐅𝐨𝐫 𝐓𝐚𝐠𝐠𝐢𝐧𝐠..")
    else:
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
        if msg is None:
            return await event.respond(
                "/mtag 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 𝐎𝐫 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞..."
            )

    spam_chats.append(chat_id)
    async for usr in client.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        user_id = usr.id
        mention_text = f"[{usr.first_name}](tg://user?id={user_id}) {random.choice(MUSIC)}"
        await client.send_message(chat_id, mention_text)
        time.sleep(5)
        
    try:
        spam_chats.remove(chat_id)
    except:
        pass
        
        
        
        
SRAID = [
    " **इश्क़ है या कुछ और ये पता नहीं, पर जो तुमसे है किसी और से नहीं 😁😁** ",
    " **मै कैसे कहू की उसका साथ कैसा है, वो एक शख्स पुरे कायनात जैसा है** ",
    " **तेरा होना ही मेरे लिये खास है, तू दूर ही सही मगर मेरे दिल के पास है** ",
    " **मुझे तेरा साथ ज़िन्दगी भर नहीं चाहिये, बल्कि जब तक तू साथ है तबतक ज़िन्दगी चाहिए 😖😖** ",
    " **तुझसे मोहब्बत कुछ अलग सी है मेरी, तुझे खयालो में नहीं दुआओ में याद करते है😍😍** ",
    " **तू हज़ार बार भी रूठे तो मना लूँगा तुझे** ",
    " **मगर देख मोहब्बत में शामिल कोई दूसरा ना हो😁😁** ",
    " **किस्मत यह मेरा इम्तेहान ले रही है😒😒** ",
    " **तड़प कर यह मुझे दर्द दे रही है😌😌** ",
    " **दिल से कभी भी मैंने उसे दूर नहीं किया😉😉** ",
    " **फिर क्यों बेवफाई का वह इलज़ाम दे रही है😎😎** ",
    " **मरे तो लाखों होंगे तुझ पर😚😚** ",
    " **मैं तो तेरे साथ जीना चाहता हूँ😫😫** ",
    " **वापस लौट आया है हवाओं का रुख मोड़ने वाला😣😣** ",
    " **दिल में फिर उतर रहा है दिल तोड़ने वाला🥺🥺** ",
    " **अपनों के बीच बेगाने हो गए हैं🥰🥰** ",
    " **प्यार के लम्हे अनजाने हो गए हैं😘😘** ",
    " **जहाँ पर फूल खिलते थे कभी😍😍** ",
    " **आज वहां पर वीरान हो गए हैं🥰🥰** ",
    " **जो शख्स तेरे तसव्वुर से हे महक जाये😁😁** ",
    " **सोचो तुम्हारे दीदार में उसका क्या होगा😒😒** ",
    " **मोहब्बत का एहसास तो हम दोनों को हुआ था** ",
    " **फर्क सिर्फ इतना था की उसने किया था और मुझे हुआ था** ",
    " **सांसों की डोर छूटती जा रही है** ",
    " **किस्मत भी हमे दर्द देती जा रही है** ",
    " **मौत की तरफ हैं कदम हमारे** ",
    " **मोहब्बत भी हम से छूटती जा रही है** ",
    " **समझता ही नहीं वो मेरे अलफ़ाज़ की गहराई** ",
    " **मैंने हर लफ्ज़ कह दिया जिसे मोहब्बत कहते है** ",
    " **समंदर न सही पर एक नदी तो होनी चाहिए** ",
    " **तेरे शहर में ज़िन्दगी कही तो होनी चाहिए** ",
    " **नज़रों से देखो तोह आबाद हम हैं** ",
    " **दिल से देखो तोह बर्बाद हम हैं** ",
    " **जीवन का हर लम्हा दर्द से भर गया** ",
    " **फिर कैसे कह दें आज़ाद हम हैं** ",
    " **मुझे नहीं मालूम वो पहली बार कब अच्छा लगा** ",
    " **मगर उसके बाद कभी बुरा भी नहीं** ",
    " **सच्ची मोहब्बत कभी खत्म नहीं होती** ",
    " **वक़्त के साथ खामोश हो जाती है** ",
    " **ज़िन्दगी के सफ़र में आपका सहारा चाहिए** ",
    " **आपके चरणों का बस आसरा चाहिए** ",
    " **हर मुश्किलों का हँसते हुए सामना करेंगे** ",
    " **बस ठाकुर जी आपका एक इशारा चाहिए** ",
    " **जिस दिल में बसा था नाम तेरा हमने वो तोड़ दिया** ",
    " **न होने दिया तुझे बदनाम बस तेरे नाम लेना छोड़ दिया** ",
    " **प्यार वो नहीं जो हासिल करने के लिए कुछ भी करव दे** ",
    " **प्यार वो है जो उसकी खुशी के लिए अपने अरमान चोर दे** ",
    " **आशिक के नाम से सभी जानते हैं😍😍** ",
    " **इतना बदनाम हो गए हम मयखाने में🥰🥰** ",
    " **जब भी तेरी याद आती है बेदर्द मुझे😍😍** ",
    " **तोह पीते हैं हम दर्द पैमाने में🥰🥰** ",
    " **हम इश्क़ के वो मुकाम पर खड़े है😁😁** ",
    " **जहाँ दिल किसी और को चाहे तो गुन्हा लगता है😒😒** ",
    " **सच्चे प्यार वालों को हमेशा लोग गलत ही समझते है👀👀** ",
    " **जबकि टाइम पास वालो से लोग खुश रहते है आज कल🙈🙈** ",
    " **गिलास पर गिलास बहुत टूट रहे हैं😋😋** ",
    " **खुसी के प्याले दर्द से भर रहे हैं🤨🤨** ",
    " **मशालों की तरह दिल जल रहे हैं🤭🤭** ",
    " **जैसे ज़िन्दगी में बदकिस्मती से मिल रहे हैं😌😌** ",
    " **सिर्फ वक़्त गुजरना हो तो किसी और को अपना बना लेना🤫🤫** ",
    " **हम दोस्ती भी करते है तो प्यार की तरह😊😊** ",
    " **जरूरी नहीं इश्क़ में बनहूँ के सहारे ही मिले😏😏** ",
    " **किसी को जी भर के महसूस करना भी मोहब्बत है😚😚** ",
    " **नशे में भी तेरा नाम लब पर आता है😘😘** ",
    " **चलते हुए मेरे पाँव लड़खड़ाते हैं😍😍** ",
    " **दर्द सा दिल में उठता है मेरे😘😘** ",
    " **हसीं चेहरे पर भी दाग नजर आता है😍😍** ",
    " **हमने भी एक ऐसे शख्स को चाहा😝😝** ",
    " **जिसको भुला न सके और वो किस्मत मैं भी नहीं😜😜** ",
    " **सच्चा प्यार किसी भूत की तरह होता है🥰🥰** ",
    " **बातें तो सब करते है देखा किसी ने नहीं😚😚** ",
    " **मत पूछ ये की मैं तुझे भुला नहीं सकता😝😝** ",
    " **तेरी यादों के पन्ने को मैं जला नहीं सकता😜😜** ",
    " **संघर्ष यह है कि खुद को मारना होगा🥰🥰** ",
    " **और अपने सुकून की खातिर तुझे रुला नहीं सकता😚😚** ",
    " **दुनिया को आग लगाने की ज़रूरत नहीं😎😎** ",
    " **नाले दुनिया पुरी घुमावा🙈🙈** ",
    " **तो मेरे साथ चसल आग खुद लग जाएगी💙💙** ",
    " **तरस गये है हम तेरे मुंह से कुछ सुनने को हम🙊🙊** ",
    " **प्यार की बात न सही कोई शिकायत ही कर दे 🙈🙈** ",
    " **तुम नहीं हो पास मगर तन्हाँ रात वही है ❤️❤️** ",
    " **वही है चाहत यादों की बरसात वही है🙈🙈** ",
    " **हर खुशी भी दूर है मेरे आशियाने से ❤️❤️** ",
    " **खामोश लम्हों में दर्द-ए-हालात वही है💫💫** ",
    " **करने लगे जब शिकवा उससे उसकी बेवफाई का😁😁** ",
    " **रख कर होंट को होंट से खामोश कर दिया😆😆** ",
    " **राह में मिले थे हम, राहें नसीब बन गईं😙😙** ",
    " **ना तू अपने घर गया, ना हम अपने घर गये😉😉** ",
    " **तुम्हें नींद नहीं आती तो कोई और वजह होगी😅😅** ",
    " **अब हर ऐब के लिए कसूरवार इश्क तो नहीं😘😘** ",
    " **अना कहती है इल्तेजा क्या करनी😆😆** ",
    " **वो मोहब्बत ही क्या जो मिन्नतों से मिले💕💕** ",
    " **न जाहिर हुई तुमसे और न ही बयान हुई हमसे💓💓** ",
    " **बस सुलझी हुई आँखो में उलझी रही मोहब्बत🥺🥺** ",
    " **गुफ्तगू बंद न हो बात से बात चले🥵🥵** ",
    " **नजरों में रहो कैद दिल से दिल मिले😁😁** ",
    " **है इश्क़ की मंज़िल में हाल कि जैसे😘😘** ",
    " **लुट जाए कहीं राह में सामान किसी का🥰** ",
    " **मुकम्मल ना सही अधूरा ही रहने दो😂😂** ",
    " **ये इश्क़ है कोई मक़सद तो नहीं है🤩🤩** ",
    " **वजह नफरतों की तलाशी जाती है😘😘** ",
    " **मोहब्बत तो बिन वजह ही हो जाती है 😍😍** ",
    " **सिर्फ मरी हुई मछली को ही पानी का बहाव चलाती है 😙😙** ",
    " **जिस मछली में जान होती है वो अपना रास्ता खुद तय करती है** ",
    " **कामयाब लोगों के चेहरों पर दो चीजें होती है 😘😘** ",
    " **एक साइलेंस और दूसरा स्माइल🤔🤔** ",
    " **मेरी चाहत देखनी है तो मेरे दिल पर अपना दिल रखकर देख😌😌** ",
    " **तेरी धड़कन ना भड्जाये तो मेरी मोहब्बत ठुकरा देना🤫🤫** ",
    " **गलतफहमी की गुंजाईश नहीं सच्ची मोहब्बत में🤪🤪** ",
    " **जहाँ किरदार हल्का हो कहानी डूब जाती है☺️☺️** ",
    " **होने दो मुख़ातिब मुझे आज इन होंटो से अब्बास🤗🤗** ",
    " **बात न तो ये समझ रहे है पर गुफ़्तगू जारी है😶😶** ",
    " **उदासियाँ इश्क़ की पहचान है🤗🤗** ",
    " **मुस्कुरा दिए तो इश्क़ बुरा मान जायेगा😗😗** ",
    " **कुछ इस अदा से हाल सुनाना हमारे दिल😘😘** ",
    " **वो खुद ही कह दे किदी भूल जाना बुरी बात है🥲** ",
    " **माना की उससे बिछड़कर हम उमर भर रोते रहे🤔🤔** ",
    " **पर मेरे मार जाने के बाद उमर भर रोएगा वो😅😅** ",
    " **दिल में तुम्हारी अपनी कभी चोर जायेंगे😁😁** ",
    " **आँखों में इंतज़ार की लकीर छोड़ जायेंगे🙈🙈** ",
    " **किसी मासूम लम्हे मैं किसी मासूम चेहरे से🙉🙉** ",
    " **मोहब्बत की नहीं जाती मोहब्बत हो जाती है😌😌** ",
    " **करीब आओ तो शायद हम समझ लोगे😌😌** ",
    " **ये दूरिया तो केवल फसले बढ़ती है🤫🤫** ",
    " **तेरे इश्क़ में इस तरह मैं नीलाम हो जाओ🤔🤔** ",
    " **आखरी हो मेरी बोली और मैं तेरे नाम हो जाऊ😌😌** ",
    " **आप जब तक रहेंगे आंखों में नजारा बनकर😁😁** ",
    " **रोज आएंगे मेरी दुनिया में उजाला बनकर👅👅** ",
    " **उसे जब से बेवफाई की है मैं प्यार की राह में चल ना सका😅😅** ",
    " **उसे तो किसी और का हाथ थाम लियाबस फिर कभी सम्भल नहीं सका👅👅** ",
    " **एक ही ख़्वाब देखा है कई बार मैंने🤬🤬** ",
    " **तेरी शादी में उलझी है चाहिए मेरे घर की😈😈** ",
    " **तुम्हे मेरी मोहब्बत की कसम सच बताना😎😎** ",
    " **गले में डाल कर बाहें किससे सीखाया है😍😍** ",
    " **नहीं पता की वो कभी मेरी थी भी या नहीं😋😋** ",
    " **मुझे ये पता है बस की माई तो था उमर बस उसी का रहा😌😌** ",
    " **तुमने देखा कभी चाँद से पानी गिरते हुए😏😏** ",
    " **मैंने देखा ये मंज़र तू में चेहरा धोते हुए😉😉** ",
    " **ठुकरा दे कोई चाहत को तू हस के सह लेना😊😊** ",
    " **प्यार की तबियत में ज़बर जस्ती नहीं होती😉😉** ",
    " **तेरा पता नहीं पर मेरा दिल कभी तैयार नहीं होगा😌😌** ",
    " **मुझे तेरे अलावा कभी किसी और से प्यार नहीं होगा😍😍** ",
    " **दिल में आहट सी हुई रूह में दस्तक गूँजी🤫🤫** ",
    " **किस की खुशबू ये मुझे मेरे सिरहाने आई😁😁** ",
    " **उम्र भर लिखते रहे फिर भी वारक सदा रहा😏😏** ",
    " **जाने किया लफ्ज़ थे जो हम लिख नहीं पाये😌😌** ",
    " **लगा के फूल हाथों से उसने कहा चुपके से😶😶** ",
    " **अगर यहाँ कोई नहीं होता तो फूल की जगह तुम होते😆😆** ",
    " **जान जब प्यारी थी मरने का शौक था🥵🥵** ",
    " **अब मरने का शौक है तो कातिल नहीं मिल रहा🤫🤫** ",
    " **सिर्फ याद बनकर न रह जाये प्यार मेरा🥲🥲** ",
    " **कभी कभी कुछ वक़्त के लिए आया करो😎😎** ",
    " **मुझ को समझाया ना करो अब तो हो चुकी हूँ मुझ मैं😌😌** ",
    " **मोहब्बत मशवरा होती तो तुम से पूछ लेता😁😁** ",
    " **उन्हों ने कहा बहुत बोलते हो अब क्या बरस जाओगे😂😂** ",
    " **हमने कहा जिस दिन चुप हो गया तुम तरस जाओ गए😶😶** ",
    " **कुछ ऐसे हस्दे ज़िन्दगी मैं होते है🤔🤔** ",
    " **की इंसान तो बच जाता है मगर ज़िंदा नहीं रहता😂💓** ",
]
        
@client.on(events.NewMessage(pattern="^/stag ?(.*)"))
async def mention_all(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond(
            "__This command can be used in groups and channels!__"
        )

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧 𝐂𝐚𝐧 𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐓𝐨 𝐀𝐥𝐥 𝐁𝐚𝐛𝐲...")
    
    if event.pattern_match.group(1):
        return await event.respond("/stag  👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 𝐎𝐤 𝐅𝐨𝐫 𝐓𝐚𝐠𝐠𝐢𝐧𝐠..")
    else:
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
        if msg is None:
            return await event.respond(
                "/stag 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 𝐎𝐫 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞..."
            )

    spam_chats.append(chat_id)
    async for usr in client.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        user_id = usr.id
        mention_text = f"[{usr.first_name}](tg://user?id={user_id}) {random.choice(SRAID)}"
        await client.send_message(chat_id, mention_text)
        time.sleep(5)
        
    try:
        spam_chats.remove(chat_id)
    except:
        pass
        
   
ROMANTIC = [
    "You are the sunshine that brightens up my life.",
    "Every moment with you is like a beautiful dream.",
    "I am forever grateful for the happiness you bring into my life.",
    "Your smile is the most beautiful thing I've ever seen.",
    "My heart belongs to you, now and forever.",
    "In your arms is where I belong.",
    "You are the missing piece in my life's puzzle.",
    "I love you more than words can express.",
    "You complete me in every way.",
    "You are the love of my life.",
    "Every day with you feels like Valentine's Day.",
    "You make my heart skip a beat.",
    "Your love is a treasure I cherish every day.",
    "I am the luckiest person in the world to have you.",
    "Being with you is like a fairy tale come true.",
    "My love for you grows stronger with each passing day.",
    "You are the reason behind my smile.",
    "I can't imagine my life without you in it.",
    "You are the most beautiful person I know, inside and out.",
    "You are the one I want to spend the rest of my life with.",
    "Your love is like a gentle breeze on a hot summer day.",
    "You are the light of my life.",
    "I fall in love with you more and more every day.",
    "You are the best thing that ever happened to me.",
    "I love you to the moon and back.",
    "Your love is my greatest blessing.",
    "You are the music to my heart's melody.",
    "With you, every moment is special.",
    "You are the star that guides me through life's journey.",
    "I am so grateful to have you in my life.",
    "You make my world a better place.",
    "You are the love story I've always dreamed of.",
    "You are my forever love.",
    "I love you with all my heart and soul.",
    "You are my happily ever after.",
    "You are the one who holds the key to my heart.",
    "You are the reason I believe in love.",
    "You are the sweetest thing in my life.",
    "I want to grow old with you.",
    "You are the most amazing person I know.",
    "You are my heart's desire.",
    "My love for you knows no bounds.",
    "You are my one and only.",
    "You are the fire in my heart.",
    "I love you more than all the stars in the sky.",
    "You are the love that fills my soul.",
    "You are the best part of my life.",
    "I love you with all my heart, mind, and soul.",
    "You are the love of my life, today and always.",
    "You are the reason I wake up with a smile every day.",
    "You are my everything.",
    "You are the light of my life's path.",
    "I love you unconditionally.",
    "You are the answer to all my prayers.",
    "You are the most beautiful person I know.",
    "You are the love that completes me.",
    "You are my heart's true desire.",
    "You are the love of my past, present, and future.",
    "I am forever thankful for your love.",
    "You are the melody of my heart.",
    "You are my greatest love story.",
    "You are the reason I believe in forever.",
    "I love you more than words can express.",
    "You are the love of my life, and I cherish every moment with you.",
    "You are the one I want to grow old with.",
    "You are the most precious gift in my life.",
    "You are the love that makes my heart sing.",
    "I love you more and more each day.",
    "You are my one and only true love.",
    "You are the warmth in my heart on a cold night.",
    "You are the love that makes my life complete.",
    "You are my forever love, and I am yours.",
    "You are the love of my dreams.",
    "You are my heart's greatest joy.",
    "You are the love that lights up my world.",
    "You are the love that fills my heart with happiness.",
    "I love you with all my heart, and I always will.",
    "You are the love that makes my life beautiful.",
    "You are the love that makes every day special.",
    "You are the love that makes my heart beat faster.",
    "You are the love that I will cherish forever.",
    "You are the love that gives my life meaning.",
    "You are the love that makes my life complete.",
    "You are the love that I will love for all eternity.",
    "You are the love that I have been searching for.",
    "You are the love that makes my world a better place.",
    "You are the love that makes me smile every day.",
    "You are the love that I will never let go of.",
    "You are the love that I want to spend my life with.",
    "You are the love that makes my heart sing with joy.",
    "You are the love that I am grateful for every day.",
    "You are the love that I will cherish forever.",
    "You are the love that completes me.",
]        

@client.on(events.NewMessage(pattern="^/rtag ?(.*)"))
async def mention_all(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond(
            "__This command can be used in groups and channels!__"
        )

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧 𝐂𝐚𝐧 𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐓𝐨 𝐀𝐥𝐥 𝐁𝐚𝐛𝐲...")
    
    if event.pattern_match.group(1):
        return await event.respond("/rtag  👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 𝐎𝐤 𝐅𝐨𝐫 𝐓𝐚𝐠𝐠𝐢𝐧𝐠..")
    else:
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
        if msg is None:
            return await event.respond(
                "/rtag 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 𝐎𝐫 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞..."
            )

    spam_chats.append(chat_id)
    async for usr in client.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        user_id = usr.id
        mention_text = f"[{usr.first_name}](tg://user?id={user_id}) {random.choice(ROMANTIC)}"
        await client.send_message(chat_id, mention_text)
        time.sleep(5)
        
    try:
        spam_chats.remove(chat_id)
    except:
        pass

CONVEY = [
    "How's it going?",
    "What have you been up to lately?",
    "Do you come here often?",
    "I'm sorry, I didn't catch that. Could you please repeat it?",
    "How was your day?",
    "Can you believe this weather?",
    "Have you heard the latest news?",
    "What's your favorite type of music?",
    "Do you have any plans for the weekend?",
    "What do you do for a living?",
    "I'm a bit tired today. How about you?",
    "What's your favorite movie of all time?",
    "Do you enjoy cooking?",
    "Where are you originally from?",
    "What's your favorite book?",
    "Do you have any siblings?",
    "Have you traveled anywhere interesting recently?",
    "What's your favorite place to eat in town?",
    "How do you like to spend your free time?",
    "Do you have any pets?",
    "Have you ever been to [insert a place]?",
    "What's the most adventurous thing you've done?",
    "Do you like going to concerts?",
    "How do you stay motivated?",
    "What's your dream vacation destination?",
    "Have you tried any new hobbies recently?",
    "Do you prefer coffee or tea?",
    "What's your favorite season?",
    "What's your favorite sport?",
    "What's your go-to karaoke song?",
    "Are you a morning person or a night owl?",
    "Do you like to dance?",
    "What's your favorite holiday?",
    "Do you enjoy hiking?",
    "What's the last movie you watched?",
    "Do you like video games?",
    "What's your favorite board game?",
    "Are you a cat person or a dog person?",
    "Do you believe in aliens?",
    "What's your favorite childhood memory?",
    "What's the best advice you've ever received?",
    "Do you like spicy food?",
    "What's your favorite dessert?",
    "Do you enjoy gardening?",
    "What's the most beautiful place you've been to?",
    "Do you have a favorite quote?",
    "What's your biggest accomplishment?",
    "Do you have a hidden talent?",
    "What's the most interesting book you've read recently?",
    "Are you into fitness?",
    "What's your favorite workout?",
    "What's your favorite type of art?",
    "What's your dream job?",
    "Do you like attending live events?",
    "What's your favorite way to relax?",
    "Do you have any phobias?",
    "What's your favorite type of cuisine?",
    "What's your favorite app on your phone?",
    "Do you like to take photos?",
    "What's your favorite social media platform?",
    "Do you like to cook or order takeout?",
    "What's your favorite childhood TV show?",
    "Do you enjoy stargazing?",
    "What's your favorite planet?",
    "What's your favorite quote from a movie?",
]
                  

@client.on(events.NewMessage(pattern="^/ctag ?(.*)"))
async def mention_all(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond(
            "__This command can be used in groups and channels!__"
        )

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧 𝐂𝐚𝐧 𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐓𝐨 𝐀𝐥𝐥 𝐁𝐚𝐛𝐲...")
    
    if event.pattern_match.group(1):
        return await event.respond("/ctag 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 𝐎𝐤 𝐅𝐨𝐫 𝐓𝐚𝐠𝐠𝐢𝐧𝐠..")
    else:
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
        if msg is None:
            return await event.respond(
                "/ctag 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 𝐎𝐫 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞..."
            )

    spam_chats.append(chat_id)
    async for usr in client.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        user_id = usr.id
        mention_text = f"[{usr.first_name}](tg://user?id={user_id}) {random.choice(CONVEY)}"
        await client.send_message(chat_id, mention_text)
        time.sleep(5)
        
    try:
        spam_chats.remove(chat_id)
    except:
        pass


PUNJABI = [
    "ਤੂੰ ਮੇਰੀ ਆਖਾਂ ਦੀ ਕੰਬਲ, ਮੈਂ ਤੇਰਾ ਦਿਲ ਦਾ ਕੀਤਾ ਇੱਕ ਕੋਨਾ।",
    "ਤੇਰੇ ਬਿਨਾ ਜੀਣਾ ਸਵਾਰਾ, ਰੰਗੀ ਦੁਨੀਆ ਵਿਚ ਬਸਾਰਾ।",
    "ਤੂੰ ਮੇਰੇ ਦਿਲ ਦੀ ਧੜਕਨ, ਤੂੰ ਮੇਰਾ ਇੱਸ਼ਕ ਦਾ ਜਵਾਬ।",
    "ਤੇਰੇ ਬਿਨਾ ਕੁਝ ਵੀ ਨਾਹੀ, ਮੇਰਾ ਦਿਲ ਇੱਕ ਸੁੰਦਰ ਬਿਮਾਰ ਹੈ।",
    "ਤੇਰੀ ਹੱਸੀ ਮੇਰੇ ਦਿਲ ਦੀ ਜਿੰਦਗੀ, ਤੂੰ ਮੇਰੇ ਖੁਸ਼ਿਆਂ ਦਾ ਕਾਰਣ ਹੈ।",
    "ਤੂੰ ਮੇਰੀ ਆਖਾਂ ਦੀ ਰੋਸ, ਤੇਰੇ ਬਿਨਾ ਮੇਰਾ ਦਿਲ ਰੁਕਦਾ ਨਹੀਂ।",
    "ਤੂੰ ਮੇਰਾ ਪਿਆਰ ਹੈ, ਤੂੰ ਮੇਰੀ ਆਸ਼ਿਕੀ ਦਾ ਸਿਰਰਫ ਇੱਕ ਹਿੱਸਾ ਨਹੀਂ।",
    "ਮੈਂ ਤੇਰੀ ਹਰ ਹਸੀ, ਤੁਹਾਨੂੰ ਪਿਆਰ ਦਿਲਾ ਦਿੰਦਾ ਹਾਂ।",
    "ਤੂੰ ਮੇਰੇ ਦਿਲ ਦਾ ਰਾਜਾ ਹੈ, ਤੂੰ ਮੇਰੀ ਆਵਾਜ਼ ਦਾ ਰਾਗ ਹੈ।",
    "ਮੇਰੇ ਲਈ ਤੂੰ ਸਭ ਕੁਝ ਹੈ, ਤੁਹਾਨੂੰ ਖੋਣ ਨੂੰ ਦਿਲ ਚਾਹੁੰਦਾ ਹਾਂ।",
    "ਤੂੰ ਮੇਰੀ ਦੁਨੀਆ ਦਾ ਅੱਖਰੀ ਲਫਜ਼ ਹੈ, ਤੇਰੇ ਬਿਨਾ ਮੇਰੀ ਦੁਨੀਆ ਅਧੂਰੀ ਹੈ।",
    "ਮੈਂ ਤੇਰੇ ਬਿਨਾ ਨਹੀਂ ਜੀ ਸਕਦਾ, ਤੂੰ ਮੇਰੀ ਆਤਮਾ ਦਾ ਹਿੱਸਾ ਹੈ।",
    "ਮੈਂ ਤੁਹਾਨੂੰ ਸਾਰੀ ਉੱਮਰ ਸਥਾਪਤ ਕਰਾਂਗਾ, ਤੇਰੀ ਖੁਸ਼ਬੂ ਨੂੰ ਆਪਣੀ ਛੋਣ ਦੀ ਪੁਰੀ ਜ਼ਿੰਦਗੀ ਬਣਾ ਦੇਵਾਂਗਾ।",
    "ਤੇਰੇ ਬਿਨਾ ਮੇਰੀ ਦੁਨੀਆ ਸੁੰਦਰ ਨਹੀਂ ਲਗਦੀ।",
    "ਤੇਰੇ ਪਿਆਰ ਵਿਚ ਮੈਂ ਖੋਲ ਕੇ ਹਾਂ, ਤੁਹਾਨੂੰ ਅਪਣਾ ਦਿਲ ਦਿੰਦਾ ਹਾਂ।",
    "ਤੂੰ ਮੇਰੇ ਜ਼ਿੰਦਗੀ ਦਾ ਰੰਗ ਹੈ, ਤੂੰ ਮੇਰੇ ਖੁਸ਼ਿਆਂ ਦਾ ਗੀਤ ਹੈ।",
    "ਤੂੰ ਮੇਰੀ ਆਖਾਂ ਦੀ ਪ੍ਰਿਯਤਮਾ, ਮੇਰੇ ਖੰਭ ਦੇ ਅੱਗੇ ਦੀ ਸੁੰਦਰੀ ਕਵੀ।",
    "ਮੈਂ ਤੁਹਾਨੂੰ ਸਾਰੀ ਉੱਮਰ ਨਹੀਂ ਭੁਲਦਾ, ਤੁਹਾਨੂੰ ਪਿਆਰ ਕਰਦਾ ਰਹੇਗਾ।",
    "ਤੂੰ ਮੇਰੀ ਆਸਮਾਨ ਦੀ ਤਾਰਾ, ਮੇਰੇ ਜ਼ਿੰਦਗੀ ਦਾ ਚਾਂਦ ਹੈ।",
    "ਤੂੰ ਮੇਰੀ ਖੁਸ਼ਬੂ ਹੈ, ਮੈਂ ਤੇਰੇ ਬਿਨਾ ਨਹੀਂ ਜੀ ਸਕਦਾ।",
    "ਤੇਰੇ ਨਾਲ ਹੋਣ ਦੀ ਕਿਰਪਾ ਕਰੋ, ਤੇ ਮੇਰੀ ਆਖਾਂ ਦੀ ਰੋਸ ਨਾਲ ਮਿਲੋ।",
    "ਤੇਰੇ ਬਿਨਾ, ਮੇਰੇ ਦਿਲ ਵਿਚ ਖਾਮੋਸੀ ਹੈ।",
    "ਤੂੰ ਮੇਰੇ ਜੀਵਨ ਦਾ ਉਜਾਲਾ, ਮੇਰੇ ਦਿਲ ਦਾ ਚਾਂਦ ਹੈ।",
    "ਤੂੰ ਮੇਰੇ ਬਿਨਾ, ਮੇਰੇ ਦਿਲ ਨੂੰ ਸੁਕੂਣ ਨਹੀਂ ਮਿਲਦਾ।",
    "ਤੂੰ ਮੇਰੇ ਜੀਵਨ ਦਾ ਅੱਖਰੀ ਹੱਸੀ ਹੈ, ਤੂੰ ਮੇਰੀ ਦੁਨੀਆ ਦਾ ਅੱਖਰੀ ਇੱਕ ਅੱਖਰੀ ਅੱਖਰੀ ਹੱਸੀ ਹੈ।",
    "ਮੈਂ ਤੁਹਾਨੂੰ ਸਾਰੀ ਉੱਮਰ ਦਾ ਸਾਥੀ ਬਣਾਂਗਾ, ਤੇਰੇ ਨਾਲ ਜੀਵਨ ਦਾ ਹਰ ਪੱਲ ਆਨੰਦਮਯੀ ਹੋਵੇਗਾ।",
    "ਮੈਂ ਤੁਹਾਨੂੰ ਸਾਰੀ ਉੱਮਰ ਨਹੀਂ ਭੁਲਦਾ, ਤੁਸੀਂ ਮੇਰੀ ਜ਼ਿੰਦਗੀ ਦੀ ਸਭ ਕੁਝ ਹੋ।",
    "ਤੂੰ ਮੇਰੀ ਜ਼ਿੰਦਗੀ ਦੀ ਸਭ ਕੁਝ ਹੈ, ਤੂੰ ਮੇਰਾ ਸੱਚਾ ਪਿਆਰ ਹੈ।",
    "ਤੂੰ ਮੇਰੀ ਜ਼ਿੰਦਗੀ ਦੀ ਚਮਕ, ਤੇਰੀ ਹੱਸੀ ਦੀ ਸਵਾਰੀ ਹੈ।",
    "ਮੈਂ ਤੁਹਾਨੂੰ ਸਾਰੀ ਉੱਮਰ ਦਾ ਸਾਥੀ ਬਣਾਂਗਾ, ਤੇਰੇ ਬਿਨਾ ਜੀਵਨ ਨਾਮੂਨਾ ਹੋਵੇਗਾ।",
    "ਮੈਂ ਤੁਹਾਨੂੰ ਸਾਰੀ ਉੱਮਰ ਨਹੀਂ ਭੁਲਦਾ, ਤੁਹਾਨੂੰ ਪਿਆਰ ਦੀ ਦੁਨੀਆ ਦੇ ਰੰਗ ਦਿੰਦਾ ਹਾਂ।",
    "ਤੂੰ ਮੇਰੀ ਜ਼ਿੰਦਗੀ ਦਾ ਚਾਂਦ, ਤੇਰੇ ਬਿਨਾ ਮੇਰਾ ਦਿਨ ਸੁਨਸਾਨ ਹੈ।",
    "ਤੂੰ ਮੇਰੀ ਜ਼ਿੰਦਗੀ ਦਾ ਸੁੰਦਰ ਖੰਭ, ਤੇਰੇ ਬਿਨਾ ਮੇਰੀ ਜ਼ਿੰਦਗੀ ਅਧੂਰੀ ਹੈ।",
    "ਮੈਂ ਤੁਹਾਨੂੰ ਸਾਰੀ ਉੱਮਰ ਨਹੀਂ ਭੁਲਦਾ, ਤੁਹਾਨੂੰ ਪਿਆਰ ਦੇ ਅੰਗ ਬਣਾਂਗਾ।",
    "ਤੂੰ ਮੇਰੇ ਜਿੰਦਗੀ ਦਾ ਰੰਗ, ਤੇਰੇ ਬਿਨਾ ਮੇਰੀ ਦੁਨੀਆ ਬੇਰੰਗ ਹੈ।",
    "ਤੂੰ ਮੇਰੀ ਜ਼ਿੰਦਗੀ ਦਾ ਸੋਹਣਾ ਪੱਟ, ਤੇਰੇ ਬਿਨਾ ਮੇਰਾ ਦਿਲ ਸੁੰਦਰ ਨਹੀਂ ਲਗਦਾ।",
    "ਮੈਂ ਤੁਹਾਨੂੰ ਸਾਰੀ ਉੱਮਰ ਨਹੀਂ ਭੁਲਦਾ, ਤੁਹਾਨੂੰ ਪਿਆਰ ਦੀ ਸਿਪਾਹੀ ਬਣਾਂਗਾ।",
    "ਤੂੰ ਮੇਰੇ ਜ਼ਿੰਦਗੀ ਦਾ ਸੁੰਦਰ ਰੰਗ, ਤੇਰੇ ਬਿਨਾ ਮੇਰਾ ਦਿਲ ਬਿਨਾ ਰੰਗ ਹੈ।",
    "ਤੂੰ ਮੇਰੇ ਦਿਲ ਦਾ ਸਚਾ ਪਿਆਰ, ਤੇਰੇ ਬਿਨਾ ਮੇਰੇ ਜਿੰਦਗੀ ਬੇਮਾਨ ਹੈ।",
    "ਮੈਂ ਤੁਹਾਨੂੰ ਸਾਰੀ ਉੱਮਰ ਨਹੀਂ ਭੁਲਦਾ, ਤੁਹਾਨੂੰ ਪਿਆਰ ਦਾ ਹੱਸੀ ਦੀ ਮਿਸਾਲ ਬਣਾਂਗਾ।",
    "ਤੂੰ ਮੇਰੇ ਜ਼ਿੰਦਗੀ ਦਾ ਸਬ ਕੁਛ, ਤੇਰੇ ਬਿਨਾ ਮੇਰਾ ਜੀਵਨ ਅਧੂਰਾ ਹੈ।",
    "ਤੂੰ ਮੇਰੇ ਦਿਲ ਦਾ ਰਾਜਾ, ਤੇਰੇ ਬਿਨਾ ਮੇਰਾ ਦਿਲ ਸੁੰਦਰ ਨਹੀਂ ਲਗਦਾ।",
    "ਤੂੰ ਮੇਰੇ ਜੀਵਨ ਦਾ ਆਸਮਾਨ, ਤੇਰੇ ਬਿਨਾ ਮੇਰੀ ਦੁਨੀਆ ਬੇਸਿਮਾਰ ਹੈ।",
    "ਤੂੰ ਮੇਰੇ ਖੁਸ਼ਿਆਂ ਦਾ ਕਾਰਣ, ਤੇਰੇ ਬਿਨਾ ਮੇਰੇ ਜੀਵਨ ਵਿਚ ਖੁਸ਼ਬੂ ਹੈ।",
    "ਮੈਂ ਤੁਹਾਨੂੰ ਸਾਰੀ ਉੱਮਰ ਦਾ ਸਾਥੀ ਬਣਾਂਗਾ, ਤੁਹਾਨੂੰ ਪਿਆਰ ਦੀ ਮਿਸਾਲ ਬਣਾਂਗਾ।",
    "ਮੈਂ ਤੁਹਾਨੂੰ ਸਾਰੀ ਉੱਮਰ ਨਹੀਂ ਭੁਲਦਾ, ਤੁਸੀਂ ਮੇਰੀ ਦਿਲ ਦੀ ਆਵਾਜ਼ ਹੋ।",
    "ਤੂੰ ਮੇਰੇ ਜਿੰਦਗੀ ਦਾ ਰੰਗ, ਤੇਰੇ ਬਿਨਾ ਮੇਰੀ ਦੁਨੀਆ ਅਧੂਰੀ ਹੈ।",
    "ਤੂੰ ਮੇਰੇ ਦਿਲ ਦਾ ਸਚਾ ਪਿਆਰ, ਤੇਰੇ ਬਿਨਾ ਮੇਰੇ ਜਿੰਦਗੀ ਦਾ ਸਬ ਕੁਛ ਖੋਜ ਹੈ।",
    "ਮੈਂ ਤੁਹਾਨੂੰ ਸਾਰੀ ਉੱਮਰ ਨਹੀਂ ਭੁਲਦਾ, ਤੁਸੀਂ ਮੇਰੇ ਜੀਵਨ ਦਾ ਉਜਾਲਾ ਹੋ।",
    "ਤੂੰ ਮੇਰੇ ਜੀਵਨ ਦਾ ਸੁੰਦਰ ਖੰਭ, ਤੇਰੇ ਬਿਨਾ ਮੇਰਾ ਦਿਲ ਸੁੰਦਰ ਨਹੀਂ ਲਗਦਾ।",
    "ਮੈਂ ਤੁਹਾਨੂੰ ਸਾਰੀ ਉੱਮਰ ਦਾ ਸਾਥੀ ਬਣਾਂਗਾ, ਤੇਰੇ ਬਿਨਾ ਮੇਰੀ ਜਿੰਦਗੀ ਬਿਨਾ ਰੰਗ ਹੈ।",
    "ਮੈਂ ਤੁਹਾਨੂੰ ਸਾਰੀ ਉੱਮਰ ਨਹੀਂ ਭੁਲਦਾ, ਤੁਸੀਂ ਮੇਰੀ ਜਿੰਦਗੀ ਦਾ ਚਾਂਦ ਹੋ।",
    "ਤੂੰ ਮੇਰੇ ਜਿੰਦਗੀ ਦਾ ਰੰਗ, ਤੇਰੇ ਬਿਨਾ ਮੇਰਾ ਦਿਲ ਗੇਹੇ ਦਾ ਮੋਤੀ ਹੈ।",
    "ਤੂੰ ਮੇਰੇ ਦਿਲ ਦਾ ਸਚਾ ਪਿਆਰ, ਤੇਰੇ ਬਿਨਾ ਮੇਰਾ ਦਿਲ ਬਿਨਾ ਚੰਗੇ ਸੁੰਦਰ ਹੈ।",
    "ਮੈਂ ਤੁਹਾਨੂੰ ਸਾਰੀ ਉੱਮਰ ਦਾ ਸਾਥੀ ਬਣਾਂਗਾ, ਤੁਸੀਂ ਮੇਰੀ ਜਿੰਦਗੀ ਦੇ ਸਬ ਕੁਛ ਹੋ।",
    "ਮੈਂ ਤੁਹਾਨੂੰ ਸਾਰੀ ਉੱਮਰ ਨਹੀਂ ਭੁਲਦਾ, ਤੁਹਾਨੂੰ ਪਿਆਰ ਦੇ ਰੰਗ ਦੇ ਰੰਗੀ ਬਣਾਂਗਾ।",
    "ਤੂੰ ਮੇਰੇ ਜ਼ਿੰਦਗੀ ਦਾ ਚਾਂਦ, ਤੇਰੇ ਬਿਨਾ ਮੇਰੇ ਜੀਵਨ ਦਾ ਸੁੰਦਰ ਰੰਗ ਹੈ।",
    "ਤੂੰ ਮੇਰੇ ਦਿਲ ਦਾ ਸਚਾ ਪਿਆਰ, ਤੇਰੇ ਬਿਨਾ ਮੇਰੇ ਜਿੰਦਗੀ ਦਾ ਸੁੰਦਰ ਰੰਗ ਹੈ।",
    "ਮੈਂ ਤੁਹਾਨੂੰ ਸਾਰੀ ਉੱਮਰ ਦਾ ਸਾਥੀ ਬਣਾਂਗਾ, ਤੁਸੀਂ ਮੇਰੇ ਸਚਾ ਪਿਆਰ ਦੀ ਮਿਸਾਲ ਹੋ।",
    "ਮੈਂ ਤੁਹਾਨੂੰ ਸਾਰੀ ਉੱਮਰ ਨਹੀਂ ਭੁਲਦਾ, ਤੁਹਾਨੂੰ ਪਿਆਰ ਦੇ ਸਚਾ ਪਿਆਰ ਦਾ ਸਚਾ ਪਿਆਰ ਦੀ ਸਿਪਾਹੀ ਬਣਾਂਗਾ।",
    "ਤੂੰ ਮੇਰੇ ਦਿਲ ਦਾ ਸਚਾ ਪਿਆਰ, ਤੇਰੇ ਬਿਨਾ ਮੇਰੇ ਜਿੰਦਗੀ ਦਾ ਸਭ ਕੁਛ ਬੇਹੱਦ ਸੁੰਦਰ ਹੈ।",
    "ਮੈਂ ਤੁਹਾਨੂੰ ਸਾਰੀ ਉੱਮਰ ਦਾ ਸਾਥੀ ਬਣਾਂਗਾ, ਤੁਹਾਨੂੰ ਪਿਆਰ ਦੀ ਸਭ ਕੁਝ ਸਾਂਝਾ ਕਰਨ ਦਾ ਸਾਥੀ ਬਣਾਂਗਾ।",
    "ਮੈਂ ਤੁਹਾਨੂੰ ਸਾਰੀ ਉੱਮਰ ਨਹੀਂ ਭੁਲਦਾ, ਤੁਹਾਨੂੰ ਪਿਆਰ ਦੇ ਰੰਗ ਦੇ ਰੰਗੀ ਬਣਾਂਗਾ।",
    "ਤੂੰ ਮੇਰੇ ਜ਼ਿੰਦਗੀ ਦਾ ਚਾਂਦ, ਤੇਰੇ ਬਿਨਾ ਮੇਰੇ ਜੀਵਨ ਦਾ ਸੁੰਦਰ ਖੰਭ ਹੈ।",
    "ਤੂੰ ਮੇਰੇ ਦਿਲ ਦਾ ਸਚਾ ਪਿਆਰ, ਤੇਰੇ ਬਿਨਾ ਮੇਰਾ ਦਿਲ ਦੇ ਸਚਾ ਪਿਆਰ ਦਾ ਸਚਾ ਪਿਆਰ ਹੈ।",
]


@client.on(events.NewMessage(pattern="^/ptag ?(.*)"))
async def mention_all(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond(
            "__This command can be used in groups and channels!__"
        )

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧 𝐂𝐚𝐧 𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐓𝐨 𝐀𝐥𝐥 𝐁𝐚𝐛𝐲...")
    
    if event.pattern_match.group(1):
        return await event.respond("/ptag 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 𝐎𝐤 𝐅𝐨𝐫 𝐓𝐚𝐠𝐠𝐢𝐧𝐠..")
    else:
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
        if msg is None:
            return await event.respond(
                "/ptag 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 𝐎𝐫 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞..."
            )

    spam_chats.append(chat_id)
    async for usr in client.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        user_id = usr.id
        mention_text = f"[{usr.first_name}](tg://user?id={user_id}) {random.choice(PUNJABI)}"
        await client.send_message(chat_id, mention_text)
        time.sleep(5)
        
    try:
        spam_chats.remove(chat_id)
    except:
        pass


INDO = [
    "Kaulah sinar matahari dalam hidupku.",
    "Jatuh cinta padamu adalah seperti bunga-bunga mekar di hatiku.",
    "Bersamamu, setiap hari adalah petualangan yang tak terlupakan.",
    "Cintaku untukmu tak akan pernah pudar, seperti bintang yang selalu bersinar di langit malam.",
    "Kaulah nafas segar dalam pagi hariku.",
    "Ketika kita bersama, dunia terasa sempurna.",
    "Cintaku untukmu lebih dalam dari lautan yang tak berujung.",
    "Kau adalah senyum terindah dalam hidupku.",
    "Denganmu, aku merasa lengkap.",
    "Kaulah mata air kebahagiaanku.",
    "Cinta kita bagaikan lagu yang indah, selalu terdengar dalam hatiku.",
    "Ketika kau tersenyum, dunia terasa lebih cerah.",
    "Setiap detik bersamamu adalah berharga.",
    "Cintaku padamu bagaikan api yang tak pernah padam.",
    "Ketika kita bersama, waktu terasa berhenti.",
    "Kaulah keajaiban dalam hidupku.",
    "Cintaku untukmu tak bisa diukur, karena tak terbatas.",
    "Kaulah impian yang selalu kuinginkan.",
    "Bersamamu adalah tempat terbaik dalam dunia ini.",
    "Cintaku padamu adalah seperti hujan lebat yang mengalir di hatiku.",
    "Ketika kau dekat, hatiku berdebar lebih cepat.",
    "Cintaku padamu melebihi segala kata-kata.",
    "Kau adalah bagian terindah dalam hidupku.",
    "Bersamamu adalah semua yang kubutuhkan.",
    "Cintaku untukmu tak akan pernah luntur.",
    "Kaulah cinta sejati dalam hidupku."
]


@client.on(events.NewMessage(pattern="^/itag ?(.*)"))
async def mention_all(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond(
            "__This command can be used in groups and channels!__"
        )

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧 𝐂𝐚𝐧 𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐓𝐨 𝐀𝐥𝐥 𝐁𝐚𝐛𝐲...")
    
    if event.pattern_match.group(1):
        return await event.respond("/itag 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 𝐎𝐤 𝐅𝐨𝐫 𝐓𝐚𝐠𝐠𝐢𝐧𝐠..")
    else:
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
        if msg is None:
            return await event.respond(
                "/itag 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 𝐎𝐫 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞..."
            )

    spam_chats.append(chat_id)
    async for usr in client.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        user_id = usr.id
        mention_text = f"[{usr.first_name}](tg://user?id={user_id}) {random.choice(INDO)}"
        await client.send_message(chat_id, mention_text)
        time.sleep(5)
        
    try:
        spam_chats.remove(chat_id)
    except:
        pass



ARABIC = [
    "حينما نلتقي، يصبح العالم أكثر سحرًا.",
    "عندما أنظر إليك، يمتلئ قلبي بالسعادة.",
    "لقاؤنا كان مثل القدر، مكتوب منذ الأزل.",
    "أنت ليس فقط حبيبي، بل أنت صديقي الأعز وروحي.",
    "عيونك تحمل الكثير من الأسرار الجميلة.",
    "كلما ابتسمت، يزهر العالم من حولي.",
    "أحب أن أمضي كل لحظة معك.",
    "حياتي لا تكتمل إلا بك بجانبي.",
    "صوتك يعزف أجمل الألحان في قلبي.",
    "أحبك بكل ما أملك وبكل ما أكون عليه.",
    "أنت نجمة ساطعة في سمائي اللامتناهية.",
    "لا توجد كلمات تكفي لوصف مدى حبي لك.",
    "قلبي ينبض بقوة كلما كنت بجواري.",
    "أنت أملي وسعادتي في هذه الحياة.",
    "أنت تمنح الحياة معنى وجمالًا.",
    "أتمنى أن يستمر حبنا إلى الأبد وأبعد.",
    "بجانبك أجد السلام والسعادة.",
    "عندما تبتسم، تنير حياتي كالشمس.",
    "قلبي يخبرني دائمًا أنك الشخص الصحيح بالنسبة لي.",
    "حياتي معك هي أفضل حياة يمكنني أن أحلم بها.",
    "أنت جميلة من الداخل والخارج.",
    "لطالما أعشق أوقاتنا المميزة سويًا.",
    "أنت عالمي وكل شيء فيه.",
    "بجانبك أشعر بالأمان والحماية.",
    "أنت نعمة لا تقدر بثمن في حياتي.",
    "لن أتوقف أبدًا عن حبك واهتمامي بك.",
    "أنت اللغز الذي أريد أن أحله طوال حياتي.",
    "عندما أقول 'أحبك'، فإن ذلك يعني الكثير.",
    "لا يوجد أجمل من تواجدك في حياتي.",
    "أنت رمز الجمال والأناقة بالنسبة لي.",
    "كل يوم أقضيه معك هو يوم جميل وسعيد.",
    "علاقتنا هي أكثر من مجرد حب، إنها مغامرة رائعة.",
    "لا يهم ما يحدث، سأكون دائمًا بجانبك.",
    "أحب أن أسمع صوتك وأرى وجهك كل يوم.",
    "أنت ملاذي ومصدر قوتي في الأوقات الصعبة.",
    "ببساطة، أنت حب حياتي وأملي الوحيد.",
    "أنت تمنح الحياة لونًا وجمالًا مختلفًا.",
    "بجانبك أجد السعادة التي بحثت عنها طويلاً.",
    "عندما تضحك، يضيء يومي بالسرور.",
    "أنت سبب ابتسامتي وفرحي الدائم.",
    "حبك هو أجمل هدية أنعم بها.",
    "أتمنى أن تظلي دائمًا بجانبي في كل رحلة.",
    "قلبي ينبض باسمك فقط، أنت حب حياتي.",
    "لا توجد كلمات تصف مدى عظمة مشاعري نحوك.",
    "أنت الشخص الذي أريد أن أقضي باقي حياتي معه.",
    "أنت أماني وأحلامي التي تتحقق يومًا بعد يوم.",
    "أنت الشخص الوحيد الذي يجعل قلبي ينبض بقوة.",
    "حينما أكون بجانبك، أشعر أني في عالم آخر.",
    "أحبك لأنك أنت، وليس لأي شيء آخر.",
    "أنت مصدر الفرح في حياتي وسبب ابتسامتي.",
    "كل لحظة معك هي لحظة قيمة في حياتي.",
    "لا توجد كلمات تفيك حقك في قلبي.",
]


@client.on(events.NewMessage(pattern="^/atag ?(.*)"))
async def mention_all(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond(
            "__This command can be used in groups and channels!__"
        )

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧 𝐂𝐚𝐧 𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐓𝐨 𝐀𝐥𝐥 𝐁𝐚𝐛𝐲...")
    
    if event.pattern_match.group(1):
        return await event.respond("/atag 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 𝐎𝐤 𝐅𝐨𝐫 𝐓𝐚𝐠𝐠𝐢𝐧𝐠..")
    else:
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
        if msg is None:
            return await event.respond(
                "/atag 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 𝐎𝐫 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞..."
            )

    spam_chats.append(chat_id)
    async for usr in client.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        user_id = usr.id
        mention_text = f"[{usr.first_name}](tg://user?id={user_id}) {random.choice(ARABIC)}"
        await client.send_message(chat_id, mention_text)
        time.sleep(5)
        
    try:
        spam_chats.remove(chat_id)
    except:
        pass





@client.on(events.NewMessage(pattern="^/cancel$"))
@client.on(events.NewMessage(pattern="^/stop$"))
async def cancel_spam(event):
    if not event.chat_id in spam_chats:
        return await event.respond("𝐇𝐞𝐫𝐞 𝐍𝐨 𝐀𝐧𝐲 𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐈𝐬 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐁𝐲 𝐌𝐞..")
    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐈𝐬 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐀𝐝𝐦𝐢𝐧𝐬.. 𝐘𝐨𝐮 𝐂𝐚𝐧'𝐭 𝐔𝐬𝐞 𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝..")

    else:
        try:
            spam_chats.remove(event.chat_id)
        except:
            pass
        return await event.respond("♦𝐒𝐭𝐨𝐩𝐩𝐞𝐝 𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐁𝐚𝐛𝐲♦")


