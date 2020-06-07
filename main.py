'''BEATBOXER'''


import discord
import signal
import time
import random
import math
import sys

#id = 536306191421145110

version = '0.1.2'

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
        return job[user][0], job[user][1]
    except KeyError:
        job[user] = [0,0]
        return job[user][0], job[user][1]

def setjob(user, new_job=None, number_of_hours=None):
    if new_job is None:
        new_job = getjob(user)[0]
    if number_of_hours is None:
        number_of_hours = getjob(user)[1]
    job[user] = [new_job, number_of_hours]

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

def terminate_handler(signal, frame):
    print('Caught termination signal, exiting.')
    save_all()
    sys.exit(0)
signal.signal(signal.SIGINT, terminate_handler)

@client.event
async def on_ready():
    channel = client.get_channel(713162380338659426)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="'Phenomonal Loop' on YouTube: https://www.youtube.com/channel /UChAvZlXVfJGSg0tgd9l7GzQ"))
    print('Successfully logged in and online')
    await channel.send(f'Bot booted up and running. **Version {version}**.')
    #I am SUCH A GENIUS!!!

    #Geeson: Are you tho?

@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "join-quit":
            print('Recognized that ' + member.name + ' joined Beatbox Studio')
            await channel.send(f"""Welcome to the **Beatbox Studio**, {member.mention} :fire::fire::fire:!""")

