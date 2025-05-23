import discord, random, pytz, json, os, math
from discord.ext import commands
from discord import app_commands
from datetime import datetime, timezone

def load_data():
    DATA_FILE = "PS.json"
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_data(data):
    DATA_FILE = "PS.json"
    with open("PS.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def init_user(user_id, name, user_name):
    curTinTW = get_date()
    return {
        "kingdom": "",
        "name" : user_name,
        "STR": 0,
        "DOM": 0,
        "INT": 0,
        "CHR": 0,
        "MIL": 1,
        "BUS": 1,
        "TEC": 1,
        "CUL": 1,
        "stamina": 3,
        "hunger": 20,
        "MIL_rs": 0,
        "BUS_rs": 0,
        "TEC_rs": 0,
        "CUL_rs": 0,
        "last_login": str(curTinTW),
        "last_feed": str(curTinTW),
        "vacation": False
    }

def init_state(userid):
    data = load_data() 
    user_id = str(userid)
    cuts = sorted(random.sample(range(1, 16), 3))
    data[user_id]["STR"] = cuts[0]
    data[user_id]["DOM"] = cuts[1] - cuts[0]
    data[user_id]["INT"] = cuts[2] - cuts[1]
    data[user_id]["CHR"] = 16 - cuts[2]
    save_data(data)

def kingdom_info(userid,kingdom):
    data = load_data() 
    user_id = str(userid)
    data[user_id]["kingdom"] = kingdom
    save_data(data)

def Work_update(userid, mount: int):
    data = load_data() 
    user_id = str(userid)
    todate = get_date()
    if data[user_id]["stamina"] != 0:
        data[user_id][state_name] += mount
        data[user_id]["stamina"] -= 1
        save_data(data)

def display_warehouse(userid):
    data = load_data() 
    user = data[str(userid)]
    displaypersonalstate = discord.Embed(title=f"倉庫")
    displaypersonalstate.add_field(name=f":dagger: 軍事  LV{(user['MIL'])} :     {(user['MIL_rs'])}", value="",inline=False)
    displaypersonalstate.add_field(name=f":scales: 商業  LV{(user['BUS'])} :     {(user['BUS_rs'])}", value="",inline=False)
    displaypersonalstate.add_field(name=f":brain: 科技  LV{(user['TEC'])} :     {(user['TEC_rs'])}", value="",inline=False)
    displaypersonalstate.add_field(name=f":heart: 文化  LV{(user['CUL'])} :     {(user['CUL_rs'])}", value="",inline=False)
    displaypersonalstate.set_author(name=f"{user['name']}")
    return displaypersonalstate

def display_state(userid):
    data = load_data() 
    user = data[str(userid)]
    hunger = ""
    for i in range(user['hunger']):
        hunger += " ■"
    hunger += "\n▔ ▔ ▔ ▔ ▔ ▔ ▔ ▔ ▔ ▔ ▔ ▔ ▔ ▔ ▔ ▔ ▔ ▔ ▔ ▔\n----------------------------------------------------"
    displaypersonalstate = discord.Embed(title=f"{user['name']}", color=discord.Color.green())
    displaypersonalstate.add_field(name="飽食度：", value=hunger,inline=False)
    displaypersonalstate.add_field(name=f":dagger: 武力 : {rank_check(user['STR'])}", value="",inline=False)
    displaypersonalstate.add_field(name=f":scales: 內政 : {rank_check(user['DOM'])}", value="",inline=False)
    displaypersonalstate.add_field(name=f":brain: 智力 : {rank_check(user['INT'])}", value="",inline=False)
    displaypersonalstate.add_field(name=f":heart: 魅力 : {rank_check(user['CHR'])}", value="",inline=False)
    displaypersonalstate.add_field(name=f":wheelchair: 行動力 : {user['stamina']}", value="",inline=False)
    displaypersonalstate.set_author(name=f"{user['kingdom']}")
    return displaypersonalstate

def daily_check(userid):
    data = load_data() 
    user_id = str(userid)
    todate = get_date()
    if data[user_id]["last_login"] == todate:
        if data[user_id]["stamina"] == 0:
            return(1)
        else:
            return(0)
    else:
        data[user_id]["stamina"] = 3
        last_login = datetime.strptime(data[user_id]["last_login"], "%Y%m%d")
        last_feed = datetime.strptime(data[user_id]["last_feed"], "%Y%m%d")
        now = datetime.strptime(todate, "%Y%m%d")
        delta = now - last_feed
        days = delta.days
        if days >= 10:
            return(4)
        hunger = 0
        for i in range(days):
            if i < 4: 
                hunger += 1 
            elif i >= 4 and i < 8:
                hunger += 2
            elif i >= 8 and i < 11:
                hunger += 3  
        data[user_id]["hunger"] -= hunger
        if data[user_id]["last_login"] != data[user_id]["last_feed"]:
            prehdelta = last_login - last_feed
            predays = prehdelta.days
            prehunger = 0
            for i in range(predays):
                if i < 4: 
                    prehunger += 1 
                elif i >= 4 and i < 8:
                    prehunger += 2
                elif i >= 8 and i < 11:
                    prehunger += 3  
            data[user_id]["hunger"] += prehunger
        data[user_id]["last_login"] = todate 
    save_data(data)
    return(2)
    
# 0 checked before
# 1 checked before, no stamina
# 2 checked, alive
# 4 dead

def feed(userid,meal):
    data = load_data() 
    user_id = str(userid)
    todate = get_date() 
    if meal == 1 and data[user_id]["stamina"] > 0:
        data[user_id]["hunger"] += 1
        data[user_id]["stamina"] -= 1 
    elif meal == 2 and data[user_id]["stamina"] > 1:
        data[user_id]["hunger"] += 3
        data[user_id]["stamina"] -= 2
    elif meal == 3 and data[user_id]["stamina"] == 3:
        data[user_id]["hunger"] += 6
        data[user_id]["stamina"] -= 3
    else:
        return(1)
    data[user_id]["last_feed"] = todate
    save_data(data)

def event_lottery(userid,A,B,C,D,types):
    data = load_data() 
    user_id = str(userid)
    prob = 0 
    if types == 1:
        event_weights = {
            "event1": {A: 0, B: 0},
            "event2": {B: 0, A: 0},
            "event3": {A: 0, C: 0},
            "event4": {D: 0, C: 0},
            "event5": {A: 0},
        }
    elif types == 2:
        event_weights = {
            "event1": {C: 0, B: 0},
            "event2": {A: 0, B: 0},
            "event3": {C: 0, A: 0},
            "event4": {A: 0, D: 0},
            "event5": {A: 0},
        }
    elif types == 3:
        event_weights = {
            "event1": {B: 0, A: 0},
            "event2": {A: 0, C: 0},
            "event3": {A: 0, B: 0},
            "event4": {D: 0, C: 0},
            "event5": {A: 0, D: 0},
        }
    elif types == 4:
        event_weights = {
            "event1": {B: 0, A: 0},
            "event2": {B: 0, C: 0},
            "event3": {D: 0, A: 0},
            "event4": {D: 0, C: 0},
            "event5": {A: 0, C: 0},
        }
    for resource in [A, B, C, D]:      
        if data[user_id][resource] == 1:
            for event in event_weights:
                if resource in event_weights[event]:
                    event_weights[event][resource] = 0.3
            prob += 0.3
        elif data[user_id][resource] == 2:
            for event in event_weights:
                if resource in event_weights[event]:
                    event_weights[event][resource] = 0.4
            prob += 0.4
        elif data[user_id][resource] == 3:
            for event in event_weights:
                if resource in event_weights[event]:
                    event_weights[event][resource] = 0.6
            prob += 0.6
        elif data[user_id][resource] == 4:
            for event in event_weights:
                if resource in event_weights[event]:
                    event_weights[event][resource] = 0.8
            prob += 0.8
        elif data[user_id][resource] == 5:
            for event in event_weights: 
                if resource in event_weights[event]:
                    event_weights[event1][resource] = 1
            prob += 1
    if random.random() > prob/4:
        return(0)
    else:
        event_names = list(event_weights.keys())
        scores = [sum(event_weights["event1"].values()),sum(event_weights["event2"].values()),sum(event_weights["event3"].values()),sum(event_weights["event4"].values()),sum(event_weights["event5"].values()) * 2]
        exp_scores = [math.exp(s) for s in scores]
        total = sum(exp_scores)
        probs = [s / total for s in exp_scores]
        r = random.random()
        cumulative = 0
        for event, prob in zip(event_names, probs):
            cumulative += prob
            if r <= cumulative:
                return list(event_weights[event].keys())
        return None

def resource_mag(userid,state):
    data = load_data() 
    user_id = str(userid)
    if data[user_id][state] < 3:
            return(1)
    elif 3 <= data[user_id][state] < 10:
            return(2)
    elif 10 <= data[user_id][state] < 23:
            return(3)
    elif 23 <= data[user_id][state] < 40:
            return(5)
    elif 40 <= data[user_id][state] < 63:
            return(7)
    elif 63 <= data[user_id][state] < 92:
            return(10)
    elif 92 <= data[user_id][state]:
            return(14)

def gain_state(userid,state,amount):
    data = load_data() 
    user_id = str(userid)
    if state in ('MIL','BUS','TEC','CUL'):
        if state == 'MIL':
            data[user_id]['STR'] += amount
        elif state == 'BUS':
            data[user_id]['DOM'] += amount
        elif state == 'TEC':
            data[user_id]['INT'] += amount
        elif state == 'CUL':
            data[user_id]['CHR'] += amount
    else:
        data[user_id][state] += amount
    save_data(data)

def gain_resource(userid,resource,amount):
    data = load_data() 
    user_id = str(userid)
    data[user_id][resource] += amount
    save_data(data)

def get_date():
    TWtz = pytz.timezone("Asia/Taipei")
    timeInTW = datetime.now(TWtz)
    curTinTW = timeInTW.strftime("%Y%m%d")
    return(curTinTW)

def resource_levelup(userid,resource):
    data = load_data() 
    user_id = str(userid) 
    resource_rs = resource + "_rs"
    if data[user_id][resource] == 1 and data[user_id][resource_rs] >= 50:
        data[user_id][resource_rs] -= 50
        data[user_id][resource] += 1
    elif data[user_id][resource] == 2 and data[user_id][resource_rs] >= 100:
        data[user_id][resource_rs] -= 100
        data[user_id][resource] += 1
    elif data[user_id][resource] == 3 and data[user_id][resource_rs] >= 200:
        data[user_id][resource_rs] -= 200
        data[user_id][resource] += 1
    elif data[user_id][resource] == 4 and data[user_id][resource_rs] >= 400:
        data[user_id][resource_rs] -= 400
        data[user_id][resource] += 1
    elif data[user_id][resource] == 5:
        return("等級封頂")
    else:
        return("資源不夠")
    save_data(data)
    return_text = "升級"
    if resource == "MIL":
        return_text += "軍事"
    elif resource == "BUS":
        return_text += "商業"
    elif resource == "TEC":
        return_text += "科技"
    elif resource == "CUL":
        return_text += "文化"
    return_text += "至 LV：" + str(data[user_id][resource])
    return(return_text)

def rank_check(number):
    if number < 3:
        return("F")
    elif 3 <= number < 10:
        return("E")
    elif 10 <= number < 23:
        return("D")
    elif 23 <= number < 40:
        return("C")
    elif 40 <= number < 63:
        return("B")
    elif 63 <= number< 92:
        return("A")
    elif 92 <= number:
        return("S")


def rename(userid, user_name):
    data = load_data() 
    user_id = str(userid)
    data[user_id]["name"] = user_name
    save_data(data)

def erase(userid):
    data = load_data() 
    user_id = str(userid)
    if user_id in data:
        del data[user_id]
        save_data(data)

