import sys
import asyncio

from os import execle, getenv, environ

from pyrogram import Client, filters, idle
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler
from pyrogram.errors import FloodWait


# ------------- SESSIONS -------------

SESSION1 = getenv('SESSION1', default=None)
SESSION2 = getenv('SESSION2', default=None)
SESSION3 = getenv('SESSION3', default=None)
SESSION4 = getenv('SESSION4', default=None)
SESSION5 = getenv('SESSION5', default=None)


# ------------- CLIENTS -------------

if SESSION1:
    M1 = Client(SESSION1, api_id=25981592, api_hash="709f3c9d34d83873d3c7e76cdd75b866")
else:
    M1 = None

if SESSION2:
    M2 = Client(SESSION2, api_id=25981592, api_hash="709f3c9d34d83873d3c7e76cdd75b866")
else:
    M2 = None

if SESSION3:
    M3 = Client(SESSION3, api_id=25981592, api_hash="709f3c9d34d83873d3c7e76cdd75b866")
else:
    M3 = None

if SESSION4:
    M4 = Client(SESSION4, api_id=25981592, api_hash="709f3c9d34d83873d3c7e76cdd75b866")
else:
    M4 = None

if SESSION5:
    M5 = Client(SESSION5, api_id=25981592, api_hash="709f3c9d34d83873d3c7e76cdd75b866")
else:
    M5 = None


