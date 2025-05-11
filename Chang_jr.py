import discord, random
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True
Token = ''
channelid = 

GUILD_ID = discord.Object(channelid)

class Index(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(label="去工作",style=discord.ButtonStyle.primary, custom_id='1')
    async def button_work(self,button, interactionl):
        await button.response.send_message(view=Work(),ephemeral=True)
    @discord.ui.button(label="個人狀態",style=discord.ButtonStyle.primary, custom_id='2')
    async def button_state(self,button, interaction):
        personalstate = discord.Embed(title="個人狀態Beta",url="https://blogs.mtdv.me/blog/posts/nDIQhaU8Kd", description="由於技術上的問題方士團仍無法在Discord 上重現渾元萬劫的個人狀態的部分，但有對此功能仍有興趣的諸侯們仍然可以透過上方「個人狀態Beta」連結體驗測試版")
        await button.response.send_message(embed=personalstate,ephemeral=True)
    @discord.ui.button(label="請安",style=discord.ButtonStyle.primary, custom_id='3')
    async def button_morning(self,button, interaction):
        await button.response.send_message("早奄",ephemeral=True)

class Work(discord.ui.View):
    # @discord.ui.button(label="校場",style=discord.ButtonStyle.primary, row=0)
    # async def button_field(self,button, interaction):
    #     await button.response.send_message(view=FieldEvent(),ephemeral=True)
    # @discord.ui.button(label="太學",style=discord.ButtonStyle.primary, row=0)
    # async def button_college(self,button, interaction):
    #     await button.response.send_message("太學",ephemeral=True)
    # @discord.ui.button(label="科學院",style=discord.ButtonStyle.primary, row=0)
    # async def button_sciences(self,button, interaction):
    #     await button.response.send_message("科學院",ephemeral=True)
    # @discord.ui.button(label="樂府",style=discord.ButtonStyle.primary, row=0)
    # async def button_balladss(self,button, interaction):
    #     await button.response.send_message("樂府",ephemeral=True)
        
    # @discord.ui.button(label="兵營",style=discord.ButtonStyle.success, row=1)
    # async def button_military(self,button, interaction):
    #     await button.response.send_message("兵營",ephemeral=True)
    # @discord.ui.button(label="市集",style=discord.ButtonStyle.success, row=1)
    # async def button_market(self,button, interaction):
    #     await button.response.send_message("市集",ephemeral=True)
    # @discord.ui.button(label="匠人坊",style=discord.ButtonStyle.success, row=1)
    # async def button_workshop(self,button, interaction):
    #     await button.response.send_message("匠人坊",ephemeral=True)
    # @discord.ui.button(label="茶館",style=discord.ButtonStyle.success, row=1)
    # async def button_teahouse(self,button, interaction):
    #     await button.response.send_message("茶館",ephemeral=True)

    # @discord.ui.button(label="兵工廠",style=discord.ButtonStyle.danger, row=2)
    # async def button_arsenal(self,button, interaction):
    #     await button.response.send_message("兵工廠",ephemeral=True)
    # @discord.ui.button(label="接待所",style=discord.ButtonStyle.danger, row=2)
    # async def button_reception(self,button, interaction):
    #     await button.response.send_message("接待所",ephemeral=True)
    # @discord.ui.button(label="加工所",style=discord.ButtonStyle.danger, row=2)
    # async def button_factory(self,button, interaction):
    #     await button.response.send_message("加工所",ephemeral=True)
    # @discord.ui.button(label="博物院",style=discord.ButtonStyle.danger, row=2)
    # async def button_museum(self,button, interaction):
    #     await button.response.send_message("博物院",ephemeral=True)
    
    @discord.ui.button(label="海港",style=discord.ButtonStyle.secondary, row=3)
    async def button_dock(self,button, interaction):
        number = random.randint(1,29)
        dockclose = DockEvent(number)
        await button.response.send_message(embed=dockclose,ephemeral=True)

def DockEvent(arg):
    match arg:
        case 1:
            dockclose = discord.Embed(title="拜師學藝",description="➤你探訪一處幽僻深山，恰巧遇到隱居在此的絕世高人，不想卻在拜師學藝的過程中弄傷了腿，只得無奈下山")
            dockclose.add_field(name=" ",value="-----------------------------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="🗡️武力⬇️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 2:
            dockclose = discord.Embed(title="野營受寒",description="➤你獨自來到山林野營，磨練自己的意志與生存技巧，卻不幸因受寒生病被迫提前下山。")
            dockclose.add_field(name=" ",value="-----------------------------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="🗡️武力⬇️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 3:
            dockclose = discord.Embed(title="遭遇搶劫",description="➤你來到偏僻的小鎮，此處工藝鼎盛，但近年來治安不佳。你回程時天色已晚，果然遭遇搶劫，萬幸是並無大礙。")
            dockclose.add_field(name=" ",value="-----------------------------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="👓內政⬇️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 4:
            dockclose = discord.Embed(title="討價還價",description="➤你與兜售紀念品的小販周旋，成功將心儀的商品閃成半價。本以為賺到，事後才發現自己被敲了竹槓。")
            dockclose.add_field(name=" ",value="-----------------------------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="👓內政⬇️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 5:
            dockclose = discord.Embed(title="海關扣留",description="➤你一不小心上錯了船，抵達目的地後才發現不對，又因沒有簽證導致被扣押在外國海關。")
            dockclose.add_field(name=" ",value="-----------------------------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="🧠智力⬇️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 6:
            dockclose = discord.Embed(title="粗心大意",description="➤你此趟欲探訪秘境，然而出門前才驚覺沒帶證件。最後你只能眼睜睜看著船離岸，一邊對自己的粗心感到喪氣。")
            dockclose.add_field(name=" ",value="-----------------------------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="🧠智力⬇️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 7:
            dockclose = discord.Embed(title="小鎮導覽",description="➤你請了一位地陪明天為你進行小鎮導覽，然而不小心睡過頭導致對方等了你好一會，使對方對你的印象不佳。")
            dockclose.add_field(name=" ",value="-----------------------------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="🩷魅力⬇️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 8:
            dockclose = discord.Embed(title="火災警報",description="➤你被火災警報驚醒，來不及梳整就奪門而出，卻發現只是惡作劇，而你邋遢的模樣被同行的其他人無情嘲笑。")
            dockclose.add_field(name=" ",value="-----------------------------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="🩷魅力⬇️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 9:
            dockclose = discord.Embed(title="山林修練",description="➤你獨自來到山林野營，磨練自己的意志與生存技巧。雖然艱苦，但山林的幽靜讓你得以沉澱自我。")
            dockclose.add_field(name=" ",value="-----------------------------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="🗡️武力⬆️⬆️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 10:
            dockclose = discord.Embed(title="觀摩商店街",description="➤你此次來到鄰國的首都，花了許多時間仔細觀摩商店街的店舖與動線規劃，得到很大的啟發。")
            dockclose.add_field(name=" ",value="-----------------------------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="👓內政⬆️⬆️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 11:
            dockclose = discord.Embed(title="輪船遊歷",description="➤你搭乘輪船，沿著海岸線遊歷多地、看盡山川地形，對於這些地區的地理環境與氣候有了更深的了解。")
            dockclose.add_field(name=" ",value="-----------------------------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="🧠智力⬆️⬆️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 12:
            dockclose = discord.Embed(title="料理祕方",description="➤你此趟探訪海濱的小村莊，當地的婆婆媽媽們與你十分投緣，進而傳授你當地殊季節料理的製作秘方。")
            dockclose.add_field(name=" ",value="-----------------------------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="🩷魅力⬆️⬆️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose 
        
        case 13:
            dockclose = discord.Embed(title="先發制人",description="➤你旅途中偶然聽見外地商人談及敵軍調動與物資轉運，便默記於心。回家後立即上報軍方，經研判屬實，我軍隨即調整部署，成功先發制人。")
            dockclose.add_field(name=" ",value="-----------------------------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="⚔️軍事➕20")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 14:
            dockclose = discord.Embed(title="邊疆觀光",description="➤你探訪邊疆小鎮，此處手工藝鼎盛，令你讚歎不已。你立刻上書提議大力扶植該鎮觀光，果然大獲成功")
            dockclose.add_field(name=" ",value="-----------------------------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="⚖️商業➕20")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 15:
            dockclose = discord.Embed(title="地方祭典",description="➤你恰巧遇上當地祭典，深受文化衝擊與感動。返國後，你上書將此祭典列為官方節日，自此成為地方一大盛事。")
            dockclose.add_field(name=" ",value="-----------------------------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="🏺文化➕20")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 16:
            dockclose = discord.Embed(title="工廠參訪",description="➤你來到偏僻的小鎮並參訪當地工廠，驚覺該廠商技術力驚人。回家後，你上書促成政府與該廠商合作，果然造就雙贏局面")
            dockclose.add_field(name=" ",value="-----------------------------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="🧪科技➕20")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 17:
            dockclose = discord.Embed(title="奄國觀光",description="➤你來到以回收產業發達出名的奄國，吃了當地的特產水餃與包子。遇到一群以理服人的大肌肌奄國人，還跟他們一起上山下海立旗子。")
            dockclose.add_field(name="Make 奄國 great again ！！",value="-----------------------------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value=" 旅遊回憶⬆️⬆️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 18:
            dockclose = discord.Embed(title="天降大獎？",description="➤你手滑不小心參加了一個...什麼......【Nintendo Switch 2購買資格抽選】，還不小心抽中了！！！\n但你不知道這到底是什麼東西啊！？下一刻直接把資格丟向大海。")
            dockclose.add_field(name=" ",value="-----------------------------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="🍀幸運值？ ⬆️⬆️⬆️\n🎮NS2？ ⬇️ (已蛋雕)")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 19:
            dockclose = discord.Embed(title="起來重跳！！！",description="➤再次看到海港的你非常的激動，不管三七二十一直接一躍而下，或許是水花太大的緣故，老張不知道為什麼從旁邊浮出來並舉牌出很低的分數要你重新再跳港一次。")
            dockclose.add_field(name=" ",value="-----------------------------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="❌跳水不及格成績 ⬆️⬆️ ")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose
        
        case 20:
            dockclose = discord.Embed(title="好討厭的感覺啊！",description="➤既然你誠心誠意地發問了，為了防止世界被破壞，為了守護世界的和平......")
            dockclose.add_field(name=" ",value="-----------------------------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="🖤貫徹愛與真實的邪惡！ ⬆️⬆️⬆️\n❤️可愛又迷人的反派角色！ ⬆️⬆️⬆️\n🐱就是這樣！喵！ ⬆️⬆️⬆️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 21:
            dockclose = discord.Embed(title="你知道嗎",description="➤你夢到你因為來不及在頻道關閉前離開，而被困在封存頻道的時空夾縫中。長久的孤獨逐漸剝奪你的時間感、空間感，甚至是理智。在你即將崩潰之際，你竟然碰到了兩位諸侯。\n「你好！我是夏國人。我叫納茲汀！」\n「你好！我是瀛國人。叫我羊羊就可以了！」\n接著二位以「你知道嗎」起頭，交替向你傳遞各種神奇小知識。你逐漸失去意識……\n\n意識恢復後，你躺在熟悉的床上，你深知那是一場夢，然而那些小知識已經深深地刻印在你的腦海裡了。")
            dockclose.add_field(name=" ",value="-----------------------------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="SAN值⬇️⬇️⬇️⬇️ ")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 22:
            dockclose = discord.Embed(title="通商惠商",description="➤你到商國進行出國考察，親身體驗以商為立國之本的理念。最後你攜帶的盤纏所剩無幾。")
            dockclose.add_field(name=" ",value="-----------------------------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="商國 :scales: 商業 ➕ 1")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 23:
            dockclose = discord.Embed(title="海闡普渡",description="➤今天是普渡回到陽間亡者的日子，於是你到闡國參與了該國的全國大普渡。\n雖然諸侯們的身影在成型與消散的狀態中往復的景象有些駭人，但看到這些老朋友還是讓你很開心，也想起當年觀光時與他們跳海的回憶。")
            dockclose.add_field(name=" ",value="-----------------------------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="🏊 跳海⬆️⬆️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 24:
            dockclose = discord.Embed(title="搖曳露營△",description="➤你在奄國的深夜發現有人圍著營火，你出於好奇湊上前去。\n一開始只是溫馨的爐邊談話，你也就這麼聽著。然而隨著時間流逝，話題逐漸偏移。連餘燼都熄滅之時，話題早已轉到各種蟲蟲危機經驗談跟爬蟲冷知識。\n\n「我突然覺得世界頻道好像比較正常一點。」你望著天邊的魚肚白，又默默地插了一把旗子。")
            dockclose.add_field(name=" ",value="-----------------------------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="🚩 旗子➕ 10  ")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 25:
            dockclose = discord.Embed(title="心不在奄",description="➤奄茶出了新口味，你下班後開心地去買了一杯，打算回家好好享用。\n然而要扶人過馬路時不慎手滑，剛買的飲料就這麼貢獻給蓬萊的大地。\n「啊！！！我的奄茶！！！！30塊！！！奄茶！！！！」你不禁大叫起來。")
            dockclose.add_field(name=" ",value="-----------------------------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value=" 👛 資產 :heavy_minus_sign:  30元")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 26:
            dockclose = discord.Embed(title="反海宣導講座",description="➤為了因應日漸嚴重的跳海成癮趨勢，奄國在海港舉辦了一場反海宣導講座，播放在混元末期海港關閉時拍攝的紀錄片。\n只見影片裡一群跳海成癮末期的太陽人像殭屍一樣抓著海港的欄杆大喊：「放我進去！！！我要跳海！！！」，鏡頭一轉看到已經乾到不成太陽人形的太陽人倒在路邊，嘴裏喃喃著：「好想跳海⋯」，甚至還有太陽人一邊喊著「火海也是海！」一邊往火裡跳⋯⋯\n\n這真是太可怕了。\n你決定珍愛生命，遠離海港。")
            dockclose.add_field(name=" ",value="-----------------------------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value=" 🌊 跳海慾望⬇️⬇️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 27:
            dockclose = discord.Embed(title="拾金不昧",description="➤你在海邊散步的時候撿到了1000金！\n\n經過一番掙扎後，你最後還是決定把金送到警察局，聞訊而來的失主對你感激萬分，給了你100金表達謝意。此事件傳開後，大家對你拾金不昧的善舉感到欽佩，你的略微名聲上升。")
            dockclose.add_field(name=" ",value="-----------------------------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="資產➕100金\n名聲⬆️⬆️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 28:
            dockclose = discord.Embed(title="拾金而昧",description="➤你在海邊散步的時候撿到了1000金！\n\n雖然你也想過要不要送去警察局，但錢錢的誘惑太大，你左看右看四下無人，決定將這1000金偷偷拿走。\n\n你用這些金買了返笑、不願和九月三款遊戲，在海邊撿到金真是太幸運了！")
            dockclose.add_field(name=" ",value="-----------------------------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="獲得遊戲 X 3\n罪惡感⬆️⬆️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 29:
            dockclose = discord.Embed(title="海邊的紅包不要亂撿",description="➤你在海邊散步的時候撿到了一個紅包，裡面居然有1000金！\n\n你開心的拿走這些錢，但回家的路上總覺得有人跟在你身後......")
            dockclose.add_field(name=" ",value="-----------------------------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="SAN值⬇️⬇️⬇️⬇️ ")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose


# class FieldEvent(discord.ui.View):
#     async def FieldEventPrint(self):
#         dockclose = discord.Embed(title="[校場特殊事件-結算]", description='dock_description')
#         await interaction.response.send_message(embed=dockclose,ephemeral=True)
#     @discord.ui.button(label="選項一",style=discord.ButtonStyle.primary)
#     async def choose_one(self,button, interaction):
#         await button.response.send_message("拜師學藝",ephemeral=True)
#     @discord.ui.button(label="選項二",style=discord.ButtonStyle.primary)
#     async def choose_two(self,button, interaction):
#         await button.response.send_message("拜師學藝",ephemeral=True)


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
    await interaction.response.send_message(view=Index())

client.run(Token)
