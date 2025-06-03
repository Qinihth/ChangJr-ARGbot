import discord, random, pytz 
from discord.ext import commands
from ARG import resource_mag,load_data

def Event(workspace,event,user_id=0,amount=0,amountt=0):
    match workspace:
        case 'Field':
            match event:
                case 'event1':
                    fieldembed = discord.Embed(title="結訓演講",description="➤這日負責人請你協助安排新兵實習內容，你決定安排⋯⋯",color=discord.Color.red())
                    fieldembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    fieldembed.add_field(name="▼ 請選擇：",value="•（１）軍人應時刻保持侵略性\n•（２）軍人的職責是守衛和平",inline=False)
                    fieldembed.add_field(name="❖ 工作結算：",value="• 你前往校場進行障礙突破訓練，武力<:MNR_INC_B:1375507280711123087>。",inline=False)
                    fieldembed.set_author(name="校場特殊事件")
                    # choice1
                    fieldclose1 = discord.Embed(title="結訓演講",description="➤你強調軍隊是國家實力的基石，唯有強者才能免受威脅。你的話語振聾發聵，新兵們眼中燃起對勝利的渴望。",color=discord.Color.red())
                    fieldclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    fieldclose1.add_field(name="❖ 事件結果：",value="• 武力<:SLT_INC_B:1375507405059657778>",inline=False)
                    fieldclose1.set_author(name="校場特殊事件-結算")
                    # choice2
                    fieldclose2 = discord.Embed(title="結訓演講",description="➤你強調軍隊是守護人民的防線，唯有令百姓安居，國家才能強盛。你的話語令新兵們紛紛高呼誓死報效國家。",color=discord.Color.red())
                    fieldclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    fieldclose2.add_field(name="❖ 事件結果：",value="• 內政<:SLT_INC_B:1375507405059657778>",inline=False)
                    fieldclose2.set_author(name="校場特殊事件-結算")
                    return([fieldembed,fieldclose1,'STR',1,fieldclose2,'DOM',1])
                case 'event2':
                    fieldembed = discord.Embed(title="實習安排",description="➤這日負責人請你協助安排新兵實習內容，你決定安排⋯⋯",color=discord.Color.red())
                    fieldembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    fieldembed.add_field(name="▼ 請選擇：",value="•（１）救援行動，安排疏導民眾並搬運物資\n•（２）假想敵作戰，練習陣法替換",inline=False)
                    fieldembed.add_field(name="❖ 工作結算：",value="• 你前往校場進行障礙突破訓練，武力<:MNR_INC_B:1375507280711123087>")
                    fieldembed.set_author(name="校場特殊事件")
                    # choice1
                    fieldclose1 = discord.Embed(title="實習安排",description="➤你精通內政，下令實施市集火災演習。訓練效果卓越，此後救援行動中總少不了他們的身影。",color=discord.Color.red())
                    fieldclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    fieldclose1.add_field(name="❖ 事件結果：",value="• 內政<:SLT_INC_B:1375507405059657778>",inline=False)
                    fieldclose1.set_author(name="校場特殊事件-結算")
                    # choice2
                    fieldclose2 = discord.Embed(title="實習安排",description="➤你精通運兵與布陣，特將新兵分隊演練陣型。訓練效果卓越，士兵熟悉陣法與武器，戰力大增。",color=discord.Color.red())
                    fieldclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    fieldclose2.add_field(name="❖ 事件結果：",value="• 武力<:SLT_INC_B:1375507405059657778>",inline=False)
                    fieldclose2.set_author(name="校場特殊事件-結算")
                    return([fieldembed,fieldclose1,'DOM',1,fieldclose2,'STR',1])
                case 'event3':
                    fieldembed = discord.Embed(title="新兵訓練",description="➤本梯新兵素質優異，你將負責人對其寄予厚望。因此，希望在基礎訓練外增加額外課程，重點應放在⋯⋯",color=discord.Color.red())
                    fieldembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    fieldembed.add_field(name="▼ 請選擇：",value="•（１）提升個人戰力\n•（２）提升戰略素養",inline=False)
                    fieldembed.add_field(name="❖ 工作結算：",value="• 你前往校場進行障礙突破訓練，武力<:MNR_INC_B:1375507280711123087>",inline=False)
                    fieldembed.set_author(name="校場特殊事件")
                    # choice1
                    fieldclose1 = discord.Embed(title="新兵訓練",description="➤你認為提升個人戰力至關重要，特邀資深老將授課操練。過程中，你自己也受益良多，習得部分老將的私藏武學。",color=discord.Color.red())
                    fieldclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    fieldclose1.add_field(name="❖ 事件結果：",value="• 武力<:SLT_INC_B:1375507405059657778>",inline=False)
                    fieldclose1.set_author(name="校場特殊事件-結算")
                    # choice2
                    fieldclose2 = discord.Embed(title="新兵訓練",description="➤你重視戰略素養，邀請名師講授兵法。你在旁全程筆記，從中領悟不少兵家要義，見識亦隨之精進。",color=discord.Color.red())
                    fieldclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    fieldclose2.add_field(name="❖ 事件結果：",value="• 智力<:SLT_INC_B:1375507405059657778>",inline=False)
                    fieldclose2.set_author(name="校場特殊事件-結算")
                    return([fieldembed,fieldclose1,'STR',1,fieldclose2,'INT',1])
                case 'event4':
                    fieldembed = discord.Embed(title="破格提拔",description="➤新兵即將結訓，明日正式編入軍隊。你作為訓練官，決定破格提拔一人為儲備將領，因為他⋯⋯",color=discord.Color.red())
                    fieldembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    fieldembed.add_field(name="▼ 請選擇：",value="•（１）奮勇當先、體恤他人\n•（２）有智謀、能精準分析情勢",inline=False)
                    fieldembed.add_field(name="❖ 工作結算：",value="• 你前往校場進行障礙突破訓練，武力<:MNR_INC_B:1375507280711123087>",inline=False)
                    fieldembed.set_author(name="校場特殊事件")
                    # choice1
                    fieldclose1 = discord.Embed(title="破格提拔",description="➤你慧眼識才，選中的將領年紀輕輕就執掌兵符，卻屢建奇功。然而他功高震主，最終屢遭猜忌，蒙受不白之冤。",color=discord.Color.red())
                    fieldclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    fieldclose1.add_field(name="❖ 事件結果：",value="• 魅力<:SLT_INC_B:1375507405059657778>",inline=False)
                    fieldclose1.set_author(name="校場特殊事件-結算")
                    # choice2
                    fieldclose2 = discord.Embed(title="破格提拔",description="➤你慧眼識才，此人成長為一代軍師，多次逆轉劣勢，然而，他冷血無情的作風亦令士兵心生忌憚。",color=discord.Color.red())
                    fieldclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    fieldclose2.add_field(name="❖ 事件結果：",value="• 智力<:SLT_INC_B:1375507405059657778>",inline=False)
                    fieldclose2.set_author(name="校場特殊事件-結算")
                    return([fieldembed,fieldclose1,'CHR',1,fieldclose2,'INT',1])
                case 'event5':
                    fieldembed = discord.Embed(title="特訓單位",description="➤今晨，你巡視軍校，聽聞負責人提議設立「猛虎班」─專為體能與武藝出眾的新兵打造的特訓單位，臨行前，你決定先處理的是⋯⋯",color=discord.Color.red())
                    fieldembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    fieldembed.add_field(name="▼ 請選擇：",value="•（１）參與測驗設計,確保訓練課程實戰有效\n•（２）潛入初選現場,親自挑選合格人選",inline=False)
                    fieldembed.add_field(name="❖ 工作結算：",value="• 你前往校場進行障礙突破訓練，武力<:MNR_INC_B:1375507280711123087>",inline=False)
                    fieldembed.set_author(name="校場特殊事件")
                    # choice1
                    fieldclose1 = discord.Embed(title="特訓單位",description="➤你親手設計出一套近身格鬥測驗，並自告奮勇參與首日試煉。連日實戰打磨，你不僅確保訓練標準，也意外讓肌肉記憶與反應大幅進化。",color=discord.Color.red())
                    fieldclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    fieldclose1.add_field(name="❖ 事件結果：",value="• 武力<:SLT_INC_B:1375507405059657778>",inline=False)
                    fieldclose1.set_author(name="校場特殊事件-結算")
                    # choice2
                    fieldclose2 = discord.Embed(title="特訓單位",description="➤你喬裝身份潛入現場，實地觀察每位候選人應對訓練的表現。為了測試其中一名新兵的反應，你還與之過招數輪，意外激發鬥志，雙雙揮汗對練，讓你技藝更精。",color=discord.Color.red())
                    fieldclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    fieldclose2.add_field(name="❖ 事件結果：",value="• 武力<:SLT_INC_B:1375507405059657778>",inline=False)
                    fieldclose2.set_author(name="校場特殊事件-結算")
                    return([fieldembed,fieldclose1,'STR',1,fieldclose2,'STR',1])
        case 'College':
            match event:
                case 'event1':
                    collegeembed = discord.Embed(title="招生制度",description="➤太學進行了擴建，負責人向你請益招生制度是否要更動。對此你決定⋯⋯",color=discord.Color.gold())
                    collegeembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    collegeembed.add_field(name="▼ 請選擇：",value="•（１）迴護利益集團，維持士族教育\n•（２）倡導平等，鼓勵平民受教育",inline=False)
                    collegeembed.add_field(name="❖ 工作結算：",value="• 你前往太學閱讀名家經典，內政<:MNR_INC_B:1375507280711123087>。",inline=False)
                    collegeembed.set_author(name="太學特殊事件")
                    # choice1
                    collegeclose1 = discord.Embed(title="招生制度",description="➤士族壟斷教育與統治維持了階級穩定，促進商業繁榮。然而，階級間不平等待遇引發平民不滿，加劇對立，埋下隱患。",color=discord.Color.gold())
                    collegeclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    collegeclose1.add_field(name="❖ 事件結果：",value="• 內政<:SLT_INC_B:1375507405059657778>",inline=False)
                    collegeclose1.set_author(name="太學特殊事件-結算")
                    # choice2
                    collegeclose2 = discord.Embed(title="招生制度",description="➤此決定提升你的支持度，階級流動增加，不平等逐漸消弭。然而，生員過多超出政府承載力，反觀農工產業後繼無人，出現斷層危機。",color=discord.Color.gold())
                    collegeclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    collegeclose2.add_field(name="❖ 事件結果：",value="• 魅力<:SLT_INC_B:1375507405059657778>",inline=False)
                    collegeclose2.set_author(name="太學特殊事件-結算")
                    return([collegeembed,collegeclose1,'DOM',1,collegeclose2,'CHR',1])
                case 'event2':
                    collegeembed = discord.Embed(title="官員選拔",description="➤經多場討論，終於確立官員選拔制度。說明會上有應屆畢業生詢問官員提拔標準，你沉思片刻後作出回答⋯⋯",color=discord.Color.gold())
                    collegeembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    collegembed.add_field(name="▼ 請選擇：",value="•（１）富有領袖魅力，大肚能容者\n•（２）品德高尚、政治素養佳者",inline=False)
                    collegeembed.add_field(name="❖ 工作結算：",value="• 你前往太學閱讀名家經典，內政<:MNR_INC_B:1375507280711123087>")
                    collegeembed.set_author(name="太學特殊事件")
                    # choice1
                    collegeclose1 = discord.Embed(title="官員選拔",description="➤你認為官員最重要的是領袖魅力、號召力與寬容的心。此後選考機構也以此為重要條件來評斷應試者。",color=discord.Color.gold())
                    collegeclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    collegeclose1.add_field(name="❖ 事件結果：",value="• 魅力<:SLT_INC_B:1375507405059657778>",inline=False)
                    collegeclose1.set_author(name="太學特殊事件-結算")
                    # choice2
                    collegeclose2 = discord.Embed(title="官員選拔",description="➤你認為官員最重要的是品德與修養，此外政治素養與溝通力亦不可或缺。此後選考機構也以此為重要條件來評斷應試者。",color=discord.Color.gold())
                    collegeclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    collegeclose2.add_field(name="❖ 事件結果：",value="• 內政<:SLT_INC_B:1375507405059657778>",inline=False)
                    collegeclose2.set_author(name="太學特殊事件-結算")
                    return([collegeembed,collegeclose1,'CHR',1,collegeclose2,'DOM',1])
                case 'event3':
                    collegeembed = discord.Embed(title="示威抗議",description="➤近期的決策使太學生們發起示威抗議，甚至造成多起違法事件。衛隊奉命前來解散集會，身為執政官的你決定⋯⋯",color=discord.Color.gold())
                    collegeembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    collegeembed.add_field(name="▼ 請選擇：",value="•（１）阻止衛隊，希望和平解決\n•（２）違法行為不可取，允許行動並批准鎮壓反抗者",inline=False)
                    collegeembed.add_field(name="❖ 工作結算：",value="• 你前往太學閱讀名家經典，內政<:MNR_INC_B:1375507280711123087>",inline=False)
                    collegeembed.set_author(name="太學特殊事件")
                    # choice1
                    collegeclose1 = discord.Embed(title="示威抗議",description="➤你驅離衛隊，選擇和平解決問題。你以禮相待，然而，此舉引發多場罷工與不合作運動，導致國家部分機能停擺。",color=discord.Color.gold())
                    collegeclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    collegeclose1.add_field(name="❖ 事件結果：",value="• 內政<:SLT_INC_B:1375507405059657778>",inline=False)
                    collegeclose1.set_author(name="太學特殊事件-結算")
                    # choice2
                    collegeclose2 = discord.Embed(title="示威抗議",description="➤違法行為不可取，允許行動並批准鎮壓反抗者。",color=discord.Color.gold())
                    collegeclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    collegeclose2.add_field(name="❖ 事件結果：",value="• 武力<:SLT_INC_B:1375507405059657778>",inline=False)
                    collegeclose2.set_author(name="太學特殊事件-結算")
                    return([collegeembed,collegeclose1,'DOM',1,collegeclose2,'STR',1])                    
                case 'event4':
                    collegeembed = discord.Embed(title="課程內容",description="➤太學負責人向你請益課程內容是否要更新，你認為必須要加強⋯⋯",color=discord.Color.gold())
                    collegeembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    collegeembed.add_field(name="▼ 請選擇：",value="•（１）國際情勢與軍事相關課程\n•（２）科學相關課程",inline=False)
                    collegeembed.add_field(name="❖ 工作結算：",value="• 你前往太學閱讀名家經典，內政<:MNR_INC_B:1375507280711123087>",inline=False)
                    collegeembed.set_author(name="太學特殊事件")
                    # choice1
                    collegeclose1 = discord.Embed(title="課程內容",description="➤你認為了解國際情勢與軍事知識更為重要，讓學生更加了解國家現狀，為培養國家的外交與軍事人才埋下良好基礎。",color=discord.Color.gold())
                    collegeclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    collegeclose1.add_field(name="❖ 事件結果：",value="• 武力<:SLT_INC_B:1375507405059657778>",inline=False)
                    collegeclose1.set_author(name="太學特殊事件-結算")
                    # choice2
                    collegeclose2 = discord.Embed(title="課程內容",description="➤你認為通曉科學知識更為重要，為學生進入研究機構打下了堅實的基礎。國內的科技研發隨之突飛猛進，短短幾年就取得多項專利。",color=discord.Color.gold())
                    collegeclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    collegeclose2.add_field(name="❖ 事件結果：",value="• 智力<:SLT_INC_B:1375507405059657778>",inline=False)
                    collegeclose2.set_author(name="太學特殊事件-結算")
                    return([collegeembed,collegeclose1,'STR',1,collegeclose2,'INT',1])                   
                case 'event5':
                    collegeembed = discord.Embed(title="改革提案",description="➤許多學子反應太學氛圍過於守舊，你決定引進國外教材並聘請知名講師執教。此外，你提議⋯⋯",color=discord.Color.gold())
                    collegeembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    collegeembed.add_field(name="▼ 請選擇：",value="•（１）與外國進行文化交流\n•（２）進行制度面的改革",inline=False)
                    collegeembed.add_field(name="❖ 工作結算：",value="• 你前往太學閱讀名家經典，內政<:MNR_INC_B:1375507280711123087>",inline=False)
                    collegeembed.set_author(name="太學特殊事件")
                    # choice1
                    collegeclose1 = discord.Embed(title="改革提案",description="➤因缺乏升學與工商業支持，新教材與教育系統成效不彰。然而，此舉促進外國新思潮交流，並催生國內嶄新思維。",color=discord.Color.gold())
                    collegeclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    collegeclose1.add_field(name="❖ 事件結果：",value="• 內政<:SLT_INC_B:1375507405059657778>",inline=False)
                    collegeclose1.set_author(name="太學特殊事件-結算")
                    # choice2
                    collegeclose2 = discord.Embed(title="改革提案",description="➤你組織團隊考究並引進新制度，新舊思想碰撞孕育璀璨文化。這批學子進入社會後，推動新制度與技術，讓國家躋身一線強國。",color=discord.Color.gold())
                    collegeclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    collegeclose2.add_field(name="❖ 事件結果：",value="• 內政<:SLT_INC_B:1375507405059657778>",inline=False)
                    collegeclose2.set_author(name="太學特殊事件-結算")
                    return([collegeembed,collegeclose1,'DOM',1,collegeclose2,'DOM',1])
        case 'Sciences':
            match event:
                case 'event1':
                    sciencesembed = discord.Embed(title="資源分配",description="➤中央撥了一筆經費給科學院，負責人請示你應該如何處理，你決定⋯⋯",color=discord.Color.green())
                    sciencesembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    sciencesembed.add_field(name="▼ 請選擇：",value="•（１）審慎評估，將資源挹注於更有前瞻性的項目\n•（２）力排眾議，分配給起步較晚的國防相關項目",inline=False)
                    sciencesembed.add_field(name="❖ 工作結算：",value="• 你前往科學院完成實驗紀錄，智力<:MNR_INC_B:1375507280711123087>。",inline=False)
                    sciencesembed.set_author(name="科學院特殊事件")
                    # choice1
                    sciencesclose1 = discord.Embed(title="資源分配",description="➤你深入了解多項研究後，將資源集中於關鍵技術突破。研究團隊快速取得進展，你也因此熟稔相關理論與評估流程。",color=discord.Color.green())
                    sciencesclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    sciencesclose1.add_field(name="❖ 事件結果：",value="• 智力<:SLT_INC_B:1375507405059657778>",inline=False)
                    sciencesclose1.set_author(name="科學院特殊事件-結算")
                    # choice2
                    sciencesclose2 = discord.Embed(title="資源分配",description="➤你堅持將資金投入軍事技術。在密集討論與驗證過程中，你對現代武器結構與應用理解更深。",color=discord.Color.green())
                    sciencesclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    sciencesclose2.add_field(name="❖ 事件結果：",value="• 武力<:SLT_INC_B:1375507405059657778>",inline=False)
                    sciencesclose2.set_author(name="科學院特殊事件-結算")
                    return([sciencesembed,sciencesclose1,'INT',1,sciencesclose2,'STR',1])
                case 'event2':
                    sciencesembed = discord.Embed(title="首席研究員",description="➤科學院的首席研究員突然退休，留下滿桌未完成的案子。你受命處理後續人選，思考許久後，決定任命⋯⋯",color=discord.Color.green())
                    sciencesembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    sciencesmbed.add_field(name="▼ 請選擇：",value="•（１）會與機械對話的怪人博士\n•（２）退役的狂人教授",inline=False)
                    sciencesembed.add_field(name="❖ 工作結算：",value="• 你前往科學院完成實驗紀錄，智力<:MNR_INC_B:1375507280711123087>")
                    sciencesembed.set_author(name="科學院特殊事件")
                    # choice1
                    sciencesclose1 = discord.Embed(title="首席研究員",description="➤你任命那位總像從垃圾堆爬出來的怪人博士接手研究。在他的指導下，你漸漸掌握機械回饋與演算邏輯，對工程原理領悟大增。",color=discord.Color.green())
                    sciencesclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    sciencesclose1.add_field(name="❖ 事件結果：",value="• 智力<:SLT_INC_B:1375507405059657778>",inline=False)
                    sciencesclose1.set_author(name="科學院特殊事件-結算")
                    # choice2
                    sciencesclose2 = discord.Embed(title="首席研究員",description="➤你任命那位因熱愛炸藥而退役的火藥狂人回鍋授課，他帶你實測新配方，多次爆炸後，你也學會了控制引爆的技巧。",color=discord.Color.green())
                    sciencesclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    sciencesclose2.add_field(name="❖ 事件結果：",value="• 武力<:SLT_INC_B:1375507405059657778>",inline=False)
                    sciencesclose2.set_author(name="科學院特殊事件-結算")
                    return([sciencesembed,sciencesclose1,'INT',1,sciencesclose2,'STR',1])
                case 'event3':
                    sciencesembed = discord.Embed(title="人才招募",description="➤科學院近期有招募人才的計畫，負責人請示你的想法，對此你覺得⋯⋯",color=discord.Color.green())
                    sciencesembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    sciencesembed.add_field(name="▼ 請選擇：",value="•（１）主動出擊，至各大院所徵才，並祭出優渥條件\n•（２）優質環境才是長久之道，發展好人才自然會來",inline=False)
                    sciencesembed.add_field(name="❖ 工作結算：",value="• 你前往科學院完成實驗紀錄，智力<:MNR_INC_B:1375507280711123087>",inline=False)
                    sciencesembed.set_author(name="科學院特殊事件")
                    # choice1
                    sciencesclose1 = discord.Embed(title="人才招募",description="➤你求才若渴，親自帶項目負責人前往各大院所徵才。與學生暢談科學理想，令他們嚮往不已，再加上優渥條件，成功吸引一批優秀人才。",color=discord.Color.green())
                    sciencesclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    sciencesclose1.add_field(name="❖ 事件結果：",value="• 魅力<:SLT_INC_B:1375507405059657778>",inline=False)
                    sciencesclose1.set_author(name="科學院特殊事件-結算")
                    # choice2
                    sciencesclose2 = discord.Embed(title="人才招募",description="➤你深諳良禽擇木而棲之理，不急於招募，而是穩紮穩打推動計畫，營造優良學術環境。數年後，果然吸引越來越多青年才俊加入。",color=discord.Color.green())
                    sciencesclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    sciencesclose2.add_field(name="❖ 事件結果：",value="• 智力<:SLT_INC_B:1375507405059657778>",inline=False)
                    sciencesclose2.set_author(name="科學院特殊事件-結算")
                    return([sciencesembed,sciencesclose1,'CHR',1,sciencesclose2,'INT',1])                    
                case 'event4':
                    sciencesembed = discord.Embed(title="仲裁紛爭",description="➤你前往科學院參訪，正好撞見兩位學者在爭吵，他們要求路過的你決斷誰的觀點才是正確的。對於這場爭執你決定⋯⋯",color=discord.Color.green())
                    sciencesembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    sciencesembed.add_field(name="▼ 請選擇：",value="•（１）鼓勵開放自由的學術辯論，不發表意見\n•（２）協助仲裁，阻止衝突、讓溝通更順暢",inline=False)
                    sciencesembed.add_field(name="❖ 工作結算：",value="• 你前往科學院完成實驗紀錄，智力<:MNR_INC_B:1375507280711123087>",inline=False)
                    sciencesembed.set_author(name="科學院特殊事件")
                    # choice1
                    sciencesclose1 = discord.Embed(title="仲裁紛爭",description="➤你認為這是正常的學術交流，選擇不發表意見。經過數小時辯論，兩位學者達成共識。科學院在這種風氣下持續發展，在國際間傳為美談。",color=discord.Color.green())
                    sciencesclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    sciencesclose1.add_field(name="❖ 事件結果：",value="• 魅力<:SLT_INC_B:1375507405059657778>",inline=False)
                    sciencesclose1.set_author(name="科學院特殊事件-結算")
                    # choice2
                    sciencesclose2 = discord.Embed(title="仲裁紛爭",description="➤為促進溝通，你依見解裁斷。此後，科學院轉向由政府主導，專注國家所需技術研究。雖然限制學術探索的可能性，但許多研究迅速取得豐碩成果。",color=discord.Color.green())
                    sciencesclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    sciencesclose2.add_field(name="❖ 事件結果：",value="• 內政<:SLT_INC_B:1375507405059657778>",inline=False)
                    sciencesclose2.set_author(name="科學院特殊事件-結算")
                    return([sciencesembed,sciencesclose1,'CHR',1,sciencesclose2,'DOM',1])                  
                case 'event5':
                    sciencesembed = discord.Embed(title="革新技術",description="➤一位年輕學者來訪，簡報革新技術。你聽後欣喜，願意出資協助。新研究室落成當日，你私下叮囑他⋯⋯",color=discord.Color.green())
                    sciencesembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    sciencesembed.add_field(name="▼ 請選擇：",value="•（１）按部就班、穩扎穩打\n•（２）力求盡快有所成果",inline=False)
                    sciencesembed.add_field(name="❖ 工作結算：",value="• 你前往科學院完成實驗紀錄，智力<:MNR_INC_B:1375507280711123087>",inline=False)
                    sciencesembed.set_author(name="科學院特殊事件")
                    # choice1
                    sciencesclose1 = discord.Embed(title="革新技術",description="➤在你與政府積極支持下，研發順利展開。學者沉穩務實，數月內即見成效，並成功進入實用階段。你也在過程中多次參與討論，深化了對科技的理解。",color=discord.Color.green())
                    sciencesclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    sciencesclose1.add_field(name="❖ 事件結果：",value="• 智力<:SLT_INC_B:1375507405059657778>",inline=False)
                    sciencesclose1.set_author(name="科學院特殊事件-結算")
                    # choice2
                    sciencesclose2 = discord.Embed(title="革新技術",description="➤在你與政府支持下，研發迅速展開，卻因操之過急最終失敗。儘管如此，你參與多次驗證與評估，仍大有收穫。",color=discord.Color.green())
                    sciencesclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    sciencesclose2.add_field(name="❖ 事件結果：",value="• 智力<:SLT_INC_B:1375507405059657778>",inline=False)
                    sciencesclose2.set_author(name="科學院特殊事件-結算")
                    return([sciencesembed,sciencesclose1,'INT',1,sciencesclose2,'INT',1])
        case 'Balladss':
            match event:
                case 'event1':
                    balladssembed = discord.Embed(title="蒐集民謠",description="➤這日你奉命前往一處小鎮，蒐集當地的民謠。你決定先去⋯⋯",color=discord.Color.purple())
                    balladssembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    balladssembed.add_field(name="▼ 請選擇：",value="•（１）與當地民眾攀談，力求保留原始民歌魅力\n•（２）去茶樓、梨園問問，節省時間以進行細部考察",inline=False)
                    balladssembed.add_field(name="❖ 工作結算：",value="• 你前往樂府抄錄古典詩集，魅力<:MNR_INC_B:1375507280711123087>。",inline=False)
                    balladssembed.set_author(name="樂府特殊事件")
                    # choice1
                    balladssclose1 = discord.Embed(title="蒐集民謠",description="➤你與當地民眾攀談，在你的引導下，他們分享故事，各年齡層齊唱民謠。這些歌詞淺白、旋律簡單，最貼近民眾生活。",color=discord.Color.purple())
                    balladssclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    balladssclose1.add_field(name="❖ 事件結果：",value="• 魅力<:SLT_INC_B:1375507405059657778>",inline=False)
                    balladssclose1.set_author(name="樂府特殊事件-結算")
                    # choice2
                    balladssclose2 = discord.Embed(title="蒐集民謠",description="➤你徑直前往茶樓與梨園詢問，省去了不少時間。在當地表演者幫助下，你成功學會並謄錄多首民謠，其優美的旋律與詞句仍讓你沈醉不已。",color=discord.Color.purple())
                    balladssclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    balladssclose2.add_field(name="❖ 事件結果：",value="• 智力<:SLT_INC_B:1375507405059657778>",inline=False)
                    balladssclose2.set_author(name="樂府特殊事件-結算")
                    return([balladssembed,balladssclose1,'CHR',1,balladssclose2,'INT',1])
                case 'event2':
                    balladssembed = discord.Embed(title="爭取預算",description="➤政府近期打算削減預算，樂府首當其衝，獲得金援減少許多。為此你代表樂府去與官員協商，你決定⋯⋯",color=discord.Color.purple())
                    balladssembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    balladssmbed.add_field(name="▼ 請選擇：",value="•（１）動之以情\n•（２）曉之以理",inline=False)
                    balladssembed.add_field(name="❖ 工作結算：",value="• 你前往樂府抄錄古典詩集，魅力<:MNR_INC_B:1375507280711123087>")
                    balladssembed.set_author(name="樂府特殊事件")
                    # choice1
                    balladssclose1 = discord.Embed(title="爭取預算",description="➤你決定動之以情，親自拜訪官員，邀請他攜家帶眷觀賞演出。官員一家如期赴約，事後，他親自來訪致謝，更帶來政府撤銷削減預算的好消息。",color=discord.Color.purple())
                    balladssclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    balladssclose1.add_field(name="❖ 事件結果：",value="• 魅力<:SLT_INC_B:1375507405059657778>",inline=False)
                    balladssclose1.set_author(name="樂府特殊事件-結算")
                    # choice2
                    balladssclose2 = discord.Embed(title="爭取預算",description="➤你決定曉之以理，親自拜訪官員，詳細列舉樂府職責，並分析近年支出與活動成效，讓官員理解樂府的重要性，最終成功說服他取消削減預算。",color=discord.Color.purple())
                    balladssclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    balladssclose2.add_field(name="❖ 事件結果：",value="• 智力<:SLT_INC_B:1375507405059657778>",inline=False)
                    balladssclose2.set_author(name="樂府特殊事件-結算")
                    return([balladssembed,balladssclose1,'CHR',1,balladssclose2,'INT',1])
                case 'event3':
                    balladssembed = discord.Embed(title="編纂成冊",description="➤你正協助整理從各地蒐集而來的民謠與詩歌並編纂成冊。編纂過程中，你對其中一類作品產生了濃厚興趣，那就是⋯⋯",color=discord.Color.purple())
                    balladssembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    balladssembed.add_field(name="▼ 請選擇：",value="•（１）講述民間生活百態的民謠\n•（２）描述鄉愁深閨、游子他鄉的詩歌",inline=False)
                    balladssembed.add_field(name="❖ 工作結算：",value="• 你前往樂府抄錄古典詩集，魅力<:MNR_INC_B:1375507280711123087>",inline=False)
                    balladssembed.set_author(name="樂府特殊事件")
                    # choice1
                    balladssclose1 = discord.Embed(title="編纂成冊",description="➤你深入分析這些貼近生活的歌謠，不僅編排曲目，更主動走訪市集與村落，對照歌詞與實況，建立起一套觀察民情的筆記系統。這份洞察力讓你對庶務經營與社會運作有了全新理解。",color=discord.Color.purple())
                    balladssclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    balladssclose1.add_field(name="❖ 事件結果：",value="• 內政<:SLT_INC_B:1375507405059657778>",inline=False)
                    balladssclose1.set_author(name="樂府特殊事件-結算")
                    # choice2
                    balladssclose2 = discord.Embed(title="編纂成冊",description="➤你沉浸於詩歌的情感結構與語言節奏，甚至試圖用自己的方式演繹與改寫。你開始模仿不同時代詩人的筆法與修辭技巧，逐漸提升了自己在人際互動與情感表達上的掌握力。",color=discord.Color.purple())
                    balladssclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    balladssclose2.add_field(name="❖ 事件結果：",value="• 魅力<:SLT_INC_B:1375507405059657778>",inline=False)
                    balladssclose2.set_author(name="樂府特殊事件-結算")
                    return([balladssembed,balladssclose1,'DOM',1,balladssclose2,'CHR',1])                   
                case 'event4':
                    balladssembed = discord.Embed(title="演出決策",description="➤樂府受多方邀約演出，負責人以檔期已滿推辭，但兩機構盛情難卻。負責人為難，向你出面協助，你決定去⋯⋯",color=discord.Color.purple())
                    balladssembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    balladssembed.add_field(name="▼ 請選擇：",value="•（１）軍營勞軍\n•（２）官府宴會",inline=False)
                    balladssembed.add_field(name="❖ 工作結算：",value="• 你前往樂府抄錄古典詩集，魅力<:MNR_INC_B:1375507280711123087>",inline=False)
                    balladssembed.set_author(name="樂府特殊事件")
                    # choice1
                    balladssclose1 = discord.Embed(title="演出決策",description="➤你決定親赴軍營勞軍。為激勵士氣，你親自登台舞劍，動作俐落，劍光如虹。老將們頻頻點頭，你也從排練中獲得不少啟發，武藝大有精進。",color=discord.Color.purple())
                    balladssclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    balladssclose1.add_field(name="❖ 事件結果：",value="• 武力<:SLT_INC_B:1375507405059657778>",inline=False)
                    balladssclose1.set_author(name="樂府特殊事件-結算")
                    # choice2
                    balladssclose2 = discord.Embed(title="演出決策",description="➤你決定前往官府獻藝，特選名家劇本並邀資深演員登台，你也親自參與演出籌備與接待事宜。過程中與多位官員深談，獲益良多，對治理知道有更深體悟。",color=discord.Color.purple())
                    balladssclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    balladssclose2.add_field(name="❖ 事件結果：",value="• 內政<:SLT_INC_B:1375507405059657778>",inline=False)
                    balladssclose2.set_author(name="樂府特殊事件-結算")
                    return([balladssembed,balladssclose1,'STR',1,balladssclose2,'DOM',1])                  
                case 'event5':
                    balladssembed = discord.Embed(title="樂府新星",description="➤樂府收留孤兒，盼培養為演出生力軍。對於這些孩子，你視為樂府未來，細心培養，盼給與安穩生活與光明前途⋯⋯",color=discord.Color.purple())
                    balladssembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    balladssembed.add_field(name="▼ 請選擇：",value="•（１）讓他們多加參與演出相關課程，以求早日成為樂府的生力軍\n•（２）環境的耳濡目染才是最好的老師，同時放任他們自由發展",inline=False)
                    balladssembed.add_field(name="❖ 工作結算：",value="• 你前往樂府抄錄古典詩集，魅力<:MNR_INC_B:1375507280711123087>",inline=False)
                    balladssembed.set_author(name="樂府特殊事件")
                    # choice1
                    balladssclose1 = discord.Embed(title="樂府新星",description="➤你傾力培養孩子成藝人，卻發現他們更熱衷於買賣與手工藝。長大後，他們多成為匠人與商販，但感念樂府與你的恩情，經常觀賞演出，並送來物資或協助場地修建。",color=discord.Color.purple())
                    balladssclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    balladssclose1.add_field(name="❖ 事件結果：",value="• 魅力<:SLT_INC_B:1375507405059657778>",inline=False)
                    balladssclose1.set_author(name="樂府特殊事件-結算")
                    # choice2
                    balladssclose2 = discord.Embed(title="樂府新星",description="➤在你悉心培養下，孩子們展現驚人天賦。學藝之餘，他們協助後台，並受樂府藝人傾囊相授。數年後，他們初登舞台即嶄露鋒芒，名揚海外。",color=discord.Color.purple())
                    balladssclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    balladssclose2.add_field(name="❖ 事件結果：",value="• 魅力<:SLT_INC_B:1375507405059657778>",inline=False)
                    balladssclose2.set_author(name="樂府特殊事件-結算")
                    return([balladssembed,balladssclose1,'CHR',1,balladssclose2,'CHR',1])
        case 'Military':
            match event:
                case 'event1':
                    militaryembed = discord.Embed(title="研發選擇",description="➤軍方希望研發一種複雜的新防禦工事，你建議⋯⋯",color=discord.Color.red())
                    militaryembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    militaryembed.add_field(name="▼ 請選擇：",value="•（１）親自協調本地廠商，深入參與研發流程\n•（２）主導國際合作計畫，擔任技術協調窗口",inline=False)
                    militaryembed.add_field(name="❖ 工作結算：",value=f"• 你前往兵營進行補給物資訓練，武力<:SLT_INC_B:1375507405059657778>，且軍事<:INC:1375507210448277595>{amount}。",inline=False)
                    militaryembed.set_author(name="兵營特殊事件")
                    # choice1
                    militaryclose1 = discord.Embed(title="研發選擇",description="➤你選擇全程參與國內研發，從材料選擇到測試設計皆親力親為。過程中，你深入理解軍備構造與部署邏輯，實戰規劃能力大幅提升。",color=discord.Color.red())
                    militaryclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    militaryclose1.add_field(name="❖ 事件結果：",value=f"• 武力<:SLT_INC_B:1375507405059657778>",inline=False)
                    militaryclose1.set_author(name="兵營特殊事件-結算")
                    # choice2
                    militaryclose2 = discord.Embed(title="研發選擇",description="➤你發揮語言與判斷能力，成功整合外部資源，協助軍方導入先進技術。長時間參與技術討論與設計調整，使你與軍工科技與系統規劃有了嶄新理解。",color=discord.Color.red())
                    militaryclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    militaryclose2.add_field(name="❖ 事件結果：",value=f"• 智力<:SLT_INC_B:1375507405059657778>",inline=False)
                    militaryclose2.set_author(name="兵營特殊事件-結算")
                    return([militaryembed,militaryclose1,'STR',1,militaryclose2,'INT',1])
                case 'event2':
                    militaryembed = discord.Embed(title="軍隊擴編",description="➤政府近期打算削減預算，兵營首當其衝，獲得金援減少許多。為此你代表兵營去與官員協商，你決定⋯⋯",color=discord.Color.red())
                    militaryembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    militarymbed.add_field(name="▼ 請選擇：",value="•（１）強制徵招\n•（２）提升軍人福利與待遇再次招募",inline=False)
                    militaryembed.add_field(name="❖ 工作結算：",value=f"• 你前往兵營進行補給物資訓練，武力<:SLT_INC_B:1375507405059657778>，且軍事<:INC:1375507210448277595>{amount}。",inline=False)
                    militaryembed.set_author(name="兵營特殊事件")
                    # choice1
                    amount_c1 = resource_mag(user_id,'INT') * random.randint(6,8)
                    militaryclose1 = discord.Embed(title="軍隊擴編",description="➤強制徵招引發反戰思潮，民眾與學子上街示威。在強大壓力下，上級最終宣布撤銷擴編計畫，轉而資金注入科技產業。",color=discord.Color.red())
                    militaryclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    militaryclose1.add_field(name="❖ 事件結果：",value=f"• 科技<:INC:1375507210448277595>{amount_c1}",inline=False)
                    militaryclose1.set_author(name="兵營特殊事件-結算")
                    # choice2
                    amount_c2 = resource_mag(user_id,'STR') * random.randint(5,14)
                    militaryclose2 = discord.Embed(title="軍隊擴編",description="➤優渥福利與待遇吸引一批有志青年從軍，其中不乏專業人才。他們迅速嶄露頭角，並以奉獻精神贏得人民愛戴。",color=discord.Color.red())
                    militaryclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    militaryclose2.add_field(name="❖ 事件結果：",value=f"• 軍事<:INC:1375507210448277595>{amount_c2}",inline=False)
                    militaryclose2.set_author(name="兵營特殊事件-結算")
                    return([militaryembed,militaryclose1,'TEC_rs',amount_c1,militaryclose2,'MIL_rs',amount_c2])
                case 'event3':
                    militaryembed = discord.Embed(title="新兵報到",description="➤今天是兵營新兵報到的日子，這批新兵個個散漫的樣子被巡視的你和衛隊隊長看在眼裡。對此你決定⋯⋯",color=discord.Color.red())
                    militaryembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    militaryembed.add_field(name="▼ 請選擇：",value="•（１）教訓他們，樹立軍威\n•（２）以關懷代替訓斥，讓他們產生歸屬與責任感",inline=False)
                    militaryembed.add_field(name="❖ 工作結算：",value=f"• 你前往兵營進行補給物資訓練，武力<:SLT_INC_B:1375507405059657778>，且軍事<:INC:1375507210448277595>{amount}。",inline=False)
                    militaryembed.set_author(name="兵營特殊事件")
                    # choice1
                    amount_c1 = resource_mag(user_id,'STR') * random.randint(6,8)
                    militaryclose1 = discord.Embed(title="新兵報到",description="➤你大聲斥責令新兵嚇破了膽，不敢造次。你的鐵血作風為大眾所知，兵營在你的領導下，始終維持嚴明紀律。",color=discord.Color.red())
                    militaryclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    militaryclose1.add_field(name="❖ 事件結果：",value=f"• 軍事<:INC:1375507210448277595>{amount_c1}",inline=False)
                    militaryclose1.set_author(name="兵營特殊事件-結算")
                    # choice2
                    amount_c2 = resource_mag(user_id,'CHR') * random.randint(5,8)
                    militaryclose2 = discord.Embed(title="新兵報到",description="➤衛隊隊長正欲發作卻被你制止。你以誠懇之語與眾人對談，令在場之人深受感動。你溫和的作風廣為人知，在堅守規範的同時，亦從不忽視人性的溫度。",color=discord.Color.red())
                    militaryclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    militaryclose2.add_field(name="❖ 事件結果：",value=f"• 文化<:INC:1375507210448277595>{amount_c2}",inline=False)
                    militaryclose2.set_author(name="兵營特殊事件-結算")
                    return([militaryembed,militaryclose1,'MIL_rs',amount_c1,militaryclose2,'CUL_rs',amount_c2])                   
                case 'event4':
                    militaryembed = discord.Embed(title="救援任務",description="➤兵營接獲兩起緊急事件，衛隊隊長迅速分派任務展開救援，隨後請示你的指示。你權衡情勢後，決定先前往⋯⋯",color=discord.Color.red())
                    militaryembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    militaryembed.add_field(name="▼ 請選擇：",value="•（１）勸降挾持全住宅區居民為人質的炸彈犯\n•（２）協助撲滅市集大火",inline=False)
                    militaryembed.add_field(name="❖ 工作結算：",value=f"• 你前往兵營進行補給物資訓練，武力<:SLT_INC_B:1375507405059657778>，且軍事<:INC:1375507210448277595>{amount}。",inline=False)
                    militaryembed.set_author(name="兵營特殊事件")
                    # choice1
                    militaryclose1 = discord.Embed(title="救援任務",description="➤你與隊長感到，展現善意與之對話，經你勸導後廢人痛哭懺悔，終於放下引爆裝置。居民紛紛表達感謝，盛讚你的無邊魅力。",color=discord.Color.red())
                    militaryclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    militaryclose1.add_field(name="❖ 事件結果：",value=f"• 魅力<:SLT_INC_B:1375507405059657778>",inline=False)
                    militaryclose1.set_author(name="兵營特殊事件-結算")
                    # choice2
                    militaryclose2 = discord.Embed(title="救援任務",description="➤雖然商鋪被燒毀，但人員多數平安，民眾感念衛隊救援。政府隨後撥款重建市集，並重新規劃動線與擴建。最終，新市集比過往更加繁榮。",color=discord.Color.red())
                    militaryclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    militaryclose2.add_field(name="❖ 事件結果：",value=f"• 內政<:SLT_INC_B:1375507405059657778>",inline=False)
                    militaryclose2.set_author(name="兵營特殊事件-結算")
                    return([militaryembed,militaryclose1,'CHR',1,militaryclose2,'DOM',1])                  
                case 'event5':
                    militaryembed = discord.Embed(title="人選決策",description="➤一名高級將領提議建立新式軍隊，你同意協助籌資。敲定細節後，關於負責人人選，你決定⋯⋯",color=discord.Color.red())
                    militaryembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    militaryembed.add_field(name="▼ 請選擇：",value="•（１）邀請其他軍隊高層共同負責\n•（２）交由高級將領全權負責",inline=False)
                    militaryembed.add_field(name="❖ 工作結算：",value=f"• 你前往兵營進行補給物資訓練，武力<:SLT_INC_B:1375507405059657778>，且軍事<:INC:1375507210448277595>{amount}。",inline=False)
                    militaryembed.set_author(name="兵營特殊事件")
                    # choice1
                    amount_c1 = resource_mag(user_id,'STR') * random.randint(9,11)
                    militaryclose1 = discord.Embed(title="人選決策",description="➤你成功籌措經費，但軍隊高層腐敗，資金遭侵占，計畫最終失敗。然而，在你與高級將領的不懈努力下，成功揪出腐敗源頭，使軍隊重回嚴明軍紀。",color=discord.Color.red())
                    militaryclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    militaryclose1.add_field(name="❖ 事件結果：",value=f"• 軍事<:INC:1375507210448277595>{amount_c1}",inline=False)
                    militaryclose1.set_author(name="兵營特殊事件-結算")
                    # choice2
                    amount_c2 = resource_mag(user_id,'STR') * random.randint(15,17)
                    militaryclose2 = discord.Embed(title="人選決策",description="➤你成功籌措經費，高級將領親自挑選精英士兵，配備最先進武器，並接受科技與情資訓練。最終，這支軍隊成為我國國防的堅實基礎。",color=discord.Color.red())
                    militaryclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    militaryclose2.add_field(name="❖ 事件結果：",value=f"• 軍事<:INC:1375507210448277595>{amount_c2}",inline=False)
                    militaryclose2.set_author(name="兵營特殊事件-結算")
                    return([militaryembed,militaryclose1,'MIL_rs',amount_c1,militaryclose2,'MIL_rs',amount_c2])
        case 'Market':
            match event:
                case 'event1':
                    marketembed = discord.Embed(title="搶劫事件",description="➤市集發生搶劫，搶匪竟是名孩童，民眾抱怨近期治安不穩，要求官員給個說法。作為代表，你沉穩回應道⋯⋯",color=discord.Color.gold())
                    marketembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    marketembed.add_field(name="▼ 請選擇：",value="•（１）加強國民素養，對罪犯進行感化教育\n•（２）國家律令不容挑戰，依法處以刑責",inline=False)
                    marketembed.add_field(name="❖ 工作結算：",value=f"• 你前往市集規劃促銷活動，內政<:SLT_INC_B:1375507405059657778>，且商業<:INC:1375507210448277595>{amount}。",inline=False)
                    marketembed.set_author(name="市集特殊事件")
                    # choice1
                    amount_c1 = resource_mag(user_id,'CHR') * random.randint(5,9)
                    marketclose1 = discord.Embed(title="搶劫事件",description="➤你認為犯罪者皆有改過機會，決定帶回孩童親自教育。民眾敬佩你的仁義，卻不滿此法無法迅速遏止犯罪。此後，你被視為施行仁政的官員，但也因成效不彰而受批評。",color=discord.Color.gold())
                    marketclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    marketclose1.add_field(name="❖ 事件結果：",value=f"• 文化<:INC:1375507210448277595>{amount_c1}",inline=False)
                    marketclose1.set_author(name="市集特殊事件-結算")
                    # choice2
                    amount_c2 = resource_mag(user_id,'STR') * 5
                    marketclose2 = discord.Embed(title="搶劫事件",description="➤你堅持犯罪者應受刑責。民眾敬佩你的公正，但也為犯人求情。你認為放任只會導致偏差行為，果斷拒絕。此後，你的鐵血作風廣為人知。",color=discord.Color.gold())
                    marketclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    marketclose2.add_field(name="❖ 事件結果：",value=f"• 軍事<:INC:1375507210448277595>{amount_c2}",inline=False)
                    marketclose2.set_author(name="市集特殊事件-結算")
                    return([marketembed,marketclose1,'CUL_rs',amount_c1,marketclose2,'MIL_rs',amount_c2])
                case 'event2':
                    marketembed = discord.Embed(title="推銷贗品",description="➤地攤商跟你套近乎，用接近情緒勒索的話術推銷你商品，但你發現他賣的是贗品。你決定⋯⋯",color=discord.Color.gold())
                    marketembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    marketembed.add_field(name="▼ 請選擇：",value="•（１）為了贊助窮人還是跟他收購\n•（２）盜版不可取，為了公平戳破他",inline=False)
                    marketembed.add_field(name="❖ 工作結算：",value=f"• 你前往市集規劃促銷活動，內政<:SLT_INC_B:1375507405059657778>，且商業<:INC:1375507210448277595>{amount}。",inline=False)
                    marketembed.set_author(name="市集特殊事件")
                    # choice1
                    marketclose1 = discord.Embed(title="推銷贗品",description="➤地攤商稱讚你是個好人，你的舉動廣受民眾追捧，各種募資募物活動盛行。然而，最終這些資金是否真正幫助到需要的人，無人知曉。",color=discord.Color.gold())
                    marketclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    marketclose1.add_field(name="❖ 事件結果：",value=f"• 魅力<:SLT_INC_B:1375507405059657778>",inline=False)
                    marketclose1.set_author(name="市集特殊事件-結算")
                    # choice2
                    marketclose2 = discord.Embed(title="推銷贗品",description="➤地攤商不滿，指責你吝嗇。然而，你拒絕盜版的堅持廣受讚譽，民眾在你的以身作則下逐漸培養版權意識。",color=discord.Color.gold())
                    marketclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    marketclose2.add_field(name="❖ 事件結果：",value=f"• 內政<:SLT_INC_B:1375507405059657778>",inline=False)
                    marketclose2.set_author(name="市集特殊事件-結算")
                    return([marketembed,marketclose1,'CHR',1,marketclose2,'DOM',1])
                case 'event3':
                    marketembed = discord.Embed(title="物價飛漲",description="➤物價飛漲，百姓苦不堪言。他們向你陳情希望控制民生物資價格，否則日子過不下去。你決定⋯⋯",color=discord.Color.gold())
                    marketembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    marketembed.add_field(name="▼ 請選擇：",value="•（１）出手干預價格\n•（２）以領土爭議轉移民眾注意力",inline=False)
                    marketembed.add_field(name="❖ 工作結算：",value=f"• 你前往市集規劃促銷活動，內政<:SLT_INC_B:1375507405059657778>，且商業<:INC:1375507210448277595>{amount}。",inline=False)
                    marketembed.set_author(name="市集特殊事件")
                    # choice1
                    marketclose1 = discord.Embed(title="物價飛漲",description="➤你迅速設立價格管制機制,並與供應商協商調度資源,穩定民生市場。雖造成部分廠商間摩擦,但你的行政手腕與調控能力獲得高度肯定。",color=discord.Color.gold())
                    marketclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    marketclose1.add_field(name="❖ 事件結果：",value=f"• 內政<:SLT_INC_B:1375507405059657778>",inline=False)
                    marketclose1.set_author(name="市集特殊事件-結算")
                    # choice2
                    marketclose2 = discord.Embed(title="物價飛漲",description="➤你選擇強硬應對，調派軍隊維穩街頭秩序。軍方迅速鎮壓零星暴動，展現武力震攝力，雖招來爭議，卻也有效遏止事態擴大。",color=discord.Color.gold())
                    marketclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    marketclose2.add_field(name="❖ 事件結果：",value=f"• 武力<:SLT_INC_B:1375507405059657778>",inline=False)
                    marketclose2.set_author(name="市集特殊事件-結算")
                    return([marketembed,marketclose1,'DOM',1,marketclose2,'STR',1])                    
                case 'event4':
                    marketembed = discord.Embed(title="市集活動",description="➤市集同時舉辦了兩個活動，你決定先去看看⋯⋯",color=discord.Color.gold())
                    marketembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    marketmbed.add_field(name="▼ 請選擇：",value="•（１）鄰國協辦的文化交流會\n•（２）高科技產品的發布會",inline=False)
                    marketembed.add_field(name="❖ 工作結算：",value=f"• 你前往市集規劃促銷活動，內政<:SLT_INC_B:1375507405059657778>，且商業<:INC:1375507210448277595>{amount}。",inline=False)
                    marketembed.set_author(name="市集特殊事件")
                    # choice1
                    amount_c1 = resource_mag(user_id,'DOM') * random.randint(9,14)
                    marketclose1 = discord.Embed(title="市集活動",description="➤交流會精采紛呈，不僅讓你結識眾多來自鄰國的商人，也讓你窺見商業合作的契機。",color=discord.Color.gold())
                    marketclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    marketclose1.add_field(name="❖ 事件結果：",value=f"• 商業<:INC:1375507210448277595>{amount_c1}",inline=False)
                    marketclose1.set_author(name="市集特殊事件-結算")
                    # choice2
                    amount_c2 = resource_mag(user_id,'INT') * random.randint(5,6)
                    marketclose2 = discord.Embed(title="市集活動",description="➤發佈會精彩非凡，尤其我國科學院協助開發的多款產品展現科技進步，令你決定上書追加科學院經費。",color=discord.Color.gold())
                    marketclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    marketclose2.add_field(name="❖ 事件結果：",value=f"• 科技<:INC:1375507210448277595>{amount_c2}",inline=False)
                    marketclose2.set_author(name="市集特殊事件-結算")
                    return([marketembed,marketclose1,'BUS_rs',amount_c1,marketclose2,'TEC_rs',amount_c2])                    
                case 'event5':
                    marketembed = discord.Embed(title="查封商鋪",description="➤你查封投機客商鋪，他趁機賄絡，承諾高額回報換取免罪與資助。經評估，你決定⋯⋯",color=discord.Color.gold())
                    marketembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    marketembed.add_field(name="▼ 請選擇：",value="•（１）承諾將他過去的刑責一筆勾銷，並少不了他的好處\n•（２）扣留他的證件以作要脅，讓他不敢輕舉妄動",inline=False)
                    marketembed.add_field(name="❖ 工作結算：",value=f"• 你前往市集規劃促銷活動，內政<:SLT_INC_B:1375507405059657778>，且商業<:INC:1375507210448277595>{amount}。",inline=False)
                    marketembed.set_author(name="市集特殊事件")
                    # choice1
                    amount_c1 = resource_mag(user_id,'DOM') * random.randint(20,62)
                    marketclose1 = discord.Embed(title="查封商鋪",description="➤投機客被你的真誠打動，並許下承諾。他手腕高明，成功販售一批來源不明的高價商品，按約定帶回報酬。你將這筆錢投入國家基礎建設，最終造福人民。",color=discord.Color.gold())
                    marketclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    marketclose1.add_field(name="❖ 事件結果：",value=f"• 商業<:INC:1375507210448277595>{amount_c1}",inline=False)
                    marketclose1.set_author(name="市集特殊事件-結算")
                    # choice2
                    amount_c2 = resource_mag(user_id,'DOM') * random.randint(8,14)
                    marketclose2 = discord.Embed(title="查封商鋪",description="➤你被投機客欺騙，他持偽造證件欲捲款潛逃，幸好海關檢測出其為在逃通緝犯，並當場拘捕。後來你循線查封此人名下產業，收歸國有，總算是有所收穫。",color=discord.Color.gold())
                    marketclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    marketclose2.add_field(name="❖ 事件結果：",value=f"• 商業<:INC:1375507210448277595>{amount_c2}",inline=False)
                    marketclose2.set_author(name="市集特殊事件-結算")
                    return([marketembed,marketclose1,'BUS_rs',amount_c1,marketclose2,'BUS_rs',amount_c2])
        case 'Workshop':
            match event:
                case 'event1':
                    workshopembed = discord.Embed(title="調解紛爭",description="➤兩位客人為爭搶一柄玄鐵劍僵持不下，令匠人不知所措。你在旁觀察許久，決定出手調停，於是你說⋯⋯",color=discord.Color.green())
                    workshopembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    workshopembed.add_field(name="▼ 請選擇：",value="•（１）唯智者方可駕馭利劍\n•（２）武藝高者才配得上此劍",inline=False)
                    workshopembed.add_field(name="❖ 工作結算：",value=f"• 你前往匠人坊擔任學徒，智力<:SLT_INC_B:1375507405059657778>，且科技<:INC:1375507210448277595>{amount}。",inline=False)
                    workshopembed.set_author(name="匠人坊特殊事件")
                    # choice1
                    amount_c1 = resource_mag(user_id,'INT') * random.randint(6,9)
                    workshopclose1 = discord.Embed(title="調解紛爭",description="➤你設下鍛造知識小考，請匠人當場出題評分，兩人爭答之際，意外揭露劍身熱處理的小缺陷，匠人大為震驚，決定據此改良流程。",color=discord.Color.green())
                    workshopclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    workshopclose1.add_field(name="❖ 事件結果：",value=f"• 科技<:INC:1375507210448277595>{amount_c1}",inline=False)
                    workshopclose1.set_author(name="匠人坊特殊事件-結算")
                    # choice2
                    amount_c2 = resource_mag(user_id,'STR') * 8
                    workshopclose2 = discord.Embed(title="調解紛爭",description="➤你提議比劍決勝，高挑者技高一籌取勝，對手也甘拜下風。匠人觀戰後決定將比試規則納入訓練課程，用於模擬士兵格鬥。",color=discord.Color.green())
                    workshopclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    workshopclose2.add_field(name="❖ 事件結果：",value=f"• 軍事<:INC:1375507210448277595>{amount_c2}",inline=False)
                    workshopclose2.set_author(name="匠人坊特殊事件-結算")
                    return([workshopembed,workshopclose1,'TEC_rs',amount_c1,workshopclose2,'MIL_rs',amount_c2])
                case 'event2':
                    workshopembed = discord.Embed(title="外地商人",description="➤匠人坊來了一名外地商人，他自豪宣稱手中之矛可刺穿任何防禦，地上之盾能抵禦任何攻擊。你觀察許久後決定⋯⋯",color=discord.Color.green())
                    workshopembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    workshopembed.add_field(name="▼ 請選擇：",value="•（１）與之攀談，提出令你在意的癥結點\n•（２）買下他的商品，用來練手",inline=False)
                    workshopembed.add_field(name="❖ 工作結算：",value=f"• 你前往匠人坊擔任學徒，智力<:SLT_INC_B:1375507405059657778>，且科技<:INC:1375507210448277595>{amount}。",inline=False)
                    workshopembed.set_author(name="匠人坊特殊事件")
                    # choice1
                    workshopclose1 = discord.Embed(title="外地商人",description="➤商人熱情推銷，但你不為所動，認真詢問若用此矛攻擊此盾如何。商人聞言支吾以對，群眾紛紛起鬨要求試驗。見場面難堪，他連忙收拾包袱落荒而逃。",color=discord.Color.green())
                    workshopclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    workshopclose1.add_field(name="❖ 事件結果：",value=f"• 智力<:SLT_INC_B:1375507405059657778>",inline=False)
                    workshopclose1.set_author(name="匠人坊特殊事件-結算")
                    # choice2
                    workshopclose2 = discord.Embed(title="外地商人",description="➤你正愁缺少稱手兵器，便爽快掏錢買下。後來，你帶兵器給老將人品評，卻被告知材料、工法平凡，讓你頗為尷尬。幸好並無偷工減料，對習武之人而言已足夠實用。",color=discord.Color.green())
                    workshopclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    workshopclose2.add_field(name="❖ 事件結果：",value=f"• 武力<:SLT_INC_B:1375507405059657778>",inline=False)
                    workshopclose2.set_author(name="匠人坊特殊事件-結算")
                    return([workshopembed,workshopclose1,'INT',1,workshopclose2,'STR',1])
                case 'event3':
                    workshopembed = discord.Embed(title="技術瓶頸",description="➤匠人坊近期在技術上遇到不少瓶頸，匠人們求好心切，滿心想著有所突破卻始終不得其門而入。於是你提出⋯⋯",color=discord.Color.green())
                    workshopembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    workshopembed.add_field(name="▼ 請選擇：",value="•（１）與其他國家進行技術交流，催生出好點子\n•（２）從產品本身的使用問題下手，參考消費者意見",inline=False)
                    workshopembed.add_field(name="❖ 工作結算：",value=f"• 你前往匠人坊擔任學徒，智力<:SLT_INC_B:1375507405059657778>，且科技<:INC:1375507210448277595>{amount}。",inline=False)
                    workshopembed.set_author(name="匠人坊特殊事件")
                    # choice1
                    amount_c1 = resource_mag(user_id,'INT') * random.randint(5,18)
                    workshopclose1 = discord.Embed(title="技術瓶頸",description="➤你認為技術交流能激發新點子，遂奔走促成與鄰國合作。交流圓滿成功，不僅催生嶄新想法，也使技藝更上一層樓。",color=discord.Color.green())
                    workshopclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    workshopclose1.add_field(name="❖ 事件結果：",value=f"• 科技<:INC:1375507210448277595>{amount_c1}",inline=False)
                    workshopclose1.set_author(name="匠人坊特殊事件-結算")
                    # choice2
                    amount_c2 = resource_mag(user_id,'DOM') * random.randint(4,8)
                    workshopclose2 = discord.Embed(title="技術瓶頸",description="➤你協助匠人學習與顧客溝通。透過聆聽需求與觀察使用方式，他們驚覺許多細節影響重大。此次交流讓匠人開始思考如何在製作中更貼近使用者習慣。",color=discord.Color.green())
                    workshopclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    workshopclose2.add_field(name="❖ 事件結果：",value=f"• 商業<:INC:1375507210448277595>{amount_c2}",inline=False)
                    workshopclose2.set_author(name="匠人坊特殊事件-結算")
                    return([workshopembed,workshopclose1,'TEC_rs',amount_c1,workshopclose2,'BUS_rs',amount_c2])                   
                case 'event4':
                    workshopembed = discord.Embed(title="手工藝品",description="➤前些日子你在市集閒逛時偶然購得一塊上好的木材，熱愛手工藝的你決定將其製作成⋯⋯",color=discord.Color.green())
                    workshopembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    workshopmbed.add_field(name="▼ 請選擇：",value="•（１）實用的漆器\n•（２）華麗的樂器",inline=False)
                    workshopembed.add_field(name="❖ 工作結算：",value=f"• 你前往匠人坊擔任學徒，智力<:SLT_INC_B:1375507405059657778>，且科技<:INC:1375507210448277595>{amount}。",inline=False)
                    workshopembed.set_author(name="匠人坊特殊事件")
                    # choice1
                    workshopclose1 = discord.Embed(title="手工藝品",description="➤你將此木材製作成漆器，因其兼具公益與實用性，卻又飽含藝術價值，令你情有獨鍾。",color=discord.Color.green())
                    workshopclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    workshopclose1.add_field(name="❖ 事件結果：",value=f"• 內政<:SLT_INC_B:1375507405059657778>",inline=False)
                    workshopclose1.set_author(name="匠人坊特殊事件-結算")
                    # choice2
                    workshopclose2 = discord.Embed(title="手工藝品",description="➤你將此木材製作成樂器，因其能承載情感，極具浪漫，令你情有獨鍾。",color=discord.Color.green())
                    workshopclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    workshopclose2.add_field(name="❖ 事件結果：",value=f"• 魅力<:SLT_INC_B:1375507405059657778>",inline=False)
                    workshopclose2.set_author(name="匠人坊特殊事件-結算")
                    return([workshopembed,workshopclose1,'DOM',1,workshopclose2,'CHR',1])                   
                case 'event5':
                    workshopembed = discord.Embed(title="翻新匠人坊",description="➤匠人坊老舊且動線混亂，買家經常迷路。負責人希望你出資規劃並與匠人協作翻新，你欣然同意並決定⋯⋯",color=discord.Color.green())
                    workshopembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    workshopembed.add_field(name="▼ 請選擇：",value="•（１）相信專業，全權交由匠人們設計與承造\n•（２）積極參與討論、規劃，邀請顧問參謀",inline=False)
                    workshopembed.add_field(name="❖ 工作結算：",value=f"• 你前往匠人坊擔任學徒，智力<:SLT_INC_B:1375507405059657778>，且科技<:INC:1375507210448277595>{amount}。",inline=False)
                    workshopembed.set_author(name="匠人坊特殊事件")
                    # choice1
                    amount_c1 = resource_mag(user_id,'INT') * random.randint(10,11)
                    workshopclose1 = discord.Embed(title="翻新匠人坊",description="➤此次翻修由全體匠人共同協作，因未與匠人充分溝通，導致格局失衡，動線受損。最終，雖比舊匠人坊有所改善，但仍未達你預期的理想效果。",color=discord.Color.green())
                    workshopclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    workshopclose1.add_field(name="❖ 事件結果：",value=f"• 科技<:INC:1375507210448277595>{amount_c1}",inline=False)
                    workshopclose1.set_author(name="匠人坊特殊事件-結算")
                    # choice2
                    amount_c2 = resource_mag(user_id,'INT') * random.randint(12,46)
                    workshopclose2 = discord.Embed(title="翻新匠人坊",description="➤你請來建築顧問參謀，並在動工前與每位匠人深入討論，最終敲定完整藍圖。此次翻修由全體匠人協作，因規劃周全，重建工作順利完成。",color=discord.Color.green())
                    workshopclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    workshopclose2.add_field(name="❖ 事件結果：",value=f"• 科技<:INC:1375507210448277595>{amount_c2}",inline=False)
                    workshopclose2.set_author(name="匠人坊特殊事件-結算")
                    return([workshopembed,workshopclose1,'TEC_rs',amount_c1,workshopclose2,'TEC_rs',amount_c2])
        case 'Teahouse':
            match event:
                case 'event1':
                    teahouseembed = discord.Embed(title="江湖藝人",description="➤茶館近期想邀請江湖藝人演出以吸引人潮，負責人希望交友廣闊的你能給個人選。於是你決定⋯⋯",color=discord.Color.purple())
                    teahouseembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    teahouseembed.add_field(name="▼ 請選擇：",value="•（１）著重市場與宣傳，邀請名氣響亮者\n•（２）著重技藝與內涵，邀請技巧精湛者",inline=False)
                    teahouseembed.add_field(name="❖ 工作結算：",value=f"• 你前往茶館安排藝人演出，魅力<:SLT_INC_B:1375507405059657778>，且文化<:INC:1375507210448277595>{amount}。",inline=False)
                    teahouseembed.set_author(name="茶館特殊事件")
                    # choice1
                    teahouseclose1 = discord.Embed(title="江湖藝人",description="➤你認為吸引人潮需靠噱頭，遂邀名氣響亮的表演者並大肆宣傳。策略奏效，首日萬人空巷，茶館爆滿，甚至有不少大官私下透過關係請你保留位置。",color=discord.Color.purple())
                    teahouseclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    teahouseclose1.add_field(name="❖ 事件結果：",value=f"• 內政<:SLT_INC_B:1375507405059657778>",inline=False)
                    teahouseclose1.set_author(name="茶館特殊事件-結算")
                    # choice2
                    teahouseclose2 = discord.Embed(title="江湖藝人",description="➤你認為吸引人潮需靠實力，遂邀技巧精湛的表演者，並廣發請帖給業界與官員。此人技藝卓越，聯名家接讚嘆你的眼光。",color=discord.Color.purple())
                    teahouseclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    teahouseclose2.add_field(name="❖ 事件結果：",value=f"• 魅力<:SLT_INC_B:1375507405059657778>",inline=False)
                    teahouseclose2.set_author(name="茶館特殊事件-結算")
                    return([teahouseembed,teahouseclose1,'DOM',1,teahouseclose2,'CHR',1])
                case 'event2':
                    teahouseembed = discord.Embed(title="乏人問津",description="➤茶館剛開幕生意不佳，負責人與你安排了幾場精彩的演出，沒想到卻都乏人問津。你決心要讓這裡熱鬧起來，於是打算⋯⋯",color=discord.Color.purple())
                    teahouseembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    teahouseembed.add_field(name="▼ 請選擇：",value="•（１）動用人脈力量，邀請知名人士觀看演出\n•（２）帶隊遊街演出，用表演魅力吸引目光",inline=False)
                    teahouseembed.add_field(name="❖ 工作結算：",value=f"• 你前往茶館安排藝人演出，魅力<:SLT_INC_B:1375507405059657778>，且文化<:INC:1375507210448277595>{amount}。",inline=False)
                    teahouseembed.set_author(name="茶館特殊事件")
                    # choice1
                    teahouseclose1 = discord.Embed(title="乏人問津",description="➤你憑豐富人脈，親自邀請名人觀賞演出。演出精廣受好評，再加上名人光環加持，茶館生意自此扶搖直上。",color=discord.Color.purple())
                    teahouseclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    teahouseclose1.add_field(name="❖ 事件結果：",value=f"• 智力<:SLT_INC_B:1375507405059657778>",inline=False)
                    teahouseclose1.set_author(name="茶館特殊事件-結算")
                    # choice2
                    teahouseclose2 = discord.Embed(title="乏人問津",description="➤你率小隊換上華麗表演服，在市集主幹道奏樂遊行、雜技以宣傳茶館演出，成功吸引民眾圍觀，生意自此扶搖直上。",color=discord.Color.purple())
                    teahouseclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    teahouseclose2.add_field(name="❖ 事件結果：",value=f"• 武力<:SLT_INC_B:1375507405059657778>",inline=False)
                    teahouseclose2.set_author(name="茶館特殊事件-結算")
                    return([teahouseembed,teahouseclose1,'DOM',1,teahouseclose2,'CHR',1])
                case 'event3':
                    teahouseembed = discord.Embed(title="側耳傾聽",description="➤你坐在茶館角落歇息，正巧鄰桌兩人悄聲交談。你不經意聽見幾句後，發現這似乎不是尋常閒話⋯⋯",color=discord.Color.purple())
                    teahouseembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    teahouseembed.add_field(name="▼ 請選擇：",value="•（１）繼續偷聽，分析兩人對話內容\n•（２）親自上前搭話，試圖確認消息真假",inline=False)
                    teahouseembed.add_field(name="❖ 工作結算：",value=f"• 你前往茶館安排藝人演出，魅力<:SLT_INC_B:1375507405059657778>，且文化<:INC:1375507210448277595>{amount}。",inline=False)
                    teahouseembed.set_author(name="茶館特殊事件")
                    # choice1
                    amount_c1 = resource_mag(user_id,'INT') * random.randint(6,15)
                    teahouseclose1 = discord.Embed(title="側耳傾聽",description="➤你壓低帽簷、屏息傾聽，判斷出他們談論的是某項絕密的古籍發現，語中暗藏地點與關鍵細節。你立刻將資訊整理備份，轉交給我國學術機構，促使新一輪文化研究熱潮。",color=discord.Color.purple())
                    teahouseclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    teahouseclose1.add_field(name="❖ 事件結果：",value=f"• 科技<:INC:1375507210448277595>{amount_c1}",inline=False)
                    teahouseclose1.set_author(name="茶館特殊事件-結算")
                    # choice2
                    amount_c2 = resource_mag(user_id,'DOM') * random.randint(5,8)
                    teahouseclose2 = discord.Embed(title="側耳傾聽",description="➤你點了壺茶佯裝巧遇，與兩人寒暄幾句後，借機切入話題。發現他們其實是某高等研究機構的工程師，剛從實驗基地出差返程。你提問敏銳，對方反倒願意分享更多細節，使你成功掌握一項前沿技術走向。",color=discord.Color.purple())
                    teahouseclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    teahouseclose2.add_field(name="❖ 事件結果：",value=f"• 商業<:INC:1375507210448277595>{amount_c2}",inline=False)
                    teahouseclose2.set_author(name="茶館特殊事件-結算")
                    return([teahouseembed,teahouseclose1,'CUL_rs',amount_c1,teahouseclose2,'TEC_rs',amount_c2])                    
                case 'event4':
                    teahouseembed = discord.Embed(title="酒醉鬧事",description="➤這日茶館十分熱鬧，不巧遇上有人喝醉鬧事，還驚擾到鄰座的客人。氣氛劍拔弩張，眼看就要大打出手，你決定⋯⋯",color=discord.Color.purple())
                    teahouseembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    teahousembed.add_field(name="▼ 請選擇：",value="•（１）巧施手段\n•（２）武力勸服",inline=False)
                    teahouseembed.add_field(name="❖ 工作結算：",value=f"• 你前往茶館安排藝人演出，魅力<:SLT_INC_B:1375507405059657778>，且文化<:INC:1375507210448277595>{amount}。",inline=False)
                    teahouseembed.set_author(name="茶館特殊事件")
                    # choice1
                    amount_c1 = resource_mag(user_id,'INT') * random.randint(5,6)
                    teahouseclose1 = discord.Embed(title="酒醉鬧事",description="➤你立刻叫停演出，請資深俳優解圍。老師傅妙語如珠，讓醉漢羞愧離場，觀眾笑聲不斷。沒想到，鬧事者竟是剛入境的外籍學者，醉後失態。為表歉意，他主動分享了一份珍貴的研究筆記，意外促成我國科技突破。",color=discord.Color.purple())
                    teahouseclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    teahouseclose1.add_field(name="❖ 事件結果：",value=f"• 科技<:INC:1375507210448277595>{amount_c1}",inline=False)
                    teahouseclose1.set_author(name="茶館特殊事件-結算")
                    # choice2
                    amount_c2 = resource_mag(user_id,'STR') * 8
                    teahouseclose2 = discord.Embed(title="酒醉鬧事",description="➤你立刻派人請來衛隊隊長，及時制服了醉漢。你連忙安撫受牽連的客人，送上招待券並吩咐伙計款待，終讓他們消氣。多虧你與隊長及時出手，避免一場災難，從此無人敢在茶館鬧事。",color=discord.Color.purple())
                    teahouseclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    teahouseclose2.add_field(name="❖ 事件結果：",value=f"• 軍事<:INC:1375507210448277595>{amount_c2}",inline=False)
                    teahouseclose2.set_author(name="茶館特殊事件-結算")
                    return([teahouseembed,teahouseclose1,'TEC_rs',amount_c1,teahouseclose2,'MIL_rs',amount_c2])                   
                case 'event5':
                    teahouseembed = discord.Embed(title="舞台翻新",description="➤負責人提議翻新舞台，以迎接即將到來的大型演出。你同意資助。對於這次工程，你決定⋯⋯",color=discord.Color.purple())
                    teahouseembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    teahouseembed.add_field(name="▼ 請選擇：",value="•（１）負責人對此較為熟悉，因此全權交由他處理\n•（２）積極參與，推薦熟識的大建商",inline=False)
                    teahouseembed.add_field(name="❖ 工作結算：",value=f"• 你前往茶館安排藝人演出，魅力<:SLT_INC_B:1375507405059657778>，且文化<:INC:1375507210448277595>{amount}。",inline=False)
                    teahouseembed.set_author(name="茶館特殊事件")
                    # choice1
                    amount_c1 = resource_mag(user_id,'CHR') * random.randint(8,9)
                    teahouseclose1 = discord.Embed(title="舞台翻新",description="➤你沒料到負責人一時糊塗，選了人手不足的小作坊承造。雖做工精細，但工期嚴重延誤，讓你與負責人焦頭爛額，好在完工後場地品質尚可。",color=discord.Color.purple())
                    teahouseclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    teahouseclose1.add_field(name="❖ 事件結果：",value=f"• 文化<:INC:1375507210448277595>{amount_c1}",inline=False)
                    teahouseclose1.set_author(name="茶館特殊事件-結算")
                    # choice2
                    amount_c2 = resource_mag(user_id,'CHR') * random.randint(15,33)
                    teahouseclose2 = discord.Embed(title="舞台翻新",description="➤為趕上演出檔期，你委託城內最大營造作坊承造，並優先處理此案，確保品質的同時如期完工。此次不僅翻新舞台，後台設備也全面更新，使演出更流暢。",color=discord.Color.purple())
                    teahouseclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    teahouseclose2.add_field(name="❖ 事件結果：",value=f"• 文化<:INC:1375507210448277595>{amount_c2}",inline=False)
                    teahouseclose2.set_author(name="茶館特殊事件-結算")
                    return([teahouseembed,teahouseclose1,'CUL_rs',amount_c1,teahouseclose2,'CUL_rs',amount_c2])
        case 'Arsenal':
            match event:
                case 'event1':
                    arsenalembed = discord.Embed(title="前衛武器",description="➤一名工匠設計出前衛武器，因缺乏支持求助於你。你賞識奇才，當即資助。他頻繁向你報告與商談，而你總是⋯⋯",color=discord.Color.red())
                    arsenalembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    arsenalembed.add_field(name="▼ 請選擇：",value="•（１）聚焦實用與需求，親自參與調整方向\n•（２）充分信任，協助他自由開發並共同測試",inline=False)
                    arsenalembed.add_field(name="❖ 工作結算：",value=f"• 你前往兵工廠協助武器製造，軍事<:INC:1375507210448277595>{amount}、商業<:INC:1375507210448277595>{amountt}。",inline=False)
                    arsenalembed.set_author(name="兵工廠特殊事件")
                    # choice1
                    amount_c1 = resource_mag(user_id,'INT') * 8
                    arsenalclose1 = discord.Embed(title="前衛武器",description="➤你認為資源應用得其所，便根據軍方當前需求與他深入討論，調整設計方向。雖然實驗最終失敗，工匠因涉密被捕，但你保留的手稿啟發後續研發，引起科學界高度重視。",color=discord.Color.red())
                    arsenalclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    arsenalclose1.add_field(name="❖ 事件結果：",value=f"• 科技<:INC:1375507210448277595>{amount_c1}",inline=False)
                    arsenalclose1.set_author(name="兵工廠特殊事件-結算")
                    # choice2
                    amount_c2 = resource_mag(user_id,'STR') * 18
                    arsenalclose2 = discord.Embed(title="前衛武器",description="➤你提供必要支援，尊重工匠決策，全程陪同測試與改良。短短數月內武器完成，且由你親自驗證性能卓越。新武器一經亮相便震懾四方，為我國帶來強大軍事聲望。",color=discord.Color.red())
                    arsenalclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    arsenalclose2.add_field(name="❖ 事件結果：",value=f"• 軍事<:INC:1375507210448277595>{amount_c2}",inline=False)
                    arsenalclose2.set_author(name="兵工廠特殊事件-結算")
                    return([arsenalembed,arsenalclose1,'TEC_rs',amount_c1,arsenalclose2,'MIL_rs',amount_c2])
                case 'event2':
                    arsenalembed = discord.Embed(title="技術出售",description="➤經多年努力，兵工廠成功研製先進武器系統。遠方大國聞訊遣使者來訪，開出天價欲買斷技術與產品。對此，你決定⋯⋯",color=discord.Color.red())
                    arsenalembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    arsenalmbed.add_field(name="▼ 請選擇：",value="•（１）不賣\n•（２）賣",inline=False)
                    arsenalembed.add_field(name="❖ 工作結算：",value=f"• 你前往兵工廠協助武器製造，軍事<:INC:1375507210448277595>{amount}、商業<:INC:1375507210448277595>{amountt}。",inline=False)
                    arsenalembed.set_author(name="兵工廠特殊事件")
                    # choice1
                    amount_c1 = resource_mag(user_id,'STR') * 9
                    arsenalclose1 = discord.Embed(title="技術出售",description="➤你堅定拒絕，並表示這是我國賴以生存的根本。",color=discord.Color.red())
                    arsenalclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    arsenalclose1.add_field(name="❖ 事件結果：",value=f"• 軍事<:INC:1375507210448277595>{amount_c1}",inline=False)
                    arsenalclose1.set_author(name="兵工廠特殊事件-結算")
                    # choice2
                    amount_c2 = resource_mag(user_id,'DOM') * 12
                    arsenalclose2 = discord.Embed(title="技術出售",description="➤你本想大聲斥責，但使者給的實在太多了。",color=discord.Color.red())
                    arsenalclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    arsenalclose2.add_field(name="❖ 事件結果：",value=f"• 商業<:INC:1375507210448277595>{amount_c2}",inline=False)
                    arsenalclose2.set_author(name="兵工廠特殊事件-結算")
                    return([arsenalembed,arsenalclose1,'MIL_rs',amount_c1,arsenalclose2,'BUS_rs',amount_c2])
                case 'event3':
                    arsenalembed = discord.Embed(title="設計瓶頸",description="➤兵工廠的年輕工匠們在設計上遇到了一些瓶頸。你建議他們⋯⋯",color=discord.Color.red())
                    arsenalembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    arsenalembed.add_field(name="▼ 請選擇：",value="•（１）去校場觀摩\n•（２）與科學院交流",inline=False)
                    arsenalembed.add_field(name="❖ 工作結算：",value=f"• 你前往兵工廠協助武器製造，軍事<:INC:1375507210448277595>{amount}、商業<:INC:1375507210448277595>{amountt}。",inline=False)
                    arsenalembed.set_author(name="兵工廠特殊事件")
                    # choice1
                    amount_c1 = resource_mag(user_id,'STR') * 10
                    arsenalclose1 = discord.Embed(title="設計瓶頸",description="➤經過長時間的觀察和與軍人的相處，這批年輕工匠設計出來的武器與防禦系統更貼近軍人的使用習慣。",color=discord.Color.red())
                    arsenalclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    arsenalclose1.add_field(name="❖ 事件結果：",value=f"• 軍事<:INC:1375507210448277595>{amount_c1}",inline=False)
                    arsenalclose1.set_author(name="兵工廠特殊事件-結算")
                    # choice2
                    amount_c2 = resource_mag(user_id,'INT') * 9
                    arsenalclose2 = discord.Embed(title="設計瓶頸",description="➤經過與科學院的切磋交流，工匠與科學家們都有所斬獲，年輕工匠們也將許多新研發的技術應用在武器與防禦系統上。",color=discord.Color.red())
                    arsenalclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    arsenalclose2.add_field(name="❖ 事件結果：",value=f"• 科技<:INC:1375507210448277595>{amount_c2}",inline=False)
                    arsenalclose2.set_author(name="兵工廠特殊事件-結算")
                    return([arsenalembed,arsenalclose1,'MIL_rs',amount_c1,arsenalclose2,'TEC_rs',amount_c2])                    
                case 'event4':
                    arsenalembed = discord.Embed(title="簽訂協議",description="➤你代表兵工廠與他國官員簽訂長期合作協議，期間他國的官員屢屢對你出言不遜。作為一國之代表的你選擇⋯⋯",color=discord.Color.red())
                    arsenalembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    arsenalembed.add_field(name="▼ 請選擇：",value="•（１）維持禮節，用笑容從容應對\n•（２）沒什麼好爭的，重要的是達成協議",inline=False)
                    arsenalembed.add_field(name="❖ 工作結算：",value=f"• 你前往兵工廠協助武器製造，軍事<:INC:1375507210448277595>{amount}、商業<:INC:1375507210448277595>{amountt}。",inline=False)
                    arsenalembed.set_author(name="兵工廠特殊事件")
                    # choice1
                    amount_c1 = resource_mag(user_id,'CHR') * 9
                    arsenalclose1 = discord.Embed(title="簽訂協議",description="➤對方雖冷嘲熱諷，但你進退得宜，更使其無從占便宜。最終談判圓滿完成，他國官員對你得體的應對進退，也不禁稱嘆不愧是禮儀之邦。",color=discord.Color.red())
                    arsenalclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    arsenalclose1.add_field(name="❖ 事件結果：",value=f"• 文化<:INC:1375507210448277595>{amount_c1}",inline=False)
                    arsenalclose1.set_author(name="兵工廠特殊事件-結算")
                    # choice2
                    amount_c2 = resource_mag(user_id,'DOM') * random.randint(9,12)
                    arsenalclose2 = discord.Embed(title="簽訂協議",description="➤你冷靜應對，專注推進談判。對方逐漸察覺，你的避重就輕並非退讓，而是穩扎穩打，最終談成有利我國的貿易協定，不禁喟嘆不該小覷你。",color=discord.Color.red())
                    arsenalclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    arsenalclose2.add_field(name="❖ 事件結果：",value=f"• 商業<:INC:1375507210448277595>{amount_c2}",inline=False)
                    arsenalclose2.set_author(name="兵工廠特殊事件-結算")
                    return([arsenalembed,arsenalclose1,'CUL_rs',amount_c1,arsenalclose2,'BUS_rs',amount_c2])                   
                case 'event5':
                    arsenalembed = discord.Embed(title="加班趕工",description="➤今天是年節第一天，兵工廠仍為政府重要訂單趕工。你明白工人無法與家人團聚的辛勞，又看著他們連日操勞，你最終深思後說道⋯⋯",color=discord.Color.red())
                    arsenalembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    arsenalembed.add_field(name="▼ 請選擇：",value="•（１）「加油，再撐一下，我們一起完成它，晚上還趕得及回家吃團圓飯。」\n•（２）「辛苦大家了。政府那邊我來處理，今天都先回家過節吧。」",inline=False)
                    arsenalembed.add_field(name="❖ 工作結算：",value=f"• 你前往兵工廠協助武器製造，軍事<:INC:1375507210448277595>{amount}、商業<:INC:1375507210448277595>{amountt}。",inline=False)
                    arsenalembed.set_author(name="兵工廠特殊事件")
                    # choice1
                    amount_c1 = resource_mag(user_id,'STR') * 13
                    arsenalclose1 = discord.Embed(title="加班趕工",description="➤你深知此訂單重要，且已近完成，便與工人並肩奮戰至傍晚，終順利結案。感激他們的辛勞，你宣布加發獎金並多給幾天假期。工人雖疲憊，卻滿心喜悅地回家過節。",color=discord.Color.red())
                    arsenalclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    arsenalclose1.add_field(name="❖ 事件結果：",value=f"• 軍事<:INC:1375507210448277595>{amount_c1}",inline=False)
                    arsenalclose1.set_author(name="兵工廠特殊事件-結算")
                    # choice2
                    amount_c2 = resource_mag(user_id,'CHR') * 8
                    arsenalclose2 = discord.Embed(title="加班趕工",description="➤你決定讓全廠停工團圓，並主動承擔政府責難。消息傳開後，各地媒體讚揚你的決斷，提升了工人尊嚴與社會觀感。",color=discord.Color.red())
                    arsenalclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    arsenalclose2.add_field(name="❖ 事件結果：",value=f"• 文化<:INC:1375507210448277595>{amount_c2}",inline=False)
                    arsenalclose2.set_author(name="兵工廠特殊事件-結算")
                    return([arsenalembed,arsenalclose1,'MIL_rs',amount_c1,arsenalclose2,'CUL_rs',amount_c2])
        case 'Reception':
            match event:
                case 'event1':
                    receptionembed = discord.Embed(title="緊急事態",description="➤外國使節的女兒丟失珍貴髮飾，此時一名神秘人承諾若給予金錢，會盡快找回髮飾。你當即付錢，但久久未收到消息，你瀕臨崩潰，脫口而出⋯⋯",color=discord.Color.gold())
                    receptionembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    receptionembed.add_field(name="▼ 請選擇：",value="•（１）「拜託快點回來吧！哪怕是做個類似的也可以，趕快拿來能讓我交差啊啊啊啊啊！」\n•（２）「拜託快點找到吧！要是找不到原來那個髮飾，我怎麼跟使節交代啊啊啊啊啊啊！」",inline=False)
                    receptionembed.add_field(name="❖ 工作結算：",value=f"• 你前往接待所協助接待外賓，商業<:INC:1375507210448277595>{amount}、科技<:INC:1375507210448277595>{amountt}。",inline=False)
                    receptionembed.set_author(name="接待所特殊事件")
                    # choice1
                    amount_c1 = resource_mag(user_id,'DOM') * random.randint(18,22)
                    receptionclose1 = discord.Embed(title="緊急事態",description="➤又過好一陣子，神秘人終於現身，帶來全國頂尖匠人精心復刻的髮飾。雖然時間超出預期讓你不滿，但使節對你的協助深表感激，最終與你達成科技交流計畫。",color=discord.Color.gold())
                    receptionclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    receptionclose1.add_field(name="❖ 事件結果：",value=f"• 商業<:INC:1375507210448277595>{amount_c1}",inline=False)
                    receptionclose1.set_author(name="接待所特殊事件-結算")
                    # choice2
                    amount_c2 = resource_mag(user_id,'INT') * random.randint(12,36)
                    receptionclose2 = discord.Embed(title="緊急事態",description="➤過了將近半天，神秘人終於現身，交還遺失的髮飾，原來是被市集的孩子撿走。雖然時間超出預期讓你不滿，但使節與女兒非常高興，最終你更順勢談成一份貿易協定。",color=discord.Color.gold())
                    receptionclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    receptionclose2.add_field(name="❖ 事件結果：",value=f"• 科技<:INC:1375507210448277595>{amount_c2}",inline=False)
                    receptionclose2.set_author(name="接待所特殊事件-結算")
                    return([receptionembed,receptionclose1,'BUS_rs',amount_c1,receptionclose2,'TEC_rs',amount_c2])
                case 'event2':
                    receptionembed = discord.Embed(title="經濟下滑",description="➤針對近期經濟狀況下滑、物價高漲一事，你在接待所附近召開記者會，向社會大眾致歉。期間你強調政府已施行相關措施，並表示⋯⋯",color=discord.Color.gold())
                    receptionembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    receptionmbed.add_field(name="▼ 請選擇：",value="•（１）希望大家靜心等待，市場自然會恢復平衡\n•（２）以身作則，希望能與大家互相扶持、共體時艱",inline=False)
                    receptionembed.add_field(name="❖ 工作結算：",value=f"• 你前往接待所協助接待外賓，商業<:INC:1375507210448277595>{amount}、科技<:INC:1375507210448277595>{amountt}。",inline=False)
                    receptionembed.set_author(name="接待所特殊事件")
                    # choice1
                    amount_c1 = resource_mag(user_id,'INT') * random.randint(7,14)
                    receptionclose1 = discord.Embed(title="經濟下滑",description="➤你公開展示一套由國家智庫所研發的新經濟模型，詳細模擬價格變動與供需調整趨勢。這場說明不僅穩住民心，也為後續政策制定提供珍貴依據。",color=discord.Color.gold())
                    receptionclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    receptionclose1.add_field(name="❖ 事件結果：",value=f"• 科技<:INC:1375507210448277595>{amount_c1}",inline=False)
                    receptionclose1.set_author(name="接待所特殊事件-結算")
                    # choice2
                    amount_c2 = resource_mag(user_id,'CHR') * random.randint(6,30)
                    receptionclose2 = discord.Embed(title="經濟下滑",description="➤你發起「節用同行」運動，號召政界與民間共同實踐簡約生活。你的行動掀起一波公共文化省思，進而帶動社會倫理與生活價值的廣泛討論。",color=discord.Color.gold())
                    receptionclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    receptionclose2.add_field(name="❖ 事件結果：",value=f"• 文化<:INC:1375507210448277595>{amount_c2}",inline=False)
                    receptionclose2.set_author(name="接待所特殊事件-結算")
                    return([receptionembed,receptionclose1,'TEC_rs',amount_c1,receptionclose2,'CUL_rs',amount_c2])
                case 'event3':
                    receptionembed = discord.Embed(title="合作提案",description="➤外國商團代表其國家提案，願在特定產業協助進行建設，並派遣顧問協助。我國正值發展關鍵期，你決定將經費花在⋯⋯",color=discord.Color.gold())
                    receptionembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    receptionembed.add_field(name="▼ 請選擇：",value="•（１）提升軍事防禦體系\n•（２）改善交通與基礎建設",inline=False)
                    receptionembed.add_field(name="❖ 工作結算：",value=f"• 你前往接待所協助接待外賓，商業<:INC:1375507210448277595>{amount}、科技<:INC:1375507210448277595>{amountt}。",inline=False)
                    receptionembed.set_author(name="接待所特殊事件")
                    # choice1
                    amount_c1 = resource_mag(user_id,'STR') * random.randint(6,10)
                    receptionclose1 = discord.Embed(title="合作提案",description="➤你認為亂世中先求自保最為重要。該國信守承諾，按期完工。系統完成後，大幅提升我國防禦能力，應對外敵更加從容。",color=discord.Color.gold())
                    receptionclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    receptionclose1.add_field(name="❖ 事件結果：",value=f"• 軍事<:INC:1375507210448277595>{amount_c1}",inline=False)
                    receptionclose1.set_author(name="接待所特殊事件-結算")
                    # choice2
                    amount_c2 = resource_mag(user_id,'DOM') * random.randint(9,31)
                    receptionclose2 = discord.Embed(title="合作提案",description="➤你認為亂世中應穩紮穩打，提升民生才能促進國家發展。該國信守承諾，按期完工。此舉促進商業繁榮，催生眾多中小企業，帶動經濟正向循環。",color=discord.Color.gold())
                    receptionclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    receptionclose2.add_field(name="❖ 事件結果：",value=f"• 商業<:INC:1375507210448277595>{amount_c2}",inline=False)
                    receptionclose2.set_author(name="接待所特殊事件-結算")
                    return([receptionembed,receptionclose1,'MIL_rs',amount_c1,receptionclose2,'BUS_rs',amount_c2])                    
                case 'event4':
                    receptionembed = discord.Embed(title="援助鄰國",description="➤鄰國陷入戰爭，派出使節請求支援，説如果願意提供救援，就會在各國面前公開感謝。對此你決定⋯⋯",color=discord.Color.gold())
                    receptionembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    receptionembed.add_field(name="▼ 請選擇：",value="•（１）派軍進駐以防範敵軍，並要求軍事干預權\n•（２）提供物資，維持民生，但要求簽署長期貿易協定",inline=False)
                    receptionembed.add_field(name="❖ 工作結算：",value=f"• 你前往接待所協助接待外賓，商業<:INC:1375507210448277595>{amount}、科技<:INC:1375507210448277595>{amountt}。",inline=False)
                    receptionembed.set_author(name="接待所特殊事件")
                    # choice1
                    amount_c1 = resource_mag(user_id,'STR') * random.randint(8,22)
                    receptionclose1 = discord.Embed(title="援助鄰國",description="➤該國勉強同意，你隨即派軍協防。我軍派遣將領守城有方，關鍵戰役大破敵軍，一戰成名。此外，我國掌握軍事干預權，進一步穩固軍政實力。",color=discord.Color.gold())
                    receptionclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    receptionclose1.add_field(name="❖ 事件結果：",value=f"• 軍事<:INC:1375507210448277595>{amount_c1}",inline=False)
                    receptionclose1.set_author(name="接待所特殊事件-結算")
                    # choice2
                    amount_c2 = resource_mag(user_id,'CHR') * 8
                    receptionclose2 = discord.Embed(title="援助鄰國",description="➤該國勉強同意，你即刻提供物資穩定民心與物價。物資在饑荒前送達，免去災難。戰後，貿易協定加深鄰國對我國的依賴，兩國更締結長久商業同盟。",color=discord.Color.gold())
                    receptionclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    receptionclose2.add_field(name="❖ 事件結果：",value=f"• 文化<:INC:1375507210448277595>{amount_c2}",inline=False)
                    receptionclose2.set_author(name="接待所特殊事件-結算")
                    return([receptionembed,receptionclose1,'MIL_rs',amount_c1,receptionclose2,'CUL_rs',amount_c2])                  
                case 'event5':
                    receptionembed = discord.Embed(title="錄用新人",description="➤來訪的外國商人日漸增多，接待所人手捉襟見肘，上級委請你擔任面試官，你決定錄取⋯⋯",color=discord.Color.gold())
                    receptionembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    receptionembed.add_field(name="▼ 請選擇：",value="•（１）市井出身，經商多年、處事圓滑的中年人\n•（２）書院出身，有政治抱負的年輕學子",inline=False)
                    receptionembed.add_field(name="❖ 工作結算：",value=f"• 你前往接待所協助接待外賓，商業<:INC:1375507210448277595>{amount}、科技<:INC:1375507210448277595>{amountt}。",inline=False)
                    receptionembed.set_author(name="接待所特殊事件")
                    # choice1
                    amount_c1 = resource_mag(user_id,'DOM') * 41
                    receptionclose1 = discord.Embed(title="錄用新人",description="➤此人八面玲瓏、做事面面俱到，尤其面對外國商人時總能使談判取得上風，談成不少商業合作案。",color=discord.Color.gold())
                    receptionclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    receptionclose1.add_field(name="❖ 事件結果：",value=f"• 商業<:INC:1375507210448277595>{amount_c1}",inline=False)
                    receptionclose1.set_author(name="接待所特殊事件-結算")
                    # choice2
                    amount_c2 = resource_mag(user_id,'CHR') * 6
                    receptionclose2 = discord.Embed(title="錄用新人",description="➤此人禮儀滿分，應對外國官員十分得體，作為本國顏面讓人留下溫文爾雅的深刻印象。",color=discord.Color.gold())
                    receptionclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    receptionclose2.add_field(name="❖ 事件結果：",value=f"• 文化<:INC:1375507210448277595>{amount_c2}",inline=False)
                    receptionclose2.set_author(name="接待所特殊事件-結算")
                    return([receptionembed,receptionclose1,'BUS_rs',amount_c1,receptionclose2,'CUL_rs',amount_c2])
        case 'Factory':
            match event:
                case 'event1':
                    factoryembed = discord.Embed(title="策略選擇",description="➤加工所剛起步，資金運轉有問題，需要手段度過難關。你建議⋯⋯",color=discord.Color.green())
                    factoryembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    factoryembed.add_field(name="▼ 請選擇：",value="•（１）試試合作接案，做些「話題性高」的商品撐撐看\n•（２）將倉庫那批失敗品重新拆解，嘗試拼出能賣的新東西",inline=False)
                    factoryembed.add_field(name="❖ 工作結算：",value=f"• 你前往加工所協助安排進出貨，科技<:INC:1375507210448277595>{amount}、文化<:INC:1375507210448277595>{amountt}。",inline=False)
                    factoryembed.set_author(name="加工所特殊事件")
                    # choice1
                    amount_c1 = resource_mag(user_id,'CHR') * random.randint(6,9)
                    factoryclose1 = discord.Embed(title="策略選擇",description="➤你們與在地劇團、畫家、小出版社合作，製作一批獨特限量商品。這批設計新穎、風格強烈的作品意外走紅，甚至被當成收藏品轉售。加工所的名聲迅速打開，也讓不少文藝單位主動洽談合作。",color=discord.Color.green())
                    factoryclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    factoryclose1.add_field(name="❖ 事件結果：",value=f"• 文化<:INC:1375507210448277595>{amount_c1}",inline=False)
                    factoryclose1.set_author(name="加工所特殊事件-結算")
                    # choice2
                    amount_c2 = resource_mag(user_id,'INT') * random.randint(10,22)
                    factoryclose2 = discord.Embed(title="策略選擇",description="➤你主導團隊進行技術測試與零件重組，拆東補西，設法從報廢材料中拼出可販售的商品雛型。雖然充滿挑戰，但也累積下不少工程經驗。這些重組製程的技術，為日後發展打下良好基礎。",color=discord.Color.green())
                    factoryclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    factoryclose2.add_field(name="❖ 事件結果：",value=f"• 科技<:INC:1375507210448277595>{amount_c2}",inline=False)
                    factoryclose2.set_author(name="加工所特殊事件-結算")
                    return([factoryembed,factoryclose1,'CUL_rs',amount_c1,factoryclose2,'TEC_rs',amount_c2])
                case 'event2':
                    factoryembed = discord.Embed(title="生產方向決策",description="➤負責人表示接下來應該可以有點餘裕，要決定生產方向，向你諮詢建議。你建議⋯⋯",color=discord.Color.green())
                    factoryembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    factorymbed.add_field(name="▼ 請選擇：",value="•（１）大量生產便宜的商品，賺取大量外匯\n•（２）開發高端創新商品，打造技術品牌",inline=False)
                    factoryembed.add_field(name="❖ 工作結算：",value=f"• 你前往加工所協助安排進出貨，科技<:INC:1375507210448277595>{amount}、文化<:INC:1375507210448277595>{amountt}。",inline=False)
                    factoryembed.set_author(name="加工所特殊事件")
                    # choice1
                    amount_c1 = resource_mag(user_id,'DOM') * 9
                    factoryclose1 = discord.Embed(title="生產方向決策",description="➤我國推出價格低廉的民生物資。這些商品物美價廉，成為輸出外國的強力貨物。經過數年培養，如今已為國家賺進大壩外匯。",color=discord.Color.green())
                    factoryclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    factoryclose1.add_field(name="❖ 事件結果：",value=f"• 商業<:INC:1375507210448277595>{amount_c1}",inline=False)
                    factoryclose1.set_author(name="加工所特殊事件-結算")
                    # choice2
                    amount_c2 = resource_mag(user_id,'INT') * 9
                    factoryclose2 = discord.Embed(title="生產方向決策",description="➤我國導入先進製程，研發高品質創新飾品，並強化品牌形象。商品結合科技與美學，逐漸建立起國際聲譽，成為技術實力的象徵。",color=discord.Color.green())
                    factoryclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    factoryclose2.add_field(name="❖ 事件結果：",value=f"• 科技<:INC:1375507210448277595>{amount_c2}",inline=False)
                    factoryclose2.set_author(name="加工所特殊事件-結算")
                    return([factoryembed,factoryclose1,'BUS_rs',amount_c1,factoryclose2,'TEC_rs',amount_c2])
                case 'event3':
                    factoryembed = discord.Embed(title="行前叮囑",description="➤加工所欲開設新產線，但缺乏關鍵技術。員工自願前往鄰國留學，要求足夠盤纏。你同意後，臨行前對他說⋯⋯",color=discord.Color.green())
                    factoryembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    factoryembed.add_field(name="▼ 請選擇：",value="•（１）「希望你能兢兢業業、力求學到精髓。」\n•（２）「希望你放寬心胸、放開手腳去做。」",inline=False)
                    factoryembed.add_field(name="❖ 工作結算：",value=f"• 你前往加工所協助安排進出貨，科技<:INC:1375507210448277595>{amount}、文化<:INC:1375507210448277595>{amountt}。",inline=False)
                    factoryembed.set_author(name="加工所特殊事件")
                    # choice1
                    amount_c1 = resource_mag(user_id,'INT') * 55
                    factoryclose1 = discord.Embed(title="行前叮囑",description="➤此人沉著冷靜，留學期間成功掌握關鍵技術。回國後，他協助加工所完成新產線，使我國加工所成為高科技大廠的合作夥伴。",color=discord.Color.green())
                    factoryclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    factoryclose1.add_field(name="❖ 事件結果：",value=f"• 科技<:INC:1375507210448277595>{amount_c1}",inline=False)
                    factoryclose1.set_author(name="加工所特殊事件-結算")
                    # choice2
                    amount_c2 = resource_mag(user_id,'CHR') * 9
                    factoryclose2 = discord.Embed(title="行前叮囑",description="➤此人雖沒能成功取得關鍵技術的資料，但他在鄰國學得的街頭民謠與舞蹈在民間刮起一陣旋風，使年輕人競相模仿。",color=discord.Color.green())
                    factoryclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    factoryclose2.add_field(name="❖ 事件結果：",value=f"• 文化<:INC:1375507210448277595>{amount_c2}",inline=False)
                    factoryclose2.set_author(name="加工所特殊事件-結算")
                    return([factoryembed,factoryclose1,'TEC_rs',amount_c1,factoryclose2,'CUL_rs',amount_c2])                    
                case 'event4':
                    factoryembed = discord.Embed(title="材料分配",description="➤加工所剛製作好一批材料，正巧遇到軍方與營造商來批貨，雙方都想要這批材料並爭相出價。這時正好路過的你便被請來裁斷，你決定⋯⋯",color=discord.Color.green())
                    factoryembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    factoryembed.add_field(name="▼ 請選擇：",value="•（１）給軍方\n•（２）給營造商",inline=False)
                    factoryembed.add_field(name="❖ 工作結算：",value=f"• 你前往加工所協助安排進出貨，科技<:INC:1375507210448277595>{amount}、文化<:INC:1375507210448277595>{amountt}。",inline=False)
                    factoryembed.set_author(name="加工所特殊事件")
                    # choice1
                    amount_c1 = resource_mag(user_id,'STR') * random.randint(8,9)
                    factoryclose1 = discord.Embed(title="材料分配",description="➤你決定優先軍需。事後得知，軍方正進行新式裝備研發，這批材料完美契合需求。隨即提出長期合作，帶動整體軍工產線升級。",color=discord.Color.green())
                    factoryclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    factoryclose1.add_field(name="❖ 事件結果：",value=f"• 軍事<:INC:1375507210448277595>{amount_c1}",inline=False)
                    factoryclose1.set_author(name="加工所特殊事件-結算")
                    # choice2
                    amount_c2 = resource_mag(user_id,'DOM') * 9
                    factoryclose2 = discord.Embed(title="材料分配",description="➤你決定優先民用。事後得知，營造商正試行模組化建築技術，這批材料大幅提升施工效率，示範案迅速落成，引發市場關注。訂單湧入，加工所與營造業生營大譟，商業活動隨之蓬勃發展。",color=discord.Color.green())
                    factoryclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    factoryclose2.add_field(name="❖ 事件結果：",value=f"• 商業<:INC:1375507210448277595>{amount_c2}",inline=False)
                    factoryclose2.set_author(name="加工所特殊事件-結算")
                    return([factoryembed,factoryclose1,'MIL_rs',amount_c1,factoryclose2,'BUS_rs',amount_c2])                   
                case 'event5':
                    factoryembed = discord.Embed(title="監守自盜",description="➤加工所中有員工監守自盜，經過幾日的調查只堪堪鎖定了幾個嫌疑人，為此你決定⋯⋯",color=discord.Color.green())
                    factoryembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    factoryembed.add_field(name="▼ 請選擇：",value="•（１）反向追查貨物流向\n•（２）請軍方介入偵辦",inline=False)
                    factoryembed.add_field(name="❖ 工作結算：",value=f"• 你前往加工所協助安排進出貨，科技<:INC:1375507210448277595>{amount}、文化<:INC:1375507210448277595>{amountt}。",inline=False)
                    factoryembed.set_author(name="加工所特殊事件")
                    # choice1
                    amount_c1 = resource_mag(user_id,'INT') * 8
                    factoryclose1 = discord.Embed(title="監守自盜",description="➤你未直接審問嫌犯，而是調閱貨物流通記錄，並暗中託人調查交易紀錄。最終查出失竊物品流入黑市，還發現系統漏洞，間接推動加工所強化內部資訊系統。",color=discord.Color.green())
                    factoryclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    factoryclose1.add_field(name="❖ 事件結果：",value=f"• 科技<:INC:1375507210448277595>{amount_c1}",inline=False)
                    factoryclose1.set_author(name="加工所特殊事件-結算")
                    # choice2
                    amount_c2 = resource_mag(user_id,'STR') * 7
                    factoryclose2 = discord.Embed(title="監守自盜",description="➤你請軍方協助，對加工所展開突襲式搜查，短時間內控制全場並扣押可疑人物。雖然過程驚動不少無辜員工，但也確實查出多人串通、密謀販售機密零件至黑市，並順勢揪出幾名潛伏的敵國線人。",color=discord.Color.green())
                    factoryclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    factoryclose2.add_field(name="❖ 事件結果：",value=f"• 軍事<:INC:1375507210448277595>{amount_c2}",inline=False)
                    factoryclose2.set_author(name="加工所特殊事件-結算")
                    return([factoryembed,receptionclose1,'TEC_rs',amount_c1,factoryclose2,'MIL_rs',amount_c2])
        case 'Museum':
            match event:
                case 'event1':
                    museumembed = discord.Embed(title="翻譯團隊",description="➤負責人向你提議建置一個翻譯團隊常駐於博物院，讓他們翻譯各領域的重要典籍。對此你表示⋯⋯",color=discord.Color.purple())
                    museumembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    museumembed.add_field(name="▼ 請選擇：",value="•（１）重質不重量，追求翻譯的精準度，務必事事考究\n•（２）時間寶貴，追求翻譯的廣度與總量",inline=False)
                    museumembed.add_field(name="❖ 工作結算：",value=f"• 你前往博物院協助進行導覽，文化<:INC:1375507210448277595>{amount}、軍事<:INC:1375507210448277595>{amountt}。",inline=False)
                    museumembed.set_author(name="博物院特殊事件")
                    # choice1
                    amount_c1 = resource_mag(user_id,'CHR') * random.randint(15,20)
                    museumclose1 = discord.Embed(title="翻譯團隊",description="➤你強調品質為先，堅持審慎考據與逐句推敲。翻譯團隊因此與多位學者密切合作，確保文本忠實原意，為我國文化傳承奠定基石。",color=discord.Color.purple())
                    museumclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    museumclose1.add_field(name="❖ 事件結果：",value=f"• 文化<:INC:1375507210448277595>{amount_c1}",inline=False)
                    museumclose1.set_author(name="博物院特殊事件-結算")
                    # choice2
                    amount_c2 = resource_mag(user_id,'DOM') * 12
                    museumclose2 = discord.Embed(title="翻譯團隊",description="➤你主張快速傳播為先，翻譯團隊因此聚焦效率、拓展數量，雖偶有偏誤，卻成功滿足市場需求，各學院書局皆迅速上架，知識出版業為之一振。",color=discord.Color.purple())
                    museumclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    museumclose2.add_field(name="❖ 事件結果：",value=f"• 商業<:INC:1375507210448277595>{amount_c2}",inline=False)
                    museumclose2.set_author(name="博物院特殊事件-結算")
                    return([museumembed,museumclose1,'CUL_rs',amount_c1,museumclose2,'BUS_rs',amount_c2])
                case 'event2':
                    museumembed = discord.Embed(title="博物院導覽",description="➤博物院落成以來你總在此流連忘返，負責人熱情邀請你擔任導覽解說員，並讓你自行選擇感興趣的展。你決定選擇⋯⋯",color=discord.Color.purple())
                    museumembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    museummbed.add_field(name="▼ 請選擇：",value="•（１）《舞文弄墨──書畫名家展》\n•（２）《戰地驚雷──火藥技術展》",inline=False)
                    museumembed.add_field(name="❖ 工作結算：",value=f"•你前往博物院協助進行導覽，文化<:INC:1375507210448277595>{amount}、軍事<:INC:1375507210448277595>{amountt}。",inline=False)
                    museumembed.set_author(name="博物院特殊事件")
                    # choice1
                    amount_c1 = resource_mag(user_id,'CHR') * random.randint(6,10)
                    museumclose1 = discord.Embed(title="博物院導覽",description="➤你精選歷代傳世名作，細述字裡行間的筆鋒與情感，並將其與當代藝術脈絡相互對照，引發觀眾對文化傳承的深刻共鳴。",color=discord.Color.purple())
                    museumclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    museumclose1.add_field(name="❖ 事件結果：",value=f"• 文化<:INC:1375507210448277595>{amount_c1}",inline=False)
                    museumclose1.set_author(name="博物院特殊事件-結算")
                    # choice2
                    amount_c2 = resource_mag(user_id,'STR') * random.randint(6,8)
                    museumclose2 = discord.Embed(title="博物院導覽",description="➤你從古代火藥配方講到現代應用，結合圖像與實驗模擬，向觀眾清晰解釋能量轉化與火藥演進史，引來學者與軍事技術單位高度關注。",color=discord.Color.purple())
                    museumclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    museumclose2.add_field(name="❖ 事件結果：",value=f"• 軍事<:INC:1375507210448277595>{amount_c2}",inline=False)
                    museumclose2.set_author(name="博物院特殊事件-結算")
                    return([museumembed,museumclose1,'CUL_rs',amount_c1,museumclose2,'MIL_rs',amount_c2])
                case 'event3':
                    museumembed = discord.Embed(title="演講內容",description="➤負責人計畫在博物院舉辦大型演講，邀請你擔任主講人，他提供兩個方向供你參考，你決定選⋯⋯",color=discord.Color.purple())
                    museumembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    museumembed.add_field(name="▼ 請選擇：",value="•（１）《論領導者的人格魅力》\n•（２）《商場如戰場》",inline=False)
                    museumembed.add_field(name="❖ 工作結算：",value=f"•你前往博物院協助進行導覽，文化<:INC:1375507210448277595>{amount}、軍事<:INC:1375507210448277595>{amountt}。",inline=False)
                    museumembed.set_author(name="博物院特殊事件")
                    # choice1
                    amount_c1 = resource_mag(user_id,'CHR') * random.randint(8,28)
                    museumclose1 = discord.Embed(title="演講內容",description="➤你以歷史與現代人物為例，剖析魅力型領導者如何凝聚人心、化解衝突。講座過程幽默生動、寓教於樂，引發現場熱烈討論，也讓文化部表示願意將內容編輯成教育教材。",color=discord.Color.purple())
                    museumclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    museumclose1.add_field(name="❖ 事件結果：",value=f"• 文化<:INC:1375507210448277595>{amount_c1}",inline=False)
                    museumclose1.set_author(name="博物院特殊事件-結算")
                    # choice2
                    amount_c2 = resource_mag(user_id,'DOM') * 9
                    museumclose2 = discord.Embed(title="演講內容",description="➤你以幾場知名併購案為例，揭示背後的談判技巧與權力博弈，並邀請業界人士分享決策現場的瞬息萬變。講座結束後，引起企業界熱烈迴響，相關分析更被多國商學院引用。",color=discord.Color.purple())
                    museumclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    museumclose2.add_field(name="❖ 事件結果：",value=f"• 商業<:INC:1375507210448277595>{amount_c2}",inline=False)
                    museumclose2.set_author(name="博物院特殊事件-結算")
                    return([museumembed,museumclose1,'CUL_rs',amount_c1,museumclose2,'BUS_rs',amount_c2])                   
                case 'event4':
                    museumembed = discord.Embed(title="政治理想",description="➤博物院的負責人非常有學識，你與他相見恨晚。這天他邀你小酌，暢聊政治議題與理想。席間他鄭重請教你認為我國的未來應當如何，你回答⋯⋯",color=discord.Color.purple())
                    museumembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    museumembed.add_field(name="▼ 請選擇：",value="•（１）以軍事立國，成為天下共主，使諸國朝拜\n•（２）以智慧周旋於諸國間，不參與爭鬥而休養生息",inline=False)
                    museumembed.add_field(name="❖ 工作結算：",value=f"•你前往博物院協助進行導覽，文化<:INC:1375507210448277595>{amount}、軍事<:INC:1375507210448277595>{amountt}。",inline=False)
                    museumembed.set_author(name="博物院特殊事件")
                    # choice1
                    amount_c1 = resource_mag(user_id,'STR') * 6
                    museumclose1 = discord.Embed(title="政治理想",description="➤你認為亂世無道，唯有武力才能換得和平。我國若能立於兵鋒之巔，自可震懾四方，從此步入強國之路。",color=discord.Color.purple())
                    museumclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    museumclose1.add_field(name="❖ 事件結果：",value=f"• 軍事<:INC:1375507210448277595>{amount_c1}",inline=False)
                    museumclose1.set_author(name="博物院特殊事件-結算")
                    # choice2
                    amount_c2 = resource_mag(user_id,'INT') * 10
                    museumclose2 = discord.Embed(title="政治理想",description="➤你主張在強權對峙時另闢蹊徑，避開鋒芒、以智制勝。科技與策略，才是維繫國運與長治久安的關鍵。",color=discord.Color.purple())
                    museumclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    museumclose2.add_field(name="❖ 事件結果：",value=f"• 科技<:INC:1375507210448277595>{amount_c2}",inline=False)
                    museumclose2.set_author(name="博物院特殊事件-結算")
                    return([museumembed,museumclose1,'MIL_rs',amount_c1,museumclose2,'TEC_rs',amount_c2])
                case 'event5':
                    museumembed = discord.Embed(title="新書推薦",description="➤博物院近期拓展出版業務，負責人希望你擔任兩本熱門新書的推薦人，你慎重考慮後，決定選擇⋯⋯",color=discord.Color.purple())
                    museumembed.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    museumembed.add_field(name="▼ 請選擇：",value="•（１）《群眾與舞台：領袖魅力的美學解構》\n•（２）《未來之形：元能科技與文明進程》",inline=False)
                    museumembed.add_field(name="❖ 工作結算：",value=f"•你前往博物院協助進行導覽，文化<:INC:1375507210448277595>{amount}、軍事<:INC:1375507210448277595>{amountt}。",inline=False)
                    museumembed.set_author(name="博物院特殊事件")
                    # choice1
                    amount_c1 = resource_mag(user_id,'CHR') * 8
                    museumclose1 = discord.Embed(title="新書推薦",description="➤你讚賞作者從戲劇理論與歷史人物出發，深入剖析領袖如何透過姿態、語調與敘事技巧贏得大眾信任。你認為這本書有助推動文化與教育對魅力表達的理解與研究，因此欣然推薦。",color=discord.Color.purple())
                    museumclose1.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    museumclose1.add_field(name="❖ 事件結果：",value=f"• 文化<:INC:1375507210448277595>{amount_c1}",inline=False)
                    museumclose1.set_author(name="博物院特殊事件-結算")
                    # choice2
                    amount_c2 = resource_mag(user_id,'INT') * 5
                    museumclose2 = discord.Embed(title="新書推薦",description="➤你認為這本書詳實梳理元能科技的發展脈絡，並深入探討其在醫療、交通與通訊領域的應用。你指出，這類著作有助提升全民的科技素養，甚至影響後續政策與教育方向，因此決定親自背書。",color=discord.Color.purple())
                    museumclose2.add_field(name=" ",value="----------------------------------------------------",inline=False)
                    museumclose2.add_field(name="❖ 事件結果：",value=f"• 科技<:INC:1375507210448277595>{amount_c2}",inline=False)
                    museumclose2.set_author(name="博物院特殊事件-結算")
                    return([museumembed,receptionclose1,'CUL_rs',amount_c1,museumclose2,'TEC_rs',amount_c2])