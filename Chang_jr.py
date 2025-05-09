import discord, random
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True
Token = ''
botid =

GUILD_ID = discord.Object(botid)

class Index(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(label="去工作",style=discord.ButtonStyle.primary, custom_id='1')
    async def button_work(self,button, interactionl):
        await button.response.send_message(view=Work(),ephemeral=True)
    @discord.ui.button(label="個人狀態",style=discord.ButtonStyle.primary, custom_id='2')
    async def button_state(self,button, interaction):
        await button.response.send_message("state",ephemeral=True)
    @discord.ui.button(label="請安",style=discord.ButtonStyle.primary, custom_id='3')
    async def button_morning(self,button, interaction):
        await button.response.send_message("早奄",ephemeral=True)

class Work(discord.ui.View):
    @discord.ui.button(label="校場",style=discord.ButtonStyle.primary, row=0)
    async def button_field(self,button, interaction):
        await button.response.send_message(view=FieldEvent(),ephemeral=True)
    @discord.ui.button(label="太學",style=discord.ButtonStyle.primary, row=0)
    async def button_college(self,button, interaction):
        await button.response.send_message("太學",ephemeral=True)
    @discord.ui.button(label="科學院",style=discord.ButtonStyle.primary, row=0)
    async def button_sciences(self,button, interaction):
        await button.response.send_message("科學院",ephemeral=True)
    @discord.ui.button(label="樂府",style=discord.ButtonStyle.primary, row=0)
    async def button_balladss(self,button, interaction):
        await button.response.send_message("樂府",ephemeral=True)
        
    @discord.ui.button(label="兵營",style=discord.ButtonStyle.success, row=1)
    async def button_military(self,button, interaction):
        await button.response.send_message("兵營",ephemeral=True)
    @discord.ui.button(label="市集",style=discord.ButtonStyle.success, row=1)
    async def button_market(self,button, interaction):
        await button.response.send_message("市集",ephemeral=True)
    @discord.ui.button(label="匠人坊",style=discord.ButtonStyle.success, row=1)
    async def button_workshop(self,button, interaction):
        await button.response.send_message("匠人坊",ephemeral=True)
    @discord.ui.button(label="茶館",style=discord.ButtonStyle.success, row=1)
    async def button_teahouse(self,button, interaction):
        await button.response.send_message("茶館",ephemeral=True)

    @discord.ui.button(label="兵工廠",style=discord.ButtonStyle.danger, row=2)
    async def button_arsenal(self,button, interaction):
        await button.response.send_message("兵工廠",ephemeral=True)
    @discord.ui.button(label="接待所",style=discord.ButtonStyle.danger, row=2)
    async def button_reception(self,button, interaction):
        await button.response.send_message("接待所",ephemeral=True)
    @discord.ui.button(label="加工所",style=discord.ButtonStyle.danger, row=2)
    async def button_factory(self,button, interaction):
        await button.response.send_message("加工所",ephemeral=True)
    @discord.ui.button(label="博物院",style=discord.ButtonStyle.danger, row=2)
    async def button_museum(self,button, interaction):
        await button.response.send_message("博物院",ephemeral=True)
    
    @discord.ui.button(label="海港",style=discord.ButtonStyle.secondary, row=3)
    async def button_dock(self,button, interaction):
        number = random.randint(1,16)
        switch = {
            1: "拜師學藝\n你探訪一處幽僻深山",
            2: "野營受寒\n你探訪一處幽僻深山",
            3: "遭遇搶劫\n你探訪一處幽僻深山",
            4: "討價還價\n你探訪一處幽僻深山",
            5: "海關扣留\n你探訪一處幽僻深山",
            6: "粗心大意\n你探訪一處幽僻深山",
            7: "小鎮導覽\n你探訪一處幽僻深山",
            8: "火災警報\n你探訪一處幽僻深山",
            9: "山林修練\n你探訪一處幽僻深山",
            10: "觀摩商店街\n你探訪一處幽僻深山",
            11: "輪船遊歷\n你探訪一處幽僻深山",
            12: "料理祕方\n你探訪一處幽僻深山",
            13: "先發制人\n你探訪一處幽僻深山",
            14: "先發制人\n你探訪一處幽僻深山",
            15: "先發制人\n你探訪一處幽僻深山",
            16: "先發制人\n你探訪一處幽僻深山",
            }
        dock_description = switch[number]
        dockclose = discord.Embed(title="[海港特殊事件-結算]", description=dock_description)
        await button.response.send_message(embed=dockclose,ephemeral=True)


class FieldEvent(discord.ui.View):
    async def FieldEventPrint(self):
        dockclose = discord.Embed(title="[校場特殊事件-結算]", description='dock_description')
        await interaction.response.send_message(embed=dockclose,ephemeral=True)
    @discord.ui.button(label="選項一",style=discord.ButtonStyle.primary)
    async def choose_one(self,button, interaction):
        await button.response.send_message("拜師學藝",ephemeral=True)
    @discord.ui.button(label="選項二",style=discord.ButtonStyle.primary)
    async def choose_two(self,button, interaction):
        await button.response.send_message("拜師學藝",ephemeral=True)


class PresistentViewBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents().all()
        super().__init__(command_prefix=commands.when_mentioned_or('.'), intents=intents)
    async def setup_hook(self) -> None:
        self.add_view(Index())
    async def on_ready(self):
        print(f'Ligged on as {self.user}!')
        try:
            guild = discord.Object(botid)
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}')
        except:
            print(f'Error syncing commands: {e}')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

client = PresistentViewBot()

@client.tree.command(name="summon", description="summon Chang Jr", guild=GUILD_ID)
async def summonCJ(interaction: discord.Interaction):
    await interaction.response.send_message(view=Index())

client.run(Token)