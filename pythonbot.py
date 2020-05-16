import random
import discord
import datetime
import calendar
import time
import operator
import config
import json
import threading
import asyncio
from decimal import Decimal
from discord.ext import commands
from discord.utils import get
bot = commands.Bot(command_prefix="=")
channel = "abc"

# PUSH LIVE - Change channel to (Test) 518199222340812801 or (Live) 701135988260339852. Change ADMIN/GMAdmin. Change filenames and folder.
# TODO: add dice roll %age to stats

# ON SERVER
# ps -ef | grep 'gmc'
# kill <pid>
# nohup python3 //root/gm1c/pythonbot.py &
# sed -i 's+E:/Dropbox/Discord+/root+g' pythonbot.py

categories=["Collection Power [#]", \
"Strongest Team Power [#]", \
"Highest Power Character", \
"Lowest Power Character", \
"Gold + Red Stars [Single Character]", \
"10+ Gold & Red Stars [Total Characters]", \
"Alliance MVP Ranking [#]", \
"War MVPs [#]", \
"Characters Unlocked [#]", \
"Characters with Multiple T4s", \
"Most 6664+", \
"Characters at 7 Stars [#]", \
"Characters at 6+ Stars", \
"Characters at 5+ Stars", \
"Characters at 4+ Stars", \
"Characters at 100K+", \
"Characters at 70K+", \
"Characters at 60K+", \
"Characters at 50K+", \
"Characters at 40K+", \
"Characters at 30K+", \
"Characters at 20K+", \
"Characters at 10K+", \
"All Time Arena Rank [#]", \
"Current Arena Rank [#]", \
"Gear 14 Characters", \
"Gear 13+ Characters", \
"Gear 12+ Characters", \
"Gear 11+ Characters", \
"Character Rank Ups", \
"Strongest Power Minion", \
"Strongest 'X' Team", \
"Strongest 'X' Team", \
"Strongest 'X' Team", \
"Strongest 'X' Team", \
"Strongest 'X' Team", \
"Strongest 'X' Team", \
"Strongest 'X' Team", \
"Strongest 'X' Team", \
"Strongest 'X' Team", \
"Strongest 'X' Team", \
"Level 75 Characters", \
"Ultimus Shards", \
"Highest Power non-6664", \
"Highest Power 0 T4s", \
"Gear 1 Characters", \
"Current Blitz Score", \
"Last Ultimus Raid Ranking", \
"Last Event Raid Ranking", \
"Last/Current War Battles [#]", \
"Last/Current War Damage Done [#]", \
"Strongest War Defence [#]", \
"Arena Battles", \
"Days Logged In", \
"Level 1 Characters", \
"Discord Leaderboard [#]", \
"Blitz Wins [#]", \
"Random Character Power Level [Level]", \
"Random Character Shards", \
"Raid Credits Hoarder", \
"War Credits Hoarder", \
"Blitz Credits Hoarder", \
"Arena Credits Hoader", \
"ABC Hoarder", \
"T4s Hoarder", \
"T3s Hoarder", \
"T2s Hoarder", \
"Power Core Hoarder", \
"Gold Hoarder", \
"10 Avatar Challenge [#]", \
"DD1 Timed", \
"DD2 Timed", \
"Lowest Team Power", \
"Un-opened Orbs", \
"Most Campaign Energy", \
"World Warrior Placement [#]", \
"Strongest Random Team", \
"Strongest Random Team", \
"Strongest Random Team", \
"Strongest Random Team", \
"Strongest Random Team", \
"Strongest Random Team", \
"Strongest Random Team", \
"Strongest Random Team", \
"Strongest Random Team", \
"Strongest Random Team", \
"Strongest Random Team", \
"Strongest Random Team", \
"Strongest Random Team", \
"Strongest Random Team", \
"Strongest Random Team", \
"Random Character Power Level [Character]", \
"Random Character Power Level [Character]", \
"Random Character Power Level [Character]", \
"Random Character Power Level [Character]", \
"Random Character Power Level [Character]", \
"Random Character Power Level [Level]", \
"Random Character Power Level [Level]", \
"Random Character Power Level [Level]", \
"Random Character Power Level [Level]", \
"Random Character Power Level [Level]", \
"Random Character Power Level [Level]", \
"Random Character Power Level [Level]", \
"Random Character Power Level [Level]", \
"Random Character Power Level [Level]", \
"Random Character Shards", \
"Random Character Shards", \
"Random Character Shards", \
"Champions Choice", \
"Challengers Choice"]
traits=["Inhuman", "AIM", "Hydra", "Shield", "Defenders (MM or Pun)", "Spiderverse (Non S6)", "GotG", "Avengers", "Wakandans", "X-Men", "Brotherhood", \
"S6", "Kree", "Hand", "Merc", "Military", "Blaster", "Bio", "Brawler", "City", "Controller", "Cosmic", "Global", "Martial Artist", "Minion", "Mutant", \
"Mystic", "Protector", "Skill", "Support", "Tech", "Hero", "Villain"]
characters=["AIM Assaulter", "AIM Infector", "AIM Monstrosity", "AIM Researcher", "AIM Security", "Agent Coulson", "America Chavez", "Ant-Man", "Blackbolt", "Black Panther", "Black Widow", "Blob", "Bullseye", "Cable", \
            "Captain America", "Captain Marvel", "Carnage", "Colossus", "Crossbones", "Crystal", "Cyclops", "Daredevil", "Deadpool", "Doctor Strange", "Drax", "Elektra", "Elsa", "Falcon", "Gamora", "Ghost Rider", "Graviton", "Green Goblin", \
            "Groot", "Hand Archer", "Hand Assassin", "Hand Blademaster", "Hand Sentry", "Hand Sorceress", "Hawkeye", "Hulk", "Human Torch", "Hydra Armored Guard", "Hydra Grenadier", \
            "Hydra Rifle Trooper", "Hydra Scientist", "Hydra Sniper", "Invisible Woman", "Iron Fist", "Iron Man", "Jessica Jones", "Juggernaut", "Karnak", "Killmonger", "Kingpin", "Korath", \
            "Kree Cyborg", "Kree Noble", "Kree Oracle", "Kree Reaper", "Kree Royal Guard", "Loki", "Luke Cage", "M'Baku", "Magneto", "Mantis", "Merc Lieutenant", \
            "Merc Riot Guard", "Merc Sniper", "Merc Soldier", "Minn-Erva", "Mister Fantasic", "Mister Sinister", "Mordo", "Ms. Marvel", "Mysterio", "Mystique", "Namor", "Nebula", "Nick Fury", "Night Nurse", "Nobu", "Okoye", \
            "Phoenix", "Proxima", "Psylocke", "Punisher", "Pyro", "Quake", "Ravager Boomer", "Ravager Bruiser", "Ravager Stitcher", "Red Skull", "Rescue", "Rhino", "Rocket", "Ronan", "SHIELD Assault", \
            "SHIELD Medic", "SHIELD Operative", "SHIELD Security", "SHIELD Trooper", "Sabretooth", "Scarlet Witch", "Scientist Supreme", "Shocker", "Shuri", "Spider-Man", "Spider-Man (Miles)", "Spider-Man (Symbiote)", \
            "Star-Lord", "Storm", "Stryfe", "Thanos", "The Thing", "Thor", "Toad", "Ultimus", "Ultron", "Venom", "Vision", "Vulture", "War-Machine", "Wasp", "Winter Soldier", "Wolverine", "Yo-Yo", "Yondu"]
