# Role Assigning Bot 
import discord

class Client(discord.Client):
  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)
    self.target_message_id = 931897298299027578
  
  async def on_ready(self):
    print("Anandu BOT LLC ")
  
  async def on_raw_reaction_add(self,payload):
    if payload.message_id != self.target_message_id:
      return 
    guild = client.get_guild(payload.guild_id)
    print(payload.emoji.name)
    #if payload.emoji.name == 

intents = discord.Intents.default()
intents.members = True
client = Client(intents = intents)
client.run("OTMxODkwNDQ5OTQ0MjgxMTA5.YeLAnA.NgeOxPvS1d0XgUp5CG3-Te49tSQ")