@client.event
async def on_member_remove(member):
    for channel in member.guild.channels:
        if str(channel) == "join-quit":
            print('Recognized that ' + member.name + ' quit Beatbox Studio')
            await channel.send(f"""Goodbye **{member.name}**, hope you had a good time in Beatbox Studio :cry:.""")

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
        
        elif message.content.lower() == "|help currency" or message.content.lower() == "|help $":
            embed = discord.Embed(title = 'Beatboxer Cmds, Currency', description = 'Have time on your hands? Try this exclusive currency, provided by Beatboxer!', color = 0x4161ff)
            embed.add_field(name = '|balance', value = "Also |bal, Beatboxer will tell you your current Disc balance (Beatboxer's exclusive currency!")
            embed.add_field(name = '|leaderboard', value = 'Also |lead, Beatboxer will tell you the current most wealthiest members in Discs!')
            embed.add_field(name = '|daily', value = 'Will give you your daily 2500 Discs. 24 hour cooldown.')
            embed.add_field(name = '|jobs', value = 'Will let you know of available jobs by providing a full on list! You can choose one job.')
            embed.add_field(name = '|work', value = 'Type |work *job you want* to get the job, |work quit to quit your job (12 hour cooldown before applying for another job) or just |work to work. You may work once per hour.')
            embed.add_field(name = ':fire:', value = 'Just type it and you will get 5 Discs! 3 second cooldown.')
            embed.add_field(name = '|give', value = 'Use the syntax |give [target] [amount] to give who you want to give the amount of Discs indicated!')
            embed.add_field(name = '|parent', value = 'Just in case you need $$$, and, trust me, you would WANT THAT $$$.')
            await message.channel.send(embed = embed)

        elif message.content == "|hi":
            number = random.randint(1, 50)
            if number <= 10:
                await message.channel.send("Hello!")
            elif number <= 20:
                await message.channel.send("Howdy!")
            elif number <= 30:
                await message.channel.send("Hi.")
            elif number <= 40:
                await message.channel.send("Heyo, how's it goin'?")
            elif number <= 50:
                await message.channel.send("Wassup, how's the vibing?")
       
        elif message.content == "|users":
            await message.channel.send(f"""# of members: {guild_id.member_count}""")
       
        elif message.content.startswith('|say'):
            await message.channel.send(message.content[5:])
       
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
            embed.add_field(name='Fast Food Worker', value='850 Discs/hr, 1 hr/day required') # 1
            embed.add_field(name='Firefighter', value='945 Discs/hr, 1 hr/day required') # 2
            embed.add_field(name='Prostitute', value='180 Discs/hr, 8 hr/day required') # 3
            embed.add_field(name='Nuclear Scientist', value='2150 Discs/hr, 4 hr/day required') # 4
            embed.add_field(name='COVID-19 Analyst', value='2325 Discs/hr, 6 hr/day required') # 5
            await message.channel.send(embed=embed)
        
        elif message.content.lower() == '|work fast food worker':
            if getjob(user)[0] == 0 and getquit(user) < time.time():
                setjob(user, 1, 0)
                setsalary(user, 850)
                await message.channel.send("Congratulations! You are now working as a fast food worker!")
            elif getjob(user)[0] != 0:
                await message.channel.send("You already work a job. You have to '|work quit' your current job and wait 12 hours to work this job.")
            elif getquit(user) > time.time():
                await message.channel.send(f"""Nonononono, you cannot apply for a job for another **{int((quit[user]-time.time())/3600)} hours, {int((quit[user]-time.time())/60)%60} minutes, and {int(quit[user]-time.time())%60} seconds**""")

        elif message.content.lower() == '|work firefighter':
            if getjob(user)[0] == 0 and getquit(user) < time.time():
                setjob(user, 2, 0)
                setsalary(user, 945)
                await message.channel.send("Congratulations! You are now working as a firefighter!")
            elif getjob(user)[0] != 0:
                await message.channel.send(f"""Nonononono, you cannot apply for a job for another **{int((quit[user]-time.time())/3600)} hours, {int((quit[user]-time.time())/60)%60} minutes, and {int(quit[user]-time.time())%60} seconds**""")
            elif getquit(user) > time.time():
                await message.channel.send(f"""Nonononono, you cannot apply for a job for another **{int((quit[user]-time.time())/60)%60} minutes and {int(quit[user]-time.time())%60} seconds**""")

        elif message.content.lower() == '|work prositute':
            if getjob(user)[0] == 0 and getquit(user) < time.time():
                setjob(user, 3, 0)
                setsalary(user, 180)
                await message.channel.send("Congratulations! You are now working as a prostitute!")
            elif getjob(user)[0] != 0:
                await message.channel.send("You already work a job. You have to '|work quit' your current job and wait 12 hours to work this job.")
            elif getquit(user) > time.time():
                await message.channel.send(f"""Nonononono, you cannot apply for a job for another **{int((quit[user]-time.time())/3600)} hours, {int((quit[user]-time.time())/60)%60} minutes, and {int(quit[user]-time.time())%60} seconds**""")

        elif message.content.lower() == '|work nuclear scientist':
            if getjob(user)[0] == 0 and getquit(user) < time.time():
                setjob(user, 4, 0)
                setsalary(user, 2150)
                await message.channel.send("Congratulations! You are now working as a nuclear scientist!")
            elif getjob(user)[0] != 0:
                await message.channel.send("You already work a job. You have to '|work quit' your current job and wait 12 hours to work this job.")
            elif getquit(user) > time.time():
                await message.channel.send(f"""Nonononono, you cannot apply for a job for another **{int((quit[user]-time.time())/3600)} hours, {int((quit[user]-time.time())/60)%60} minutes, and {int(quit[user]-time.time())%60} seconds**""")

        elif message.content.lower() == '|work covid-19 analyst':
            if getjob(user)[0] == 0 and getquit(user) < time.time():
                setjob(user, 5, 0)
                setsalary(user, 2325)
                await message.channel.send("Congratulations! You are now working as a COVID-19 Analyst! Note: This job is exclusive and only temporary; once this job is deleted after long notice, you will be fired and will have to wait 12 hours to apply for another job.")
            elif getjob(user)[0] != 0:
                await message.channel.send("You already work a job. You have to '|work quit' your current job and wait 12 hours to work this job.")
            elif getquit(user) > time.time():
                await message.channel.send(f"""Nonononono, you cannot apply for a job for another **{int((quit[user]-time.time())/3600)} hours, {int((quit[user]-time.time())/60)%60} minutes, and {int(quit[user]-time.time())%60} seconds**""")

        elif message.content == '|work quit':
            if getjob(user)[0] != 0:
                setjob(user, 0, 0)
                setwork(user, 0)
                setsalary(user, 0)
                quit[user] = time.time() + 43200
                await message.channel.send("You quit your job. You have to wait **12 hours** until you can apply for another job.")
            else:
                await message.channel.send("You don't have a job to quit, you idiot.")

        elif message.content == '|work':
            #1 = Fast food worker
            #2 = Firefighter
            #3 = Prostitute (!)
            #4 = Nuclear scientist
            #5 = COVID - 19 Analyst
            if getjob(user)[0] == 0:
                await message.channel.send('You need to have a job to work. Try "|jobs" and do "|work *job*" to apply for the job you want to apply for.')
            if getjob(user)[0] != 0 and (user in work) and work[user] > time.time():
                await message.channel.send(f"""You need to wait **{int((work[user]-time.time())/60)%60} minutes and {int(work[user]-time.time())%60} seconds** before you could work again""")
            else:
                await message.channel.send(f"""You successfully worked and got {str(salary[user])} Discs!""")
                setjob(user, None, getjob(user)[1]+1)
                work[user] = time.time() + 3600
                setdiscs(user, getdiscs(user)+getsalary(user))
        
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
                await message.channel.send("Can't rob. Sorry.")
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
                    await message.channel.send(f'**Parent** You know, I used to be a great DJ back in my day... *proceeds to reminesce* **{numberfinal} Discs** ')
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
            embed.add_field(name = '**Pet Blue Ball**', value = '5500 Discs')
            embed.add_field(name = '**Pet Shrub**', value = '9500 Discs')
            embed.add_field(name = '**Pet Cat**', value = '15500 Discs')
            embed.add_field(name = '**Pet Dog**', value = '16000 Discs')
            embed.add_field(name = '**Pet Parrot**', value = '31500 Discs')
            embed.add_field(name = '**Pet Bear**', value = '75000 Discs')
            embed.add_field(name = '**Pet Tiger**', value = '185000 Discs')
            embed.add_field(name = '**Pet Computer**', value = '355000 Discs')
            embed.add_field(name = '**Pet DJ** (No, this is *not* slavery)', value = '725000 Discs')
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
                    embed.set_thumbnail("https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F37%2F2016%2F05%2F15230910%2Funconventional-zen-garden-boxwood-102003721.jpg")
                    await message.channel.send(embed = embed)
                elif getpet(user) == 3:
                    embed = discord.Embed(title = "**Your pet**", description = "Pet cat")
                    embed.set_thumbnail("data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxISEhUQExIQEhIVEBASEBAQDw8PEBUPFRUWFhUSFRUYHSggGBolGxUVITEhJSkrLi4uFx8zODMtNygtLisBCgoKDg0OFRAQFy0ZFR0rLS0rLS0tLS0tKy0tKy0tLS0tLS0tLS0tLS0tLS0tNys3Nzc3LS03LS03LSsrKzctK//AABEIAOEA4QMBIgACEQEDEQH/xAAcAAAABwEBAAAAAAAAAAAAAAAAAQIDBAUGBwj/xAA8EAACAQMCBAMHAgMGBwEAAAAAAQIDBBEFIQYSMVFBYXEHEyIyQoGRFFJDobEVcoLB0fAWIzRTYpLhF//EABkBAAMBAQEAAAAAAAAAAAAAAAABAgMEBf/EACARAQEBAQEAAwEAAwEAAAAAAAABEQISAyExQQQTMiL/2gAMAwEAAhEDEQA/AOV145wV1aG5byj8LwiprxZpGlNIXB49RtChUl/oVebksNnQaEm0m+3U5bp124vCeOxveHLyUotSeexl1G/x1o7eo49GTnSpXC5ZxWemcLJVwnkfhUw8kc3KuyMfxRwPUhLnpLmTfh2Mlc27guWSaZ3e3vIyWH6bkLVeFqFeL2xJrZrZ5NpWHXOOEAUTW6rwbVo1VFJyh+4RV4WqrdRePQpGMtygwXtXQZrLaf4YzHQ6jXNyyXbYWhTjmMolz0uovB/gj1aMovDWA0GGAXVjgTgYEDIp+gtUhEQkJlIXJDeAA2EHkJgYwxIAAwBBjAAAAAuKHR+hV10XNnBNfYqruOMrzCHUFgAEgI7bv4kafRtW5ZpY22RmI9y30ehzPOcLPiTYrmukW1dNZ7klIrdOlFxUU84LKjIwv66eb9JVFPJdWs3t2K+2jnqWNPbBU6Z9RInRjLqunQVK2j+1CYsdgytRiNV0ynLrFfgWtHp4xhfgloeix6WKeroNFveMfwU9/wAE29V9MeaNZz7h4KhWOdXvs1ptfBJ57si2fs2Sl8csryOocojlwGkwk/Z3SxiP5IlX2eY3Utux0eMgmAxyLU+DJRjlRf2Rir6ylTeGmj0k4prDWTPa5wrQr+GG+y8R6McFhTbEM63W9n8Ungo7v2fVfpxjzD6hSVz7IefJmzo8A13NKSxHxNbY8D0ILElzfzFeory5XaWNSe0Yt/YtbThWtL6Wjq9vptGkvhhFeeEFVvoxzhIn0ucOa/8ABdXswHQP7RYBeqfiOY2rxsV+oU/ifnuXMIJYK3Un8XTqjVkpJIMVU7dhCYJpdNkyhVkls8EKLJFHsKnGn4bvZKaT3TN3aU29zCcLW7lNHTbGjhbmN+2/N+j9CngkwkN5FZIUk0pkiJCpkuA/SbEmmwTYmITeRzoYOItSGshSmX6TYfcxEqhGnWC94VE4kKoB1CK6grn2GLD/ADMKFQYlPYblPArTkTveLuMTkkVda7wQ7m8ZFq+eVjcXST6lfc6j2Kmvd98+QxCq2SvynzuZS8WNKGRMUOpNblYk17oA/wC9APC2Ob20WRdUi+pMt5PIzq0cxybSMLVBW6jY/XiMsVLQyTrCGWl5ohrBoeHrZSmtvFE37iua2nC+n4xI18XhFfYQUYJJYEXmpxp/M8GFreRaJhqWCsstUpz6SX5LHOSKo7SeSTTZDjsSaQtCYpCZTwN5G5TFKeHnMJyIlSoNKtv1L1OJM5B4GYzQrnNpUWFsDYMgaKSS5AnIS1gZmyKqGq0StrQZY1JYGJSIXKpKtBt7hRpNdCfWXiReZ52KitKUsbEhVF47keElLbxG7nMN+qLiKmbdgFN/a8e4C8T9MrSjuM6isxaJFIaud0ymOM/UlsMtD8ljK7DUhUsO29HLSOhcIaTjEmYrS6eZLHc6poNHlgjHu404i9pUkUnFOnKVNtLuaGm9h6dKMlho59dEjglW7qUqjSbWGa3hTiec5qEs9smi13gilWzJPll5IrdD4QdvPmbyafVjP71tKfRMfiRYywPRqk40kSJyG5LIFITUqKKzkjDpupHcYeEU+scQxp57mRv+L5bpZLnNqbXQ/fxW2VntkcjXXl+TnFrxNTqQcZNwqJNpvoyHYcRXLnhPmWe2TWVH663CS/2x9GW0m7qzS5lj7Gkt0/Er1CsOyjkjVKROcfMTOkg/RKqqkRhwLOVuMO2ZPkara8exEz3Rczs9vEqbum08AekU6OXsRddrKnSeX4FlTXJFuWxguLdW95LkT2yXyjuqz9dH9z/ICmyEXrPWqcMEas9u4/KpsRKzKwKep8xH8SRcLcaWMioX3Dcc1EdOtHhJeRznhSOZo6DnGPQ5+2nK5o1STCoU9vcEyFUysaypkpkStMRc1+WOSr/VuTwE+lSas6bH1gqYXWCTQulIa8TnIYuIOSHoxHow6CTWQ1Lhr3uXnlZnrjgup9Lz6o6jKn5C1S9B+sLHKrPgWrL5nsjW6NwjCjhtZNRGIQetGQmFKMdkkSFNDORDmVEdH5VBLqjLmIczWIxK5w+oxFjsWNJcYbYIlezTeSTziZyHhKbiOnihLHY4pfZcnv4s7hrS5qUl5M4nqtHlnL1HmJqFyACywAGnlHYjXMkkTJkG5isYNArq++BqMFnJMrUm1shFK37v+ZFDScI0/jybG4kZThlKL26miqVcmdawdKu8lrb1impywTaFZGVi4tLmnzReOxm3cOnLEi/p3SWxTavSUviRONvjiFcaj5PHkP2Fy87Jg06iujX5NDZWkOuEC+j+nTk1uWDG6eI9A5VAZU5JhKbI7rDc64k6mOoIdQgyuxn9Wu+AwrU6pWI067I0q3ZiFWNIlNVQUpEalUHvArSSI1RcK+5Cc2F7wNKrF1AucixqilI15+0VF1WXwS9Gcf1uXxyXmzrmpSzBryORazT+OW/i/wCpdiVVgMVhgFgaWayRKzjkk1JESUd8scOCqT2aXYZo2/RyeSVKKXqRveJbE2nWj0B5lsaCVPcqOGaWVnBfqjkx6q4gy2FQrkmtQKi7g4sn9UsKl+l1e5Cr33hn7FBqNeTzuVsbma8yvLXjpuLO6TLi2uJeD+xzajfyjusl9puu52lsybyfVbqN2KVYoKOoprwJUbvzJxnq0dTxEymmQFcvrkP9QBF1qyWww/iQ27jI5Tw15jKi9yyTQgwoDtMNIuMcDmBKHEGgMCZQF5HBhGewqNQkuI3Okjo4RVVrNfEH6HKdVqNyb8zqOuQ+BvyZy3UXu/U0ZIO4A/uEINIRGsy8iTNjMdhKgq+EiJQiubfuP1ll9RmgsSJqq6BoSioLHYtYGc4euljBoUzn6acjaK3UaW2cFmQbt5FDZ26tObohFDTl0cS8pxQ+qSHesVzVBPSoYIs9PxujTSooadpkJdazMZWjcShLG5c22oeG3+Y/U0uLecCVpaWGhsrElXSxtL8iVqL6DDsvNhwtPASIe/UPOSXRrsbo23cm0rXyFTPUaqJNKoiNG1YuFBpi05EuEhcZEeD3JKGVh2MR2K3wMKQ4plRJ6QifQROqJdU6OPxnVZqrThL0ZyrV4fE15nUdXqrlfocs1d/G/UaIrwBZYBabRVHt4EfOSvlfyYlX0uyGqJrWCNOTUgv1TfgBwy87iNqOGrlZwavnOfabP3b5jRw1+GFntujLrletBGXmMVGip/4ipeYa1ug/qx6oz8jUvmwx33uxXVdTpS6TQ2r2P7sh5PVo345EOqyujeLuPq7jjqLFek+nNByqrcrHdJdBmd4VIVqydRClNFXSuG30LK0t2xdfRc/adQRPoyWCPStcEl0SLVYdUxRGUcMcdQkxy7i4zGOcTKoWVSveLwApkOM2hz3hpzGXVSZSG5yEOZGuLlLxOnmM7Vfrc8Qb8jmt9PMmbDie+XI0nuYSpJ5YqUHkAgBIGmHBN9E5eiydG0D2ZTklO4lyr9kfmN5pfCVpRxyU19ypDjh9jpFxUeI0qj/wtI0lnwTeSx/ysL/ykdqoUIR2jGC9EOZ8gsOVyGfAl2/pS8sjU+A7z9q9TskmFIixTiNXge9W3Kn+SLV4OvY/ws+h3hBSIwPPj4duovehU+wmVhXj1p1F9mehU12X4GpUIPrGP4QG88vni91NeqYKlx5v+aO+19JoS604/grbjhCzn1p49NhHjiDvH3Djdy7nXbn2cWkunMivr+zCj9NRoYc3hqU49Cws+JaseqRqqvsvl9NVfcgV/Zzcx6cshfVLLEKnxdPO6JlPi7vAg1eCryP8LPoRp8P3MetGf2QrzD9VoIcU0n1jJD0OI6T7ryaMjUsKketOa/wsEaT7P7rAvI2trDWaL+pDivab3UkYhU2KSa8WPyPTeQuYvxQtVE/FGIhUfXP9RcLqa6Sf5LkxPX22UmQri25vUz8dRqL6n+RX9t1F5+prKysRdd0yfUyVeg4vc1F1xPOS5XGOO5RXd2pdUs+QrdVEAMPn8ggw3pinV9P6hXF3CnCU5vljGOW2/Ah05mD9q+suMYWsekt5GvUxE+0m79rMFPEKTcE2srxXc03D/HNndYXN7up+2W25wSnERlqWU2sdGnhmPpT1G6kMZ5o4/vIQqsH9Uf8A2R5leqV2kvfVceHxsdo6hX/71VP++wU9MxWd108gnH/eThWh+0O7tkotqrBPdVM5wdh4Y4gpXtFVYNKX1wTzgmms1ESkOPYCRIIaE8o5gJoSpSGAPAbQlE8wMh4BFEUDiEkuy/AeAgIipbwfWMX9kRKuj0JdaUH9ibkIemqqnC1pL+Gl6ECrwNbS6c0fRmkQpMU6TYxtT2fQ+ms16oj1PZnW6wrU35ZNzkNTfcv0Xly674Lu4fRzecWilvtDuIZTpVPw2dsVRh+8+/2RU7K8vNt3bTi/ijJeqaIj2PSte0oVPnpQk+7iirvOD7Gr1oxXosD9QvLz7zIB3P8A/OrH9gA9DzU9HMfalQcbiFTrFwx90dM5vEwntWqpQoxfXdnZ3+Meb9ueJjMvyOzmnjAnKOVqKdVNYxgbi8McpSUZZ6+TE1JJvbuNQIstC1mtaz95Sm1vvH6X3K1Cwod34W45pXSxJclRL4uzNEr6m/qPN1heOjUjUi3tJN4fVHWdN1JVqaqR6Pz8TO3A36kn4oGTHU7p/u/mPRv5L6jO9wea1jQWDNQ1Of7ibb6q8pPdfzD1D+1u0Fgg3euUKbSlLGdl6+ZKt7mE1mEoy74YaelgwKYEKnpPKFyhhpgCQYFCWxAMBNB5DAiUBBgiMxIAtR/34AUl3iLS9CyAHPH90fygD9FrN2VzGccwfMvI5x7Tbj3lWKXSCwu+Svsddq0ViMmiFf3Uqr5pNvP9TsvybGHPP2p4Btj7t3vsO2un1J/LFtGd/GlQs5EuJLvdPq0n8UWl4bEVb+opfoanWmnue6aSH5aLPyaH7Wg4xXX7Eqlczh/ozC9p9K+ppE14Z6bGr4TuuSn7uSxu/HBSVbyUuouF1tt17k3vR7beFSL3THXPyMH+scfqf5JlLUppc0ZZ+/iZ2L/2Ne546vA9QqY6P7mLlrFRpZYI6rUfjj7ho9tJxBGDSk3u2kn5nQuH9Ho04QjCUXNwTk08s41UrTqbN9upc6Xe1qE1NVXzY6Z6rsbfHZ/WV7uuxy0ufgMTsJrblf2KXTePOaKjJfFsm/MkVONZZxGGX3w8fk2/8qnab+nfZjfIIpcVwcfiUObDxBZTf3KK41yc23nlXY5/k+TnlrxbWhcBLiUFvrE0990aTS6tKvHPMozz8reNhfH8k7uHb5NcompNJZbUV3bBrFLFJzi+ZJ4bj3MJqVxKr8LnJLtkru+UX5Gi1Lie3pbc3M+yM9dccyfyQST2TZApaNDx+IkPRKXytNZ6Psc/+zWd71V3fFNzL+I8POcEGOq13n45vPn4i7/S3Sm47YT6t+D8RyzsMtNyWF27BrO9VH/W1/3y/IC6/T0+6/ACdG1ziv1F+CCAejG/KTT/AMi80bovuAAfL+J6/S+I/kMPT+b7gARz/wAm1Vr0XoM1PmYAGNRTUeoj/wCgAT/UkVh7TvEMA6oZJpgASaVD/QmVfmh6AAXwmnLf5jS2fygAV/UjrfNH0YF0AA4f8j9dfwnY9A4dQAK/xf8Aovm/Fxo3/TS9TKT+Z+oYDo+dzVNpdPuSq/0gAcv9TGU43+eP2/oVulgAbT8C2AABAf/Z")
                    await message.channel.send(embed = embed)
                elif getpet(user) == 4:
                    embed = discord.Embed(title = "**Your pet**", description = "Pet dog")
                    embed.set_thumbnail("https://images-na.ssl-images-amazon.com/images/I/81-yKbVND-L.png")
                    await message.channel.send(embed = embed)
                elif getpet(user) == 5:
                    embed = discord.Embed(title = "**Your pet**", description = "Pet parrot")
                    embed.set_thumbnail("https://cdn-central.azureedge.net/-/media/images/kaytee-na/us/learn-care/ask-the-pet-bird-experts/ways-to-show-parrot-love/parrot%20png.png?h=304&la=en&w=499&hash=D9B5C2B1A3D578FB86E0237C99E4DB6E2BB9878C")
                    await message.channel.send(embed = embed)
                elif getpet(user) == 6:
                    embed = discord.Embed(title = "**Your pet**", description = "Pet Bear")
                    embed.set_thumbnail("data:image/jpeg;base64,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")
                    await message.channel.send(embed = embed)
                elif getpet(user) == 7:
                    embed = discord.Embed(title = "**Your pet**", description = "Pet tiger")
                    embed.set_thumbnail("https://api.time.com/wp-content/uploads/2020/03/tiger-king-joe-exotic-netflix.jpg")
                    await message.channel.send(embed = embed)
                elif getpet(user) == 8:
                    embed = discord.Embed(title = "**Your pet**", description = "Pet computer")
                    embed.set_thumbnail("https://i.kym-cdn.com/entries/icons/mobile/000/005/635/63e51038_f4b0_682c.jpg")
                    await message.channel.send(embed = embed)
                else:
                    embed = discord.Embed(title = "**Your pet**", description = "Pet Beatboxer")
                    embed.set_thumbnail("https://ibb.co/CvqnRyN")
                    await message.channel.send(embed = embed)

    save_all()

client.run(token)