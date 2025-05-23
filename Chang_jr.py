import discord, random, pytz, json, os, math, ARG
from discord.ext import commands
from discord import app_commands
from datetime import datetime, timezone
from DockEvent import DockEvent 


intents = discord.Intents.default()
intents.message_content = True
Token = ''
channelid = 

GUILD_ID = discord.Object(channelid)

class Index(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(label="去工作",style=discord.ButtonStyle.primary, custom_id='1')
    async def button_work(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(view=Work(),ephemeral=True)
    @discord.ui.button(label="個人狀態",style=discord.ButtonStyle.primary, custom_id='2')
    async def button_state(self, interaction: discord.Interaction, button: discord.ui.Button):
        user = interaction.user.id 
        print(f"{user}")
        personalstate = discord.Embed(title="個人狀態Beta",url="https://blogs.mtdv.me/blog/posts/nDIQhaU8Kd", description="由於技術上的問題方士團仍無法在Discord 上重現渾元萬劫的個人狀態的部分，但有對此功能仍有興趣的諸侯們仍然可以透過上方「個人狀態Beta」連結體驗測試版")
        await interaction.response.send_message(embed=personalstate,ephemeral=True)
    @discord.ui.button(label="請安",style=discord.ButtonStyle.primary, custom_id='3')
    async def button_morning(self, interaction: discord.Interaction, button: discord.ui.Button):
        TWtz = pytz.timezone("Asia/Taipei")
        timeInTW = datetime.now(TWtz)
        curTinTW = timeInTW.strftime("%H")
        curTinTW = int(curTinTW)
        if curTinTW >= 23 or curTinTW <= 6:
            greeting = "給奄去睡覺喔！" 
        elif 6 < curTinTW < 11:
            greeting = "早奄"
        elif 11 <= curTinTW < 18:
            greeting = "午奄"
        else:
            greeting = "晚奄"
        await interaction.response.send_message(greeting,ephemeral=True)
    @discord.ui.button(label="電子貓",style=discord.ButtonStyle.primary, custom_id='4',)
    async def button_state2(self, interaction: discord.Interaction, button: discord.ui.Button):
        data = ARG.load_data()
        user_id = str(interaction.user.id) 
        if user_id not in data:
            opening = "```diff\n! Initializing YAST ( Yan Academy of Sciences Terminal ) confirming permissions...\n! 奄國科學院控制系統初始化，確認權限中...\n\n! Authorization granted.\n! 權限認證通過。\n\n! Restructuring structural and temporal data...\n! 正在進行結構資料及時空資料重整...\n\n! Please enter designated project authorization code:\n! 請輸入指定計畫授權碼：\n> ████████████████\n\n! Initiating detection and assessment of Yan citizens and lords’ capabilities.\n! 開始偵測及檢查奄國國民及諸侯的各項能力。\n\n> Progress:[ ▓▓░░░░░░░░░░░░░░░░░░░░░░ ] 12%...\n> Progress:[ ▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░ ] 31%...\n> Progress:[ ▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░ ] 39%...\n> Progress:[ ▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░ ] 41%...\n> Progress:[ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░ ] 53%...\n> Progress:[ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░ ] 63%...\n> Progress:[ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░ ] 78%...\n> Progress:[ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░ ] 92%...\n> Progress:[ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] 100%...\n\n! Detection and assessment complete!\n! 偵測及檢查完畢！\n\n! Majority of Yan citizens show only ~1% deviation compared to previous assessment — within acceptable range.\n! 奄國多數國民各項能力與上次檢測結果對比能力誤差約為1%，為可容許值。\n\n- WARNING: Significant capability drop detected among Yan lords! Deviation exceeds 98%! Affected attributes include, but are not limited to: Physical Power, Command, Mental Force, and Charisma. Lords’ Capability Table must be re-established!\n- 警告：奄國諸侯職位國民能力大幅降低！能力誤差值超過98%！降低能力包括且不限於肉體能力、統御力、精神力、親和力，需重新建立諸侯能力表！\n\n> Send re-evaluation request to lord personal devices?\n> 是否向諸侯隨身裝置發送重新檢測請求？\n> (Y/N)\n```"
            await interaction.response.send_message(opening,view=newopening(),ephemeral=True)
        else:
            check_mark = ARG.daily_check(user_id) 
            if check_mark == 4: 
                await  interaction.response.send_message("charactor Dead",ephemeral=True)
            else:
                displaypersonalstate = ARG.display_state(user_id)            
                await interaction.response.send_message(embed=displaypersonalstate,view=MainOffice(),ephemeral=True)
    @discord.ui.button(label="自由海港",style=discord.ButtonStyle.primary, custom_id='5')
    async def button_freedock(sself, interaction: discord.Interaction, button: discord.ui.Button):
        number = random.randint(17,69)
        dockclose = DockEvent(number) 
        if number == 69:       
            oifile =  discord.File("51121.gif")
            await interaction.response.send_message(embed=dockclose,file=oifile,ephemeral=True)
        elif number == 51:
            oifile =  discord.File("old_chang_oiioii.mp4")
            await interaction.response.send_message(file=oifile,ephemeral=True)
        else:
            await interaction.response.send_message(embed=dockclose,ephemeral=True)

class newopening(discord.ui.View):
    @discord.ui.button(label="Y",style=discord.ButtonStyle.success)
    async def button_YES(self, interaction: discord.Interaction, button: discord.ui.Button):
        data = ARG.load_data()
        user_id = str(interaction.user.id) 
        data[user_id] = ARG.init_user(user_id, interaction.user.id, interaction.user.display_name)
        ARG.save_data(data)
        await interaction.response.send_message(view=Init_Kingdom(),ephemeral=True)
    @discord.ui.button(label="N",style=discord.ButtonStyle.danger)
    async def button_NO(self, interaction: discord.Interaction, button: discord.ui.Button):
        denymessage = "oof"
        await interaction.response.send_message(denymessage,ephemeral=True)

class Init_Kingdom(discord.ui.View):
    @discord.ui.button(label="奄",style=discord.ButtonStyle.primary)
    async def button_KD(self, interaction: discord.Interaction, button: discord.ui.Button):
        user_id = str(interaction.user.id)
        ARG.kingdom_info(user_id,"奄")
        ARG.init_state(user_id)
        embed = discord.Embed(title="登記成功", description="test")
        await interaction.response.send_message(embed=embed,ephemeral=True)

class MainOffice(discord.ui.View):
    @discord.ui.button(label="戶政事務所",style=discord.ButtonStyle.primary)
    async def button_RegistOffice(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(title="戶政事務所", description="test")
        await interaction.response.send_message(embed=embed,view=RegistOffice(),ephemeral=True)
    @discord.ui.button(label="食堂",style=discord.ButtonStyle.success)
    async def button_Foodcourt(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(title="食堂", description="test")
        await interaction.response.send_message(embed=embed,view=FoodCourt(),ephemeral=True)
    @discord.ui.button(label="倉庫",style=discord.ButtonStyle.secondary)
    async def button_Warehouse(self, interaction: discord.Interaction, button: discord.ui.Button):
        displaywarehouse = ARG.display_warehouse(str(interaction.user.id))
        await interaction.response.send_message(embed=displaywarehouse,view=Shop(),ephemeral=True)

class RegistOffice(discord.ui.View):
    @discord.ui.button(label="更名",style=discord.ButtonStyle.secondary)
    async def button_rename(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.nick != None:
            ARG.rename(str(interaction.user.id),interaction.user.nick)
        else:
            ARG.rename(str(interaction.user.id),interaction.user.display_name)
        embed = discord.Embed(title="更名成功", description="test")
        await interaction.response.send_message(embed=embed,ephemeral=True)
    @discord.ui.button(label="請/收假",style=discord.ButtonStyle.primary)
    async def button_vacation(self, interaction: discord.Interaction, button: discord.ui.Button):
        data = ARG.load_data() 
        user_id = str(interaction.user.id)
        if data[user_id]["vacation"] == False:
            data[user_id]["vacation"] = True
            ARG.save_data(data)
            embed = discord.Embed(title="請假成功", description="test")
            await interaction.response.send_message(embed=embed,ephemeral=True)
        elif data[user_id]["vacation"] == True:
            data[user_id]["vacation"] = False
            ARG.save_data(data)
            embed = discord.Embed(title="收假成功", description="test")
            await interaction.response.send_message(embed=embed,ephemeral=True)
    @discord.ui.button(label="註銷",style=discord.ButtonStyle.danger)
    async def button_erase(self, interaction: discord.Interaction, button: discord.ui.Button):
        erase(str(interaction.user.id))
        embed = discord.Embed(title="註銷成功", description="test")
        await interaction.response.send_message(embed=embed,ephemeral=True)


class FoodCourt(discord.ui.View):
    @discord.ui.button(label="水餃",style=discord.ButtonStyle.primary)
    async def button_meal1(self, interaction: discord.Interaction, button: discord.ui.Button):
        feeding = ARG.feed(str(interaction.user.id),1)
        if feeding == 1:
            embed = discord.Embed(title="行動力不足", description="test")
        else:
            embed = discord.Embed(title="吃飽", description="test")
        await interaction.response.send_message(embed=embed,ephemeral=True)
    @discord.ui.button(label="包子",style=discord.ButtonStyle.primary)
    async def button_meal2(self, interaction: discord.Interaction, button: discord.ui.Button):
        feeding = ARG.feed(str(interaction.user.id),2)
        if feeding == 1:
            embed = discord.Embed(title="行動力不足", description="test")
        else:
            embed = discord.Embed(title="吃飽", description="test")
        await interaction.response.send_message(embed=embed,ephemeral=True)
    @discord.ui.button(label="奄茶特餐",style=discord.ButtonStyle.primary)
    async def button_meal3(self, interaction: discord.Interaction, button: discord.ui.Button):
        feeding = ARG.feed(str(interaction.user.id),3)
        if feeding == 1:
            embed = discord.Embed(title="行動力不足", description="test")
        else:
            embed = discord.Embed(title="吃飽", description="test")
        await interaction.response.send_message(embed=embed,ephemeral=True)
    
class Shop(discord.ui.View):
    @discord.ui.button(label="升級軍事",style=discord.ButtonStyle.primary)
    async def button_MIL_upgrade(self, interaction: discord.Interaction, button: discord.ui.Button):
        shop_result = ARG.resource_levelup(str(interaction.user.id),'MIL')
        await interaction.response.send_message(shop_result,ephemeral=True)
    @discord.ui.button(label="升級商業",style=discord.ButtonStyle.primary)
    async def button_BUS_upgrade(self, interaction: discord.Interaction, button: discord.ui.Button):
        shop_result = ARG.resource_levelup(str(interaction.user.id),'BUS')
        await interaction.response.send_message(shop_result,ephemeral=True)
    @discord.ui.button(label="升級科技",style=discord.ButtonStyle.primary)
    async def button_TEC_upgrade(self, interaction: discord.Interaction, button: discord.ui.Button):
        shop_result = ARG.resource_levelup(str(interaction.user.id),'TEC')
        await interaction.response.send_message(shop_result,ephemeral=True)
    @discord.ui.button(label="升級文化",style=discord.ButtonStyle.primary)
    async def button_CUL_upgrade(self, interaction: discord.Interaction, button: discord.ui.Button):
        shop_result = ARG.resource_levelup(str(interaction.user.id),'CUL')
        await interaction.response.send_message(shop_result,ephemeral=True)

class Work(discord.ui.View):
    @discord.ui.button(label="校場",style=discord.ButtonStyle.primary, row=0)
    async def button_field(self, interaction: discord.Interaction, button: discord.ui.Button):
        check_mark = ARG.daily_check(str(interaction.user.id))
        if check_mark == 1:
            await  interaction.response.send_message("no enough stamina",ephemeral=True)
        elif check_mark == 4:
            await  interaction.response.send_message("charactor Dead",ephemeral=True)
        else:
            selected_event = ARG.event_lottery(interaction.user.id,'MIL','BUS','TEC','CUL',1)
            if selected_event == 0:
                ARG.gain_state(str(interaction.user.id),'STR',2)
                await  interaction.response.send_message("nothing happend",ephemeral=True)
            else:
                await  interaction.response.send_message(view=EventChoice("FieldEvent",selected_event),ephemeral=True)
    @discord.ui.button(label="太學",style=discord.ButtonStyle.primary, row=0)
    async def button_college(self, interaction: discord.Interaction, button: discord.ui.Button):
        check_mark = ARG.daily_check(str(interaction.user.id))
        if check_mark == 1:
            await  interaction.response.send_message("no enough stamina",ephemeral=True)
        elif check_mark == 4:
            await  interaction.response.send_message("charactor Dead",ephemeral=True)
        else:
            selected_event = ARG.event_lottery(interaction.user.id,'BUS','CUL','MIL','TEC',1)
            if selected_event == 0:
                ARG.gain_state(str(interaction.user.id),'DOM',2)
                await  interaction.response.send_message("nothing happend",ephemeral=True)
            else:
                await  interaction.response.send_message(view=EventChoice("CollegeEvent",selected_event),ephemeral=True)
    @discord.ui.button(label="科學院",style=discord.ButtonStyle.primary, row=0)
    async def button_sciences(self, interaction: discord.Interaction, button: discord.ui.Button):
        check_mark = ARG.daily_check(str(interaction.user.id))
        if check_mark == 1:
            await  interaction.response.send_message("no enough stamina",ephemeral=True)
        elif check_mark == 4:
            await  interaction.response.send_message("charactor Dead",ephemeral=True)
        else:
            selected_event = ARG.event_lottery(interaction.user.id,'TEC','MIL','CUL','BUS',1)
            if selected_event == 0:
                ARG.gain_state(str(interaction.user.id),'INT',2)
                await  interaction.response.send_message("nothing happend",ephemeral=True)
            else:
                await  interaction.response.send_message(view=EventChoice("SciencesEvent",selected_event),ephemeral=True)
    @discord.ui.button(label="樂府",style=discord.ButtonStyle.primary, row=0)
    async def button_balladss(self, interaction: discord.Interaction, button: discord.ui.Button):
        check_mark = ARG.daily_check(str(interaction.user.id))
        if check_mark == 1:
            await  interaction.response.send_message("no enough stamina",ephemeral=True)
        elif check_mark == 4:
            await  interaction.response.send_message("charactor Dead",ephemeral=True)
        else:
            selected_event = ARG.event_lottery(interaction.user.id,'CUL','TEC','BUS','MIL',1)
            if selected_event == 0: 
                ARG.gain_state(str(interaction.user.id),'CHR',2)
                await  interaction.response.send_message("nothing happend",ephemeral=True)
            else:
                await  interaction.response.send_message(view=EventChoice("BalladssEvent",selected_event),ephemeral=True)
        
    @discord.ui.button(label="兵營",style=discord.ButtonStyle.success, row=1)
    async def button_military(self, interaction: discord.Interaction, button: discord.ui.Button):
        check_mark = ARG.daily_check(str(interaction.user.id))
        if check_mark == 1:
            await  interaction.response.send_message("no enough stamina",ephemeral=True)
        elif check_mark == 4:
            await  interaction.response.send_message("charactor Dead",ephemeral=True)
        else:
            selected_event = ARG.event_lottery(interaction.user.id,'MIL','TEC','CUL','BUS',1)
            if selected_event == 0: 
                ARG.gain_state(str(interaction.user.id),'STR',1) 
                amount = ARG.resource_mag(str(interaction.user.id),'STR') * (random.randint(4,9))
                ARG.gain_resource(str(interaction.user.id),'MIL_rs',amount)
                await  interaction.response.send_message("nothing happend",ephemeral=True)
            else:
                await  interaction.response.send_message(view=EventChoice("MilitaryEvent",selected_event),ephemeral=True)
    @discord.ui.button(label="市集",style=discord.ButtonStyle.success, row=1)
    async def button_market(self, interaction: discord.Interaction, button: discord.ui.Button):
        check_mark = ARG.daily_check(str(interaction.user.id))
        if check_mark == 1:
            await  interaction.response.send_message("no enough stamina",ephemeral=True)
        elif check_mark == 4:
            await  interaction.response.send_message("charactor Dead",ephemeral=True)
        else:
            selected_event = ARG.event_lottery(interaction.user.id,'BUS','CUL','MIL','TEC',2)
            if selected_event == 0: 
                ARG.gain_state(str(interaction.user.id),'DOM',1) 
                amount = ARG.resource_mag(str(interaction.user.id),'DOM') * (random.randint(4,9))
                ARG.gain_resource(str(interaction.user.id),'BUS_rs',amount)
                await  interaction.response.send_message("nothing happend",ephemeral=True)
            else:
                await  interaction.response.send_message(view=EventChoice("MarketEvent",selected_event),ephemeral=True)
    @discord.ui.button(label="匠人坊",style=discord.ButtonStyle.success, row=1)
    async def button_workshop(self, interaction: discord.Interaction, button: discord.ui.Button):
        check_mark = ARG.daily_check(str(interaction.user.id))
        if check_mark == 1:
            await  interaction.response.send_message("no enough stamina",ephemeral=True)
        elif check_mark == 4:
            await  interaction.response.send_message("charactor Dead",ephemeral=True)
        else:
            selected_event = ARG.event_lottery(interaction.user.id,'MIL','TEC','CUL','BUS',1)
            if selected_event == 0: 
                ARG.gain_state(str(interaction.user.id),'INT',1) 
                amount = ARG.resource_mag(str(interaction.user.id),'INT') * (random.randint(4,9))
                ARG.gain_resource(str(interaction.user.id),'TEC_rs',amount)
                await  interaction.response.send_message("nothing happend",ephemeral=True)
            else:
                await  interaction.response.send_message(view=EventChoice("WorkshopEvent",selected_event),ephemeral=True)
    @discord.ui.button(label="茶館",style=discord.ButtonStyle.success, row=1)
    async def button_teahouse(self, interaction: discord.Interaction, button: discord.ui.Button):
        check_mark = ARG.daily_check(str(interaction.user.id))
        if check_mark == 1:
            await  interaction.response.send_message("no enough stamina",ephemeral=True)
        elif check_mark == 4:
            await  interaction.response.send_message("charactor Dead",ephemeral=True)
        else:
            selected_event = ARG.event_lottery(interaction.user.id,'MIL','TEC','CUL','BUS',1)
            if selected_event == 0: 
                ARG.gain_state(str(interaction.user.id),'CHR',1) 
                amount = ARG.resource_mag(str(interaction.user.id),'CHR') * (random.randint(4,9))
                ARG.gain_resource(str(interaction.user.id),'CUL_rs',amount)
                await  interaction.response.send_message("nothing happend",ephemeral=True)
            else:
                await  interaction.response.send_message(view=EventChoice("TeahouseEvent",selected_event),ephemeral=True)

    @discord.ui.button(label="兵工廠",style=discord.ButtonStyle.danger, row=2)
    async def button_arsenal(self, interaction: discord.Interaction, button: discord.ui.Button):
        check_mark = ARG.daily_check(str(interaction.user.id))
        if check_mark == 1:
            await  interaction.response.send_message("no enough stamina",ephemeral=True)
        elif check_mark == 4:
            await  interaction.response.send_message("charactor Dead",ephemeral=True)
        else:
            selected_event = ARG.event_lottery(interaction.user.id,'MIL','TEC','BUS','CUL',3)
            if selected_event == 0: 
                amount = ARG.resource_mag(str(interaction.user.id),'STR') * 10
                ARG.gain_resource(str(interaction.user.id),'MIL_rs',amount)
                await  interaction.response.send_message("nothing happend",ephemeral=True)
            else:
                await  interaction.response.send_message(view=EventChoice("ArsenalEvent",selected_event),ephemeral=True)
    @discord.ui.button(label="接待所",style=discord.ButtonStyle.danger, row=2)
    async def button_reception(self, interaction: discord.Interaction, button: discord.ui.Button):
        check_mark = ARG.daily_check(str(interaction.user.id))
        if check_mark == 1:
            await  interaction.response.send_message("no enough stamina",ephemeral=True)
        elif check_mark == 4:
            await  interaction.response.send_message("charactor Dead",ephemeral=True)
        else:
            selected_event = ARG.event_lottery(interaction.user.id,'MIL','TEC','BUS','CUL',3)
            if selected_event == 0: 
                amount = ARG.resource_mag(str(interaction.user.id),'DOM') * 10
                ARG.gain_resource(str(interaction.user.id),'BUS_rs',amount)
                await  interaction.response.send_message("nothing happend",ephemeral=True)
            else:
                await  interaction.response.send_message(view=EventChoice("ReceptionEvent",selected_event),ephemeral=True)
    @discord.ui.button(label="加工所",style=discord.ButtonStyle.danger, row=2)
    async def button_factory(self, interaction: discord.Interaction, button: discord.ui.Button):
        check_mark = ARG.daily_check(str(interaction.user.id))
        if check_mark == 1:
            await  interaction.response.send_message("no enough stamina",ephemeral=True)
        elif check_mark == 4:
            await  interaction.response.send_message("charactor Dead",ephemeral=True)
        else:
            selected_event = ARG.event_lottery(interaction.user.id,'MIL','TEC','BUS','CUL',3)
            if selected_event == 0: 
                amount = ARG.resource_mag(str(interaction.user.id),'INT') * 10
                ARG.gain_resource(str(interaction.user.id),'TEC_rs',amount)
                await  interaction.response.send_message("nothing happend",ephemeral=True)
            else:
                await  interaction.response.send_message(view=EventChoice("FactoryEvent",selected_event),ephemeral=True)
    @discord.ui.button(label="博物院",style=discord.ButtonStyle.danger, row=2)
    async def button_museum(self, interaction: discord.Interaction, button: discord.ui.Button):
        check_mark = ARG.daily_check(str(interaction.user.id))
        if check_mark == 1:
            await  interaction.response.send_message("no enough stamina",ephemeral=True)
        elif check_mark == 4:
            await  interaction.response.send_message("charactor Dead",ephemeral=True)
        else:
            selected_event = ARG.event_lottery(interaction.user.id,'MIL','TEC','BUS','CUL',3)
            if selected_event == 0: 
                amount = ARG.resource_mag(str(interaction.user.id),'CHR') * 10
                ARG.gain_resource(str(interaction.user.id),'CUL_rs',amount)
                await  interaction.response.send_message("nothing happend",ephemeral=True)
            else:
                await  interaction.response.send_message(view=EventChoice("MuseumEvent",selected_event),ephemeral=True)
    
    @discord.ui.button(label="海港",style=discord.ButtonStyle.secondary, row=3)
    async def button_dock(self, interaction: discord.Interaction, button: discord.ui.Button):
        number = random.randint(1,69)
        dockclose = DockEvent(number) 
        if number == 69:       
            oifile =  discord.File("51121.gif")
            await interaction.response.send_message(embed=dockclose,file=oifile,ephemeral=True)
        elif number == 51:
            oifile =  discord.File("old_chang_oiioii.mp4")
            await interaction.response.send_message(file=oifile,ephemeral=True)
        else:
            await interaction.response.send_message(embed=dockclose,ephemeral=True)

class EventChoice(discord.ui.View):
    def __init__(self, workname, states):
        super().__init__()
        self.workname = workname
        self.state = states
    @discord.ui.button(label="選項一",style=discord.ButtonStyle.primary)
    async def button_first(self, interaction: discord.Interaction, button: discord.ui.Button):
        # ARG.gain_state(str(interaction.user.id),self.state[0],1)
        await interaction.response.send_message("選項一",ephemeral=True)
    @discord.ui.button(label="選項二",style=discord.ButtonStyle.primary)
    async def button_second(self, interaction: discord.Interaction, button: discord.ui.Button):
        # ARG.gain_state(str(interaction.user.id),self.state[1],1)
        await interaction.response.send_message("選項二",ephemeral=True)


class PresistentViewBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents().all()
        super().__init__(command_prefix=commands.when_mentioned_or('.'), intents=intents)
    async def setup_hook(self) -> None:
        self.add_view(Index())
    async def on_ready(self):
        print(f'Ligged on as {self.user}!')
        try:
            guild = discord.Object(channelid)
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}')
        except:
            print(f'Error syncing commands: {e}')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

client = PresistentViewBot()

@client.tree.command(name="summon", description="summon Chang Jr", guild=GUILD_ID)
async def summonCJ(interaction: discord.Interaction):
    thumbnailfile = discord.File("Yan_State.png")
    await interaction.channel.send(file = thumbnailfile,view=Index())

client.run(Token)