ONE_WORDS = ["k⃠y⃠a⃠", "r⃠e⃠", "r⃠n⃠d⃠i⃠", "k⃠a⃠l⃠a⃠p⃠", "r⃠a⃠", "𝐒𝐏𝐄𝐄𝐃", "𝐋𝐀", "𝐀𝐀𝐀𝐁", "𝐒𝐂𝐑𝐈𝐏𝐓", "𝐁𝐎𝐋", "𝐊𝐄", "𝐑𝐎", "𝐃𝐄𝐆𝐀", "𝐓𝐔", 
    "𝐓𝐀𝐓𝐓𝐄", "𝐁𝐇𝐀𝐆", "𝐌𝐀𝐓", "𝐒𝐏𝐄𝐄𝐃", "𝐏𝐀𝐊𝐀𝐃", "𝐀𝐀𝐀𝐁", "𝐓𝐔𝐔", "𝐂𝐇𝐔𝐃", "𝐊𝐄 ", "𝐅𝐑𝐀𝐑",
    "𝐇𝐎𝐆𝐀", "𝐁𝐇𝐀𝐆𝐍𝐀 ", "𝐌𝐀𝐓", "𝐎𝐍𝐄", "𝐏𝐋𝐔𝐒", "𝐎𝐍𝐄", "𝐓𝐄𝐑𝐈", "𝐌𝐀", "𝐊𝐈", "𝐂𝐇𝐔𝐓", "𝐌𝐄", "𝐆𝐘𝐀",
    "𝐋𝐔𝐍𝐃", "𝐓𝐄𝐑𝐄", "𝐊𝐇𝐀𝐍𝐃𝐀𝐍", "𝐌𝐄", "𝐒𝐀𝐀𝐑𝐈", "𝐋𝐀𝐃𝐊𝐈𝐀𝐀", "𝐂𝐇𝐔𝐃𝐄𝐆𝐈", "𝐌𝐀𝐀", "𝐊𝐄", "𝐋𝐖𝐃𝐄", "𝐓𝐄𝐑𝐈𝐈",
    "𝐌𝐀𝐀", "𝐊𝐈", "𝐆𝐀𝐍𝐃🍑", "𝐏𝐄", "𝐓𝐇𝐀𝐏𝐀𝐃", "𝐌𝐀𝐑𝐔𝐍𝐆𝐀", "𝐈𝐓𝐍𝐄", "𝐍𝐀", "𝐉𝐀𝐀𝐍𝐄", "𝐊𝐈𝐓𝐍𝐄", "𝐓𝐄𝐑𝐈", "𝐌𝐀",
    "𝐊𝐈","𝐆𝐀𝐍𝐃","𝐌𝐄","𝐌𝐄𝐑𝐀","𝐊𝐀𝐋𝐀","𝐋𝐔𝐍𝐃🍆","𝐌𝐀𝐀𝐀","𝐊𝐄","𝐋𝐖𝐃𝐄𝐄𝐄𝐄𝐄𝐄𝐄","𝐀𝐉𝐀𝐀𝐀𝐀","𝐒𝐏𝐄𝐄𝐄𝐄𝐃𝐃𝐃𝐃𝐃","𝐋𝐀𝐀𝐀𝐀𝐀𝐀","𝐓𝐀𝐓𝐓𝐓𝐄𝐄","𝐑𝐎 𝐆𝐘𝐀 𝐒𝐔𝐀𝐑", 
    "𝐓𝐄𝐑𝐈𝐈","𝐁𝐔𝐀","𝐊𝐀","𝐑𝐀𝐎𝐄","𝐊𝐀𝐑","𝐃𝐈𝐀𝐀𝐀","𝐓𝐄𝐑𝐈𝐈","𝐌𝐀𝐀𝐀","𝐊𝐈𝐈𝐈","𝐒𝐄𝐗𝐘𝐘","𝐂𝐇𝐔𝐓𝐓𝐓𝐓","𝐋𝐖𝐃𝐑𝐄𝐄𝐄","𝐓𝐀𝐓𝐓𝐓𝐓𝐄𝐄","𝐅𝐑𝐀𝐑",
    "𝐇𝐎","𝐆𝐘𝐀","𝐀𝐀𝐁","𝗞𝗜𝗧𝗡𝗔𝗔𝗔","𝗥𝗢𝗬𝗘𝗚𝗔𝗔𝗔","𝗔𝗝𝗔𝗔𝗔","𝗧𝗔𝗧𝗧𝗧𝗘𝗘","#𝗜𝗡𝗦𝗔𝗡𝗘_𝗢𝗣","𝗙𝗥𝗔𝗥","𝗡𝗔𝗔𝗔","𝗛𝗢𝗢𝗢","𝗔𝗔𝗨𝗞𝗔𝗔𝗧𝗧",
    "𝗟𝗘𝗦𝗦𝗦","𝗕𝗔𝗔𝗖𝗖𝗛𝗛𝗘𝗘","𝗕𝗛𝗔𝗔𝗔𝗔𝗚𝗚𝗚𝗚","𝗠𝗔𝗔𝗔𝗧","𝗧𝗔𝗧𝗧𝗧𝗧𝗧𝗘𝗘𝗘𝗘𝗘","𝗔𝗔𝗝𝗔𝗔𝗔𝗔","𝗞𝗛𝗔𝗔𝗔𝗔𝗔𝗔","𝗕𝗛𝗔𝗔𝗚𝗚𝗚𝗚","𝗚𝗬𝗔𝗔𝗔𝗔𝗔𝗔𝗔","𝗧𝗘𝗥𝗜𝗜𝗜𝗜𝗜","𝗠𝗔𝗔𝗔𝗔𝗔 ","𝗞𝗜𝗜𝗜","𝗦𝗘𝗫𝗬👅",
    "𝗫𝗛𝗨𝗧𝗧𝗧","𝗠𝗔𝗥𝗨","𝗧𝗘𝗥𝗘","𝗞𝗛𝗔𝗡𝗗𝗔𝗡","𝗞𝗔𝗔𝗔","𝗕𝗛𝗢𝗫𝗗𝗔𝗔𝗔𝗔𝗔𝗔𝗔","𝗙𝗔𝗧𝗧𝗧𝗧","𝗚𝗬𝗔𝗔𝗔","𝗦𝗣𝗘𝗘𝗗⚡️","𝗕𝗗𝗔","𝗟𝗘𝗘𝗘","𝐀𝐉𝐀","𝐁𝐀𝐋𝐀𝐊","𝐀𝐁𝐁",
    "𝐒𝐏𝐄𝐄𝐄𝐃𝐃","𝐂𝐕𝐑𝐑𝐑𝐑","𝐍𝐀","𝐇𝐎𝐑𝐈","𝐊𝐘𝐀𝐀𝐐","𝐓𝐀𝐓𝐓𝐓𝐄","𝐒𝐂𝐑𝐈𝐏𝐓","𝐁𝐎𝐋𝐋𝐋","𝐊𝐄𝐄","𝐑𝐎𝐎","𝐑𝐀𝐀","𝐒𝐔𝐀𝐀𝐀𝐑",
    "𝐊𝐄𝐄𝐄𝐄","𝐓𝐀𝐓𝐓𝐓𝐓𝐄","𝐁𝐇𝐄𝐍𝐍𝐍","𝐊𝐄𝐄𝐄","𝐓𝐀𝐊𝐄","𝐓𝐔","𝐆𝐀𝐋𝐈","𝐃𝐄𝐆𝐀𝐀","𝐒𝐏𝐄𝐄𝐃","𝐋𝐀𝐀𝐀","𝐀𝐁𝐁𝐁𝐁","𝐓𝐀𝐓𝐓𝐓𝐄","𝐁𝐇𝐄𝐍𝐍𝐍",
    "𝐊𝐄𝐄𝐄","𝐋𝐖𝐃𝐄𝐄𝐄𝐄𝐄𝐄𝐄𝐄𝐄𝐄𝐄𝐄","𝐀𝐁𝐁𝐁","𝐁𝐎𝐋","🇹 🇦 🇹 🇪 ","🄼🄰🄰🄰","🅺︎🅴︎","ꪶ᭙ᦔꫀ","丂卩乇乇ᗪ ㄥ卂","Ҝㄚ卂卂","尺乇乇","ㄒㄩㄩ","BANEGA","𝗙𝗬𝗧𝗥",
    "𝗦𝗣𝗘𝗘𝗗","𝗟𝗔𝗔𝗔𝗔","𝗟𝗢𝗗𝗘𝗘𝗘𝗘","𝗧𝗔𝗧𝗧𝗧𝗘","CHAAR","CHAWNII","GHODEE","PEEE","TUMM","MEREE","LODEE","PEE","TERI",
    "MAA","𝗞𝗘𝗘𝗘","BOOBS","DABATA HU", "TERI", "MAA", "KI", "CHUT", "𝗔𝗝𝗔𝗔", "TERI", "MAA", "KI", "CHUT", "AJA", "TERI", "MAA", "KI", "CHUT", "FAAD", "DUNGA", "HIJDE", "TERA", "BAAP",
           "HU", "KIDXX", "SPEED", "PAKAD", "BHEN KE LAUDE", "AA BETA", "AAGYA", "TERI", "MAA ", "CHODNE",
           "AB", "TERI ", "MAA", "CHUDEGI", "KUTTE", "KI", "TARAH", "BETA", "TERI", "MAA", "KE", "BHOSDE",
           "ME", "JBL", "KE", "SPEAKER", "DAAL", "KAR", "BASS", "BOOSTED", "SONG", "SUNUNGA", "PURI",
           "RAAT", "LAGATAR", "TERI", "MAA", "KE", "SATH", "SEX", "KARUNGA🔥", "TERI", "MAA", "KE", "BOOBS",
           "DABAUNGA","XXX","TERI","MAA","KAA","CHUT","MARU","RANDI","KEE","PILEE","TERI","MAA","KAA","BHOSDAA",
           "MARU","SUAR","KEE","CHODE","TERI","MAAA","KEEE","NUDES","BECHUNGA","RANDI","KEE","PILLE","TERI","MAAA",
           "CHODU","SUAR","KEEE","PILEE","TERIII","MAAA","DAILYY","CHUDTTI","HAII","MADHARCHOD","AUKAT","BANAA",
           "LODE","TERAA","BAAP","HUU","TERI","GFF","KAA","BHOSDAA","MARUU","MADHARCHOD","TERI ","NANAI","KAA",
           "CHUTT","MARU","TERII","BEHEN","KAAA","BHOSDAA","MARU","RANDII","KEEE","CHODE","TERI","DADI","KAAA","BOOR",
           "GARAM","KARR","TERE","PUREE","KHANDAN","KOOO","CHODUNGAA","BAAP","SEE","BAKCHODI","KAREGAA","SUARR",
           "KEEE","PILLEE","NAAK","MEEE","NETAA","BAAP","KOO","KABHII","NAAH","BOLNAA","BETAA","CHUSS","LEEE",
           "MERAA","LODAA","JAISE","ALUU","KAAA","PAKODAA","TERI","MAAA","BEHEN","GFF","NANI","DIIN","RAAT","SOTEE",
           "JAGTEE","PELTAA","HUUU","LODEE","CHAAR","CHAWNII","GHODEE","PEEE","TUMM","MEREE","LODEE","PEE","TERI",
           "MAA","KAAA","BOOBS","DABATA HU", "TERI", "MAA", "KI", "CHUT", "AJA", "TERI", "MAA", "KI", "CHUT",
           "FAAD", "DUNGA", "HIJDE", "TERA", "BAAP","HU", "KIDXX", "SPEED", "PAKAD", "BHEN KE LAUDE", "AA BETA",
           "AAGYA", "TERI", "MAA ", "CHODNE","AB", "TERI ", "MAA", "CHUDEGI", "KUTTE", "KI", "TARAH", "BETA",
           "TERI", "MAA", "KE", "BHOSDE", "ME", "JBL", "KE", "SPEAKER", "DAAL", "KAR", "BASS", "BOOSTED", "SONG",
           "SUNUNGA", "PURI","RAAT", "LAGATAR", "TERI", "MAA", "KE", "SATH", "SEX", "KARUNGA🔥", "TERI", "MAA", "KE",
           "BOOBS","DABAUNGA","XXX","TERI","MAA","KAA","CHUT","MARU","RANDI","KEE","PILEE","TERI","MAA","KAA","BHOSDAA",
           "MARU","SUAR","KEE","CHODE","TERI","MAAA","KEEE","NUDES","BECHUNGA","RANDI","KEE","PILLE","TERI","MAAA",
           "CHODU","SUAR","KEEE","PILEE","TERIII","MAAA","DAILYY","CHUDTTI","HAII","MADHARCHOD","AUKAT","BANAA",
           "LODE","TERAA","BAAP","HUU","TERI","GFF","KAA","CHUD", "GAYA", "BACCHA", "BAAP SE",
           "AUKAT ME", "RAHO", "WARNA", "MAA CHOD DENGE TUMARI","BHOSDAA","MARUU","MADHARCHOD","TERI ","NANAI","KAA",
           "CHUTT","MARU","TERII","BEHEN","KAAA","BHOSDAA","MARU","RANDII","KEEE","CHODE","TERI","DADI","KAAA","BOOR",
           "GARAM","KARR","TERE","PUREE","KHANDAN","KOOO","CHODUNGAA","BAAP","SEE","BAKCHODI","KAREGAA","SUARR",
           "KEEE","PILLEE","NAAK","MEEE","NETAA","BAAP","KOO","KABHII","NAAH","BOLNAA","BETAA","CHUSS","LEEE",
           "MERAA","LODAA","JAISE","ALUU","KAAA","PAKODAA","TERI","MAAA","BEHEN","GFF","NANI","DIIN","RAAT","SOTEE",
           "JAGTEE","PELTAA","HUUU","LODEE","CHAAR","CHAWNII","GHODEE","PEEE","TUMM","MEREE","LODEE","PEE","TERI",
           "MAA","KAAA","BOOBS","DABATA HU", "TERA", "BAAP", "HU", "KIDXX", "SPEED", "PAKAD", "BHEN KE LAUDE",
           "AA BETA", "AAGYA", "TERI", "MAA ", "CHODNE",
           "AB", "TERI ", "MAA", "CHUDEGI", "KUTTE", "KI", "TARAH", "BETA", "TERI", "MAA", "KE", "BHOSDE",
           "ME", "JBL", "KE", "SPEAKER", "DAAL", "KAR", "BASS", "BOOSTED", "SONG", "SUNUNGA", "PURI",
           "RAAT", "LAGATAR", "TERI", "MAA", "KE", "SATH", "SEX", "KARUNGA🔥", "CHUD", "GAYA", "BACCHA", "BAAP SE",
           "AUKAT ME", "RAHO", "WARNA", "MAA CHOD DENGE TUMARI"]