gifs=["https://media.tenor.com/images/d3590584080460e138683333e7a93caf/tenor.gif", \
    "https://media.tenor.com/images/9e03f71d67b4efcbd7d2929f1ea305ca/tenor.gif", \
    "https://media.tenor.com/images/3a50e48fc33aa6ca296aa36259db4631/tenor.gif", \
    "https://media.tenor.com/images/17361f59edf369c1852d90c1adf3d4e1/tenor.gif", \
    "https://media.tenor.com/images/e61606c524602b99d660851c43ff0599/tenor.gif", \
    "https://media.tenor.com/images/8e5cee84715edfa568fbbaf985ad9e49/tenor.gif", \
    "https://media.tenor.com/images/45ef8ba8bd9afcc46eb2145cb0a56476/tenor.gif"]
#idMap = {<@344661859275898882>,Artikhopper,<@215981471842697217>,Calmskitzo,<@223982068131037185>,Candidme,<@273279044454187009>,ColbysGotMoore,<@479174652376252416>,Cookie_Monster86,<@473691876680269824>,FatMichael,<@689889209665978396>,Fatshady,<@483755276873498644>,GeauxRagnar,<@182901488488677376>,heet3r,<@120763659998724097>,Hypo,<@465324594597986304>,KyReezy,<@580641750582951960>,mayureshr1,<@468054768502439947>,OzDH,<@442226315291131907>,Peter G,<@458334361083707414>,RandySavage,<@255033419245813760>,ScottF,<@266447975146848257>,ShadowsRisen,<@353732092875505666>,Shev1,<@447683410014633984>,someone,<@568471080742682626>,Talon,<@473822789854560266>,TrickJames,<@330148338890702849>,Tyfighter,<@451373900069076993>,Wagon King}

@bot.event
async def on_ready():
    # Load Champ
    currentChampID = load_single_line_file("E:/Dropbox/Discord/gmc/currentchamp.txt")
    # Startup
    log('Startup : Logged in as ' + bot.user.name)
    global channel
    channel = bot.get_channel(701135988260339852) # channel ID goes here

@bot.command(pass_context=True)
async def optout(ctx):
    log("Opt Out " + str(ctx.message.author))
    opt_out_id = "<@" + str(ctx.message.author.id) + ">\n"
    ids = load_ids()
    if opt_out_id in ids:
        ids.remove(opt_out_id)
        f=open("E:/Dropbox/Discord/gmc/idlist.txt", "w")
        for id in ids:
            f.write(id)
        f.close()
        await channel.send("You have opted out " + opt_out_id + "Use *=optin* to rejoin")
    else:
        await channel.send("You are already not in the challenge " + opt_out_id + "Use *=optin* to rejoin")

@bot.command(pass_context=True)
async def optin(ctx):
    log("Opt In " + str(ctx.message.author))
    opt_in_id = "<@" + str(ctx.message.author.id) + ">\n"
    ids = load_ids()
    if opt_in_id not in ids:
        f=open("E:/Dropbox/Discord/gmc/idlist.txt", "a")
        f.write("\n" + opt_in_id)
        f.close()
        await channel.send("You have opted in " + opt_in_id)
    else:
        await channel.send("You are already in the challenge " + opt_in_id + "Use *=optout* to remove yourself")

@bot.command(pass_context = True)
async def h(ctx):
    log("Help " + str(ctx.message.author))
    await channel.send("**h** : *Print Commands Help*\n\
**printcategories** : *Prints all the Categories*\n\
**champ** : *Print the Current Champion*\n\
**myinfo** : *Prints all stats about the sender including challenges and dice rolls*\n\
**claimchallenge** : *Generate New Challenge for sender of the message*\n\
**diceroll** : *Roll the Dice to try and win a challenge*\n\
**category** : *Generate New Random Category*\n\
**gethistory** : *Print the history of the Championship*\n\
**stats** : *Show the top 5 in each stat category*\n\
**fullstats** : *Show a chart of everyones stats in each category*\n\
**category** : *Generate New Random Category*\n\n\
**Following are GMAdmin only**\n\
**defence ChampID ChallengerID** : *Logs a Successful Defence*\n\
**newchamp ID** : *Sets New Champion*\n\
**newchallenger** : *Generate New Challenger & Category*\n\
**awardchallenge ID**: *Award a challenge to given ID*\n\
**awarddiceroll ID**: *Award a diceroll to given ID*\n\
**awardult ID1 ID2 ID3 ID4 ID5 ID6**: *Award correct rewards to the top 6 in the raid*\n\
**awardwarwin**: *Award a diceroll to everyone for winning a war*\n\
**awardwarmvp ID**: *Award 2 dicerolls to the War MVP*\n\
**showinfo** : *Show all the people with available challenges*")

@bot.command(pass_context = True)
async def fullstats(ctx):
    log("Full Stats - " + str(ctx.message.author))
    reigns = {}
    defences = {}
    randoms = {}
    challenges = {}
    dicerolls = {}
    dicewins = {}
    f=open("E:/Dropbox/Discord/gmc/stats.txt", "r")
    for line in f:
        split = line.split(',')
        split[6] = split[6].split('\n')[0]
        reigns[split[0]] = int(split[1])
        defences[split[0]] = int(split[2])
        randoms[split[0]] = int(split[3])
        challenges[split[0]] = int(split[4])
        dicerolls[split[0]] = int(split[5])
        dicewins[split[0]] = int(split[6])
    f.close()
    output = "```R = Reigns | D = Defences | RS = Randomly Selected | C = Challenges | DR = Dice Rolls\n"

    for user in reigns:
        spacing = (25 - len(get_member(ctx, user))) * ' '
        output += get_member(ctx, user) + spacing + "\tR:" + str(reigns[user]) + "\tD:" + str(defences[user]) + "\tRS:" + str(randoms[user]) + "\tC:" + str(challenges[user]) + " \tDR:" + str(dicewins[user]) + "/" + str(dicerolls[user]) + "\n"

    await channel.send(output + "```")

