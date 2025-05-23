import discord, random, pytz 
from discord.ext import commands
from discord import app_commands


def DockEvent(arg):
    match arg:
        case 1:
            dockclose = discord.Embed(title="拜師學藝",description="➤你探訪一處幽僻深山，恰巧遇到隱居在此的絕世高人，不想卻在拜師學藝的過程中弄傷了腿，只得無奈下山")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="🗡️武力⬇️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 2:
            dockclose = discord.Embed(title="野營受寒",description="➤你獨自來到山林野營，磨練自己的意志與生存技巧，卻不幸因受寒生病被迫提前下山。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="🗡️武力⬇️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 3:
            dockclose = discord.Embed(title="遭遇搶劫",description="➤你來到偏僻的小鎮，此處工藝鼎盛，但近年來治安不佳。你回程時天色已晚，果然遭遇搶劫，萬幸是並無大礙。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="👓內政⬇️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 4:
            dockclose = discord.Embed(title="討價還價",description="➤你與兜售紀念品的小販周旋，成功將心儀的商品閃成半價。本以為賺到，事後才發現自己被敲了竹槓。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="👓內政⬇️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 5:
            dockclose = discord.Embed(title="海關扣留",description="➤你一不小心上錯了船，抵達目的地後才發現不對，又因沒有簽證導致被扣押在外國海關。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="🧠智力⬇️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 6:
            dockclose = discord.Embed(title="粗心大意",description="➤你此趟欲探訪秘境，然而出門前才驚覺沒帶證件。最後你只能眼睜睜看著船離岸，一邊對自己的粗心感到喪氣。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="🧠智力⬇️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 7:
            dockclose = discord.Embed(title="小鎮導覽",description="➤你請了一位地陪明天為你進行小鎮導覽，然而不小心睡過頭導致對方等了你好一會，使對方對你的印象不佳。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="🩷魅力⬇️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 8:
            dockclose = discord.Embed(title="火災警報",description="➤你被火災警報驚醒，來不及梳整就奪門而出，卻發現只是惡作劇，而你邋遢的模樣被同行的其他人無情嘲笑。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="🩷魅力⬇️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 9:
            dockclose = discord.Embed(title="山林修練",description="➤你獨自來到山林野營，磨練自己的意志與生存技巧。雖然艱苦，但山林的幽靜讓你得以沉澱自我。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="🗡️武力⬆️⬆️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 10:
            dockclose = discord.Embed(title="觀摩商店街",description="➤你此次來到鄰國的首都，花了許多時間仔細觀摩商店街的店舖與動線規劃，得到很大的啟發。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="👓內政⬆️⬆️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 11:
            dockclose = discord.Embed(title="輪船遊歷",description="➤你搭乘輪船，沿著海岸線遊歷多地、看盡山川地形，對於這些地區的地理環境與氣候有了更深的了解。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="🧠智力⬆️⬆️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 12:
            dockclose = discord.Embed(title="料理祕方",description="➤你此趟探訪海濱的小村莊，當地的婆婆媽媽們與你十分投緣，進而傳授你當地殊季節料理的製作秘方。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="🩷魅力⬆️⬆️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose 
        
        case 13:
            dockclose = discord.Embed(title="先發制人",description="➤你旅途中偶然聽見外地商人談及敵軍調動與物資轉運，便默記於心。回家後立即上報軍方，經研判屬實，我軍隨即調整部署，成功先發制人。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="⚔️軍事➕20")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 14:
            dockclose = discord.Embed(title="邊疆觀光",description="➤你探訪邊疆小鎮，此處手工藝鼎盛，令你讚歎不已。你立刻上書提議大力扶植該鎮觀光，果然大獲成功")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="⚖️商業➕20")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 15:
            dockclose = discord.Embed(title="地方祭典",description="➤你恰巧遇上當地祭典，深受文化衝擊與感動。返國後，你上書將此祭典列為官方節日，自此成為地方一大盛事。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="🏺文化➕20")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 16:
            dockclose = discord.Embed(title="工廠參訪",description="➤你來到偏僻的小鎮並參訪當地工廠，驚覺該廠商技術力驚人。回家後，你上書促成政府與該廠商合作，果然造就雙贏局面")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="🧪科技➕20")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 17:
            dockclose = discord.Embed(title="奄國觀光",description="➤你來到以回收產業發達出名的奄國，吃了當地的特產水餃與包子。遇到一群以理服人的大肌肌奄國人，還跟他們一起上山下海立旗子。")
            dockclose.add_field(name="Make 奄國 great again ！！",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value=" 旅遊回憶⬆️⬆️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 18:
            dockclose = discord.Embed(title="天降大獎？",description="➤你手滑不小心參加了一個...什麼......【Nintendo Switch 2購買資格抽選】，還不小心抽中了！！！\n但你不知道這到底是什麼東西啊！？下一刻直接把資格丟向大海。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="🍀幸運值？ ⬆️⬆️⬆️\n🎮NS2？ ⬇️ (已蛋雕)")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 19:
            dockclose = discord.Embed(title="起來重跳！！！",description="➤再次看到海港的你非常的激動，不管三七二十一直接一躍而下，或許是水花太大的緣故，老張不知道為什麼從旁邊浮出來並舉牌出很低的分數要你重新再跳港一次。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="❌跳水不及格成績 ⬆️⬆️ ")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose
        
        case 20:
            dockclose = discord.Embed(title="好討厭的感覺啊！",description="➤既然你誠心誠意地發問了，為了防止世界被破壞，為了守護世界的和平......")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="🖤貫徹愛與真實的邪惡！ ⬆️⬆️⬆️\n❤️可愛又迷人的反派角色！ ⬆️⬆️⬆️\n🐱就是這樣！喵！ ⬆️⬆️⬆️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 21:
            dockclose = discord.Embed(title="你知道嗎",description="➤你夢到你因為來不及在頻道關閉前離開，而被困在封存頻道的時空夾縫中。長久的孤獨逐漸剝奪你的時間感、空間感，甚至是理智。在你即將崩潰之際，你竟然碰到了兩位諸侯。\n「你好！我是夏國人。我叫納茲汀！」\n「你好！我是瀛國人。叫我羊羊就可以了！」\n接著二位以「你知道嗎」起頭，交替向你傳遞各種神奇小知識。你逐漸失去意識……\n\n意識恢復後，你躺在熟悉的床上，你深知那是一場夢，然而那些小知識已經深深地刻印在你的腦海裡了。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="SAN值⬇️⬇️⬇️⬇️ ")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 22:
            dockclose = discord.Embed(title="通商惠商",description="➤你到商國進行出國考察，親身體驗以商為立國之本的理念。最後你攜帶的盤纏所剩無幾。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="商國 :scales: 商業 ➕ 1")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 23:
            dockclose = discord.Embed(title="海闡普渡",description="➤今天是普渡回到陽間亡者的日子，於是你到闡國參與了該國的全國大普渡。\n雖然諸侯們的身影在成型與消散的狀態中往復的景象有些駭人，但看到這些老朋友還是讓你很開心，也想起當年觀光時與他們跳海的回憶。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="🏊 跳海⬆️⬆️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 24:
            dockclose = discord.Embed(title="搖曳露營△",description="➤你在奄國的深夜發現有人圍著營火，你出於好奇湊上前去。\n一開始只是溫馨的爐邊談話，你也就這麼聽著。然而隨著時間流逝，話題逐漸偏移。連餘燼都熄滅之時，話題早已轉到各種蟲蟲危機經驗談跟爬蟲冷知識。\n\n「我突然覺得世界頻道好像比較正常一點。」你望著天邊的魚肚白，又默默地插了一把旗子。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="🚩 旗子➕ 10  ")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 25:
            dockclose = discord.Embed(title="心不在奄",description="➤奄茶出了新口味，你下班後開心地去買了一杯，打算回家好好享用。\n然而要扶人過馬路時不慎手滑，剛買的飲料就這麼貢獻給蓬萊的大地。\n「啊！！！我的奄茶！！！！30塊！！！奄茶！！！！」你不禁大叫起來。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value=" 👛 資產 :heavy_minus_sign:  30元")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 26:
            dockclose = discord.Embed(title="反海宣導講座",description="➤為了因應日漸嚴重的跳海成癮趨勢，奄國在海港舉辦了一場反海宣導講座，播放在混元末期海港關閉時拍攝的紀錄片。\n只見影片裡一群跳海成癮末期的太陽人像殭屍一樣抓著海港的欄杆大喊：「放我進去！！！我要跳海！！！」，鏡頭一轉看到已經乾到不成太陽人形的太陽人倒在路邊，嘴裏喃喃著：「好想跳海⋯」，甚至還有太陽人一邊喊著「火海也是海！」一邊往火裡跳⋯⋯\n\n這真是太可怕了。\n你決定珍愛生命，遠離海港。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value=" 🌊 跳海慾望⬇️⬇️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 27:
            dockclose = discord.Embed(title="拾金不昧",description="➤你在海邊散步的時候撿到了1000金！\n\n經過一番掙扎後，你最後還是決定把金送到警察局，聞訊而來的失主對你感激萬分，給了你100金表達謝意。此事件傳開後，大家對你拾金不昧的善舉感到欽佩，你的略微名聲上升。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="資產➕100金\n名聲⬆️⬆️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 28:
            dockclose = discord.Embed(title="拾金而昧",description="➤你在海邊散步的時候撿到了1000金！\n\n雖然你也想過要不要送去警察局，但錢錢的誘惑太大，你左看右看四下無人，決定將這1000金偷偷拿走。\n\n你用這些金買了返笑、不願和九月三款遊戲，在海邊撿到金真是太幸運了！")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="獲得遊戲 X 3\n罪惡感⬆️⬆️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 29:
            dockclose = discord.Embed(title="海邊的紅包不要亂撿",description="➤你在海邊散步的時候撿到了一個紅包，裡面居然有1000金！\n\n你開心的拿走這些錢，但回家的路上總覺得有人跟在你身後......")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="資產➕ 1000金\n獲得家人(?) X 1\nSAN值⬇️⬇️⬇️⬇️ ")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 30:
            dockclose = discord.Embed(title="漁夫非漁夫",description="➤你在港邊散步，一位漁夫划船靠近向你搭話推銷起包包，「拿啦拿啦拿啦…」\n你心中警鈴大響，在百般糾纏之下仍嚴厲拒絕，遭拒的漁夫不屑地划船離去。\n正當以為逃過一劫，你摸摸口袋卻發現錢包消失了，抬頭只見遠去的漁夫手上有個熟悉的東西…「幹，我的錢包！」\n你急忙跳入海中，但已經來不及追上漁夫，最終渾身濕透又空虛的上岸。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value=" 👛 資產:heavy_minus_sign: 5000金、數張金融卡及證件")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose
            
        case 31:
            dockclose = discord.Embed(title="救命夏夷跳！",description="➤本來你的腦袋有源源不絕的靈感浮現，下一秒突然有隻大強飛到你面前！！！！！\n嚇到靈感瞬間噴飛......唔...呃呃呃(開始狂吐)。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="💥驚嚇感 ⬆️⬆️⬆️⬆️⬆️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 32:
            dockclose = discord.Embed(title="垃圾分類",description="➤你買了奄茶來喝，喝完卻沒有將飲料杯好好回收分類。你的舉止被羊人阿嬤發現，他手上的夾子朝你的屁股伸去。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="屁股 疼痛⬆️⬆️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 33:
            dockclose = discord.Embed(title="吾異藝而逸",description="➤在戰後和平真正降臨前，國際因戰時調度問題一度陷入二次危機。這時，所有特遣員收到來自蓬萊時空管理局的緊急訊息，你與其他化身為諸侯的特遣員開啟想確認內容，看到的卻是老張旋轉，並且在影片結尾變成老張乖乖的奇妙影片。\n\n由於影片內容太過衝擊，導致一部分諸侯在國際會議上頻頻笑場，議場充滿了快活的空氣。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="🕊️ 國際衝突趨緩，蓬萊迎來和平，感謝蓬萊時空管理局的努力。")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 34:
            dockclose = discord.Embed(title="有點杯鄙",description="➤奄國國內喝奄茶的風氣盛行，且因為奄茶有著各種特殊口味的關係，逐漸在各國拓展知名度，甚至有其他國家的民眾會為了喝上一口奄茶特地來奄國觀光。\n奄國科學院為此特別研發出奄茶專用保冰杯──「奄火杯」，並與奄茶合作，帶著奄火杯購買奄茶即享有比自帶環保杯更多的折扣。\n你因一同參與了此次研發，拿到了各色奄火杯作為紀念。原先在思考要不要分送給親友的你，突然發現奄火杯因為精美的外型加上優良保冰效果，在開賣後不久立刻銷售一空。看著大家發文徵求奄火杯，甚至不惜加價也要買到，擁有許多杯的你在這時嗅到商機，立刻將不喜歡的顏色加價掛到平台上賣，賺了一波大的。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="💰資產⬆️⬆️⬆️\n❤️ 良心⬇️⬇️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose
            
        case 35:
            dockclose = discord.Embed(title="風中耳語",description="➤你獨自漫步在海堤上，正在考慮著下海的角度時，空無一人的海堤，徐徐的海風讓你忍不住的發抖。\n你聽見了風聲彷彿耳語飄散在耳際：「我有一個小知識……」")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="你忘記如何下海，也迷失了回家的方向。\n你為數不多的精神值下降了。")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 36:
            dockclose = discord.Embed(title="海堤之夢",description="➤當你在海堤準備一躍而下的瞬間，耳際後傳來了呢喃：「有一個小知識……\n突然你的腦海充滿了各種不屬於你的回憶與畫面讓你頭痛欲裂，各種詭異的聲響與氣味讓你忍不住作嘔。\n你在寒冷的海堤醒來，腦中一片空白像是做了一個陰冷潮濕的夢。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="你的衣服跟錢包都不見了。\n行動力-3")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 37:
            dockclose = discord.Embed(title="凝視深淵",description="➤你望向海港，波光粼粼，突然發現映照在海面上的自己，並對他笑了笑，\n這時，海面上的自己突然向你揮手，你很確定你沒有把手舉起來......\n\n最後你轉身離開港口，頭也不回地離開。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="地上留下一道長長的水漬\n🐙 你甚麼也沒失去...吧")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 38:
            dockclose = discord.Embed(title="成為深淵",description="➤你望向海港，波光粼粼，突然發現映照在海面上的自己，並對他笑了笑，\n這時，海面上的自己突然向你揮手，你很確定你沒有把手舉起來，\n你興奮極了，每天來港口就等這一刻，\n你縱身一躍進入海中，身旁的景色瞬間模糊，你的手也感受到不存在於這世間的觸感。\n一聲淒厲卻又夾帶著興奮的嚎叫後，一切歸於平靜。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="尋找深淵🔍\n凝視深淵👀\n成為深淵🐙")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 39:
            dockclose = discord.Embed(title="冥冥之中",description="➤你聽見了遠處的音樂聲，一位街頭藝人正在自彈自唱，他用你聽不懂的異國語言咕噥著奇怪的小調，而他的吉他不知怎麼的發出生鏽金屬的刮擦聲，你保持沉默。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="你遠離他後在地上撿到了十塊錢。\n金錢➕10")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 40:
            dockclose = discord.Embed(title="冥冥之中",description="➤你聽見了遠處的音樂聲，一位街頭藝人正在自彈自唱，他用你聽不懂的異國語言咕噥著奇怪的小調，而他的吉他不知怎麼的發出生鏽金屬的刮擦聲，你對街頭藝人拍了張照上傳社群。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="你在拍照發文時遭遇了扒竊。\n金錢:heavy_minus_sign:10")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 41:
            dockclose = discord.Embed(title="口耳相傳",description="➤你在市集中閒逛，一個陌生女人與你擦肩而過，他轉身叫住你，靠近你的耳邊說了一個故事。\n你離開市集後已經不記得前因後果，只記得故事中提到的一個食譜。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="你照著食譜做出了美味的包子。\n魅力提升⬆️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 42:
            dockclose = discord.Embed(title="食慾不振",description="➤你在自助餐廳打工時被派去冷藏庫拿取備料，你看見角落的金屬流理臺上放著一個豬腿大的紙包，裡面是一塊帶黑色鱗片的不明大腿肉，在冷凍庫的舊螢光燈照耀下肉看起來是藍色的。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="你今天沒有吃午餐。\n武力⬇️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 43:
            dockclose = discord.Embed(title="食慾不振(?)",description="➤你在自助餐廳打工時被派去冷藏庫拿取備料，你看見角落的金屬流理臺上放著一個豬腿大的紙包，裡面是一塊帶黑色鱗片的不明大腿肉，在冷凍庫的舊螢光燈照耀下肉看起來是藍色的。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="你舔了肉塊。\n智力⬆️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 44:
            dockclose = discord.Embed(title="無妄之災",description="➤你今天來到奄國觀星臺觀光，碰到蓬萊上師來到此地為奄國人占卜，奄國人民自信地說出「會奄喔」。\n上師雙眼放光，低聲說出「原來如此...」，霎時天降異象，天空降下13條光線於群眾身上，你碰巧是其中一位。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="隨機一樣能力值降為F。")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 45:
            dockclose = discord.Embed(title="天降好事",description="➤你今天來到奄國觀星臺觀光，碰到蓬萊上師來到此地為奄國人占卜，奄國人民自信地說出「會奄喔」。\n上師雙眼放光，低聲說出「原來如此...」，霎時天降異象，天空降下13條光線於群眾身上，你碰巧是其中一位。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="隨機一樣能力值升為S。")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 46:
            dockclose = discord.Embed(title="咪咪咪咪咪！",description="➤你來到了一個尚未開發的小島上，那些綠色樹叢上開滿了白色花朵（？）\n\n「咦？好像會動，是我的錯覺嗎」")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="你全身被扒光後被塞進大砲內成為了奄火。")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 47:
            dockclose = discord.Embed(title="冥冥之中",description="➤你聽見了遠處的音樂聲，一位街頭藝人正在自彈自唱，他用你聽不懂的異國語言咕噥著奇怪的小調，而他的吉他不知怎麼的發出生鏽金屬的刮擦聲，你保持沉默。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="你遠離他後在地上撿到了十塊錢。\n金錢+10")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 48:
            dockclose = discord.Embed(title="地底之下",description="➤你在前往海港的路上不小心跌進洞裡，探索周圍後你被一朵小花搭話，你和他聊著聊著你發現到他想要殺了你並取得你的靈魂！\n在你即將被殺死的前一刻，出現一名陌生人施展魔法拯救了你...之後你就在一個深不見底的地洞旁醒來了。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="如此奇怪的夢境(？)使你充滿了決心。")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 49:
            dockclose = discord.Embed(title="另一種可能性",description="➤你經過了廣場，今天剛好有人來說故事，地上坐著許多小朋友，你在遠點的地方聽著，說書人戴著斗笠你看不清楚面貌，他說著與你熟悉的蓬萊歷史截然相反的故事，各個國家的風土民情都跟你學到的不一樣，開發昊天球的科學家夫婦有被成功解救出來，方士團也沒有成立，截通就被八國聯軍擊退。\n\n故事結束後，說書人將斗笠往上抬了抬，赫然發現他與你的長相完全一樣，只是他看起來已經上了年紀，他也看見了你，舉起食指笑著擺出「噓」的手勢，霎時你眼前一片白光，白光退去，你發現躺在家裡的床上，看了時間才發現是平常該起床的時間。\n\n「真是奇怪的夢境，但這個故事也不壞。」")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="行動力+1\n今日工作場所獲得數值微量提升")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 50:
            dockclose = discord.Embed(title="滾石",description="➤有一天夢中的你忽然的撇見了無數的過往、無數的現在、無數的未來，但始終只是撇見，無法改變已經發生的事實。一分為二，二分為四，無數無盡。\n醒來的你只覺得全身勞累，只記得一句話「終將歸於大道」。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="██屬性提升至███\n精神值減少1點\n今日行動力 -1")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 52:
            dockclose = discord.Embed(title="落日",description="➤能得見。他離家時的決意以及與對家人的不理解，他桀傲不遜。\n能得見。他被尊為師長之人背叛時的慘烈，他落魄不已。\n能得見。他復原後與無毛類人的友愛，他重拾希望。\n能得見。他為了復仇而不斷受傷的身軀以及對曾經同夥的恨意，他恨之入骨。\n能得見。他理解到家人當初的想法並走向對他人更好的道路，他感慨萬分。\n能得見。他雙眼無神的目光將弓箭射向一座大型星艦，他化為太陽。\n殞落。\n醒來的你為他淚流滿面。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="今日行動力+1\n精神值回復至100%")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 53:
            dockclose = discord.Embed(title="功夫",description="➤你走在路上，突然被一個留著花白鬍子、一身肌肉的小老頭攔住，對方拿出好幾本書不停推銷。\n你看了看，上面寫著：千手奄拳、降奄十八掌、九奄神功、一奄指......等等。\n老頭：「少年，我看你骨骼精奇，是萬中無一的武學奇才，維護世界和平就靠你了。我這有本秘籍《如來奄掌》，見與你有緣，就十塊錢賣給你了。」\n說完硬是把秘笈塞給你，從你的口袋中搶了十塊後揚長而去。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="金錢-10\n因習得從天而降的掌法，武力⬆️ ⬆️ ⬆️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 54:
            dockclose = discord.Embed(title="時間旅人",description="➤你守護海龜寶寶奔向大海，N年後海龜為了報答你，把你帶去海底奄宮遊玩三天，當回到海面時，你發現手機顯示的年份日期有點奇怪。\n\n「明明玩了三天，怎麼反而回到海龜寶寶奔向大海的那年……？」\n\n雖然身體回到鍛鍊前狀態，但對你而言，卻是改變破產命運的機會！")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="你回到過去\n各項能力⬇️ ⬇️ \n金錢+50")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 55:
            dockclose = discord.Embed(title="好吃",description="➤你來到奄國一座繁華的大城市，散步時遇到路邊攤阿嬤的熱情招呼，源源不絕的包子、水餃不斷出現在桌上。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="你少了整整一天的假期\n體重⬆️ ⬆️ ⬆️ ⬆️ ⬆️ ")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 56:
            dockclose = discord.Embed(title="傳奇人物",description="➤你在路上遇見身穿包子圖案T恤的男子，對方笑著向你大喊：「Make 奄國 Great Again！」\n像是被他歡愉的語氣感染，你和周遭的路人也紛紛跟著大喊：「Make 奄國 Great Again！」\n還有人拿出寫著標語的七彩電子看板，撥放起電音樂曲，整條路上像是舞廳一般充滿了快活的空氣。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="＼MYGA／，精神值增加10點。")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose
        
        case 57:
            dockclose = discord.Embed(title="有福同享",description="➤中午休息時間，你到了奄茶購買飲品，剛好碰上了抽獎活動，幸運抽到買 1 送 10 ，你將額外送的 10 杯帶回工作場所與同事分享，提升了大家下午工作的能量。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="❤️ 魅力⬆️⬆️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 58:
            dockclose = discord.Embed(title="小丑狙擊手",description="➤你在執行刺殺任務，看到目標正身處於眾人之中，你可以趁此機會狙擊暗殺。\n當你站在槍口架槍，準備行動時，\n不料，一個手滑，扣下扳機，直接自狙。\n\n小丑是你，你是小丑🤡")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="各項能力大幅下降⬇️⬇️⬇️⬇️\n你的人生在此寫下了一個大大污點…… ")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose
            
        case 59:
            dockclose = discord.Embed(title="讓雞排飛",description="➤你走在路上，哼著歌，手上的塑膠袋裝著剛炸好的酥脆雞排，然後突然就被土匪給劫了雞排。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="失去雞排\n心相⬇️ ⬇️ ⬇️ ⬇️ ⬇️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose
            
        case 60:
            dockclose = discord.Embed(title="做人失敗",description="➤你是一位警長，正在會議中勸導大家找出兇殺案的兇手。\n經過了各方長期論述後得出了一個結論：先把你丟下海裡與闡國人作伴！\n只能說是你平時的誠信度不足，做人失敗...\n你還來不及逃離或是反抗就在會議後被眾人綁上石頭丟下水，成為海闡的一份子。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="你不被需要了(成為幽靈)")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 61:
            dockclose = discord.Embed(title="目光",description="➤廣場上人聲鼎沸，你走近一看原來是崑崙上師新一期國勢占卜的預告公布了。\n巨型電視牆上映著崑崙上師的正臉照，你的視線被上師的眼神吸引，那雙可以洞見一切的眼睛，彷彿深深地看進了你的心底……\n回過神來，你已經走出占卜投票所，有點不確定自己剛剛投了什麼，但心中開始期待起晚上的占卜直播。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="對崑崙上師的信仰值+100%。")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 62:
            dockclose = discord.Embed(title="三人成虎",description="➤你在圖書館找不到資料的時候側耳聽到一些院士在閒聊，他們說如果在圖書館中一直找不到的某筆資料，那一定會在西側閱覽室旁最後一排的空書架上找到，但你知道閱覽室旁並沒有空的書架。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="你離開圖書館了。\n內政⬇️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 63:
            dockclose = discord.Embed(title="三人成虎",description="➤你在圖書館找不到資料的時候側耳聽到一些院士在閒聊，他們說如果在圖書館中一直找不到的某筆資料，那一定會在西側閱覽室旁最後一排的空書架上找到，但你知道閱覽室旁並沒有空的書架。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="待他們離開之後你沿著西側走，最後一個書架今天空無一物，你要的資料在躺書架旁的地上。\n內政⬆️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 64:
            dockclose = discord.Embed(title="三人成虎",description="➤你在圖書館找不到資料的時候側耳聽到一些院士在閒聊，他們說如果在圖書館中一直找不到的某筆資料，那一定會在西側閱覽室旁最後一排的空書架上找到，但你知道閱覽室旁並沒有空的書架。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="待他們離開之後你沿著西側走，最後一個書架一如往常地放著無法外借的舊工具書。\n理智⬆️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 65:
            dockclose = discord.Embed(title="三人成虎",description="➤你在圖書館找不到資料的時候側耳聽到一些院士在閒聊，他們說如果在圖書館中一直找不到的某筆資料，那一定會在西側閱覽室旁最後一排的空書架上找到，但你知道閱覽室旁並沒有空的書架。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="待他們離開之後你沿著西側走，一回神就看見斜陽照亮了書架旁的地面，你不記得你站在這裡多久了。\n理智⬇️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 66:
            dockclose = discord.Embed(title="骰子遊戲",description="➤你與其他諸侯受邀試玩了教育部自製的教學桌上遊戲，但卻反覆抽到同一張事件卡牌，於是解說員只好暫停遊戲，將所有卡片一一展示給來賓看。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="你為了化解尷尬贊助了地方中小學每校各一套遊戲。\n金錢-10000")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 67:
            dockclose = discord.Embed(title="弱弱相殘",description="➤前陣子市場主委申訴土匪騷擾的問題，當你前去視察卻不見居民反應，你那出身市場的隨行助理建議你稍作巡查後便可離開，你不是第一個來巡察的官員。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="你不被需要了(成為幽靈)")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 68:
            dockclose = discord.Embed(title="做人失敗",description="➤你是一位警長，正在會議中勸導大家找出兇殺案的兇手。\n經過了各方長期論述後得出了一個結論：先把你丟下海裡與闡國人作伴！\n只能說是你平時的誠信度不足，做人失敗...\n你還來不及逃離或是反抗就在會議後被眾人綁上石頭丟下水，成為海闡的一份子。")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="內政⬆️")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose

        case 69:
            dockclose = discord.Embed(title="如夢令",description="➤老張和你靜坐於星空之下、篝火之畔伴隨著星火點點暢談渾元萬劫往事。忽然老張為你斟上佳釀並舉杯賦詞：\n\n\t 午月沉杯燈瘦，衣坐孤燈未透。\n\t疑是帷中議，耳底兵聲再奏。\n\n\t 已久。已久。\n\t憶裡筆落未乾。\n\n吟罷與你對杯豪飲，然而你耐不住這酒太烈，一口下去一陣天旋地轉、老張的身影便逐漸模糊，只剩詩詞隱約繚繞於腦中\n「午…衣…疑…耳…---…」")
            dockclose.add_field(name=" ",value="----------------------------------------------------",inline=False)
            dockclose.add_field(name="❖ 工作結算",value="")
            dockclose.set_image(url="attachment://51121.gif")
            dockclose.set_author(name="海港特殊事件-結算")
            return dockclose