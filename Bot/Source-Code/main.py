



# Explanation: This Discord bot was skillfully crafted by PJ0001, a dedicated Senior Highschool Student with a passion for ethical hacking. PJ0001 invested several days of effort into developing this bot as a means to educate individuals about the realm of ethical hacking.
# With a deep interest in hacking, PJ0001 embarked on this journey to create an educational tool that introduces users to the concepts of ethical hacking. Through this bot, users can explore various functionalities related to cybersecurity while maintaining an ethical perspective.
# PJ0001's dedication to promoting responsible hacking practices shines through in this bot's design, which aims to provide insight into the world of hacking without compromising ethical values. By engaging with this bot, users can gain valuable knowledge and insights into the intriguing realm of cybersecurity.
#Code Starts on Line 60


log_channel = None
temporary_whitelist = {} # Ignore
blacklist = {}
kick_logs_channel = None

# Keep this here!

print('''
  _____     _  ___   ___   ___  __ 
 |  __ \   | |/ _ \ / _ \ / _ \/_ |
 | |__) |  | | | | | | | | | | || |
 |  ___/   | | | | | | | | | | || |
 | |  | |__| | |_| | |_| | |_| || |
 |_|   \____/ \___/ \___/ \___/ |_|              
      ''')

print('''

Explanation: This Discord bot was skillfully crafted by PJ0001, a dedicated Senior Highschool Student with a passion for ethical hacking. PJ0001 invested several days of effort into developing this bot as a means to educate individuals about the realm of ethical hacking.
With a deep interest in hacking, PJ0001 embarked on this journey to create an educational tool that introduces users to the concepts of ethical hacking. Through this bot, users can explore various functionalities related to cybersecurity while maintaining an ethical perspective.
PJ0001's dedication to promoting responsible hacking practices shines through in this bot's design, which aims to provide insight into the world of hacking without compromising ethical values. By engaging with this bot, users can gain valuable knowledge and insights into the intriguing realm of cybersecurity.

''')

# Importd
import requests
import discord
import random
import socket
import asyncio
import datetime
import base64
from discord.ext import commands
import os
from datetime import datetime
from dateutil.parser import parse as parse_date
import json
import subprocess
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import youtube_dl
from discord import VoiceChannel



with open('Source-Code/Config.json', 'r') as config_file:
    config = json.load(config_file)

BOT_TOKEN = config['BOT_TOKEN']
owner_id = int(config['owner_id'])
prefix = config['prefix']
presence_message = config['presence']
IPINFO_API_TOKEN = '7e2934833edb11'  # Replace with your actual API token
RAPIDAPI_KEY = 'f2cd0bb930msh67db8751fac7eb1p1a2e2fjsnb3b5580f8486'  # Replace with your actual RapidAPI key
bot = discord.Bot(debug_guilds=["1119268738278105178"])



sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="9b298b518fc549bc9fc311a7d032c4d1",
                                               client_secret="e6b2e1d3d1ca4663aeefd1293dee64be",
                                               redirect_uri="www.dsc.gg/pxdsec",
                                               scope="user-library-read"))

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=prefix, intents=intents, status=discord.Status.do_not_disturb, help_command=None)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await bot.change_presence(activity=discord.Game(name=presence_message))


@bot.event
async def on_guild_join(guild):
    # Create an embed message
    embed = discord.Embed(
        title="PxD Services",
        description="PxD Services Functions: Here are some things I can do:",
        color=0xfffff0  # You can customize the color of the embed
    )
    
    embed.add_field(name="Real-Time Protection", value="Protects your server against Cheaters - DDossers - Raiders - Leakers, etc.")
    embed.add_field(name="Whitelist System for Ethical Hacking", value="With features like NMAP via Discord and DNS lookup, etc.")
    
    system_channel = guild.system_channel
    if system_channel:
        await system_channel.send(embed=embed)