@bot.command(pass_context = True)
async def stats(ctx, entries=5):
    log("Stats " + str(ctx.message.author))
    reigns = {}
    defences = {}
    randoms = {}
    challenges = {}
    dicerolls = {}
    dicewins = {}
    f=open("E:/Dropbox/Discord/gmc/stats.txt", "r")
    for line in f:
        split = line.split(',')
        split[6] = split[6].split('\n')[0]
        reigns[split[0]] = int(split[1])
        defences[split[0]] = int(split[2])
        randoms[split[0]] = int(split[3])
        challenges[split[0]] = int(split[4])
        dicerolls[split[0]] = int(split[5])
        dicewins[split[0]] = int(split[6])
    f.close()

    reigns = sorted(reigns.items(), key=operator.itemgetter(1), reverse=True)
    defences = sorted(defences.items(), key=operator.itemgetter(1), reverse=True)
    randoms = sorted(randoms.items(), key=operator.itemgetter(1), reverse=True)
    challenges = sorted(challenges.items(), key=operator.itemgetter(1), reverse=True)
    dicerolls = sorted(dicerolls.items(), key=operator.itemgetter(1), reverse=True)
    dicewins = sorted(dicewins.items(), key=operator.itemgetter(1), reverse=True)

    await channel.send("**Championship Reigns**")
    output = "```"
    for x in range(entries):
        if x == entries-1:
            output += str(x+1) + ": " + get_member(ctx, reigns[x][0]) + " - " + str(reigns[x][1])
        else:
            output += str(x+1) + ": " + get_member(ctx, reigns[x][0]) + " - " + str(reigns[x][1]) + " | "
    await channel.send(output + "```")
    output = "```"
    await channel.send("**Championship Defences**")
    for x in range(entries):
        if x == entries-1:
            output += str(x+1) + ": " + get_member(ctx, defences[x][0]) + " - " + str(defences[x][1])
        else:
            output += str(x+1) + ": " + get_member(ctx, defences[x][0]) + " - " + str(defences[x][1]) + " | "
    await channel.send(output + "```")
    output = "```"
    await channel.send("**Randomly Selected**")
    for x in range(entries):
        if x == entries-1:
            output += str(x+1) + ": " + get_member(ctx, randoms[x][0]) + " - " + str(randoms[x][1])
        else:
            output += str(x+1) + ": " + get_member(ctx, randoms[x][0]) + " - " + str(randoms[x][1]) + " | "
    await channel.send(output + "```")
    output = "```"
    await channel.send("**Challenges**")
    for x in range(entries):
        if x == entries-1:
            output += str(x+1) + ": " + get_member(ctx, challenges[x][0]) + " - " + str(challenges[x][1])
        else:
            output += str(x+1) + ": " + get_member(ctx, challenges[x][0]) + " - " + str(challenges[x][1]) + " | "
    await channel.send(output + "```")
    output = "```"
    await channel.send("**Dice Rolls**")
    for x in range(entries):
        if x == entries-1:
            output += str(x+1) + ": " + get_member(ctx, dicerolls[x][0]) + " - " + str(dicerolls[x][1])
        else:
            output += str(x+1) + ": " + get_member(ctx, dicerolls[x][0]) + " - " + str(dicerolls[x][1]) + " | "
    await channel.send(output + "```")
    output = "```"
    await channel.send("**Dice Wins**")
    for x in range(entries):
        if x == entries-1:
            output += str(x+1) + ": " + get_member(ctx, dicewins[x][0]) + " - " + str(dicewins[x][1])
        else:
            output += str(x+1) + ": " + get_member(ctx, dicewins[x][0]) + " - " + str(dicewins[x][1]) + " | "
    await channel.send(output + "```")

@bot.command(pass_context = True)
async def gethistory(ctx):
    log("Get History " + str(ctx.message.author))
    f=open("E:/Dropbox/Discord/gmc/champhistory.txt", "r")
    output = ""
    for line in f:
        split = line.split(':')
        if len(split) == 3:
            if len(output) > 1900:
                await channel.send(output)
                output = ""
            output += "*" + split[0] + ":* New Champion! **" + get_member(ctx, split[2].split("\n")[0]) + "**\n"
        else:
            if len(output) > 1900:
                await channel.send(output)
                output = ""
            output += "*" + split[0] + ":* **" + get_member(ctx, split[2]) + "** defeats **" + get_member(ctx, split[3].split("\n")[0]) + "**\n"
    await channel.send(output)

@bot.command(pass_context=True)
async def categorystats(ctx, rows=25):
    log("Category Stats " + str(ctx.message.author))
    cats={}
    output = ""
    counter = 0
    f=open("E:/Dropbox/Discord/gmc/log.txt")
    for a in categories:
        cats[a] = 0
    for b in traits:
        entry = "Strongest 'X' Team".replace('X',b)
        cats[entry] = 0
    cats["PVP!"] = 0

    for line in f:
        for c in cats.keys():
            if c in line:
                cats[c] = cats[c]+1
                break

    cats = sorted(cats.items(), key=lambda x: x[1], reverse=True)

    if rows > 60:
        rows = 60
    for y in cats:
        y = str(y).replace('(','**').replace(')','*').replace("'",'').replace(',','** *:')
        if counter < rows:
            output += y + "\n"
            counter += 1
    await channel.send(output)

@bot.command(pass_context = True)
async def longestreign(ctx):
    log("Longest Reign " + str(ctx.message.author))
    f=open("E:/Dropbox/Discord/gmc/champhistory.txt", "r")
    name = ""
    curname = ""
    longest = 0
    current = 0
    for line in f:
        split = line.split(':')
        if len(split) == 3:
            if current > longest:
                name = curname
                longest = current
            elif current == longest:
                name += " & " + curname
            curname = split[2]
            current = 0
        else:
            current +=1
    await channel.send(name + " **" + str(longest) + " defences**")

