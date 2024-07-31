# 導入Discord.py模組
import discord
import json
from mcstatus import JavaServer

# client是跟discord連接，intents是要求機器人的權限
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)

server = JavaServer.lookup("192.168.5.223:51511")
query = server.query()

print (f"伺服器在線人數 {query.players.online}/{query.players.max} 位")
#for playerlist in list:
	#print(playerlist)
    

#print(player_list["lists"])

# 調用event函式庫
@client.event
# 當機器人完成啟動
async def on_ready():
    print(f"目前登入身份 --> {client.user}")
#
@client.event
# 當頻道有新訊息
async def on_message(message):
    query = server.query()
    player_list = {}
#    # 排除機器人本身的訊息，避免無限循環
	
    if message.author == client.user:
        return
#    # 新訊息包含Hello，回覆Hello, world!
    if message.content == "指令表":
        await message.channel.send(f"playlist")
    if message.content == "playlist":
        print(message.author.id)
        player_list["lists"] = "\n".join(query.players.names)
        await message.channel.send(f"<@{message.author.id}>\n>>> ***ESL伺服器狀態*** ****V1.1**** \n IP mc.yuwuy.com \n 伺服器在線人數 {query.players.online}/ {query.players.max} \n" + "```"+(player_list["lists"])+"```")
        del player_list["lists"]
        


client.run("")