@bot.slash_command(name="whitelist")
@commands.check(lambda ctx: ctx.author.id == owner_id)
async def whitelist(ctx):
    if whitelisted_users:
        whitelist_message = "Whitelisted Users:\n"
        
        for user_id in whitelisted_users:
            user = await bot.fetch_user(user_id)
            if user:
                if user_id in temporary_whitelist:
                    expiration_date = temporary_whitelist[user_id]
                    whitelist_message += f"{user.name}#{user.discriminator} (ID: {user.id}) - Subscribed until {expiration_date.strftime('%Y-%m-%d %H:%M:%S')}\n"
                else:
                    whitelist_message += f"{user.name}#{user.discriminator} (ID: {user.id})\n"
            else:
                whitelist_message += f"User with ID {user_id} not found\n"
                
        await ctx.send(whitelist_message)
    else:
        await ctx.send("No users are currently whitelisted.")

def save_temp_whitelist():
    with open("temporary_whitelist.txt", "w") as file:
        for user_id, expiration_date in temporary_whitelist.items():
            user_info = f"{user_id} - Subscribed until {expiration_date.strftime('%Y-%m-%d %H:%M:%S')}\n"
            file.write(user_info)


@bot.slash_command(name="tempwhitelist")
@commands.check(lambda ctx: ctx.author.id == owner_id)
async def tempwhitelist(ctx, user_id: int, date_str: str):
    try:
        end_date = parse_date(date_str)
    except ValueError:
        await ctx.send("Invalid date format. Please use a valid date format.")
        return

    if user_id not in whitelisted_users:
        whitelisted_users.append(user_id)
        temporary_whitelist[user_id] = end_date 
        save_whitelist(whitelisted_users)
        await ctx.send(f"User ID {user_id} has been temporarily subscribed until {end_date.strftime('%Y-%m-%d')}.")
        

        save_temp_whitelist()
    else:
        await ctx.send(f"User ID {user_id} is already whitelisted.")



def save_whitelist(whitelist):
  with open("whitelist.txt", "w") as file:
    for user_id in whitelist:
      file.write(str(user_id) + "\n")


def load_whitelist():
  try:
    with open("whitelist.txt", "r") as file:
      return [int(line.strip()) for line in file.readlines()]
  except FileNotFoundError:
    return []

whitelisted_users = load_whitelist()
@bot.slash_command(name="addwhitelist")
@commands.check(lambda ctx: ctx.author.id == owner_id)
async def addwhitelist(ctx, user_id: int):
  if user_id not in whitelisted_users:
    whitelisted_users.append(user_id)
    save_whitelist(whitelisted_users)
    await ctx.send(f"User ID {user_id} has been whitelisted.")
  else:
    await ctx.send(f"User ID {user_id} is already whitelisted.")


@bot.slash_command(name="unwhitelist")
@commands.check(lambda ctx: ctx.author.id == owner_id)
async def unwhitelist(ctx, user_id: int):
  if user_id in whitelisted_users:
    whitelisted_users.remove(user_id)
    save_whitelist(whitelisted_users)
    await ctx.send(f"User ID {user_id} has been removed from the whitelist.")
  else:
    await ctx.send(f"User ID {user_id} is not in the whitelist.")


def is_whitelisted(ctx):
  if ctx.author.id in whitelisted_users or ctx.author.id == owner_id:
    return True
  else:
    non_whitelisted_message = "Hello It Looks Like you don't have a subscription please purchase one at https://discord.gg/XTD3MFtXwq"
    asyncio.create_task(ctx.send(non_whitelisted_message))
    return False

IP_API_URL = 'http://ip-api.com/json/'

blacklist_file = "blacklist.txt"

# Function to load blacklist data from a file
# Function to load blacklist data from a file
def load_blacklist():
    global blacklist
    blacklist = {}  # Initialize an empty dictionary
    try:
        with open(blacklist_file, "r") as file:
            for line in file:
                user_id, reason = line.strip().split(":")
                blacklist[int(user_id)] = reason
    except FileNotFoundError:
        pass  # The file doesn't exist initially

# Function to save blacklist data to a file
def save_blacklist():
    with open(blacklist_file, "w") as file:
        for user_id, reason in blacklist.items():
            file.write(f"{user_id}:{reason}\n")


def load_blacklist():
    try:
        with open(blacklist_file, "r") as file:
            for line in file:
                user_id, reason = line.strip().split(":")
                blacklist[int(user_id)] = reason
    except FileNotFoundError:
        pass  # The file doesn't exist initially