@bot.command(pass_context = True)
async def reminder(ctx):
    log("Reminder " + str(ctx.message.author.id))
    if is_active() == 'true':
        champid = get_single_user_from_role(ctx, "Champion of Sakaar").id
        champid = "<@" + str(champid) + ">"
        challid = get_single_user_from_role(ctx, "Active Challenger").id
        challid = "<@" + str(challid) + ">"

        await channel.send(champid + " vs " + challid + " : **"  + get_category() + "**")
    else:
        await channel.send("No Active Challenge")

@bot.command(pass_context = True)
async def myinfo(ctx):
    log("My Info " + str(ctx.message.author))
    tag = "<@" + str(ctx.message.author.id) + ">"
    challenges, diceroll = load_challenges()

    await channel.send(tag + " has **" + str(challenges[tag]) + "** Challenge(s) & **" + str(diceroll[tag]) + "** Dice Roll(s)")

    reigns = {}
    defences = {}
    randoms = {}
    challenges = {}
    dicerolls = {}
    dicewins = {}
    allwins = 0
    allrolls = 0
    f=open("E:/Dropbox/Discord/gmc/stats.txt", "r")
    for line in f:
        split = line.split(',')
        split[6] = split[6].split('\n')[0]
        reigns[split[0]] = int(split[1])
        defences[split[0]] = int(split[2])
        randoms[split[0]] = int(split[3])
        challenges[split[0]] = int(split[4])
        dicerolls[split[0]] = int(split[5])
        dicewins[split[0]] = int(split[6])
        allwins += dicewins[split[0]]
        allrolls += dicerolls[split[0]]
    f.close()
    if dicerolls[tag] == 0:
        percentage = 0
    else:
        percentage = (int(dicewins[tag]) / int(dicerolls[tag])) * 100
    if allrolls == 0:
        alliancepercent = 0
    else:
        alliancepercent = (allwins / allrolls) * 100
    dicerollinfo = "**" + str(dicewins[tag]) + "/" + str(dicerolls[tag]) + " -  " + str(int(percentage)) + "%** *(Alliance Average:" + str(int(alliancepercent)) + "% Win Probability:45.6%)*"
    output = tag + " *statistics:*, Reigns - **" + str(reigns[tag]) + "**, Defences - **" + str(defences[tag]) + "**, Randomly Selected - **" + str(randoms[tag]) \
                            + "**, Challenges - **" + str(challenges[tag]) + "**, Dice Roll Info - " + dicerollinfo
    await channel.send(output)

@bot.command(pass_context = True)
async def createtournament(ctx):
    for x in range(8):
        await channel.send("**Battle " + str(x+1) + "**")
        challenger = idsForTourn[random.randint(0,len(idsForTourn)-1)]
        await channel.send("1: " + challenger)
        idsForTourn.remove(challenger)
        challenger = idsForTourn[random.randint(0,len(idsForTourn)-1)]
        await channel.send("2: " + challenger)
        idsForTourn.remove(challenger)
        challenger = idsForTourn[random.randint(0,len(idsForTourn)-1)]
        await channel.send("3: " + challenger)
        idsForTourn.remove(challenger)
        category = categories[random.randint(0,len(categories)-1)]
        if category == "Random Character Power Level (Level)":
            await channel.send("*Category: " + category + "* **" + str(random.randint(0,50000)) + "**")
        elif category == "Random Character Power Level (Character)":
            await channel.send("*Category: " + category + "* **" + characters[random.randint(0,len(characters)-1)] + "**")
        else:
            await channel.send("*Category: " + category +"*")

@bot.command(pass_context = True)
async def champ(ctx):
    log("Champ " + str(ctx.message.author) + "(Author)")
    # Load Champ
    currentChampID = load_single_line_file("E:/Dropbox/Discord/gmc/currentchamp.txt")
    await channel.send("**Current Champion is **" + str(currentChampID))

@bot.command(pass_context = True)
async def printcategories(ctx):
    log("Print Categories " + str(ctx.message.author))
    string = "```"
    total =  0
    cats={}
    for a in categories:
        total += 1
        if a not in cats:
            if len(string) > 1900:
                await channel.send(string + "```")
                string = "```"
            string += a + "\n"
            if a == "Strongest 'X' Team":
                string += " - ("
                for x in traits:
                    string += x + ", "
                string += ")\n"
            cats[a] = 1
        else:
            cats[a] = cats[a]+1
    string += "PVP!\n"
    await channel.send(string+"```")

    cats = dict(sorted(cats.items(), key=lambda x: x[1], reverse=True))

    x = Decimal((1/total)*90)
    base = round(x,2)
    base_counter = 0
    output = "PVP! - 10%\n"
    for y in cats:
        cats[y] = round(Decimal((cats[y]/total)*90),2)
        if cats[y] != base:
            output += y + " - " + str(cats[y]) + "%\n"
        else:
            base_counter += 1
    output += str(base_counter) + " other categories -  " + str(base) + "% each"
    await channel.send("```" + output + "```")

@bot.command(pass_context = True)
async def category(ctx):
    log_message = "Category " + str(ctx.message.author)
    await run_category(log_message)

@bot.command(pass_context = True)
async def bestof(ctx, i, id1, id2):
    log_message = "Best of " + i + " : " + id1 + " " + id2
    if int(i) < 16:
        await channel.send(id1 + " **vs** " + id2)
        for x in range(int(i)):
            await run_category(log_message)
    else:
        await channel.send("Maximum 15 Categories")

@bot.command(pass_context = True)
async def claimchallenge(ctx):
    tag = "<@" + str(ctx.message.author.id) + ">"
    server = ctx.message.guild

    # Load Champ
    currentChampID = load_single_line_file("E:/Dropbox/Discord/gmc/currentchamp.txt")

    # Load Challenges
    challenges, diceroll = load_challenges()

    if is_active() == 'false':
        # If any challenges...
        if int(challenges[tag]) > 0:
            add_stats(ctx, "challenge", tag)

            # Run challenge
            await channel.send("**CURRENT CHAMP : " + currentChampID + "**")
            await channel.send("**Challenger: **" + tag + " used a challenge.")

            log_message = "Claim Challenge " + str(ctx.message.author)
            await run_category(log_message)

            # Remove challenge
            challenges[tag] = int(challenges[tag])-1
            write_challenges(challenges, diceroll)
            write_to_active('true')
            await change_role(server, tag, 'add', 'Active Challenger')
            await cancel_no_challenge_timer()
            await start_active_challenge_timer(ctx)
        else:
            await channel.send("You currently have 0 challenges :(")
    else:
        await channel.send("Challenge Already Active")

@bot.command(pass_context = True)
async def diceroll(ctx):
    await run_diceroll(ctx)

