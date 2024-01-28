import nextcord, os
from nextcord.ext import commands
from keep_alive import keep_alive

keep_alive()

bot = commands.Bot(command_prefix=".", intents=nextcord.Intents.all())
msg_id = 1201270571405692958
guild_id = 1129007445407178852


@bot.event
async def on_ready():
    print("Da club bot is online")


@bot.event
async def on_raw_reaction_add(data: nextcord.RawReactionActionEvent):
    global msg_id
    global guild_id

    server = await bot.fetch_guild(guild_id)
    val_role = nextcord.utils.get(server.roles, name="Valorant")
    ow_role = nextcord.utils.get(server.roles, name="Overwatch")

    if data.message_id == msg_id:
        if data.emoji.id == 1201261549780738088:
            await data.member.add_roles(val_role)
        elif data.emoji.id == 1201261908746063902:
            await data.member.add_roles(ow_role)


@bot.event
async def on_raw_reaction_remove(data: nextcord.RawReactionActionEvent):
    global guild_id
    global msg_id

    server = await bot.fetch_guild(guild_id)
    member = await server.fetch_member(data.user_id)
    val_role = nextcord.utils.get(server.roles, name="Valorant")
    ow_role = nextcord.utils.get(server.roles, name="Overwatch")

    if data.message_id == msg_id:
        if data.emoji.id == 1201261549780738088:
            await member.remove_roles(val_role)
        elif data.emoji.id == 1201261908746063902:
            await member.remove_roles(ow_role)


'''@bot.slash_command(name="role_react", description="asdfasdf")
async def role_react(interaction: nextcord.Interaction):

    val = await interaction.guild.fetch_emoji(1201261549780738088)
    ow = await interaction.guild.fetch_emoji(1201261908746063902)

    channel = interaction.channel
    message = await channel.send(f"Get roles here based on what game you play\n{val} - Valorant\n{ow} - Overwatch")

    await message.add_reaction(val)
    await message.add_reaction(ow)

    await interaction.response.send_message("its done daddy", ephemeral=True)'''


bot.run(os.environ['token'])