@bot.slash_command(name="addblacklist")
@commands.check(lambda ctx: ctx.author.id == owner_id)
async def addblacklist(ctx, user: discord.User, *, reason=None):
    if user.id not in blacklist:
        blacklist[user.id] = reason
        save_blacklist()  # Save the updated blacklist to the file

        await ctx.author.send(f'You have been added to the blacklist. Reason: {reason}')

        # Kick the user
        try:
            await ctx.guild.kick(user, reason=f'Blacklisted - {reason}')
            await ctx.send(f'{user} has been added to the blacklist. Reason: {reason}')
        except discord.errors.Forbidden:
            await ctx.send(f"Unable to kick {user}. Make sure the bot has the necessary permissions.")
    else:
        await ctx.send(f'{user} is already blacklisted.')



@bot.slash_command(name="view_blacklist")
@commands.check(lambda ctx: ctx.author.id == owner_id)
async def view_blacklist(ctx):
    if blacklist:
        embed = discord.Embed(title="Blacklisted Users")
        for user_id, reason in blacklist.items():
            user = bot.get_user(user_id)
            if user:
                embed.add_field(name=str(user), value=f"Reason: {reason}", inline=False)
            else:
                embed.add_field(name=f"User ID: {user_id}", value=f"Reason: {reason}", inline=False)
        await ctx.send(embed=embed)
    else:
      await ctx.send("No users are blacklisted.")



@bot.slash_command(name="unblacklist")
@commands.check(lambda ctx: ctx.author.id == owner_id or 1119268738278105185 in [role.id for role in ctx.author.roles])  # Allow the owner and users with a specific role
async def unblacklist(ctx, user: discord.User):
    if user.id in blacklist:
        reason = blacklist[user.id]

        # Send a confirmation message to the owner's DM
        owner = bot.get_user(owner_id)
        if owner:
            confirmation_msg = await owner.send(f"Are you sure you want to unblacklist {user}?\nReason: {reason}\nReact with ✅ to confirm, or ❌ to cancel.")
            await confirmation_msg.add_reaction("✅")  # Checkmark
            await confirmation_msg.add_reaction("❌")  # Cross

            def check(reaction, reacting_user):
                return reacting_user == owner and str(reaction.emoji) in ["✅", "❌"]

            try:
                reaction, _ = await bot.wait_for("reaction_add", timeout=60.0, check=check)

                if str(reaction.emoji) == "✅":
                    del blacklist[user.id]
                    save_blacklist()  # Save the updated blacklist to the file

                    await ctx.send(f'{user} has been removed from the blacklist. Reason: {reason}')
                else:
                    await ctx.send(f'Unblacklist canceled for {user}.')
            except asyncio.TimeoutError:
                await ctx.send("Unblacklist confirmation timed out. No changes were made.")
        else:
            await ctx.send("Owner not found.")
    else:
        await ctx.send(f'{user} is not blacklisted.')




@bot.event
async def on_member_join(member):
    if member.id in blacklist:
        reason = blacklist[member.id]

        embed = discord.Embed(title="PxD Sec | Blacklist", color=discord.Color.red())
        embed.add_field(name=f'Blacklisted from the PxD Network Appeal  (APPEAL HERE)[https://pxdsecappeal.pj0001.repl.co]', value=f'Reason: {reason}', inline=False)

        if kick_logs_channel:
            try:
                await kick_logs_channel.send(embed=embed)
            except discord.errors.Forbidden:
                pass

        if member.guild.get_member(member.id):
            try:
                await member.send(embed=embed)
            except discord.errors.Forbidden:
                pass

        try:
            await member.kick(reason=f'Blacklisted - {reason}')
        except discord.errors.Forbidden:
            pass