@bot.command(pass_context = True)
async def alldicerolls(ctx):
    tag = "<@" + str(ctx.message.author.id) + ">"
    challenges, diceroll = load_challenges()
    if int(diceroll[tag]) > 0:
        for x in range(int(diceroll[tag])):
            await run_diceroll(ctx, True)
    else:
        await channel.send("You currently have 0 Dice Rolls :(")

async def run_diceroll(ctx, short=False):
    tag = "<@" + str(ctx.message.author.id) + ">"

    # Load Challenges
    challenges, diceroll = load_challenges()

    # If any challenges...
    if int(diceroll[tag]) > 0:
        add_stats(ctx, "diceroll", tag)
        if not short:
            await channel.send(tag + " 3 Dice. More than 11 to earn a challenge. All 3 the same number to earn the 3 challenge Jackpot!")
            time.sleep(2)
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        dice3 = random.randint(1,6)
        await channel.send("Dice 1 : **" + str(dice1) + "**")
        time.sleep(1)
        await channel.send("Dice 2 : **" + str(dice2) + "**")
        time.sleep(1)
        await channel.send("Dice 3 : **" + str(dice3) + "**")
        time.sleep(1)
        sum = dice1 + dice2 + dice3
        secretprize = False
        jackpot = False
        if dice1 == 1 and dice2 == 1 and dice3 == 4:
            secretprize = True
        if dice1 == dice2 and dice1 == dice3:
            jackpot = True
        if jackpot:
            if int(challenges[tag]) < 20:
                challenges[tag] = int(challenges[tag])+3
            add_stats(ctx, "dicewin", tag)
            await channel.send("**DING DING DING. JACKPOT. 3 Challenges Added!**" )
        elif secretprize:
            if int(challenges[tag]) < 20:
                challenges[tag] = int(challenges[tag])+5
            add_stats(ctx, "dicewin", tag)
            await channel.send("***Secret Combo Found. 1 in 216 chance. 5 Challenges Awarded!!!***")
        elif sum == 11:
            await channel.send("**Coin Flip on 11!**\n*Heads - Challenge | Tails - Nothing...*")
            time.sleep(3)
            result = random.randint(1,2)
            if result == 1:
                add_stats(ctx, "dicewin", tag)
                await channel.send("**HEADS! CONGRATULATIONS! You Won a Challenge**")
                if int(challenges[tag]) < 20:
                    challenges[tag] = int(challenges[tag])+1
            else:
                await channel.send("*TAILS! Unlucky...*")
        elif sum > 11:
            if int(challenges[tag]) < 20:
                challenges[tag] = int(challenges[tag])+1
            add_stats(ctx, "dicewin", tag)
            await channel.send("**CONGRATULATIONS! You Won a Challenge!**")
        else:
            await channel.send("No win this time...")

        # Remove diceroll
        diceroll[tag] = int(diceroll[tag])-1
        log("Dice Roll " + str(ctx.message.author) + " " + str(sum) + " " + str(jackpot) + " " + str(secretprize))
        write_challenges(challenges, diceroll)

        dicerolls = {}
        dicewins = {}
        allwins = 0
        allrolls = 0
        f=open("E:/Dropbox/Discord/gmc/stats.txt", "r")
        for line in f:
            split = line.split(',')
            split[6] = split[6].split('\n')[0]
            dicerolls[split[0]] = int(split[5])
            dicewins[split[0]] = int(split[6])
            allwins += dicewins[split[0]]
            allrolls += dicerolls[split[0]]
        f.close()
        if dicerolls[tag] == 0:
            percentage = 0
        else:
            percentage = (int(dicewins[tag]) / int(dicerolls[tag])) * 100
        if allrolls == 0:
            alliancepercent = 0
        else:
            alliancepercent = (allwins / allrolls) * 100
        dicerollinfo = "*Your Diceroll % : " + str(dicewins[tag]) + "/" + str(dicerolls[tag]) + " - **" + str(int(percentage)) + "%** (Alliance Average:" + str(int(alliancepercent)) + "% Win Probability:45.6%)*"
        await channel.send("*" + str(challenges[tag]) + " Challenges and " + str(diceroll[tag]) + " Dice Rolls Remaining* \n" + dicerollinfo)
    else:
        await channel.send("You currently have 0 Dice Rolls :(")

@bot.command(pass_context = True)
async def concede(ctx):
    if is_role(ctx, "Champion of Sakaar"):
        await run_new_champ(ctx, True)
    elif is_role(ctx, "Active Challenger"):
        await run_defence(ctx, True)
    else:
        await channel.send("You are neither Champion or Challenger")

################# ADMIN ######################

@bot.command(pass_context=True)
async def listplayers(ctx):
    if is_allowed(ctx):
        output = "```Current Players\n"
        for id in load_ids():
            output += get_member(ctx, id) + ", "
        await channel.send(output + "```")

@bot.command(pass_context = True)
async def showinfo(ctx):

    if is_allowed(ctx):
        output = "**Challenges**\n"
        f=open("E:/Dropbox/Discord/gmc/challenges.txt", "r")
        for line in f:
            split = line.split(',')
            if int(split[1]) > 0:
                output += split[0] + " : " + split[1] + "\n"
        output += "**Dice Rolls**\n"
        f.close()
        f=open("E:/Dropbox/Discord/gmc/challenges.txt", "r")
        for line in f:
            split = line.split(',')
            split[2] = split[2].split('\n')[0]
            if int(split[2]) > 0:
                output += split[0] + " : " + split[2] + "\n"
        await channel.send(output)
        log("Show Info " + str(ctx.message.author))
    else:
        await channel.send("Admin Permissions Required")

@bot.command(pass_context = True)
async def newchallenger(ctx):
    await new_challenger(ctx)

async def new_challenger(ctx, bypass_auth=False):
    server = ctx.message.guild

    # Load Champ
    currentChampID = load_single_line_file("E:/Dropbox/Discord/gmc/currentchamp.txt")

    if is_allowed(ctx) or bypass_auth:
        if is_active() == 'false':
            challenger = load_ids()[random.randint(0,len(load_ids())-1)].replace('\n','')

            await channel.send("**CURRENT CHAMPION OF SAKAAR : " + currentChampID + "**")
            while challenger == currentChampID:
                challenger = load_ids()[random.randint(0,len(load_ids())-1)].replace('\n','')
            add_stats(ctx, "random", challenger)
            await channel.send("**Challenger: **" + challenger + " - *Randomly Selected " + str(get_stat("random", challenger)) + " Times*")

            log_message = "New Challenger " + get_member(ctx, challenger)
            await run_category(log_message)

            write_to_active('true')
            await change_role(server, challenger, 'add', 'Active Challenger')
            await cancel_no_challenge_timer()
            await start_active_challenge_timer(ctx)
        else:
            await channel.send("Challenge Already Active")
    else:
        await channel.send("Admin Permissions Required")

