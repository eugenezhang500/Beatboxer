'''BEATBOXER'''

#To revert Beatboxer Testing main.py to Beatboxer main.py, get rid of 'Beta Testing' while defining the 'version' variable and replace "|" with "|"

import discord
import signal
import time
import random
import math
import sys
from discord.ext import tasks

print(sys.version)

#id = 536306191421145110

version = '0.1.4'

def read_token():
    with open("beatboxertoken.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

client = discord.Client()

with open('currency', 'r') as f:
    discs = eval(f.read())
with open('daily_timestamps', 'r') as f:
    daily = eval(f.read())
with open('work_timestamps', 'r') as f:
    work = eval(f.read())
with open('users_jobs', 'r') as f:
    job = eval(f.read())
with open('quit_job_timestamps', 'r') as f:
    quit = eval(f.read())
with open('salary_per_user', 'r') as f:
    salary = eval(f.read())
with open('fire_timestamps', 'r') as f:
    fire = eval(f.read())
with open('parent_timestamps', 'r') as f:
    parent = eval(f.read())
with open('users_pet', 'r') as f:
    pet = eval(f.read())
with open('pet_disown_timestamps', 'r') as f:
    disown = eval(f.read())
with open('search_timestamps', 'r') as f:
    search = eval(f.read())

def getdiscs(user):
    try:
        return discs[user]
    except KeyError:
        discs[user] = 0
        return 0

def setdiscs(user, new_discs):
    discs[user] = new_discs

def setwork(user, new_work_timestamp):
    work[user] = new_work_timestamp

def getjob(user):
    try:
        return job[user][0], job[user][1], job[user][2]
    except KeyError:
        job[user] = [0,0,0]
        return job[user][0], job[user][1], job[user][2]

def setjob(user, new_job=None, number_of_hours=None, new_maximum=None):
    if new_job is None:
        new_job = getjob(user)[0]
    if number_of_hours is None:
        number_of_hours = getjob(user)[1]
    if new_maximum is None:
        new_maximum = getjob(user)[2]
    job[user] = [new_job, number_of_hours, new_maximum]

def getsalary(user):
    try:
        return salary[user]
    except KeyError:
        salary[user] = 0
        return 0

def setdisown(user, disown):
    disown[user] = disown

def setsalary(user, changed_salary):
    salary[user] = changed_salary

def getquit(user):
    try:
        return quit[user]
    except KeyError:
        quit[user] = 0
        return 0

def getfire(user):
    try:
        return fire[user]
    except KeyError:
        fire[user] = 0
        return 0

def getparent(user):
    try:
        return parent[user]
    except KeyError:
        parent[user] = 0
        return 0

def getpet(user):
    try:
        return pet[user]
    except KeyError:
        pet[user] = 0
        return 0

def setpet(user, new_pet):
    pet[user] = new_pet

def getdisown(user):
    try:
        return disown[user]
    except KeyError:
        disown[user] = 0
        return 0

def getsearch(user):
    try:
        return search[user]
    except KeyError:
        search[user] = 0
        return 0

def setsearch(user, search_timestamp):
    search[user] = search_timestamp

class LeaderBoardPosition:

    def __init__(self, user, discs):
        self.user = user
        self.discs = discs

def save_all():
    with open('currency', 'w') as f:
        f.write(repr(discs))
    with open('daily_timestamps', 'w') as f:
        f.write(repr(daily))
    with open('work_timestamps', 'w') as f:
        f.write(repr(work))
    with open('users_jobs', 'w') as f:
        f.write(repr(job))
    with open('quit_job_timestamps', 'w') as f:
        f.write(repr(quit))
    with open('salary_per_user', 'w') as f:
        f.write(repr(salary))
    with open('fire_timestamps', 'w') as f:
        f.write(repr(fire))
    with open('parent_timestamps', 'w') as f:
        f.write(repr(parent))
    with open('users_pet', 'w') as f:
        f.write(repr(pet))
    with open('pet_disown_timestamps', 'w') as f:
        f.write(repr(disown))
    with open('search_timestamps', 'w') as f:
        f.write(repr(search))

def terminate_handler(signal, frame):
    print('Caught termination signal, exiting.')
    save_all()
    sys.exit(0)
signal.signal(signal.SIGINT, terminate_handler)

async def reset_job_today():
    await client.wait_until_ready()
    while not client.is_closed:
        if time.time()%84600 == 0:
            await asyncio.sleep(84600)
            for user, data in job.items():
                job[user][1] = 0

@client.event
async def on_ready():
    channel = client.get_channel(713162380338659426)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="'Phenomonal Loop' on YouTube: https://www.youtube.com/channel /UChAvZlXVfJGSg0tgd9l7GzQ"))
    print('Successfully logged in and online')
    await channel.send(f'Bot booted up and running. **Version {version}**.')

@client.event
async def on_member_update(before, after):
    if len(before.roles) < len(after.roles):
        newRole = next(role for role in after.roles if role not in before.roles)
        channel = client.get_channel(649833392854007808)
        print(f"""Recognized that {after.name} has been promoted to {newRole.name}""")
        await channel.send(f"""Congratulations {after.mention} for getting promoted to **{newRole.name}**!!""")

@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "join-quit":
            print('Recognized that ' + member.name + f' joined {member.guild}')
            await channel.send(f"""Welcome to the **{member.guild}**, {member.mention} :fire::fire::fire:!""")

@client.event
async def on_member_remove(member):
    for channel in member.guild.channels:
        if str(channel) == "join-quit":
            print('Recognized that ' + member.name + f' quit {member.guild}')
            await channel.send(f"""Goodbye **{member.name}**, hope you had a good time in the {member.guild} :cry:.""")

