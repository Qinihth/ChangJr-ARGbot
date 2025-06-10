import discord, random, pytz, json, os, math, ARG, asyncio
from discord.ext import commands
from datetime import datetime, timezone
from Event import Event 
from DockEvent import DockEvent 

intents = discord.Intents.default()
intents.message_content = True
Token = ''
serverid = 

GUILD_ID = discord.Object(serverid)

class Index(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(label="去工作",style=discord.ButtonStyle.primary, custom_id='1')
    async def button_work(self, interaction: discord.Interaction, button: discord.ui.Button):
        check_mark = ARG.daily_check(str(interaction.user.id))
        if check_mark == 1:
            nosta_message = "```diff\n- 體力不支\n```"
            await  interaction.response.send_message(nosta_message,ephemeral=True)
        elif check_mark == 4:
            dead_message = "```diff\n- 模擬失敗，角色死亡\n```"
            await  interaction.response.send_message(dead_message,ephemeral=True)
        elif check_mark == 4:
            vacation_message = "```diff\n> 休假中\n```"
            await  interaction.response.send_message(vacation_message,ephemeral=True)
        else:
            embed = discord.Embed(title="Make 奄 Great Again!", description="肌肉不會背叛你")
            embed.add_field(name="校場",value="--提升武力")
            embed.add_field(name="太學",value="--提升內政")
            embed.add_field(name="科學院",value="--提升智力")
            embed.add_field(name="樂府",value="--提升魅力")
            embed.add_field(name="兵營",value="--提升武力、增加軍事")
            embed.add_field(name="市集",value="--提升內政、增加商業")
            embed.add_field(name="匠人坊",value="--提升智力、增加科技")
            embed.add_field(name="茶館",value="--提升魅力、增加文化")
            embed.add_field(name="兵工廠",value="--增加軍事、商業")
            embed.add_field(name="接待所",value="--增加商業、科技")
            embed.add_field(name="加工所",value="--增加科技、文化")
            embed.add_field(name="博物館",value="--增加文化、軍事")
            embed.add_field(name="海港",value="--快樂")
            stamina = ARG.getstamina(str(interaction.user.id))
            await interaction.response.send_message(embed=embed,view=Work(stamina),ephemeral=True)
    @discord.ui.button(label="電子貓-Beta",style=discord.ButtonStyle.primary, custom_id='2',)
    async def button_state2(self, interaction: discord.Interaction, button: discord.ui.Button):
        data = ARG.load_data()
        user_id = str(interaction.user.id) 
        if user_id not in data:
            opening = "```diff\n! Initializing YAST ( Yan Academy of Sciences Terminal ) confirming permissions...\n! 奄國科學院控制系統初始化，確認權限中...\n\n! Authorization granted. Welcome, Seigneur ███████!\n! 權限認證通過。！歡迎諸侯███████ ！\n\n! Activating Protocol ████████████████ ...\n! 啟動代碼 ████████████████ 計畫...\n\n+ Deploying TMGT Module\n+ 正在部屬時TMGT模組\n\n> Simulation Timeframe: Turbulent Era\n> 模擬時段：「混元紀」\n\n> Target Anchor Point : ███Kingdom\n> 目標定錨點確認：███國\n\n- ERROR: Insufficient compute power! Anchor failed!\n- 錯誤：算力不足！錨定失敗！\n\n! Initiating detection and assessment of Seigneur capabilities.\n! 開始偵測及檢查諸侯各項能力。\n\n> Progress:[ ▓▓░░░░░░░░░░░░░░░░░░░░░░ ] 12%...\n> Progress:[ ▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░ ] 39%...\n> Progress:[ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░ ] 78%...\n> Progress:[ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] 100%...\n\n! Detection and assessment complete!\n! 偵測及檢查完畢！\n\n- WARNING: Significant capability drop will be apply to simulation! Deviation exceeds 98%! Affected attributes include, but are not limited to: Physical Power, Command, Mental Force, and Charisma.\n- 警告：諸侯能力在模擬中將會大幅降低！能力誤差值超過98%！降低能力包括且不限於肉體能力、統御力、精神力、親和力！\n\n> Start Simulation Hunyuan Wanjie？\n> 是否開始模擬混元萬劫？\n> (Y/N)\n```"
            await interaction.response.send_message(opening,view=newopening(),ephemeral=True)
        else:
            check_mark = ARG.daily_check(user_id) 
            if check_mark == 4: 
                await  interaction.response.send_message("charactor Dead",ephemeral=True)
            else:
                displaypersonalstate = ARG.display_state(user_id)
                await interaction.response.send_message(embed=displaypersonalstate,view=MainOffice(),ephemeral=True)
    # @discord.ui.button(label="個人狀態",style=discord.ButtonStyle.primary, custom_id='3')
    # async def button_state(self, interaction: discord.Interaction, button: discord.ui.Button):
    #     user = interaction.user.id 
    #     print(f"{user}")
    #     personalstate = discord.Embed(title="個人狀態Beta",url="https://blogs.mtdv.me/blog/posts/nDIQhaU8Kd", description="由於技術上的問題方士團仍無法在Discord 上重現渾元萬劫的個人狀態的部分，但有對此功能仍有興趣的諸侯們仍然可以透過上方「個人狀態Beta」連結體驗測試版")
    #     await interaction.response.send_message(embed=personalstate,ephemeral=True)
    @discord.ui.button(label="請安",style=discord.ButtonStyle.secondary, custom_id='4')
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
    @discord.ui.button(label="自由海港",style=discord.ButtonStyle.secondary, custom_id='5')
    async def button_freedock(sself, interaction: discord.Interaction, button: discord.ui.Button):
        number = random.randint(17,71)
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
        kingdomopening = "```diff\n- WARNING: Anchor failed! Need manually import Anchor Point\n- 警告：錨定失敗！需要手動輸入錨定點\n\n- WARNING: Simulation currently only available for Yan Kingdom national\n- 警告：模擬目前僅供奄國國民使用\n\n> Import Anchor Point:\n> 輸入錨定點:\n```"
        await interaction.response.send_message(kingdomopening,view=Init_Kingdom(),ephemeral=True)
    @discord.ui.button(label="N",style=discord.ButtonStyle.danger)
    async def button_NO(self, interaction: discord.Interaction, button: discord.ui.Button):
        denymessage = "```diff\n- ⚠️ ✸͓̳◻: ✸͓̳◻◻◻≡ r✸͓̳u ▒ ή†\n- ⚠️ ▓𓋹𓏢:̸̛̰R̵͗͌È̸̑R̸̅̌R̶̽́O̴͐̎-ΣΔ eø†◻≠a◻◻⊞ ⊟⟴ Ξ ◻◻ †☍0\n```"
        await interaction.response.send_message(denymessage,ephemeral=True)

class Init_Kingdom(discord.ui.View):
    @discord.ui.button(label="奄",style=discord.ButtonStyle.secondary)
    async def button_KD(self, interaction: discord.Interaction, button: discord.ui.Button):
        user_id = str(interaction.user.id)
        ARG.kingdom_info(user_id,"奄")
        ARG.init_state(user_id)
        startgame = "```diff\n! Simulation registration confirmed.\n! 模擬生成確認完成。\n\n! Redirecting...\n! 正在重新導向...\n```"
        displaypersonalstate = ARG.display_state(user_id)
        await interaction.response.send_message(startgame,ephemeral=True)
        await interaction.followup.send(embed=displaypersonalstate, ephemeral=True)

class MainOffice(discord.ui.View):
    @discord.ui.button(label="戶政事務所",style=discord.ButtonStyle.primary)
    async def button_RegistOffice(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(title="戶政事務所", description="辦理模擬諸侯相關事宜")
        embed.add_field(name="更名",value="--名字更改為伺服暱稱",inline=False)
        embed.add_field(name="請/收假",value="--停止扣除飽食度，無法去工作",inline=False)
        embed.add_field(name="註銷",value="--刪除模擬資料",inline=False)
        await interaction.response.send_message(embed=embed,view=RegistOffice(),ephemeral=True)
    @discord.ui.button(label="食堂",style=discord.ButtonStyle.success)
    async def button_Foodcourt(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(title="食堂", description="消耗行動值恢復飽食度")
        embed.add_field(name="水餃",value="--恢復1飽食度，消耗1行動力",inline=False)
        embed.add_field(name="包子",value="--恢復3飽食度，消耗2行動力",inline=False)
        embed.add_field(name="奄茶特餐",value="--恢復6飽食度，消耗3行動力",inline=False)
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
        rename_message = "```diff\n! 更名成功\n```"
        await interaction.response.send_message(rename_message,ephemeral=True)
    @discord.ui.button(label="請/收假",style=discord.ButtonStyle.primary)
    async def button_vacation(self, interaction: discord.Interaction, button: discord.ui.Button):
        rename_message = ARG.vacation(str(interaction.user.id))
        await interaction.response.send_message(rename_message,ephemeral=True)
    @discord.ui.button(label="註銷",style=discord.ButtonStyle.danger)
    async def button_erase(self, interaction: discord.Interaction, button: discord.ui.Button):
        ARG.erase(str(interaction.user.id))
        rename_message = "```diff\n- 註銷成功\n```"
        await interaction.response.send_message(rename_message,ephemeral=True)


class FoodCourt(discord.ui.View):
    @discord.ui.button(label="水餃",style=discord.ButtonStyle.primary)
    async def button_meal1(self, interaction: discord.Interaction, button: discord.ui.Button):
        feed_message = ARG.feed(str(interaction.user.id),1)
        await interaction.response.send_message(feed_message,ephemeral=True)
    @discord.ui.button(label="包子",style=discord.ButtonStyle.primary)
    async def button_meal2(self, interaction: discord.Interaction, button: discord.ui.Button):
        feed_message = ARG.feed(str(interaction.user.id),2)
        await interaction.response.send_message(feed_message,ephemeral=True)
    @discord.ui.button(label="奄茶特餐",style=discord.ButtonStyle.primary)
    async def button_meal3(self, interaction: discord.Interaction, button: discord.ui.Button):
        feed_message = ARG.feed(str(interaction.user.id),3)
        await interaction.response.send_message(feed_message,ephemeral=True)
    
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
    def __init__(self,stamina):
        super().__init__()
        self.stamina = stamina 
    @discord.ui.button(label="校場",style=discord.ButtonStyle.primary, row=0)
    async def button_field(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.stamina > 0:
            selected_event = ARG.event_lottery(interaction.user.id,'MIL','BUS','TEC','CUL',1)
            ARG.gain_state(str(interaction.user.id),'STR',2)
            if selected_event == 0:    
                fieldembed = discord.Embed(title="❖ 工作結算：",description="• 你前往校場進行障礙突破訓練，武力<:MNR_INC_B:1375507280711123087>。",color=discord.Color.red())
                await  interaction.response.send_message(embed=fieldembed,ephemeral=True)
            else:
                events = Event('Field',selected_event)
                embed = events[0]
                await  interaction.response.send_message(embed=embed,view=EventChoice(events),ephemeral=True)
            ARG.minus_stamina(str(interaction.user.id))
            self.stamina -= 1
        else:
            nosta_message = "```diff\n- 體力不支\n```"
            await  interaction.response.send_message(nosta_message,ephemeral=True)
    @discord.ui.button(label="太學",style=discord.ButtonStyle.primary, row=0)
    async def button_college(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.stamina > 0:
            selected_event = ARG.event_lottery(interaction.user.id,'BUS','CUL','MIL','TEC',1)
            ARG.gain_state(str(interaction.user.id),'DOM',2)
            if selected_event == 0:
                collegeembed = discord.Embed(title="❖ 工作結算：",description="• 你前往太學閱讀名家經典，內政<:MNR_INC_B:1375507280711123087>。",color=discord.Color.gold())
                await  interaction.response.send_message(embed=collegeembed,ephemeral=True)
            else:
                events = Event('College',selected_event)
                embed = events[0]
                await  interaction.response.send_message(embed=embed,view=EventChoice(events),ephemeral=True)
            ARG.minus_stamina(str(interaction.user.id))
            self.stamina -= 1
        else:
            nosta_message = "```diff\n- 體力不支\n```"
            await  interaction.response.send_message(nosta_message,ephemeral=True)
    @discord.ui.button(label="科學院",style=discord.ButtonStyle.primary, row=0)
    async def button_sciences(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.stamina > 0:
            selected_event = ARG.event_lottery(interaction.user.id,'TEC','MIL','CUL','BUS',1)
            ARG.gain_state(str(interaction.user.id),'INT',2)
            if selected_event == 0:
                sciencesembed = discord.Embed(title="❖ 工作結算：",description="• 你前往科學院完成實驗紀錄，智力<:MNR_INC_B:1375507280711123087>。",color=discord.Color.green())
                await  interaction.response.send_message(embed=sciencesembed,ephemeral=True)
            else:
                events = Event('Sciences',selected_event)
                embed = events[0]
                await  interaction.response.send_message(embed=embed,view=EventChoice(events),ephemeral=True)
            ARG.minus_stamina(str(interaction.user.id))
            self.stamina -= 1
        else:
            nosta_message = "```diff\n- 體力不支\n```"
            await  interaction.response.send_message(nosta_message,ephemeral=True)
    @discord.ui.button(label="樂府",style=discord.ButtonStyle.primary, row=0)
    async def button_balladss(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.stamina > 0:
            selected_event = ARG.event_lottery(interaction.user.id,'CUL','TEC','BUS','MIL',1)
            ARG.gain_state(str(interaction.user.id),'CHR',2)
            if selected_event == 0: 
                balladssembed = discord.Embed(title="❖ 工作結算：",description="• 你前往樂府抄錄古典詩集，魅力<:MNR_INC_B:1375507280711123087>。",color=discord.Color.purple())
                await  interaction.response.send_message(embed=balladssembed,ephemeral=True)
            else:
                events = Event('Balladss',selected_event)
                embed = events[0]
                await  interaction.response.send_message(embed=embed,view=EventChoice(events),ephemeral=True)
            ARG.minus_stamina(str(interaction.user.id))
            self.stamina -= 1
        else:
            nosta_message = "```diff\n- 體力不支\n```"
            await  interaction.response.send_message(nosta_message,ephemeral=True)
    @discord.ui.button(label="兵營",style=discord.ButtonStyle.success, row=1)
    async def button_military(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.stamina > 0:
            user_id = str(interaction.user.id)
            selected_event = ARG.event_lottery(user_id,'MIL','TEC','CUL','BUS',1)
            ARG.gain_state(user_id,'STR',1) 
            amount = ARG.resource_mag(user_id,'STR') * (random.randint(4,9))
            ARG.gain_resource(user_id,'MIL_rs',amount)
            if selected_event == 0: 
                militaryembed = discord.Embed(title="❖ 工作結算：",description=f"• 你前往兵營進行補給物資訓練，武力<:SLT_INC_B:1375507405059657778>，且軍事<:INC:1375507210448277595>{amount}。",color=discord.Color.red())
                await  interaction.response.send_message(embed=militaryembed,ephemeral=True)
            else:
                events = Event('Military',selected_event,user_id,amount)
                embed = events[0]
                await  interaction.response.send_message(embed=embed,view=EventChoice(events),ephemeral=True)
            ARG.minus_stamina(user_id)
            self.stamina -= 1
        else:
            nosta_message = "```diff\n- 體力不支\n```"
            await  interaction.response.send_message(nosta_message,ephemeral=True)
    @discord.ui.button(label="市集",style=discord.ButtonStyle.success, row=1)
    async def button_market(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.stamina > 0:
            user_id = str(interaction.user.id)
            selected_event = ARG.event_lottery(user_id,'BUS','CUL','MIL','TEC',2)
            ARG.gain_state(user_id,'DOM',1) 
            amount = ARG.resource_mag(user_id,'DOM') * (random.randint(4,9))
            ARG.gain_resource(user_id,'BUS_rs',amount)
            if selected_event == 0: 
                marketembed = discord.Embed(title="❖ 工作結算：",description=f"• 你前往市集規劃促銷活動，內政<:SLT_INC_B:1375507405059657778>，且商業<:INC:1375507210448277595>{amount}。",color=discord.Color.gold())
                await  interaction.response.send_message(embed=marketembed,ephemeral=True)
            else:
                events = Event('Market',selected_event,user_id,amount)
                embed = events[0]
                await  interaction.response.send_message(embed=embed,view=EventChoice(events),ephemeral=True)
            ARG.minus_stamina(user_id)
            self.stamina -= 1
        else:
            nosta_message = "```diff\n- 體力不支\n```"
            await  interaction.response.send_message(nosta_message,ephemeral=True)
    @discord.ui.button(label="匠人坊",style=discord.ButtonStyle.success, row=1)
    async def button_workshop(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.stamina > 0:
            user_id = str(interaction.user.id)
            selected_event = ARG.event_lottery(user_id,'TEC','MIL','BUS','CUL',1)
            ARG.gain_state(user_id,'INT',1) 
            amount = ARG.resource_mag(user_id,'INT') * (random.randint(4,9))
            ARG.gain_resource(user_id,'TEC_rs',amount)
            if selected_event == 0: 
                workshopembed = discord.Embed(title="❖ 工作結算：",description=f"• 你前往匠人坊擔任學徒，智力<:SLT_INC_B:1375507405059657778>，且科技<:INC:1375507210448277595>{amount}。",color=discord.Color.green())
                await  interaction.response.send_message(embed=workshopembed,ephemeral=True)
            else:
                events = Event('Workshop',selected_event,user_id,amount)
                embed = events[0]
                await  interaction.response.send_message(embed=embed,view=EventChoice(events),ephemeral=True)
            ARG.minus_stamina(user_id)
            self.stamina -= 1
        else:
            nosta_message = "```diff\n- 體力不支\n```"
            await  interaction.response.send_message(nosta_message,ephemeral=True)
    @discord.ui.button(label="茶館",style=discord.ButtonStyle.success, row=1)
    async def button_teahouse(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.stamina > 0:
            user_id = str(interaction.user.id)
            selected_event = ARG.event_lottery(user_id,'CUL','BUS','TEC','MIL',1)
            ARG.gain_state(user_id,'CHR',1) 
            amount = ARG.resource_mag(user_id,'CHR') * (random.randint(4,9))
            ARG.gain_resource(user_id,'CUL_rs',amount)
            if selected_event == 0: 
                teahouseembed = discord.Embed(title="❖ 工作結算：",description=f"• 你前往茶館安排藝人演出，魅力<:SLT_INC_B:1375507405059657778>，且文化<:INC:1375507210448277595>{amount}。",color=discord.Color.purple())
                await  interaction.response.send_message(embed=teahouseembed,ephemeral=True)
            else:
                events = Event('Teahouse',selected_event,user_id,amount)
                embed = events[0]
                await  interaction.response.send_message(embed=embed,view=EventChoice(events),ephemeral=True)
            ARG.minus_stamina(user_id)
            self.stamina -= 1
        else:
            nosta_message = "```diff\n- 體力不支\n```"
            await  interaction.response.send_message(nosta_message,ephemeral=True)
    @discord.ui.button(label="兵工廠",style=discord.ButtonStyle.danger, row=2)
    async def button_arsenal(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.stamina > 0:
            user_id = str(interaction.user.id)
            selected_event = ARG.event_lottery(user_id,'MIL','TEC','BUS','CUL',3)
            amount = ARG.resource_mag(user_id,'STR') * 10
            amountt = ARG.resource_mag(user_id,'DOM') * 5
            ARG.gain_resource(user_id,'MIL_rs',amount)
            ARG.gain_resource(user_id,'BUS_rs',amountt)
            if selected_event == 0: 
                arsenalembed = discord.Embed(title="❖ 工作結算：",description=f"• 你前往兵工廠協助武器製造，軍事<:INC:1375507210448277595>{amount}、商業<:INC:1375507210448277595>{amountt}。",color=discord.Color.red())
                await  interaction.response.send_message(embed=arsenalembed,ephemeral=True)
                ARG.minus_stamina(user_id)
            else:
                events = Event('Arsenal',selected_event,user_id,amount,amountt)
                embed = events[0]
                await  interaction.response.send_message(embed=embed,view=EventChoice(events),ephemeral=True)
            ARG.minus_stamina(user_id)
            self.stamina -= 1
        else:
            nosta_message = "```diff\n- 體力不支\n```"
            await  interaction.response.send_message(nosta_message,ephemeral=True)
    @discord.ui.button(label="接待所",style=discord.ButtonStyle.danger, row=2)
    async def button_reception(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.stamina > 0:
            user_id = str(interaction.user.id)
            selected_event = ARG.event_lottery(user_id,'BUS','TEC','CUL','MIL',4)
            amount = ARG.resource_mag(user_id,'DOM') * 10
            amountt = ARG.resource_mag(user_id,'INT') * 5
            ARG.gain_resource(user_id,'BUS_rs',amount)
            ARG.gain_resource(user_id,'TEC_rs',amountt)
            if selected_event == 0: 
                receptionembed = discord.Embed(title="❖ 工作結算：",description=f"• 你前往接待所協助接待外賓，商業<:INC:1375507210448277595>{amount}、科技<:INC:1375507210448277595>{amountt}。",color=discord.Color.gold())
                await  interaction.response.send_message(embed=receptionembed,ephemeral=True)
            else:
                events = Event('Reception',selected_event,user_id,amount,amountt)
                embed = events[0]
                await  interaction.response.send_message(embed=embed,view=EventChoice(events),ephemeral=True)
            ARG.minus_stamina(user_id)
            self.stamina -= 1
        else:
            nosta_message = "```diff\n- 體力不支\n```"
            await  interaction.response.send_message(nosta_message,ephemeral=True)
    @discord.ui.button(label="加工所",style=discord.ButtonStyle.danger, row=2)
    async def button_factory(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.stamina > 0:
            user_id = str(interaction.user.id)
            selected_event = ARG.event_lottery(user_id,'TEC','CUL','BUS','MIL',3)
            amount = ARG.resource_mag(user_id,'INT') * 10
            amountt = ARG.resource_mag(user_id,'CHR') * 5
            ARG.gain_resource(user_id,'TEC_rs',amount)
            ARG.gain_resource(user_id,'CUL_rs',amountt)
            if selected_event == 0: 
                factoryembed = discord.Embed(title="❖ 工作結算：",description=f"• 你前往加工所協助安排進出貨，科技<:INC:1375507210448277595>{amount}、文化<:INC:1375507210448277595>{amountt}。",color=discord.Color.gold())
                await  interaction.response.send_message(embed=factoryembed,ephemeral=True)
            else:
                events = Event('Factory',selected_event,user_id,amount,amountt)
                embed = events[0]
                await  interaction.response.send_message(embed=embed,view=EventChoice(events),ephemeral=True)
            ARG.minus_stamina(user_id)
            self.stamina -= 1
        else:
            nosta_message = "```diff\n- 體力不支\n```"
            await  interaction.response.send_message(nosta_message,ephemeral=True)
    @discord.ui.button(label="博物院",style=discord.ButtonStyle.danger, row=2)
    async def button_museum(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.stamina > 0:
            user_id = str(interaction.user.id)
            selected_event = ARG.event_lottery(user_id,'CUL','BUS','MIL','TEC',3)
            amount = ARG.resource_mag(user_id,'CHR') * 10
            amountt = ARG.resource_mag(user_id,'STR') * 5
            ARG.gain_resource(user_id,'CUL_rs',amount)
            ARG.gain_resource(user_id,'MIL_rs',amount)
            if selected_event == 0: 
                museumembed = discord.Embed(title="❖ 工作結算：",description=f"• 你前往博物院協助進行導覽，文化<:INC:1375507210448277595>{amount}、軍事<:INC:1375507210448277595>{amountt}。",color=discord.Color.gold())
                await  interaction.response.send_message(embed=museumembed,ephemeral=True)
            else:
                events = Event('Museum',selected_event,user_id,amount,amountt)
                embed = events[0]
                await  interaction.response.send_message(embed=embed,view=EventChoice(events),ephemeral=True)
            ARG.minus_stamina(user_id)
            self.stamina -= 1
        else:
            nosta_message = "```diff\n- 體力不支\n```"
            await  interaction.response.send_message(nosta_message,ephemeral=True)
    @discord.ui.button(label="海港",style=discord.ButtonStyle.secondary, row=3)
    async def button_dock(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.stamina > 0:
            user_id = str(interaction.user.id)
            number = random.randint(1,16)
            dockclose = DockEvent(number, user_id) 
            await  interaction.response.send_message(embed=dockclose,ephemeral=True)
            ARG.minus_stamina(user_id)
            self.stamina -= 1
        else:
            nosta_message = "```diff\n- 體力不支\n```"
            await  interaction.response.send_message(nosta_message,ephemeral=True)

class EventChoice(discord.ui.View):
    def __init__(self, events):
        super().__init__()
        self.event1 = events[1]
        self.state1 = events[2]
        self.amount1 = events[3]
        self.event2 = events[4]
        self.state2 = events[5]
        self.amount2 = events[6]
        self.trigger = False 
    @discord.ui.button(label="選項一",style=discord.ButtonStyle.primary)
    async def button_first(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.trigger == False :
            if self.state1 in ('STR','DOM','INT','CHR'):
                ARG.gain_state(str(interaction.user.id),self.state1,self.amount1)
            else:
                ARG.gain_resource(str(interaction.user.id),self.state1,self.amount1)
            embed=self.event1
            self.trigger = True
            await interaction.response.send_message(embed=embed,ephemeral=True)
    @discord.ui.button(label="選項二",style=discord.ButtonStyle.primary)
    async def button_second(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.trigger == False :
            if self.state1 in ('STR','DOM','INT','CHR'):
                ARG.gain_state(str(interaction.user.id),self.state2,self.amount2)
            else:
                ARG.gain_resource(str(interaction.user.id),self.state2,self.amount2)
            embed=self.event2
            self.trigger = True
            await interaction.response.send_message(embed=embed,ephemeral=True)


class PresistentViewBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents().all()
        super().__init__(command_prefix=commands.when_mentioned_or('.'), intents=intents)
    async def setup_hook(self) -> None:
        self.add_view(Index())
    async def on_ready(self):
        print(f'Ligged on as {self.user}!')
        try:
            guild = discord.Object(serverid)
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