@bot.command(pass_context = True)
async def newchamp(ctx):
    await run_new_champ(ctx)

async def run_new_champ(ctx, allowed=False):
    now = datetime.datetime.now()
    server = ctx.message.guild
    roles = ctx.message.author.roles
    oldchampfromfile = load_single_line_file("E:/Dropbox/Discord/gmc/currentchamp.txt")

    if is_allowed(ctx) or allowed:
        id = get_single_user_from_role(ctx, "Active Challenger")
        if id is not None:
            id = "<@" + str(id.id) + ">"
            f=open("E:/Dropbox/Discord/gmc/currentchamp.txt", "w")
            f.write(str(id))
            f.close()
            write_to_active('false')
            add_stats(ctx, "reign", id)
            await channel.send("New Champ is " + id + " - *" + str(get_stat("reign", id)) + " Reigns*")
            f=open("E:/Dropbox/Discord/gmc/champhistory.txt", "a")
            f.write(str(now.day) + " " + calendar.month_name[now.month] + " " + str(now.year) + ":NEW:" + str(id) + "\n")
            f.close()
            await change_role(server, oldchampfromfile, 'remove', 'Champion of Sakaar')
            await change_role(server, id, 'add', 'Champion of Sakaar')
            await change_role(server, id, 'remove', 'Active Challenger')
            log("New Champ " + get_member(ctx, id))
            await cancel_active_challenge_timer()
            await start_no_challenge_timer(ctx)
            write_cat("")
        else:
            role = get(ctx.message.guild.roles, name="GMAdmin")
            await channel.send("{} No Active Challenger role. Please assign role in Discord.".format(role.mention))
    else:
        await channel.send("Admin Permissions Required")

@bot.command(pass_context = True)
async def defence(ctx):
    await run_defence(ctx)

async def run_defence(ctx, allowed=False):
    now = datetime.datetime.now()
    server = ctx.message.guild
    currentChampID = "None"

    if is_allowed(ctx) or allowed:
        #id = id.replace('!','')
        id = get_single_user_from_role(ctx, "Active Challenger").id
        if id == None:
            role = get(ctx.message.guild.roles, name="GMAdmin")
            await channel.send("{} No Active Challenger role. Please assign role in Discord.".format(role.mention))
            return
        id = "<@" + str(id) + ">"
        #champid = champid.replace('!','')
        champid = get_single_user_from_role(ctx, "Champion of Sakaar").id
        if champid == None:
            role = get(ctx.message.guild.roles, name="GMAdmin")
            await channel.send("{} No Champion of Sakaar role. Please assign role in Discord.".format(role.mention))
            return
        champid = "<@" + str(champid) + ">"
        currentChampID = load_single_line_file("E:/Dropbox/Discord/gmc/currentchamp.txt")

        if champid == currentChampID:
            write_to_active('false')
            f=open("E:/Dropbox/Discord/gmc/champhistory.txt", "a")
            f.write(str(now.day) + " " + calendar.month_name[now.month] + " " + str(now.year) + ":DEF:" + str(currentChampID) + ":" + str(id) + "\n")
            f.close()
            add_stats(ctx, "defence", champid)
            await channel.send(champid + " defeated " + id + " - *" + str(get_stat("defence", champid)) + " Defences*")
            await change_role(server, id, 'remove', 'Active Challenger')
            log("Defence " + get_member(ctx, champid) + " " + get_member(ctx, id))
            await cancel_active_challenge_timer()
            await start_no_challenge_timer(ctx)
        else:
            await channel.send("Current Champ is " + currentChampID + ", not " + champid)
        write_cat("")
    else:
        await channel.send("Admin Permissions Required")

@bot.command(pass_context = True)
async def awardchallenge(ctx, *ids):
    challenges, diceroll = load_challenges()

    if is_allowed(ctx):
        for id in ids:
            id = id.replace('!','')
            optedids = load_ids()
            if id in optedids:
                if int(challenges[id]) < 20:
                    challenges[id] = int(challenges[id])+1
                    write_challenges(challenges, diceroll)
                    await channel.send(id + " now has " + str(challenges[id]) + " Challenge(s)")
                else:
                    await channel.send(id + " already has 20 Challenges. Please use your challenges to acquire more")
                log("Award Challenge " + get_member(ctx, id))
    else:
        await channel.send("Admin Permissions Required")

@bot.command(pass_context = True)
async def awarddiceroll(ctx, *ids):
    challenges, diceroll = load_challenges()
    if is_allowed(ctx):
        for id in ids:
            id = id.replace('!','')
            optedids = load_ids()
            if id in optedids:
                if int(diceroll[id]) < 100:
                    diceroll[id] = int(diceroll[id])+1
                    write_challenges(challenges, diceroll)
                    await channel.send(id + " now has " + str(diceroll[id]) + " Dice Roll(s)")
                else:
                    await channel.send(id + " already has 100 Dice Rolls. Please use your challenges to acquire more")
                log("Award Dice Roll " + get_member(ctx, id))
    else:
        await channel.send("Admin Permissions Required")

@bot.command(pass_context = True)
async def awardwarwin(ctx):
    challenges, diceroll = load_challenges()

    if is_allowed(ctx):
        for entry in diceroll:
            optedids = load_ids()
            if entry in optedids:
                if int(diceroll[entry]) < 100:
                    diceroll[entry] = int(diceroll[entry])+1
        write_challenges(challenges, diceroll)
        await channel.send("**War Win!** Everyone gets a Dice Roll")
        log("Award War Win " + str(ctx.message.author))
    else:
        await channel.send("Admin Permissions Required")

@bot.command(pass_context = True)
async def awarddailydicerolls(ctx):
    challenges, diceroll = load_challenges()

    if is_allowed(ctx):
        for entry in diceroll:
            optedids = load_ids()
            if entry in optedids:
                if int(diceroll[entry]) < 100:
                    diceroll[entry] = int(diceroll[entry])+1
        write_challenges(challenges, diceroll)
        await channel.send("**Daily Dice Rolls** Everyone gets a Dice Roll")
        log("Award Daily Dice Rolls " + str(ctx.message.author))
    else:
        await channel.send("Admin Permissions Required")