@bot.slash_command(name="scan_blacklist")
@commands.check(lambda ctx: ctx.author.id == owner_id)
async def scan_blacklist(ctx):
   
    kicked_members_by_guild = {}

    for guild in bot.guilds:
       
        blacklisted_members = []

        for member_id, reason in blacklist.items():
            member = guild.get_member(member_id)
            if member:
            
                try:
                    await member.kick(reason=f'Blacklisted - {reason}')
                    blacklisted_members.append(f"{member.name}#{member.discriminator} (Reason: {reason})")
                except discord.errors.Forbidden:
                    pass 

        if blacklisted_members:
            kicked_members_by_guild[guild.name] = blacklisted_members

    if kicked_members_by_guild:
        owner = bot.get_user(owner_id)
        if owner:
            for guild_name, kicked_members in kicked_members_by_guild.items():
                await owner.send(f"Kicked blacklisted members in {guild_name}:\n" + "\n".join(kicked_members))
        response_message = "\n".join([f"{guild_name}:\n" + "\n".join(kicked_members) for guild_name, kicked_members in kicked_members_by_guild.items()])
        await ctx.send("Kicked blacklisted members in each guild:\n" + response_message)
    else:
        await ctx.send("No blacklisted members were found in any guilds the bot is a member of.")


@bot.slash_command(name="iplookup", description= "This displays information about the target IP (Subscription needed)")
@commands.check(is_whitelisted)
@commands.cooldown(1, 5, commands.BucketType.user)
async def iplookup(ctx, target_ip: str):
    api_url = f"https://ipinfo.io/{target_ip}/json"

    headers = {
        'Authorization': f'Bearer {IPINFO_API_TOKEN}'  
    }

    try:
        # Retrieve IP information from ipinfo.io
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            ip_info = response.json()
            embed = discord.Embed(title=f"IP Lookup for {target_ip}",color=0xf0ffff)
            embed.add_field(name="IP Address", value=ip_info.get("ip", "N/A"))
            embed.add_field(name="Hostname", value=ip_info.get("hostname", "N/A"))
            embed.add_field(name="City", value=ip_info.get("city", "N/A"))
            embed.add_field(name="Region", value=ip_info.get("region", "N/A"))
            embed.add_field(name="Country", value=ip_info.get("country", "N/A"))
            ip_api_response = requests.get(f"{IP_API_URL}{target_ip}")
            if ip_api_response.status_code == 200:
                ip_api_info = ip_api_response.json()
                embed.add_field(name="ISP", value=ip_api_info.get("isp", "N/A"))
                embed.add_field(name="Proxy", value=ip_api_info.get("proxy", "N/A"))
                embed.add_field(name="VPN", value=ip_api_info.get("vpn", "N/A"))
                embed.add_field(name="Hosting", value=ip_api_info.get("hosting", "N/A"))
                
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"Unable to fetch information for {target_ip}.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")


@bot.slash_command(name="dnsinfo")
@commands.check(is_whitelisted)
@commands.cooldown(1, 5, commands.BucketType.user)
async def dnsinfo(ctx, target_url: str):
    try:
        api_url = 'https://webresolver.nl/api.php'
        params = {
            'key': API_KEY,
            'action': 'dns',
            'string': target_url
        }

        response = requests.get(api_url, params=params)

        if response.status_code == 200:
            dns_info = response.text

            file_name = 'dns_info.txt'
            with open(file_name, 'w') as file:
                file.write(dns_info)

            await ctx.send(f'DNS information for {target_url}:', file=discord.File(file_name))

            os.remove(file_name)
        else:
            await ctx.send(f"Unable to retrieve DNS information. API response code: {response.status_code}")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")



@bot.slash_command(name="ping")
@commands.check(is_whitelisted)
@commands.cooldown(1, 5, commands.BucketType.user)
async def ping(ctx, target_domain: str):
    try:
       
        api_key = 'K3QXX-QMHFZ-I8P2I-ELT1I'

       
        api_url = 'https://webresolver.nl/api.php'

        
        params = {
            'key': api_key,
            'action': 'ping',
            'string': target_domain,
            'html': '0'  
        }

       
        response = requests.get(api_url, params=params)

        if response.status_code == 200:
            ping_results = response.text
            await ctx.send(f'Ping results for {target_domain}:\n```{ping_results}```')
        else:
            await ctx.send(f"Unable to perform the ping request. API response code: {response.status_code}")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")


