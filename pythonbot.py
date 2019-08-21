import random
import discord
import datetime
import calendar
import time
import operator
from discord.ext import commands
from discord.utils import get
bot = commands.Bot(command_prefix="=")
channel="abc"

# PUSH LIVE - Change channel to (Test) 518199222340812801 or (Live) 576432021526544405. Change ADMIN/GMAdmin. Change filenames.

sakrebIds=["<@344661859275898882>", "<@353914644613693451>", "<@215981471842697217>", \
"<@273279044454187009>", "<@479513428638040086>", "<@473691876680269824>", "<@483755276873498644>", \
"<@476781105828069386>", "<@187617865996828673>", "<@592861817534152719>", \
"<@465324594597986304>", "<@468054768502439947>", \
"<@450729572569186324>", "<@266447975146848257>", "<@568471080742682626>", \
"<@473822789854560266>", "<@451373900069076993>"]
categories=["Collection Power [#]", "Strongest Team Power [#]", \
    "Highest Power Character", "Lowest Power Character", "Highest Power Worst Character", \
    "Gold + Red Stars (Single Character)", "10+ Gold & Red Stars (Total Characters)", \
    "Alliance MVP Ranking [#]", \
    "Dark Dimension Nodes Completed (inc. Timed Run)", \
    "Characters Unlocked [#]", \
    "Characters at 7 Stars [#]", "Characters at 6+ Stars", "Characters at 5+ Stars", "Characters at 4+ Stars", \
    "Characters at 50K+", "Characters at 40K+", "Characters at 30K+", "Characters at 20K+", "Characters at 10K+", \
    "All Time Arena Rank [#]", "Current Arena Rank [#]", \
    "Gear 13 Characters", "Gear 12+ Characters", "Gear 11+ Characters", "Gear 1 Characters", \
    "Last Completed Blitz Rank", "Last / Current Ultimus Raid Ranking", \
    "Gold Spent", "Character Rank Ups", "Arena Battles", "Days Logged In", \
    "Highest Power Minion", "Highest Power AIM Or Hydra Team", \
    "Power Core Hoarder", "Gold Hoarder", "Most 0 Red Stars", \
    "Last/Current War Battles [#]", "Last/Current War Damage Done [#]", \
    "Highest Fury/Shield Minion Team", "Highest Defenders Team", "Highest Spiderverse Team", "Highest GotG Team", "Highest Avengers Team", \
    "Highest Wakandans Team", "Highest X-Men Team", "Highest Brotherhood Team", "Highest S6 Team", "Highest Kree Team", \
    "Level 70 Characters", "Level 1 Characters", \
    "Discord Leaderboard [#]", "Blitz Wins [#]", \
    "Random Character Power Level (Character)","Random Character Power Level (Character)", \
    "Random Character Power Level (Level)", "Random Character Power Level (Level)", \
    "Random Character Shards", "Random Character Shards", \
    "Random Team Power Level", "Random Team Power Level", "Random Team Power Level", "Random Team Power Level", "Random Team Power Level", \
    "Ultimus Shards", "Hulk Shards"]
characters=["AIM Assaulter", "AIM Infector", "AIM Monstrosity", "AIM Researcher", "AIM Security", "America Chavez", "Ant-Man", "Black Panther", "Black Widow", "Bullseye", "Cable", \
            "Captain America", "Captain Marvel", "Carnage", "Colossus", "Crossbones", "Daredevil", "Deadpool", "Doctor Strange", "Drax", "Elektra", "Falcon", "Gamora", "Green Goblin", \
            "Groot", "Hand Archer", "Hand Assassin", "Hand Blademaster", "Hand Sentry", "Hand Sorceress", "Hawkeye", "Hulk", "Hydra Armored Guard", "Hydra Grenadier", \
            "Hydra Rifle Trooper", "Hydra Scientist", "Hydra Sniper", "Iron Fist", "Iron Man", "Jessica Jones", "Juggernaut", "Killmonger", "Kingpin", "Korath", \
            "Kree Cyborg", "Kree Noble", "Kree Oracle", "Kree Reaper", "Kree Royal Guard", "Loki", "Luke Cage", "M'Baku", "Magneto", "Mantis", "Merc Lieutenant", \
            "Merc Riot Guard", "Merc Sniper", "Merc Soldier", "Minn-Erva", "Mordo", "Ms. Marvel", "Mystique", "Nebula", "Nick Fury", "Night Nurse", "Nobu", "Okoye", \
            "Phoenix", "Psylocke", "Punisher", "Pyro", "Quake", "Ravager Boomer", "Ravager Bruiser", "Ravager Stitcher", "Rescue", "Rocket", "Ronan", "SHIELD Assault", \
            "SHIELD Medic", "SHIELD Operative", "SHIELD Security", "SHIELD Trooper", "Sabretooth", "Scarlet Witch", "Scientist Supreme", "Shuri", "Spider-Man", "Spider-Man (Miles)", \
            "Star-Lord", "Storm", "Thanos", "Thor", "Venom", "Vision", "War-Machine", "Wasp", "Winter Soldier", "Wolverine", "Yondu"
            ]