@bot.command(pass_context = True)
async def awardwarmvp(ctx, id):
    challenges, diceroll = load_challenges()

    if is_allowed(ctx):
        id = id.replace('!','')
        optedids = load_ids()
        if id in optedids:
            if int(challenges[id]) < 19:
                challenges[id] = int(challenges[id])+2
                write_challenges(challenges, diceroll)
                await channel.send(id + " now has " + str(challenges[id]) + " Challenge(s)")
            else:
                    await channel.send(id + " already has 20 Challenges. Please use your challenges to acquire more")
            log("Award War MVP " + get_member(ctx, id))
    else:
        await channel.send("Admin Permissions Required")

@bot.command(pass_context = True)
async def forceACTtimeout(ctx):
    log("Forced AC Timeout")
    role = get(ctx.message.guild.roles, name="GMAdmin")
    await channel.send("{} Timer has ended. Award Winner".format(role.mention))

################## TIMER ######################

class Timer:
    def __init__(self, timeout, callback, ctx):
        self._timeout = timeout
        self._callback = callback
        self._ctx = ctx
        self._task = asyncio.ensure_future(self._job())

    async def _job(self):
        await asyncio.sleep(self._timeout)
        await self._callback(self._ctx)

    def cancel(self):
        self._task.cancel()

async def start_active_challenge_timer(ctx):
    log("Active Challenge Timer Start")
    global actimer
    time = 6 * 3600
    actimer = Timer(time, ac_timeout_callback, ctx)
    await asyncio.sleep(time + 0.5)

async def start_no_challenge_timer(ctx):
    log("No Challenge Timer Start")
    global nctimer
    time = 1 * 3600
    nctimer = Timer(time, nc_timeout_callback, ctx)
    await asyncio.sleep(time + 0.5)

async def cancel_active_challenge_timer():
    if 'actimer' in globals():
        if actimer is not None:
            log("Cancelling Active Challenge Timer")
            actimer.cancel()

async def cancel_no_challenge_timer():
    if 'nctimer' in globals():
        if nctimer is not None:
            log("Cancelling No Challenge Timer")
            nctimer.cancel()

async def ac_timeout_callback(ctx):
    await asyncio.sleep(0.1)
    log("AC Timeout")
    role = get(ctx.message.guild.roles, name="GMAdmin")
    await channel.send("*{} Timer has ended. Award Winner*".format(role.mention))

async def nc_timeout_callback(ctx):
    await asyncio.sleep(0.1)
    log("NC Timeout")
    await channel.send("*No Challenge Timer Ended*")
    await new_challenger(ctx, True)

@bot.command(pass_context = True)
async def startACT(ctx):
    await start_active_challenge_timer(ctx)

@bot.command(pass_context = True)
async def startNCT(ctx):
    await start_no_challenge_timer(ctx)

@bot.command(pass_context = True)
async def cancelACT(ctx):
    #MANUAL
    log("Cancelling Active Challenge Timer")
    actimer.cancel()

@bot.command(pass_context = True)
async def cancelNCT(ctx):
    #MANUAL
    log("Cancelling No Challenge Timer")
    nctimer.cancel()

################## HELPER ######################

async def change_role(server, memberID, operation, role_name):
    memberNo = memberID.replace('!','').replace('<', '').replace('>', '').replace('@', '')
    member = server.get_member(int(memberNo))
    role = get(server.roles, name=role_name)
    if operation == 'add':
        await member.add_roles(role)
    else:
        await member.remove_roles(role)

async def run_category(log_message):
    pvp = random.randint(1,10)
    if pvp == 1:
        category = "PVP!"
    else:
        category = categories[random.randint(0,len(categories)-1)]
    if category == "Random Character Power Level [Level]":
        amount = random.randint(0,70000)
        await channel.send("*Category: " + category + "* **" + str(amount) + "**")
        category += " " + str(amount)
    elif category == "Random Character Power Level [Character]":
        character = characters[random.randint(0,len(characters)-1)]
        await channel.send("*Category: " + category + "* \n**" + character + "**")
        category += " " + character
    elif category == "Random Character Shards":
        character = characters[random.randint(0,len(characters)-1)]
        await channel.send("*Category: " + category + "* \n**" + character + "**")
        category += " " + character
    elif category == "Strongest Random Team":
        output = "\n"
        charlist = []
        for x in range(5):
            character = characters[random.randint(0,len(characters)-1)]
            if not character in charlist:
                output += character + "\n"
                charlist.append(character)
            else:
                character = characters[random.randint(0,len(characters)-1)]
                if not character in charlist:
                    output += character + "\n"
                    charlist.append(character)
        await channel.send("*Category: " + category + ":* **" + output + "**")
        category += " " + output.replace("\n",",")
    elif category == "10 Avatar Challenge [#]":
        output = "\n"
        charlist = []
        for x in range(10):
            character = characters[random.randint(0,len(characters)-1)]
            if not character in charlist:
                output += character + "\n"
                charlist.append(character)
            else:
                x -= 1
        await channel.send("*Category: " + category + ":* **" + output + "**")
    elif category == "Strongest 'X' Team":
        category = category.replace(""'X'"", traits[random.randint(0,len(traits)-1)])
        await channel.send("*Category: " + category +"*")
    else:
        await channel.send("*Category: " + category +"*")
        if category == "PVP!":
            await channel.send(gifs[random.randint(0,len(gifs)-1)])
    log(log_message + " " + category)
    write_cat(category)

def log(message):
    time = datetime.datetime.now()
    print(str(time) + " : " + message)
    f=open("E:/Dropbox/Discord/gmc/log.txt", "a")
    f.write(str(time) + " : " + message + "\n")
    f.close()

def load_single_line_file(file_name):
    f=open(file_name, "r")
    if f.mode == "r":
        to_return = f.read()
    f.close()
    return to_return

def write_to_active(output):
    f=open("E:/Dropbox/Discord/gmc/active.txt", "w")
    f.write(output)
    f.close()

def write_challenges(challenges, diceroll):
    f=open("E:/Dropbox/Discord/gmc/challenges.txt", "w")
    for user in challenges:
        f.write(user + "," + str(challenges[user]) + "," + str(diceroll[user]) + "\n")
    f.close()

def load_challenges():
    challenges = {}
    diceroll = {}
    f=open("E:/Dropbox/Discord/gmc/challenges.txt", "r")
    for line in f:
        split = line.split(',')
        split[2] = split[2].split('\n')[0]
        challenges[split[0]] = split[1]
        diceroll[split[0]] = split[2]
    f.close()
    return challenges, diceroll