@bot.slash_command(name="help")
@commands.cooldown(1, 5, commands.BucketType.user)
async def help(ctx):
  help_embed = discord.Embed(title="Bot Commands", color=discord.Color.blue())
  help_embed.add_field(name="!dm <USERID> <MESSAGE>",
                       value="dm's a person",
                       inline=False)
  help_embed.add_field(name="!portscan <IP>",
                       value="Scans for OpenPorts",
                       inline=False)
  help_embed.add_field(name="!help",
                       value="Displays this help message.",
                       inline=False)
  help_embed.add_field(name="!credits",
                       value="Shows credits for the bot.",
                       inline=False)
  help_embed.add_field(name="!domaininfo <SITE>",
                       value="Gives you the Info.",
                       inline=False)
  help_embed.add_field(name="!dnsinfo <IP>",
                       value="Gives you the Info.",
                       inline=False)
  help_embed.add_field(name="!iplookup <IP>",
                       value="Gives you the Info.",
                       inline=False)
  help_embed.add_field(name="!ping <IP>",
                       value="Checks if the ip is up",
                       inline=False)
  await ctx.send(embed=help_embed)


API_KEY = 'K3QXX-QMHFZ-I8P2I-ELT1I'


@bot.slash_command(name="domaininfo")
@commands.check(is_whitelisted)
@commands.cooldown(1, 5, commands.BucketType.user)
async def domaininfo(ctx, target_domain: str):
    try:
        api_url = 'https://webresolver.nl/api.php'
        params = {
            'key': API_KEY,
            'action': 'domaininfo',
            'string': target_domain
        }

        response = requests.get(api_url, params=params)

        if response.status_code == 200:
            domain_info = response.text

            file_name = f'{target_domain}_info.txt'
            with open(file_name, 'w') as file:
                file.write(domain_info)


            await ctx.send(f'Domain information for {target_domain}:', file=discord.File(file_name))

        
            os.remove(file_name)
        else:
            await ctx.send(f"Unable to retrieve domain information. API response code: {response.status_code}")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

@bot.slash_command(name="portscan")
@commands.check(is_whitelisted)
@commands.cooldown(1, 5, commands.BucketType.user)
async def portscan(ctx, target_ip: str):
    try:
     
        api_url = 'https://webresolver.nl/api.php'

   
        params = {
            'key': API_KEY,
            'action': 'portscan',
            'string': target_ip
        }


        response = requests.get(api_url, params=params)

        if response.status_code == 200:
            scan_results = response.text
          
            file_name = 'portscan_results.txt'
            with open(file_name, 'w') as file:
                file.write(scan_results)

   
            await ctx.send(f'Port scan results for {target_ip}:', file=discord.File(file_name))

     
            os.remove(file_name)
        else:
            await ctx.send(f"Unable to perform the port scan. API response code: {response.status_code}")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")


@bot.slash_command(name="credits")
@commands.check(is_whitelisted)
@commands.cooldown(1, 5, commands.BucketType.user)
async def credits(ctx):
  credits_embed = discord.Embed(title="Bot Credits",
                                description="This bot was made by PJ0001.",
                                color=discord.Color.blue())
  await ctx.send(embed=credits_embed)
   
@bot.slash_command(name="dm")
@commands.check(is_whitelisted)
@commands.cooldown(1, 5, commands.BucketType.user)
async def dm(ctx, user_id: int, *, message: str):
  user = await bot.fetch_user(user_id)
  if user:
    try:
      await user.send(message)
      await ctx.send(f"Message sent to user {user_id}.")
    except discord.errors.Forbidden:
      await ctx.send("I couldn't send a message to that user.")
  else:
    await ctx.send("User not found.")


# This is not done yet.
#  @bot.command()
# async def subscribe(ctx):
#    user = ctx.author
#    if user.id in whitelisted_users:
#        await ctx.send("You are already subscribed.")
#       return
#
#   subscription_embed = discord.Embed(
#       title="Subscription Confirmation",
#       description="Hi There, Please sent PJ0001 a dm to comfirm your Subscription",
#        color=discord.Color.green()
#   )
#    await user.send(embed=subscription_embed)