@client.event
async def on_message(message):
    guild_id = client.get_guild(536306191421145110)
    channels = ["beatboxer"]
    if message.author == client.user:
        return
   
    user = message.author.id
    name = message.author.name

    if str(message.channel) in channels:

        if message.content == "|help":
            embed = discord.Embed(title = 'Beatboxer Cmds', description = 'Type "|help *section*" to receive an embed on **that specific section**!', color = 0x4161ff)
            embed.add_field(name = ':dividers: Configuration', value = 'All your needs for technical commands are satisfied here!')
            embed.add_field(name = ':clap: Fun', value = 'If you want fun, here you go!')
            embed.add_field(name = ':dollar: Currency', value = 'Have time on your hands? Try this exclusive currency, provided by Beatboxer!')
            await message.channel.send(embed = embed)
        
        elif message.content.lower() == "|help config" or message.content.lower() == "|help configuration":
            embed = discord.Embed(title = 'Beatboxer Cmds, Configuration', description = 'All your needs for technical commands are satisfied here!', color = 0x4161ff)
            embed.add_field(name = '|help', value = 'Beatboxer will send an embed on its available commands')
            embed.add_field(name = '|users', value = 'Beatboxer will tell you how many members are in this current server!')
            await message.channel.send(embed = embed)
        
        elif message.content.lower() == "|help fun":
            embed = discord.Embed(title = 'Beatboxer Cmds, Fun', description = 'If you want fun, here you go!', color = 0x4161ff)
            embed.add_field(name = '|hi', value = 'Say hi to Beatboxer and it will greet back!')
            embed.add_field(name = '|say [message]', value = 'Beatboxer will repeat whatever you type after the |say command!')
            embed.add_field(name = '|fact', value = 'Let Beatboxer say a random fact!')
            embed.add_field(name = '|gayornah', value = 'Get Beatboxer to tell how gay you are!')
            await message.channel.send(embed = embed)
        
        elif message.content.lower() == "|help currency" or message.content.lower() == "|help $" or message.content.lower() == "|help currency 1" or message.content.lower() == "|help $ 1":
            embed = discord.Embed(title = 'Beatboxer Cmds, Currency Page 1', description = 'Have time on your hands? Try this exclusive currency, provided by Beatboxer! For page 2, type "|help currency 2".', color = 0x4161ff)
            embed.add_field(name = '|balance', value = "Also |bal, Beatboxer will tell you your current Disc balance (Beatboxer's exclusive currency!")
            embed.add_field(name = '|leaderboard', value = 'Also |lead, Beatboxer will tell you the current most wealthiest members in Discs!')
            embed.add_field(name = '|daily', value = 'Will give you your daily 2500 Discs. 24 hour cooldown.')
            embed.add_field(name = '|jobs', value = 'Will let you know of available jobs by providing a full on list! You can choose one job.')
            embed.add_field(name = '|work', value = 'Type |work *job you want* to get the job, |work quit to quit your job (12 hour cooldown before applying for another job) or just |work to work. You may work once per hour.')
            embed.add_field(name = ':fire:', value = 'Just type it and you will get 5 Discs! 3 second cooldown.')
            embed.add_field(name = '|give', value = 'Use the syntax |give [target] [amount] to give who you want to give the amount of Discs indicated!')
            embed.add_field(name = '|parent', value = 'Just in case you need $$$, and, trust me, you would WANT THAT $$$.')
            embed.add_field(name = '|pet', value = "Beatboxer shows an embed of your pet's status. Type |pet list for a list of pets to buy, and type |pet buy [pet] to buy the pet, *if you have enough Discs.*")
            await message.channel.send(embed = embed)
        
        elif message.content.lower() == "|help currency 2" or message.content.lower() == "|help $ 2":
            embed = discord.Embed(title = 'Beatboxer Cmds, Currency Page 2', description = 'Have time on your hands? Try this exclusive currency, provided by Beatboxer! For page 1, type "|help currency".', color = 0x4161ff)
            embed.add_field(name = '|search', value = 'You need a pet for this command, but you will search for Discs with your beloved best friend creature!')
            await message.channel.send(embed = embed)

        elif message.content == "|hi":
            number = random.randint(1, 5)
            if number == 1:
                await message.channel.send("Hello!")
            elif number == 2:
                await message.channel.send("Howdy!")
            elif number == 3:
                await message.channel.send("Hi.")
            elif number == 4:
                await message.channel.send("Heyo, how's it goin'?")
            elif number == 5:
                await message.channel.send("Wassup, how's the vibing?")
       
        elif message.content == "|users":
            await message.channel.send(f"""# of members: **{guild_id.member_count}**""")
       
        elif message.content.startswith('|say'):
            await message.channel.send(message.content[6:])
       
        elif message.content.startswith ('|bal' or '|balance'):
            embed = discord.Embed(title = 'Your balance', color = 0x38b328)
            embed.add_field(name = '**Discs**', value = f'{getdiscs(user)}')
            await message.channel.send(embed = embed)
       
        elif message.content.startswith('|lead' or '|leaderboard'):
            leaderboards = []
            for key, value in discs.items():
                leaderboards.append(LeaderBoardPosition(key, value))
            top = sorted(leaderboards, key=lambda x: x.discs, reverse = True)
            embed = discord.Embed(title = 'Most Wealthy Beatboxers', description = f'Your balance: **{getdiscs(user)}**', color = 0xffef10)
            embed.add_field(name = f':first_place: {client.get_user(top[0].user).display_name}', value = f'{top[0].discs}' + ' Discs', inline = False)
            try:
                embed.add_field(name = f':second_place: {client.get_user(top[1].user).display_name}', value = f'{top[1].discs}' + ' Discs', inline = False)
                try:
                    embed.add_field(name = f':third_place: {client.get_user(top[2].user).display_name}', value = f'{top[2].discs}' + ' Discs', inline = False)
                except IndexError: pass
            except IndexError: pass
            await message.channel.send(embed=embed)
       
        elif message.content == '|daily':
            if (user in daily) and daily[user] > time.time():
                await message.channel.send(f"""You need to wait **{int((daily[user]-time.time())/3600)} hours, {int((daily[user]-time.time())/60)%60} minutes, and {int((daily[user]-time.time())%60)} seconds** before getting more!""")
            else:
                await message.channel.send('You got 2500 daily discs!')
                setdiscs(user, getdiscs(user)+2500)
                daily[user] = time.time() + 86400
                save_all()
        
        elif message.content == '|jobs':
            embed = discord.Embed(title='Job list in Beatboxer Currency:', discription='You may choose one job by typing "|work *job*". You may work once per hour.', color=0xff8928)
            embed.add_field(name='Fast Food Worker', value='850 Discs/hr, 2 hr/day maximum') # 1
            embed.add_field(name='Firefighter', value='945 Discs/hr, 3 hr/day maximum') # 2
            embed.add_field(name='Architect', value='1650 Discs/hr, 4 hr/day maximum') # 3
            embed.add_field(name='Nuclear Scientist', value='2150 Discs/hr, 5 hr/day maximum') # 4
            embed.add_field(name='COVID-19 Analyst', value='2325 Discs/hr, 6 hr/day maximum') # 5
            await message.channel.send(embed=embed)
        
        elif message.content.lower() == '|work fast food worker':
            if getjob(user)[0] == 0 and getquit(user) < time.time():
                setjob(user, 1, 0, 2)
                setsalary(user, 850)
                await message.channel.send("Congratulations! You are now working as a fast food worker!")
            elif getjob(user)[0] != 0:
                await message.channel.send("You already work a job. You have to '|work quit' your current job and wait 12 hours to work this job.")
            elif getquit(user) > time.time():
                await message.channel.send(f"""Nonononono, you cannot apply for a job for another **{int((quit[user]-time.time())/3600)} hours, {int((quit[user]-time.time())/60)%60} minutes, and {int(quit[user]-time.time())%60} seconds**""")

        elif message.content.lower() == '|work firefighter':
            if getjob(user)[0] == 0 and getquit(user) < time.time():
                setjob(user, 2, 0, 3)
                setsalary(user, 945)
                await message.channel.send("Congratulations! You are now working as a firefighter!")
            elif getjob(user)[0] != 0:
                await message.channel.send(f"""Nonononono, you cannot apply for a job for another **{int((quit[user]-time.time())/3600)} hours, {int((quit[user]-time.time())/60)%60} minutes, and {int(quit[user]-time.time())%60} seconds**""")
            elif getquit(user) > time.time():
                await message.channel.send(f"""Nonononono, you cannot apply for a job for another **{int((quit[user]-time.time())/60)%60} minutes and {int(quit[user]-time.time())%60} seconds**""")

        elif message.content.lower() == '|work architect':
            if getjob(user)[0] == 0 and getquit(user) < time.time():
                setjob(user, 3, 0, 4)
                setsalary(user, 1650)
                await message.channel.send("Congratulations! You are now working as a architect!")
            elif getjob(user)[0] != 0:
                await message.channel.send("You already work a job. You have to '|work quit' your current job and wait 12 hours to work this job.")
            elif getquit(user) > time.time():
                await message.channel.send(f"""Nonononono, you cannot apply for a job for another **{int((quit[user]-time.time())/3600)} hours, {int((quit[user]-time.time())/60)%60} minutes, and {int(quit[user]-time.time())%60} seconds**""")

        elif message.content.lower() == '|work nuclear scientist':
            if getjob(user)[0] == 0 and getquit(user) < time.time():
                setjob(user, 4, 0, 5)
                setsalary(user, 2150)
                await message.channel.send("Congratulations! You are now working as a nuclear scientist!")
            elif getjob(user)[0] != 0:
                await message.channel.send("You already work a job. You have to '|work quit' your current job and wait 12 hours to work this job.")
            elif getquit(user) > time.time():
                await message.channel.send(f"""Nonononono, you cannot apply for a job for another **{int((quit[user]-time.time())/3600)} hours, {int((quit[user]-time.time())/60)%60} minutes, and {int(quit[user]-time.time())%60} seconds**""")

        elif message.content.lower() == '|work covid-19 analyst':
            if getjob(user)[0] == 0 and getquit(user) < time.time():
                setjob(user, 5, 0, 6)
                setsalary(user, 2325)
                await message.channel.send("Congratulations! You are now working as a COVID-19 Analyst! Note: This job is exclusive and only temporary; once this job is deleted after long notice, you will be fired and will have to wait 12 hours to apply for another job.")
            elif getjob(user)[0] != 0:
                await message.channel.send("You already work a job. You have to '|work quit' your current job and wait 12 hours to work this job.")
            elif getquit(user) > time.time():
                await message.channel.send(f"""Nonononono, you cannot apply for a job for another **{int((quit[user]-time.time())/3600)} hours, {int((quit[user]-time.time())/60)%60} minutes, and {int(quit[user]-time.time())%60} seconds**""")

        elif message.content == '|work quit':
            if getjob(user)[0] != 0:
                setjob(user, 0, 0, 0)
                setwork(user, 0)
                setsalary(user, 0)
                quit[user] = time.time() + 43200
                await message.channel.send("You quit your job. You have to wait **12 hours** until you can apply for another job.")
            else:
                await message.channel.send("You don't have a job to quit, you idiot.")

        elif message.content == '|work':
            #1 = Fast food worker
            #2 = Firefighter
            #3 = Architect
            #4 = Nuclear scientist
            #5 = COVID - 19 Analyst
            if getjob(user)[0] == 0:
                await message.channel.send('You need to have a job to work. Try "|jobs" and do "|work *job*" to apply for the job you want to apply for.')
            elif getjob(user)[0] != 0 and (user in work) and work[user] > time.time():
                await message.channel.send(f"""You need to wait **{int((work[user]-time.time())/60)%60} minutes and {int(work[user]-time.time())%60} seconds** before you could work again""")
            elif getjob(user)[1] == getjob(user)[2]:
                await message.channel.send(f"""You already worked the maximum amount of hours today!""")
            else:
                await message.channel.send(f"""You successfully worked and got **{str(getsalary(user))} Discs**!""")
                setjob(user, None, getjob(user)[1]+1, None)
                work[user] = time.time() + 3600
                setdiscs(user, getdiscs(user)+getsalary(user))
                if getjob(user)[1] == getjob(user)[2]:
                    await message.channel.send(f"""*Note: You have now worked the maximum amount of times you can have worked today.*""")
        
        elif message.content == '🔥':
            if getfire(user) >= time.time():
                await message.channel.send(f"""You need to wait for {int(getfire(user)-time.time())} seconds until you can continue vibing with the :fire:""")
            else:
                await message.channel.send("+5 Discs")
                setdiscs(user, getdiscs(user)+5)
                fire[user] = time.time() + 3
        
        elif message.content.lower() == '|fact':
            number = random.randint(1, 30)
            if number == 1:
                await message.channel.send('The word "muscle" comes from a Latin term meaning "little mouse."')
            elif number == 2:
                await message.channel.send('Tic Tac mints are named after the sound their container makes.')
            elif number == 3:
                await message.channel.send('Peanuts can be used to make dynamite.')
            elif number == 4:
                await message.channel.send('An 11-year-old is responsible for naming Pluto.')
            elif number == 5:
                await message.channel.send('On Mars, sunsets are blue.')
            elif number == 6:
                await message.channel.send('There is a Russian village where every resident is a tightrope walker.')
            elif number == 7:
                await message.channel.send('Only two national flags have the color purple on them. (Dominica and Nicaragua)')
            elif number == 8:
                await message.channel.send('A dog knows when someone is not trustworthy.')
            elif number == 9:
                await message.channel.send('The creation of Mount Rushmore cost less than $1 million.')
            elif number == 10:
                await message.channel.send('The shortest scientific –*ology* word is "oology."')
            elif number == 11:
                await message.channel.send('More than 800 languages are spoken in Papua New Guinea.')
            elif number == 12:
                await message.channel.send('The majority of polar bears live in Canada—not in the Arctic.')
            elif number == 13:
                await message.channel.send('The Eiffel Tower was inaugurated the same year Nintendo was founded; 1889. (That is an ollllld hardware company!!)')
            elif number == 14:
                await message.channel.send('Little brown bats sleep more than any other mammal on earth; ~20 hours.')
            elif number == 15:
                await message.channel.send('A 26-sided shape is known as a small rhombicuboctahedron.')
            elif number == 16:
                await message.channel.send('Great white sharks are so scared of killer whales that they will avoid an area for up to a year after spotting one.')
            elif number == 17:
                await message.channel.send('Honey is essentially bee vomit.')
            elif number == 18:
                await message.channel.send('Beavers have transparent eyelids so they can see underwater.')
            elif number == 19:
                await message.channel.send('Arkansas hosts the annual World Championship Duck Calling Contest.')
            elif number == 20:
                await message.channel.send('There is such a thing as a fear of buttons; koumpounophobia.')
            elif number == 21:
                await message.channel.send('The first TV commercial did not air until the 1940s.')
            elif number == 22:
                await message.channel.send('Singapore plans to build floating suburbs.')
            elif number == 23:
                await message.channel.send("A chameleon's tongue is twice as long as its body.")
            elif number == 24:
                await message.channel.send('Goats have different accents among each other.')
            elif number == 25:
                await message.channel.send('Lightning can heat the air it passes through to 50,000 degrees.')
            elif number == 26:
                await message.channel.send('If you heat up a magnet, it will lose its magnetism.')
            elif number == 27:
                await message.channel.send('Your brain is sometimes more active when you are asleep than when you are awake.')
            elif number == 28:
                await message.channel.send('England is hit with more tornadoes per square mile than any other country in the world.')
            elif number == 29:
                await message.channel.send("The world's oldest operating library is in Morocco.")
            elif number == 30:
                await message.channel.send('Sesame Street is a real place.')

        elif message.content.startswith('|give'):
            try:
                target, amount = message.content.split(' ')[1:]
                amount = int(amount)
            except ValueError:
                await message.channel.send('You incorrectly typed in the "|give" command, please try again (|give [target] [amount])')
            target = target[2:-1]
            if target[0] == '!':
                target = target[1:]
            target = int(target)
            if amount > getdiscs(user):
                await message.channel.send(f"""You don't have enough discs, simpleton. You need {amount-getdiscs(user)} more discs to successfully share 'em.""")
            elif amount < 0:
                await message.channel.send("Can't rob.")
                return
            else:
                setdiscs(target, getdiscs(target)+amount)
                setdiscs(user, getdiscs(user)-amount)
                await message.channel.send(f"""You have successfully given **{amount} Discs**.""")
        
        elif message.content.lower() == '|parent':
            if getparent(user) > time.time():
                await message.channel.send(f"""You have to wait **{int(getparent(user)-time.time())} seconds** before you ask your parents for money! Otherwise, it seems like you're poor... wait, are you?""")
            else:
                number = random.randint(1, 10)
                number2 = random.randint(1, 250)
                number3 = random.randint(4, 24)
                number4 = random.randint(25, 56)
                number5 = random.randint(57, 83)
                number6 = random.randint(84, 154)
                number7 = random.randint(155, 364)
                
                if number2 <= 95:
                    numberfinal = number3
                elif number2 <= 205:
                    numberfinal = number4
                elif number2 <= 235:
                    numberfinal = number5
                elif number2 <= 248:
                    numberfinal = number6
                elif number2 <= 250:
                    numberfinal = number7

                if number == 1:
                    await message.channel.send(f"""**Parent:** Please be patient, I'll be with you soon. Just one more level on Candy Crush.""")
                    parent[user] = time.time() + 30
                elif number == 2:
                    await message.channel.send(f'**Parent:** Fine, have **{numberfinal} Discs**.')
                    setdiscs(user, getdiscs(user)+numberfinal)
                    parent[user] = time.time() + 30
                elif number == 3:
                    await message.channel.send(f'**Parent:** "I am feeling nice, **{numberfinal} Discs** for you."')
                    setdiscs(user, getdiscs(user)+numberfinal)
                    parent[user] = time.time() + 30
                elif number == 4:
                    await message.channel.send(f'**Parent:** I am feeling pissed, you go before I smash your head with my personal axe **>:(**')
                    parent[user] = time.time() + 30
                elif number == 5:
                    await message.channel.send(f'**Parent:** You went to college like a good child, have some money, boy/girl/other, you never know these days... **{numberfinal} Discs**')
                    setdiscs(user, getdiscs(user)+numberfinal)
                    parent[user] = time.time() + 30
                elif number == 6:
                    if getdiscs(user)-numberfinal <  0:
                        numberfinal = getdiscs(user)
                    await message.channel.send(f"""**Stereotypical Asian Parent:** Simpleton, you need financial help? *Stupid child*. I'll take away **{numberfinal} Discs** because you didn't practice 40 hours of piano today!""")
                    setdiscs(user, getdiscs(user)-numberfinal)
                    parent[user] = time.time() + 30
                elif number == 7:
                    await message.channel.send(f"""**Parent:** Ya know what, I'm actually having a half decent day, so here's **{numberfinal} Discs**.""")
                    setdiscs(user, getdiscs(user)+numberfinal)
                    parent[user] = time.time() + 30
                elif number == 8:
                    await message.channel.send(f"""**Parent** You know, you're actually a mistake, but I'll spoil you more by giving you **{numberfinal} Discs**.""")
                    setdiscs(user, getdiscs(user)+numberfinal)
                    parent[user] = time.time() + 30
                elif number == 9:
                    await message.channel.send(f'**Parent:** Here, have **{numberfinal} Discs**. ')
                    setdiscs(user, getdiscs(user)+numberfinal)
                    parent[user] = time.time() + 30
                elif number == 10:
                    await message.channel.send(f'**Parent** You know, I used to be a great DJ back in my day... *proceeds to reminesce...* **{numberfinal} Discs** ')
                    setdiscs(user, getdiscs(user)+numberfinal)
                    parent[user] = time.time() + 30

        elif message.content.lower() == '|gayornah':
            number = random.randint(1, 100)
            if number <= 17:
                embed = discord.Embed(title = '|gayornah', color = 0xff36da)
                embed.add_field(name = f'**{number}% gay**', value = "Congrats! You're not very gay at all.")
                await message.channel.send(embed = embed)
            elif number <= 50:
                embed = discord.Embed(title = '|gayornah', color = 0xff36da)
                embed.add_field(name = f'**{number}% gay**', value = "You're a good gaymer.")
                await message.channel.send(embed = embed)
            elif number <= 75:
                embed = discord.Embed(title = '|gayornah', color = 0xff36da)
                embed.add_field(name = f'**{number}% gay**', value = "Um... Okay, you're pretty gay.")
                await message.channel.send(embed = embed)
            elif number <= 100:
                embed = discord.Embed(title = '|gayornah', color = 0xff36da)
                embed.add_field(name = f'**{number}% gay**', value = "Nononononononono, you're definitely gay.")
                await message.channel.send(embed = embed)
        
        elif message.content.lower() == '|pet list':
            embed = discord.Embed(title = 'Available Beatboxer Pets', description = 'These furry sensations can be cute, help you substantially in the currency, and play with you like its best friend!', color = 0x9e674c)
            embed.set_thumbnail(url = "https://imgflip.com/s/meme/Advice-Doge.jpg")
            embed.add_field(name = '**Blue Ball**', value = '5500 Discs')
            embed.add_field(name = '**Shrub**', value = '9500 Discs')
            embed.add_field(name = '**Cat**', value = '15500 Discs')
            embed.add_field(name = '**Dog**', value = '16000 Discs')
            embed.add_field(name = '**Parrot**', value = '31500 Discs')
            embed.add_field(name = '**Bear**', value = '75000 Discs')
            embed.add_field(name = '**Tiger**', value = '185000 Discs')
            embed.add_field(name = '**Computer**', value = '355000 Discs')
            embed.add_field(name = '**Beatboxer** (No, this is *not* slavery)', value = '725000 Discs')
            await message.channel.send(embed = embed)

        elif message.content.lower() == '|pet buy blue ball':
            #1 = Blue Ball
            if getpet(user) != 0:
                await message.channel.send("You already have a pet, you idiot. (FYI you can only have one pet at a time. If you |pet disown, you have to wait 12 hours before buying another pet)")
            elif getdisown(user) > time.time():
                await message.channel.send(f"""Since you disowned your last pet within 12 hours ago, you have to wait **{int((getdisown(user)-time.time())/3600)} hours, {int((getdisown(user)-time.time())/60)%60} minutes, and {int(getdisown(user)-time.time())%60} seconds**.""")
            elif getdiscs(user) < 5500:
                await message.channel.send(f"""You need **{5500 - getdiscs(user)} more Discs** to be able to buy this pet.""")
            else:
                await message.channel.send("Congrats, you have a new pet Blue Ball!")
                setpet(user, 1)
                setdiscs(user, getdiscs(user)-5500)

        elif message.content.lower() == '|pet buy shrub':
            #2 = Shrub
            if getpet(user) != 0:
                await message.channel.send("You already have a pet, you idiot. (FYI you can only have one pet at a time. If you |pet disown, you have to wait 12 hours before buying another pet)")
            elif getdisown(user) > time.time():
                await message.channel.send(f"""Since you disowned your last pet within 12 hours ago, you have to wait **{int((getdisown(user)-time.time())/3600)} hours, {int((getdisown(user)-time.time())/60)%60} minutes, and {int(getdisown(user)-time.time())%60} seconds**.""")
            elif getdiscs(user) < 9500:
                await message.channel.send(f"""You need **{9500 - getdiscs(user)} more Discs** to be able to buy this pet.""")
            else:
                await message.channel.send("Congrats, you have a new pet shrub!")
                setpet(user, 2)
                setdiscs(user, getdiscs(user)-9500)

        elif message.content.lower() == '|pet buy cat':
            #3 = Cat
            if getpet(user) != 0:
                await message.channel.send("You already have a pet, you idiot. (FYI you can only have one pet at a time. If you |pet disown, you have to wait 12 hours before buying another pet)")
            elif getdisown(user) > time.time():
                await message.channel.send(f"""Since you disowned your last pet within 12 hours ago, you have to wait **{int((getdisown(user)-time.time())/3600)} hours, {int((getdisown(user)-time.time())/60)%60} minutes, and {int(getdisown(user)-time.time())%60} seconds**.""")
            elif getdiscs(user) < 15500:
                await message.channel.send(f"""You need **{15500 - getdiscs(user)} more Discs** to be able to buy this pet.""")
            else:
                await message.channel.send("Congrats, you have a new pet cat!")
                setpet(user, 3)
                setdiscs(user, getdiscs(user)-15500)

        elif message.content.lower() == '|pet buy dog':
            #4 = dog
            if getpet(user) != 0:
                await message.channel.send("You already have a pet, you idiot. (FYI you can only have one pet at a time. If you |pet disown, you have to wait 12 hours before buying another pet)")
            elif getdisown(user) > time.time():
                await message.channel.send(f"""Since you disowned your last pet within 12 hours ago, you have to wait **{int((getdisown(user)-time.time())/3600)} hours, {int((getdisown(user)-time.time())/60)%60} minutes, and {int(getdisown(user)-time.time())%60} seconds**.""")
            elif getdiscs(user) < 16000:
                await message.channel.send(f"""You need **{16000 - getdiscs(user)} more Discs** to be able to buy this pet.""")
            else:
                await message.channel.send("Congrats, you have a new pet dog!")
                setpet(user, 4)
                setdiscs(user, getdiscs(user)-16000)

        elif message.content.lower() == '|pet buy parrot':
            #5 = Parrot
            if getpet(user) != 0:
                await message.channel.send("You already have a pet, you idiot. (FYI you can only have one pet at a time. If you |pet disown, you have to wait 12 hours before buying another pet)")
            elif getdisown(user) > time.time():
                await message.channel.send(f"""Since you disowned your last pet within 12 hours ago, you have to wait **{int((getdisown(user)-time.time())/3600)} hours, {int((getdisown(user)-time.time())/60)%60} minutes, and {int(getdisown(user)-time.time())%60} seconds**.""")
            elif getdiscs(user) < 31500:
                await message.channel.send(f"""You need **{31500 - getdiscs(user)} more Discs** to be able to buy this pet.""")
            else:
                await message.channel.send("Congrats, you have a new pet parrot!")
                setpet(user, 5)
                setdiscs(user, getdiscs(user)-31500)

        elif message.content.lower() == '|pet buy bear':
            #6 = Bear
            if getpet(user) != 0:
                await message.channel.send("You already have a pet, you idiot. (FYI you can only have one pet at a time. If you |pet disown, you have to wait 12 hours before buying another pet)")
            elif getdisown(user) > time.time():
                await message.channel.send(f"""Since you disowned your last pet within 12 hours ago, you have to wait **{int((getdisown(user)-time.time())/3600)} hours, {int((getdisown(user)-time.time())/60)%60} minutes, and {int(getdisown(user)-time.time())%60} seconds**.""")
            elif getdiscs(user) < 75000:
                await message.channel.send(f"""You need **{75000 - getdiscs(user)} more Discs** to be able to buy this pet.""")
            else:
                await message.channel.send("Congrats, you have a new pet bear!")
                setpet(user, 6)
                setdiscs(user, getdiscs(user)-75000)

        elif message.content.lower() == '|pet buy tiger':
            #7 = Tiger
            if getpet(user) != 0:
                await message.channel.send("You already have a pet, you idiot. (FYI you can only have one pet at a time. If you |pet disown, you have to wait 12 hours before buying another pet)")
            elif getdisown(user) > time.time():
                await message.channel.send(f"""Since you disowned your last pet within 12 hours ago, you have to wait **{int((getdisown(user)-time.time())/3600)} hours, {int((getdisown(user)-time.time())/60)%60} minutes, and {int(getdisown(user)-time.time())%60} seconds**.""")
            elif getdiscs(user) < 185000:
                await message.channel.send(f"""You need **{185000 - getdiscs(user)} more Discs** to be able to buy this pet.""")
            else:
                await message.channel.send("Congrats, you have a new pet tiger!")
                setpet(user, 7)
                setdiscs(user, getdiscs(user)-185000)

        elif message.content.lower() == '|pet buy computer':
            #8 = Computer
            if getpet(user) != 0:
                await message.channel.send("You already have a pet, you idiot. (FYI you can only have one pet at a time. If you |pet disown, you have to wait 12 hours before buying another pet)")
            elif getdisown(user) > time.time():
                await message.channel.send(f"""Since you disowned your last pet within 12 hours ago, you have to wait **{int((getdisown(user)-time.time())/3600)} hours, {int((getdisown(user)-time.time())/60)%60} minutes, and {int(getdisown(user)-time.time())%60} seconds**.""")
            elif getdiscs(user) < 355000:
                await message.channel.send(f"""You need **{355000 - getdiscs(user)} more Discs** to be able to buy this pet.""")
            else:
                await message.channel.send("Congrats, you have a new pet computer!")
                setpet(user, 8)
                setdiscs(user, getdiscs(user)-355000)

        elif message.content.lower() == '|pet buy beatboxer':
            #9 = Beatboxer
            if getpet(user) != 0:
                await message.channel.send("You already have a pet, you idiot. (FYI you can only have one pet at a time. If you |pet disown, you have to wait 12 hours before buying another pet)")
            elif getdisown(user) > time.time():
                await message.channel.send(f"""Since you disowned your last pet within 12 hours ago, you have to wait **{int((getdisown(user)-time.time())/3600)} hours, {int((getdisown(user)-time.time())/60)%60} minutes, and {int(getdisown(user)-time.time())%60} seconds**.""")
            elif getdiscs(user) < 725000:
                await message.channel.send(f"""You need **{725000 - getdiscs(user)} more Discs** to be able to buy this pet.""")
            else:
                await message.channel.send("Congrats, you have a new pet Beatboxer!")
                setpet(user, 9)
                setdiscs(user, getdiscs(user)-725000)

        elif message.content.lower() == '|pet disown':
            if getpet(user) == 0:
                await message.channel.send("You don't *have* a pet to disown, you idiot.")
            else:
                await message.channel.send("You disowned your pet. **:(**")

        elif message.content.lower() == '|pet':
            if getpet(user) == 0:
                await message.channel.send("You don't *have* a pet, you idiot.")
            else:
                if getpet(user) == 1:
                    embed = discord.Embed(title = "**Your pet**", description = "Pet Blue Ball")
                    embed.set_thumbnail(url = "https://www.t-molding.com/media/products/sanwa-balltop-light-blue-LB-35-B.jpg")
                    await message.channel.send(embed = embed)
                elif getpet(user) == 2:
                    embed = discord.Embed(title = "**Your pet**", description = "Pet shrub")
                    embed.set_thumbnail(url = "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F37%2F2016%2F05%2F15230910%2Funconventional-zen-garden-boxwood-102003721.jpg")
                    await message.channel.send(embed = embed)
                elif getpet(user) == 3:
                    embed = discord.Embed(title = "**Your pet**", description = "Pet cat")
                    embed.set_thumbnail(url = "https://images-na.ssl-images-amazon.com/images/I/414q6YhWlVL._AC_SX425_.jpg")
                    await message.channel.send(embed = embed)
                elif getpet(user) == 4:
                    embed = discord.Embed(title = "**Your pet**", description = "Pet dog")
                    embed.set_thumbnail(url = "https://media.giphy.com/media/54Vj1kxvgyF4k/giphy.gif")
                    await message.channel.send(embed = embed)
                elif getpet(user) == 5:
                    embed = discord.Embed(title = "**Your pet**", description = "Pet parrot")
                    embed.set_thumbnail(url = "https://cdn-central.azureedge.net/-/media/images/kaytee-na/us/learn-care/ask-the-pet-bird-experts/ways-to-show-parrot-love/parrot%20png.png?h=304&la=en&w=499&hash=D9B5C2B1A3D578FB86E0237C99E4DB6E2BB9878C")
                    await message.channel.send(embed = embed)
                elif getpet(user) == 6:
                    embed = discord.Embed(title = "**Your pet**", description = "Pet Bear")
                    embed.set_thumbnail(url = "https://i.imgur.com/Tdy3xqF.gif")
                    await message.channel.send(embed = embed)
                elif getpet(user) == 7:
                    embed = discord.Embed(title = "**Your pet**", description = "Pet tiger")
                    embed.set_thumbnail(url = "https://media.giphy.com/media/N1dXLHCuqwuM8/giphy.gif")
                    await message.channel.send(embed = embed)
                elif getpet(user) == 8:
                    embed = discord.Embed(title = "**Your pet**", description = "Pet computer")
                    embed.set_thumbnail(url = "https://i.kym-cdn.com/entries/icons/mobile/000/005/635/63e51038_f4b0_682c.jpg")
                    await message.channel.send(embed = embed)
                else:
                    embed = discord.Embed(title = "**Your pet**", description = "Pet Beatboxer")
                    embed.set_thumbnail(url = "https://i.ibb.co/wCTK5q3/Phenomenal-Loop.jpg")
                    await message.channel.send(embed = embed)
    
        if message.content == '|search':
            if getpet(user) == 0:
                await message.channel.send('You need a pet to search. (|pet list)')
            elif getsearch(user) > time.time():
                await message.channel.send(f'You need to wait **{int(getsearch(user)-time.time())} seconds** before you can search for more Discs.')
            elif getpet(user) >= 1:
                searchrandom = random.randint(1,100)
                searchrandom2 = random.randint(1, 20)
                if searchrandom2 <= 19:
                    if  getpet(user) == 1:
                        number = random.randint(11, 32)
                    elif getpet(user) == 2:
                        number = random.randint(16, 41)
                    elif getpet(user) == 3:
                        number = random.randint(27, 62)
                    elif getpet(user) == 4:
                        number = random.randint(42, 93)
                    elif getpet(user) == 5:
                        number = random.randint(68, 156)
                    elif getpet(user) == 6:
                        number = random.randint(106, 340)
                    elif getpet(user) == 7:
                        number = random.randint(156, 512)
                    elif getpet(user) == 8:
                        number = random.randint(206, 632)
                    elif getpet(user) == 9:
                        number = random.randint(264, 732)
                elif searchrandom2 == 20:
                    if  getpet(user) == 1:
                        number = random.randint(63, 92)
                    elif getpet(user) == 2:
                        number = random.randint(98, 128)
                    elif getpet(user) == 3:
                        number = random.randint(126, 179)
                    elif getpet(user) == 4:
                        number = random.randint(165, 285)
                    elif getpet(user) == 5:
                        number = random.randint(255, 483)
                    elif getpet(user) == 6:
                        number = random.randint(423, 792)
                    elif getpet(user) == 7:
                        number = random.randint(686, 1053)
                    elif getpet(user) == 8:
                        number = random.randint(832, 1480)
                    elif getpet(user) == 9:
                        number = random.randint(1231, 2308)

                if searchrandom <= 1:
                    deathmessage = random.randint(1, 5)
                    if deathmessage == 1:
                        await message.channel.send("You went to the local trash dump and unintentionally intoxicated yourself with a lethal dose of stinky socks. You lost 25% of your Discs. Luckily, your pet survived.")    
                    elif deathmessage == 2:
                        await message.channel.send("You went to an alley and came across a masked guy. He does something to you that you don't know, because he killed you. You lost 15% of your Discs. Your pet survives.")
                    elif deathmessage == 3:
                        await message.channel.send("You went to the nearest gas station. Unfortunately, your fuel dispenser malfunctioned and exploded. You died and lost 15% of your Discs. Your pet, much smarter than you, decided to stay in the gas station store and survived.")
                    elif deathmessage == 4:
                        await message.channel.send("You went to a casino and met a drunk man. He whacked you with a glass wine cup, which, unluckily, killed you. You lost 15% of your coins. Fortunately, your pet avenged your death and arrested the man alongside 24 police units, and survived.")
                    elif deathmessage == 5:
                        await message.channel.send("You were casually strolling alongside the highway looking for coins when a car swerved behind you and ran over you, crushing your skull and annihilating your fragile body. You lost 15% of your coins. Your pet was more aware though, and it survived.")
                    setdiscs(user, int(getdiscs(user)*.85))
                    setsearch(user, time.time()+30)
                elif searchrandom <= 5:
                    if getdiscs(user) < number:
                        number = getdiscs(user)
                    await message.channel.send(f"""You got injured while searching and went to the hospital and had to pay **{number} Discs** to pay your fees. Fortunately, your pet didn't get injured.""")
                    setdiscs(user, getdiscs(user)-number)
                    setsearch(user, time.time()+30)
                elif searchrandom <= 100:
                    wheretosearch = random.randint(1, 9)
                    if wheretosearch == 1:
                        number = random.randint(112, 316)
                        if getdiscs(user) < number:
                            number = getdiscs(user)
                            await message.channel.send(f"""**Construction Site:** You got caught when you were looking for Discs with your pet in a construction site! You had to pay **{number} Discs** to the construction manager.""")
                            number = -number
                    elif wheretosearch == 2:
                        number = random.randint(112, 316)
                        if getdiscs(user) < number:
                            number = getdiscs(user)
                            await message.channel.send(f"""**Private Estate:** You got caught while you were looking for Discs with your pet! You had to pay **{number} Discs** to the owner of the estate.""")
                            number = -number
                    elif wheretosearch == 3:
                        await message.channel.send(f"""**Park:** You walked around a local park with your pet found **{number} Discs** in between the trees.""")
                    elif wheretosearch == 4:
                        await message.channel.send(f"""**Neighborhood:** You found **{number} Discs** on your evening stroll with your pet.""")
                    elif wheretosearch == 5:
                        await message.channel.send(f"""**Gas Station:** You got **{number} Discs** at the fuel dispensers and the store while looking for Discs with your pet.""")
                    elif wheretosearch == 6:
                        await message.channel.send(f"""**Bathroom:** You looked in the bathtub, toilet, sink, and cabinets in a public potty with your pet and found **{number} Discs**.""")
                    elif wheretosearch == 7:
                        await message.channel.send(f"""**Work:** You brought your pet to work and found **{number} Discs** in between the cubicals!""")
                    elif wheretosearch == 8:
                        await message.channel.send(f"""**Highway:** You walked alongside Highway {random.randint(1, 99)} South with your pet for a couple of hours and found **{number} Discs**.""")
                    elif wheretosearch == 9:
                        await message.channel.send(f"""**Restaurant:** You got **{number} Discs** while searching the booths and tables with your pet.""")
                    setdiscs(user, getdiscs(user)+number)
                    setsearch(user, time.time()+30)
        if message.content.startswith("|configurationrank"):
            client_configuration_rank = int(client_configuration_rank)
            configuration_ranks.append(client_configuration_rank)
            print(configuration_ranks)

    save_all()

client.loop.create_task(reset_job_today())
client.run(token)