def load_ids():
    ids = []
    f=open("E:/Dropbox/Discord/gmc/idlist.txt", "r")
    for line in f:
        ids.append(line.rstrip())
    return ids

def get_stat(stat, id):
    # Load Challenges
    reigns = {}
    defences = {}
    randoms = {}
    challenges = {}
    dicerolls = {}
    dicewins = {}
    f=open("E:/Dropbox/Discord/gmc/stats.txt", "r")
    for line in f:
        split = line.split(',')
        split[6] = split[6].split('\n')[0]
        reigns[split[0]] = split[1]
        defences[split[0]] = split[2]
        randoms[split[0]] = split[3]
        challenges[split[0]] = split[4]
        dicerolls[split[0]] = split[5]
        dicewins[split[0]] = split[6]
    f.close()

    if stat == "reign":
        return reigns[id]
    elif stat == "defence":
        return defences[id]
    elif stat == "random":
        return randoms[id]
    elif stat == "challenge":
        return challenges[id]
    elif stat == "diceroll":
        return dicerolls[id]
    elif stat == "dicewin":
        return dicewins[id]

def add_stats(ctx, stat, id):
    # Load Challenges
    reigns = {}
    defences = {}
    randoms = {}
    challenges = {}
    dicerolls = {}
    dicewins = {}
    f=open("E:/Dropbox/Discord/gmc/stats.txt", "r")
    for line in f:
        split = line.split(',')
        split[6] = split[6].split('\n')[0]
        reigns[split[0]] = split[1]
        defences[split[0]] = split[2]
        randoms[split[0]] = split[3]
        challenges[split[0]] = split[4]
        dicerolls[split[0]] = split[5]
        dicewins[split[0]] = split[6]
    f.close()

    if stat == "reign":
        reigns[id] = int(reigns[id])+1
    elif stat == "defence":
        defences[id] = int(defences[id])+1
    elif stat == "random":
        randoms[id] = int(randoms[id])+1
    elif stat == "challenge":
        challenges[id] = int(challenges[id])+1
    elif stat == "diceroll":
        dicerolls[id] = int(dicerolls[id])+1
    elif stat == "dicewin":
        dicewins[id] = int(dicewins[id])+1

    f=open("E:/Dropbox/Discord/gmc/stats.txt", "w")
    for user in reigns:
        f.write(user + "," + str(reigns[user]) + "," + str(defences[user]) + "," + str(randoms[user]) + "," + str(challenges[user]) + "," + str(dicerolls[user]) + "," + str(dicewins[user]) + "\n")
    f.close()

def is_role(ctx, roleName):
    roles = ctx.message.author.roles
    for role in roles:
        if role.name == roleName:
            return True
    return False

def is_allowed(ctx):
    roles = ctx.message.author.roles
    for role in roles:
        if role.name == "GMAdmin":
            return True
    return False

def is_active():
    f=open("E:/Dropbox/Discord/gmc/active.txt", "r")
    if f.mode == "r":
        active = f.read()
    f.close()
    return active

def get_single_user_from_role(ctx, roleName):
    server = ctx.message.guild
    for member in server.members:
        for role in member.roles:
            if role.name == roleName:
                return member

def get_member(ctx, id):
    server = ctx.message.guild
    member = id.replace('!','').replace('<', '').replace('>', '').replace('@', '')
    member = server.get_member(int(member))
    return str(member)

def write_cat(output):
    f=open("E:/Dropbox/Discord/gmc/activecat.txt", "w")
    f.write(output)
    f.close()

def get_category():
    f=open("E:/Dropbox/Discord/gmc/activecat.txt", "r")
    return(f.read())

################## Deprecated ######################


@bot.command(pass_context = True)
async def veto(ctx):
    tag = "<@" + str(ctx.message.author.id) + ">"

    # Load Challenges
    challenges, diceroll = load_challenges()

    # If any challenges...
    if int(vetos[tag]) > 0:
        if is_active() == 'true':
            await channel.send("**Veto Used!**")
            log_message = "Veto " + str(ctx.message.author)
            await run_category(log_message)
            vetos[tag] = int(vetos[tag])-1
            write_challenges(challenges, diceroll)
        else:
            await channel.send("No Challenge Currently Active")
    else:
        await channel.send("You currently have 0 Vetos :(")

@bot.command(pass_context = True)
async def awardveto(ctx, id):
    challenges, diceroll = load_challenges()

    if is_allowed(ctx):
        id = id.replace('!','')
        vetos[id] = int(vetos[id])+1

        write_challenges(challenges, diceroll)
        await channel.send(id + " now has " + str(vetos[id]) + " Veto(s)")
        log("Award Veto " + get_member(ctx, id))
    else:
        await channel.send("Admin Permissions Required")

@bot.command(pass_context = True)
async def awardult(ctx, id1, id2, id3, id4, id5, id6):
    challenges, diceroll = load_challenges()

    if is_allowed(ctx):
        id1 = id1.replace('!','')
        challenges[id1] = int(challenges[id1])+1
        await channel.send(id1 + " now has " + str(challenges[id1]) + " Challenge(s)")
        id2 = id2.replace('!','')
        diceroll[id2] = int(diceroll[id2])+2
        await channel.send(id2 + " now has " + str(diceroll[id2]) + " Dice Roll(s)")
        id3 = id3.replace('!','')
        diceroll[id3] = int(diceroll[id3])+1
        await channel.send(id3 + " now has " + str(diceroll[id3]) + " Dice Roll(s)")
        id4 = id4.replace('!','')
        diceroll[id4] = int(diceroll[id4])+1
        await channel.send(id4 + " now has " + str(diceroll[id4]) + " Dice Roll(s)")
        id5 = id5.replace('!','')
        diceroll[id5] = int(diceroll[id5])+1
        await channel.send(id5 + " now has " + str(diceroll[id5]) + " Dice Roll(s)")
        id6 = id6.replace('!','')
        diceroll[id6] = int(diceroll[id6])+1
        await channel.send(id6 + " now has " + str(diceroll[id6]) + " Dice Roll(s)")
        f=open("E:/Dropbox/Discord/gmc/challenges.txt", "w")
        write_challenges(challenges, diceroll)
        log("Award Ult " + get_member(ctx, id1) + " " + get_member(ctx, id2) + " " + get_member(ctx, id3) + " " + get_member(ctx, id4) + " " + get_member(ctx, id5) + " " + get_member(ctx, id6))
    else:
        await channel.send("Admin Permissions Required")

bot.run(config.token)