@bot.slash_command(name="plans")
@commands.cooldown(1, 5, commands.BucketType.user)
async def plans(ctx):
    Plan = discord.Embed(title="Subscriptions", color=discord.Color(0xFFFFF0))

    Plan.add_field(name="€0,50 Euro",
                   value="Ontvang een exclusieve rol en toegang tot onze VIP-kanalen.",
                   inline=False)

    Plan.add_field(name="€2,50",
                   value="Krijg toegang tot de Pen-Testing Discord Bot, waarmee je Linux-functionaliteiten op Windows kunt gebruiken voor veelzijdige mogelijkheden & het Roblox Menu!",
                   inline=False)

    Plan.add_field(name="€5,00",
                   value="Ontvang toegang tot alle gewenste scripts. Ontdek de broncode van projecten en toegang tot PxD Cloud-services voor nog meer mogelijkheden.",
                   inline=False)

    Plan.add_field(name="ToS",
                   value='''
            
                           Wil je nou een van deze tiers aanschaffen, maak dan een ticket aan in #meldpunt en dan kan je het aanschaffen.

                           ben je geen 18 jaar of ouder vraag dan eerst even toestemming aan je ouder/verzorgers.

                           

                          **Dit is een eenmalige betaling**


                           ```Paypal / Tikkie  worden geaccepteerd ```




                           Met Vriendelijke Groet, Team PxD Sec.
                           ''',
                   inline=False)



    await ctx.send(embed=Plan)

@bot.slash_command(name="helpowner")
@commands.check(lambda ctx: ctx.author.id == owner_id)
async def helpowner(ctx):
    owner_help_embed = discord.Embed(title="Owner Commands", color=discord.Color.red())

    owner_help_embed.add_field(name="!whitelist", value="List all whitelisted users.", inline=False)
    owner_help_embed.add_field(name="!addwhitelist <USERID>", value="Add a user to the whitelist.", inline=False)
    owner_help_embed.add_field(name="!unwhitelist <USERID>", value="Remove a user from the whitelist.", inline=False)
    owner_help_embed.add_field(name="!tempwhitelist <USERID> <YYYY-MM-DD>", value="Temporarily whitelist a user until the specified date.", inline=False)
    owner_help_embed.add_field(name="!addblacklist <USER> [REASON]", value="Add a user to the blacklist with an optional reason.", inline=False)
    owner_help_embed.add_field(name="!unblacklist <USER>", value="Remove a user from the blacklist.", inline=False)
    owner_help_embed.add_field(name="!view_blacklist", value="View all blacklisted users and reasons.", inline=False)
    owner_help_embed.add_field(name="!scan_blacklist", value="Scan and kick blacklisted members in all servers.", inline=False)
    owner_help_embed.add_field(name="!searchblacklist <USERID>", value="Search for a user in the blacklist.", inline=False)
    owner_help_embed.add_field(name="!leave <GUILD_ID>", value="Leave a server by providing its ID.", inline=False)
    owner_help_embed.add_field(name="!servers", value="List all servers the bot is a member of.", inline=False)

    await ctx.send(embed=owner_help_embed)


@bot.slash_command(name="leave")
@commands.check(lambda ctx: ctx.author.id == owner_id)
async def leave(ctx, guild_id: int):
    try:
       
        guild = bot.get_guild(guild_id)
        
        
        if guild is not None and guild.me:
            await guild.leave()
            await ctx.send(f"Left server with ID {guild_id}.")
        else:
            await ctx.send("Either the guild doesn't exist or the bot is not a member of it.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

@bot.slash_command(name="servers")
@commands.check(lambda ctx: ctx.author.id == owner_id)
async def servers(ctx):
    servers_info = []

    for guild in bot.guilds:
        servers_info.append(f"Guild Name: {guild.name}, Guild ID: {guild.id}")

    if servers_info:
        await ctx.send("\n".join(servers_info))
    else:
        await ctx.send("The bot is not a member of any servers.")


@bot.slash_command(name="search" , description = "This allows you to search on the blacklist of PxD-Guard")
async def search(ctx, *, user: discord.User):
    if user.id in blacklist:
        reason = blacklist[user.id]

        embed = discord.Embed(title=f"Search Results for {user.name}#{user.discriminator}", color=discord.Color.blue())
        embed.add_field(name=f'User ID', value=user.id, inline=False)
        embed.add_field(name=f'Reason for Blacklist', value=reason, inline=False)
        embed.add_field(name=f'How to Appeal', value='To appeal your blacklist, go to our website and submit a request.  https://pxdsecappeal.pj0001.repl.co', inline=False)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f'{user} is not blacklisted.')


load_blacklist()
bot.run(BOT_TOKEN)