idMap={"<@344661859275898882>":"Artikhopper", "<@353914644613693451>":"Bootanka", "<@215981471842697217>":"Calmskitzo", "<@223982068131037185>":"Candidme", \
"<@273279044454187009>":"ColbysGotMoore", "<@479174652376252416>":"Cookie_Monster86", "<@479513428638040086>":"Deadpool", "<@473691876680269824>":"FatMichael", \
"<@483755276873498644>":"GeauxRagnar", "<@476781105828069386>":"H1CKROSS", "<@182901488488677376>":"heet3r", "<@187617865996828673>":"JerBear", \
"<@592861817534152719>":"KillerKarnage", "<@465324594597986304>":"KyReezy", "<@396560397257408514>":"Owinfrey", "<@468054768502439947>":"OzDH", "<@442226315291131907>":"Peter G", \
"<@458334361083707414>":"Randy Savage", "<@450729572569186324>":"ScatCuvSmuv", "<@266447975146848257>":"ShadowsRisen", "<@568471080742682626>":"Talon", \
"<@473822789854560266>":"TrickJames", "<@330148338890702849>":"Tyfighter", "<@451373900069076993>":"Wagon King", "Char":"Char"}

@bot.event
async def on_ready():
    # Load Champ
    currentChampID = load_single_line_file("currentchamp.txt")
    # Startup
    log('Startup : Logged in as ' + bot.user.name)
    global channel
    channel = bot.get_channel(576432021526544405) # channel ID goes here

