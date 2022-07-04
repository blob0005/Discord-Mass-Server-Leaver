anyerror = False
try:
    import os
    os.system("title " + "Discord Mass Server Leaver,   Made By blob#0005,   Github: github.com/blob0005")
except:
    pass
try:
  import discord
  from discord.ext import commands
  import colorama
  import requests
except:
  anyerror = True
if anyerror == True:
  print("Missing Module(s), Press Enter To Start Repair Process (Wont Always Work)")
  input("")
  try:
    import os
    os.system("pip install discord")
    os.system("pip install colorama")
    os.system("pip install requests")
    print("Problems Should Be Fixed Now, Restart The Program")
    input("")
    exit()
  except:
    print("Error While Fixing, Sorry")
    input("")
    exit()
import threading
colorama.init(autoreset=True)
url = "https://discord.com/api/v9/users/@me/guilds/"
def leaver(token):
  try:
    bot = commands.Bot(command_prefix="", self_bot=True)
  except:
    pass
  @bot.event
  async def on_ready():
    try:
        print(colorama.Fore.GREEN + f"Started On {bot.user.name}")
        ids = []
        ide = 0
        for server in bot.guilds:
          id = server.id
          ids.append(str(id))
          ide = int(ide) + 1
          print(f"[{str(ide)}] Scraped Server Id")
    except Exception as e:
      print(str(e))
      print(colorama.Fore.RED + "Invalid Token")
    if ids == []:
      print(colorama.Fore.RED + f"[{str(bot.user.name)}] Had No Servers To Leave, You May Close This Now")
    left = 0
    for idr in ids:
      idr = str(idr)
      while True:
        try:
          headers = {"authorization": token,
          "lurking": "false"
          }
          re = requests.delete(url+str(idr), headers=headers)
          re = str(re)
          if "204" in re:
            left = int(left) + 1
            print(colorama.Fore.GREEN + f"[{str(bot.user.name)}, {str(left)}] Succsesfully Left Server " + str(idr))
            break
          if "400" in re:
            print(colorama.Fore.RED + f"[{str(bot.user.name)}] Unkown Error, With " + str(idr))
            break
          if "429" in re:
            print(colorama.Fore.RED + f"[{str(bot.user.name)}] Rate Limited, Retrying")
        except:
          print(colorama.Fore.RED + "UNKOWN ERROR")
          break
    print( + "Done Leaving Servers With " + str(bot.user.name)+ " , You May Close This Now")
  try:
    bot.run(token, bot=False)
  except:
    print(colorama.Fore.RED + "Invalid Token, You May Close This Now")

tool = "1"

if tool == "1":
  invite_code = "weYYXeUSNm"
  while True:
      tokens = input("Enter Token: ")
      r1 = requests.get('https://discord.com/api/v6/auth/login', headers={"Authorization": tokens})
      if "200" not in str(r1):
          print("Invalid Token")
      if "200" in str(r1):
          r = requests.get(f'https://discord.com/api/v6/invite/{invite_code}', headers={"Authorization": tokens})
          if "200" in str(r):
              break
          if "403" in str(r):
              print("Locked Token")
  leaver(tokens)