async def pyrone(client: Client, message: Message):
    chat_id = message.chat.id
    ruser = None

    if message.reply_to_message:
        ruser = message.reply_to_message.message_id
    
    try:
        for word in ONE_WORDS:
            await client.send_chat_action(chat_id, "typing")
            await client.send_message(chat_id, word, reply_to_message_id=ruser)
            await asyncio.sleep(0.1)
    except FloodWait:
        pass


async def restart(_, __):
    args = [sys.executable, "pyrone.py"]
    execle(sys.executable, *args, environ)


# ADDING HANDLERS

if M1:
    M1.add_handler(MessageHandler(pyrone, filters.command(["T3RI", "L0L", "AJA", "AAJA", "START"], prefixes=None) & filters.me))
    M1.add_handler(MessageHandler(restart, filters.command(["XD", "FARAR", "STOP", "FUCKED"], prefixes=None) & filters.me))

if M2:
    M2.add_handler(MessageHandler(pyrone, filters.command(["T3RI", "L0L", "AJA", "AAJA", "START"], prefixes=None) & filters.me))
    M2.add_handler(MessageHandler(restart, filters.command(["XD", "FARAR", "STOP", "FUCKED"], prefixes=None) & filters.me))

if M3:
    M3.add_handler(MessageHandler(pyrone, filters.command(["T3RI", "L0L", "AJA", "AAJA", "START"], prefixes=None) & filters.me))
    M3.add_handler(MessageHandler(restart, filters.command(["XD", "FARAR", "STOP", "FUCKED"], prefixes=None) & filters.me))