@bot.command(pass_context = True)
async def h(ctx):
    log("Help " + str(ctx.message.author))
    await channel.send("**h** : *Print Commands Help*\n\
**printcategories** : *Prints all the Categories*\n\
**champ** : *Print the Current Champion*\n\
**myinfo** : *Prints all stats about the sender including challenges and dice rolls*\n\
**claimchallenge** : *Generate New Challenge for sender of the message*\n\
**diceroll** : *Roll the Dice to try and win a challenge*\n\
**veto** : *Use a veto and get the category changed*\n\
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
**awardveto ID**: *Award a veto to given ID*\n\
**awardult ID1 ID2 ID3 ID4 ID5 ID6**: *Award correct rewards to the top 6 in the raid*\n\
**awardwarwin**: *Award a diceroll to everyone for winning a war*\n\
**awardwarmvp ID**: *Award 2 dicerolls to the War MVP*\n\
**showchallenges** : *Show all the people with available challenges*")

@bot.command(pass_context = True)
async def fullstats(ctx):
    log("Full Stats - " + str(ctx.message.author))
    reigns = {}
    defences = {}
    randoms = {}
    challenges = {}
    dicerolls = {}
    dicewins = {}
    f=open("stats.txt", "r")
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
    output = "**R = Reigns | D = Defences | RS = Randomly Selected | C = Challenges | DR = Dice Rolls\n**"

    for user in reigns:
        output += user +  "\tR:" + str(reigns[user]) + "\tD:" + str(defences[user]) + "\tRS:" + str(randoms[user]) + "\tC:" + str(challenges[user]) + " \tDR:" + str(dicewins[user]) + "/" + str(dicerolls[user]) + "\n"

    await channel.send(output)

@bot.command(pass_context = True)
async def stats(ctx):
    log("Stats " + str(ctx.message.author))
    reigns = {}
    defences = {}
    randoms = {}
    challenges = {}
    dicerolls = {}
    dicewins = {}
    f=open("stats.txt", "r")
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
    for x in range(5):
        await channel.send(str(x+1) + ": " + reigns[x][0] + " - " + str(reigns[x][1]))
    await channel.send("**Championship Defences**")
    for x in range(5):
        await channel.send(str(x+1) + ": " + defences[x][0] + " - " + str(defences[x][1]))
    await channel.send("**Randomly Selected**")
    for x in range(5):
        await channel.send(str(x+1) + ": " + randoms[x][0] + " - " + str(randoms[x][1]))
    await channel.send("**Challenges**")
    for x in range(5):
        await channel.send(str(x+1) + ": " + challenges[x][0] + " - " + str(challenges[x][1]))
    await channel.send("**Dice Rolls**")
    for x in range(5):
        await channel.send(str(x+1) + ": " + dicerolls[x][0] + " - " + str(dicerolls[x][1]))
    await channel.send("**Dice Roll Wins**")
    for x in range(5):
        await channel.send(str(x+1) + ": " + dicewins[x][0] + " - " + str(dicewins[x][1]))

@bot.command(pass_context = True)
async def gethistory(ctx):
    log("Get History " + str(ctx.message.author))
    f=open("champhistory.txt", "r")
    output = ""
    for line in f:
        split = line.split(':')
        if len(split) == 3:
            if len(output) > 1900:
                await channel.send(output)
                output = ""
            output += "*" + split[0] + ":* New Champion! **" + idMap[split[2].split("\n")[0]] + "**\n"
        else:
            if len(output) > 1900:
                await channel.send(output)
                output = ""
            output += "*" + split[0] + ":* **" + idMap[split[2]] + "** defeats **" + idMap[split[3].split("\n")[0]] + "**\n"
    await channel.send(output)

@bot.command(pass_context = True)
async def myinfo(ctx):
    log("My Info " + str(ctx.message.author))
    tag = "<@" + str(ctx.message.author.id) + ">"
    challenges, diceroll, vetos = load_challenges()

    await channel.send(tag + " has **" + str(challenges[tag]) + "** Challenge(s) & **" + str(diceroll[tag]) + "** Dice Roll(s) & **" + str(vetos[tag]) + "** Veto(s)")

    reigns = {}
    defences = {}
    randoms = {}
    challenges = {}
    dicerolls = {}
    dicewins = {}
    allwins = 0
    allrolls = 0
    f=open("stats.txt", "r")
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
    percentage = (int(dicewins[tag]) / int(dicerolls[tag])) * 100
    alliancepercent = (allwins / allrolls) * 100
    dicerollinfo = "**" + str(dicewins[tag]) + "/" + str(dicerolls[tag]) + " -  " + str(int(percentage)) + "%** *(Alliance Average:" + str(int(alliancepercent)) + "% Win Probability:45.6%)*"
    output = tag + " *statistics:*\nReigns - **" + str(reigns[tag]) + "**\nDefences - **" + str(defences[tag]) + "**\nRandomly Selected - **" + str(randoms[tag]) \
                            + "**\nChallenges - **" + str(challenges[tag]) + "**\nDice Roll Info - " + dicerollinfo
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
    currentChampID = load_single_line_file("currentchamp.txt")
    await channel.send("Current Champion is " + str(currentChampID))

@bot.command(pass_context = True)
async def printcategories(ctx):
    log("Print Categories " + str(ctx.message.author))
    string = ""
    for a in categories:
        string += a + "\n"
    await channel.send(string)

@bot.command(pass_context = True)
async def category(ctx):
    log_message = "Category " + str(ctx.message.author)
    await run_category(log_message)

@bot.command(pass_context = True)
async def bestof(ctx, i, id1, id2):
    if int(i) < 16:
        await channel.send(id1 + " **vs** " + id2)
        for x in range(int(i)):
            await run_category()
    else:
        await channel.send("Maximum 15 Categories")

@bot.command(pass_context = True)
async def claimchallenge(ctx):
    tag = "<@" + str(ctx.message.author.id) + ">"
    server = ctx.message.guild

    # Load Champ
    currentChampID = load_single_line_file("currentchamp.txt")

    # Load Challenges
    challenges, diceroll, vetos = load_challenges()

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
            write_challenges(challenges, diceroll, vetos)
            write_to_active('true')
            await change_role(server, tag, 'add', 'Active Challenger')
        else:
            await channel.send("You currently have 0 challenges :(")
    else:
        await channel.send("Challenge Already Active")

@bot.command(pass_context = True)
async def diceroll(ctx):
    tag = "<@" + str(ctx.message.author.id) + ">"

    # Load Challenges
    challenges, diceroll, vetos = load_challenges()

    # If any challenges...
    if int(diceroll[tag]) > 0:
        add_stats(ctx, "diceroll", tag)
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
        if dice1 == 1 and dice2 == 4 and dice3 == 6:
            secretprize = True
        if dice1 == dice2 and dice1 == dice3:
            jackpot = True
        if jackpot:
            challenges[tag] = int(challenges[tag])+3
            add_stats(ctx, "dicewin", tag)
            await channel.send("DING DING DING. JACKPOT. 3 Challenges Added!" )
        elif secretprize:
            challenges[tag] = int(challenges[tag])+5
            add_stats(ctx, "dicewin", tag)
            await channel.send("Secret Combo Found. 1 in 216 chance. 5 Challenges Awarded!!!")
        elif sum == 11:
            await channel.send("**Coin Flip on 11!**\n*Heads - Challenge | Tails - Nothing...*")
            time.sleep(3)
            result = random.randint(1,2)
            if result == 1:
                add_stats(ctx, "dicewin", tag)
                await channel.send("**HEADS! CONGRATULATIONS! You Won a Challenge**")
                challenges[tag] = int(challenges[tag])+1
            else:
                await channel.send("*TAILS! Unlucky...*")
        elif sum > 11:
            challenges[tag] = int(challenges[tag])+1
            add_stats(ctx, "dicewin", tag)
            await channel.send("CONGRATULATIONS! You Won a Challenge!")
        elif sum < 7:
            vetos[tag] = int(vetos[tag])+1
            await channel.send("CONGRATULATIONS! You Won a Veto!")
        else:
            await channel.send("No win this time...")

        # Remove diceroll
        diceroll[tag] = int(diceroll[tag])-1
        log("Dice Roll " + str(ctx.message.author) + " " + str(sum) + " " + str(jackpot) + " " + str(secretprize))
        write_challenges(challenges, diceroll, vetos)
        await channel.send("*" + str(challenges[tag]) + " Challenges and " + str(diceroll[tag]) + " Dice Rolls Remaining*")
    else:
        await channel.send("You currently have 0 Dice Rolls :(")

@bot.command(pass_context = True)
async def veto(ctx):
    tag = "<@" + str(ctx.message.author.id) + ">"

    # Load Challenges
    challenges, diceroll, vetos = load_challenges()

    # If any challenges...
    if int(vetos[tag]) > 0:
        if is_active() == 'true':
            await channel.send("**Veto Used!**")
            log_message = "Veto " + str(ctx.message.author)
            await run_category(log_message)
            vetos[tag] = int(vetos[tag])-1
            write_challenges(challenges, diceroll, vetos)
        else:
            await channel.send("No Challenge Currently Active")
    else:
        await channel.send("You currently have 0 Vetos :(")

################# ADMIN ######################

@bot.command(pass_context = True)
async def showchallenges(ctx):

    #REFACTOR THIS
    if is_allowed(ctx):
        output = "**Challenges**\n"
        f=open("challenges.txt", "r")
        for line in f:
            split = line.split(',')
            if int(split[1]) > 0:
                output += split[0] + " : " + split[1] + "\n"
        output += "**Dice Rolls**\n"
        f.close()
        f=open("challenges.txt", "r")
        for line in f:
            split = line.split(',')
            if int(split[2]) > 0:
                output += split[0] + " : " + split[2] + "\n"
        output += "**Vetos**\n"
        f.close()
        f=open("challenges.txt", "r")
        for line in f:
            split = line.split(',')
            split[3] = split[3].split('\n')[0]
            if int(split[3]) > 0:
                output += split[0] + " : " + split[3] + "\n"
        await channel.send(output)
        log("Show Challenges " + str(ctx.message.author))
    else:
        await channel.send("Admin Permissions Required")

@bot.command(pass_context = True)
async def newchallenger(ctx):
    server = ctx.message.guild

    # Load Champ
    currentChampID = load_single_line_file("currentchamp.txt")

    if is_allowed(ctx):
        if is_active() == 'false':
            challenger = sakrebIds[random.randint(0,len(sakrebIds)-1)]

            await channel.send("**CURRENT CHAMPION OF SAKAAR : " + currentChampID + "**")
            while challenger == currentChampID:
                challenger = sakrebIds[random.randint(0,len(sakrebIds)-1)]
            add_stats(ctx, "random", challenger)
            await channel.send("**Challenger: **" + challenger + " - *Randomly Selected " + str(get_stat("random", challenger)) + " Times*")

            log_message = "New Challenger " + str(get_member(ctx, challenger))
            await run_category(log_message)

            write_to_active('true')
            await change_role(server, challenger, 'add', 'Active Challenger')
        else:
            await channel.send("Challenge Already Active")
    else:
        await channel.send("Admin Permissions Required")

@bot.command(pass_context = True)
async def newchamp(ctx, id):
    now = datetime.datetime.now()
    server = ctx.message.guild
    roles = ctx.message.author.roles
    oldchampfromfile = load_single_line_file("currentchamp.txt")

    if is_allowed(ctx):
        id = id.replace('!','')
        f=open("currentchamp.txt", "w")
        f.write(str(id))
        f.close()
        write_to_active('false')
        add_stats(ctx, "reign", id)
        await channel.send("New Champ is " + id + " - *" + str(get_stat("reign", id)) + " Reigns*")
        f=open("champhistory.txt", "a")
        f.write(str(now.day) + " " + calendar.month_name[now.month] + " " + str(now.year) + ":NEW:" + str(id) + "\n")
        f.close()
        await change_role(server, oldchampfromfile, 'remove', 'Champion of Sakaar')
        await change_role(server, id, 'add', 'Champion of Sakaar')
        await change_role(server, id, 'remove', 'Active Challenger')
        log("New Champ " + str(get_member(ctx, id)))
    else:
        await channel.send("Admin Permissions Required")

@bot.command(pass_context = True)
async def defence(ctx, champid, id):
    now = datetime.datetime.now()
    server = ctx.message.guild
    currentChampID = "None"

    if is_allowed(ctx):
        id = id.replace('!','')
        champid = champid.replace('!','')
        currentChampID = load_single_line_file("currentchamp.txt")

        if champid == currentChampID:
            write_to_active('false')
            f=open("champhistory.txt", "a")
            f.write(str(now.day) + " " + calendar.month_name[now.month] + " " + str(now.year) + ":DEF:" + str(currentChampID) + ":" + str(id) + "\n")
            f.close()
            add_stats(ctx, "defence", champid)
            await channel.send(champid + " defeated " + id + " - *" + str(get_stat("defence", champid)) + " Defences*")
            await change_role(server, id, 'remove', 'Active Challenger')
            log("Defence " + str(get_member(ctx, champid)) + " " + str(get_member(ctx, id)))
        else:
            await channel.send("Current Champ is " + currentChampID + ", not " + champid)
    else:
        await channel.send("Admin Permissions Required")

@bot.command(pass_context = True)
async def awardchallenge(ctx, id):
    challenges, diceroll, vetos = load_challenges()

    if is_allowed(ctx):
        id = id.replace('!','')
        challenges[id] = int(challenges[id])+1

        write_challenges(challenges, diceroll, vetos)
        await channel.send(id + " now has " + str(challenges[id]) + " Challenge(s)")
        log("Award Challenge " + str(get_member(ctx, id)))
    else:
        await channel.send("Admin Permissions Required")

@bot.command(pass_context = True)
async def awarddiceroll(ctx, id):
    challenges, diceroll, vetos = load_challenges()

    if is_allowed(ctx):
        id = id.replace('!','')
        diceroll[id] = int(diceroll[id])+1

        write_challenges(challenges, diceroll, vetos)
        await channel.send(id + " now has " + str(diceroll[id]) + " Dice Roll(s)")
        log("Award Dice Roll " + str(get_member(ctx, id)))
    else:
        await channel.send("Admin Permissions Required")

@bot.command(pass_context = True)
async def awardveto(ctx, id):
    challenges, diceroll, vetos = load_challenges()

    if is_allowed(ctx):
        id = id.replace('!','')
        vetos[id] = int(vetos[id])+1

        write_challenges(challenges, diceroll, vetos)
        await channel.send(id + " now has " + str(vetos[id]) + " Veto(s)")
        log("Award Veto " + str(get_member(ctx, id)))
    else:
        await channel.send("Admin Permissions Required")

@bot.command(pass_context = True)
async def awardwarwin(ctx):
    challenges, diceroll, vetos = load_challenges()

    if is_allowed(ctx):
        for entry in diceroll:
            diceroll[entry] = int(diceroll[entry])+1

        write_challenges(challenges, diceroll, vetos)
        await channel.send("**War Win!** Everyone gets a Dice Roll")
        log("Award War Win " + str(ctx.message.author))
    else:
        await channel.send("Admin Permissions Required")

@bot.command(pass_context = True)
async def awardwarmvp(ctx, id):
    challenges, diceroll, vetos = load_challenges()

    if is_allowed(ctx):
        id = id.replace('!','')
        diceroll[id] = int(diceroll[id])+2
        vetos[id] = int(vetos[id])+1

        write_challenges(challenges, diceroll, vetos)
        await channel.send(id + " now has " + str(diceroll[id]) + " Dice Roll(s) and " + str(vetos[id]) + " Veto(s)")
        log("Award War MVP " + str(get_member(ctx, id)))
    else:
        await channel.send("Admin Permissions Required")

@bot.command(pass_context = True)
async def awardult(ctx, id1, id2, id3, id4, id5, id6):
    challenges, diceroll, vetos = load_challenges()

    if is_allowed(ctx):
        id1 = id1.replace('!','')
        challenges[id1] = int(challenges[id1])+1
        vetos[id1] = int(vetos[id1])+1
        await channel.send(id1 + " now has " + str(challenges[id1]) + " Challenge(s) and " + str(vetos[id1]) + " Veto(s)")
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
        f=open("challenges.txt", "w")
        write_challenges(challenges, diceroll, vetos)
        log("Award Ult " + str(get_member(ctx, id1)) + " " + str(get_member(ctx, id2)) + " " + str(get_member(ctx, id3)) + " " + str(get_member(ctx, id4)) + " " + str(get_member(ctx, id5)) + " " + str(get_member(ctx, id6)))
    else:
        await channel.send("Admin Permissions Required")

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
    category = categories[random.randint(0,len(categories)-1)]
    log(log_message + " " + category)
    if category == "Random Character Power Level (Level)":
        await channel.send("*Category: " + category + "* **" + str(random.randint(0,50000)) + "**")
    elif category == "Random Character Power Level (Character)":
        await channel.send("*Category: " + category + "* **" + characters[random.randint(0,len(characters)-1)] + "**")
    elif category == "Random Character Shards":
        await channel.send("*Category: " + category + "* **" + characters[random.randint(0,len(characters)-1)] + "**")
    elif category == "Random Team Power Level":
        output = "\n"
        charlist = []
        for x in range(5):
            character = characters[random.randint(0,len(characters)-1)]
            if not character in charlist:
                output += character + "\n"
                charlist.append(character)
            else:
                x -= 1
        await channel.send("*Category: " + category + ":* **" + output + "**")
    else:
        await channel.send("*Category: " + category +"*")

def log(message):
    time = datetime.datetime.now()
    print(str(time) + " : " + message)
    f=open("log.txt", "a")
    f.write(str(time) + " : " + message + "\n")
    f.close()

def load_single_line_file(file_name):
    f=open(file_name, "r")
    if f.mode == "r":
        to_return = f.read()
    f.close()
    return to_return

def write_to_active(output):
    f=open("active.txt", "w")
    f.write(output)
    f.close()

def write_challenges(challenges, diceroll, vetos):
    f=open("challenges.txt", "w")
    for user in challenges:
        f.write(user + "," + str(challenges[user]) + "," + str(diceroll[user]) + "," + str(vetos[user]) + "\n")
    f.close()

def load_challenges():
    challenges = {}
    diceroll = {}
    vetos = {}
    f=open("challenges.txt", "r")
    for line in f:
        split = line.split(',')
        split[3] = split[3].split('\n')[0]
        challenges[split[0]] = split[1]
        diceroll[split[0]] = split[2]
        vetos[split[0]] = split[3]
    f.close()
    return challenges, diceroll, vetos

def get_stat(stat, id):
    # Load Challenges
    reigns = {}
    defences = {}
    randoms = {}
    challenges = {}
    dicerolls = {}
    dicewins = {}
    f=open("stats.txt", "r")
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
    f=open("stats.txt", "r")
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

    f=open("stats.txt", "w")
    for user in reigns:
        f.write(user + "," + str(reigns[user]) + "," + str(defences[user]) + "," + str(randoms[user]) + "," + str(challenges[user]) + "," + str(dicerolls[user]) + "," + str(dicewins[user]) + "\n")
    f.close()

def is_allowed(ctx):
    roles = ctx.message.author.roles
    for role in roles:
        if role.name == "GMAdmin":
            return True
    return False

def is_active():
    f=open("active.txt", "r")
    if f.mode == "r":
        active = f.read()
    f.close()
    return active

def get_member(ctx, id):
    server = ctx.message.guild
    member = id.replace('!','').replace('<', '').replace('>', '').replace('@', '')
    member = server.get_member(int(member))
    return member

bot.run("NTc1ODY1NjM0NzI3MDAyMTQy.XNOKyw.m3QJqH4U1ghn1imcCkWKvsRSh_U")