if M4:
    M4.add_handler(MessageHandler(pyrone, filters.command(["T3RI", "L0L", "AJA", "AAJA", "START"], prefixes=None) & filters.me))
    M4.add_handler(MessageHandler(restart, filters.command(["XD", "FARAR", "STOP", "FUCKED"], prefixes=None) & filters.me))

if M5:
    M5.add_handler(MessageHandler(pyrone, filters.command(["T3RI", "L0L", "AJA", "AAJA", "START"], prefixes=None) & filters.me))
    M5.add_handler(MessageHandler(restart, filters.command(["XD", "FARAR", "STOP", "FUCKED"], prefixes=None) & filters.me))


# STARTING CLIENTS

if M1:
    M1.start()
    M1.join_chat("TheAltron")

if M2:
    M2.start()
    M2.join_chat("TheAltron")

if M3:
    M3.start()
    M3.join_chat("TheAltron")

if M4:
    M4.start()
    M4.join_chat("TheAltron")

if M5:
    M5.start()
    M5.join_chat("TheAltron")

print("Pyrone Started Successfully")

idle()


# STOPPING CLIENTS

if M1:
    M1.stop()

if M2:
    M2.stop()

if M3:
    M3.stop()

if M4:
    M4.stop()

if M5:
    M5.stop()
