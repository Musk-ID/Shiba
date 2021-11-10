#!/usr/bin/python
# Creator : Kingtebe
# Date : 10-11-2021, 13:45 WIB

import os,sys,json,requests,platform
try:
	from time import sleep
	from datetime import datetime
	from telethon import TelegramClient,sync
	from telethon.tl.functions.messages import GetHistoryRequest
except:
	exit("\n# Module telethon not installed!\n")

if platform.python_version().split(".")[0] != "3":
	exit("\n# Sorry only support python3 !\n")

time = datetime.now().strftime("%H.%M.%S")
date = datetime.now().strftime("%d/%m/%Y")
site = requests.get("https://api.myip.com").json()

c = '\033[1;36m'
p = '\033[1;37m'
g = '\033[0;37m'
h = '\033[1;32m'
k = '\033[1;33m'
b = '\033[1;34m'
m = '\033[1;31m'
d = '\033[0;36m'
q = '\033[1;30m'
z = '\033[101m'
o = '\033[0m'

def runing(katakan):
	for j in katakan + "\n":
		sys.stdout.write(j)
		sys.stdout.flush()
		sleep(0.001)

def countdown(second):
	while second:
		mins,secs = divmod(second,60)
		timer = "  \033[1;33m▶ \033[1;37mWaiting\033[1;37m \033[37m⟨\033[1;32m{:02d}:{:02d}\033[1;37m⟩".format(mins,secs)
		print(timer,end="\r")
		sleep(1)
		second -= 1

def _main(nomor):
	if not os.path.exists("session"):
		os.makedirs("session")
	login = TelegramClient("session/"+nomor,"800812","db55ad67a98df35667ca788b97f771f5")
	login.connect()
	if not login.is_user_authorized():
		login.send_code_request(nomor)
		me = login.sign_in(nomor,input("\n# Enter Your Code : "))
		me = login.start()
	try:
		os.system('cls' if os.name=='nt' else 'clear')
		account = login.get_me()
		runing(f"\n  {p}Time : {time}                 {p}Date : {date}\n {m}╔{c}═════════════════════════════════════════════════{m}╗\n {c}║ {m}███████{c}╗ {m}█████{c}╗  {m}█████{c}╗ {m}██{c}╗  {m}████████{c}╗{m}██{c}╗   {m}██{c}╗ ║\n {c}║ {m}██{c}╔════╝{m}██{c}╔══{m}██{c}╗{m}██{c}╔══{m}██{c}╗{m}██{c}║  {c}╚══{m}██{c}╔══╝{m}██{c}║   {m}██{c}║ ║\n {c}║ {m}█████{c}╗  {m}███████{c}║{m}███████{c}║{m}██{c}║     {m}██{c}║   {m}██{c}║   {m}██{c}║ ║\n {c}║ {m}██{c}╔══╝  {m}██{c}╔══{m}██{c}║{m}██{c}╔══{m}██{c}║{m}██{c}║     {m}██{c}║   {c}╚{m}██{c}╗ {m}██{c}╔╝ ║\n {c}║ {m}██{c}║     {m}██{c}║  {m}██{c}║{m}██{c}║  {m}██{c}║{m}███████{c}╗{m}██{c}║    {c}╚{m}████{c}╔╝  ║\n {c}║ ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝     ╚═══╝   ║\n {c}║{k}-------------------------------------------------{c}║\n {c}║ {k}▶ {p}Author {k}: {p}Kingtebe                             {c}║\n {c}║ {k}▶ {p}Github {k}: {p}github.clom/Musk-ID        {m}[{p}ONLINE{m}]  {c}║\n {m}╚{c}═════════════════════════════════════════════════{m}╝\n {q}<══════════════[{k}{z} • FREE SCRIPT • {o}{q}]════════════════>\n  {c}▶ {p}Version {k}: {p}1.1\n  {c}▶ {p}IP Kamu {k}: {h}{site['ip']}\n  {c}▶ {p}Youtube {k}: {p}FaaL TV\n {q}<═════════════════════════════════════════════════>\n  {p}Name account {c}@{account.username} {p}with user id {h}{account.id}\n {q}<═════════════════════════════════════════════════>")
	except Exception as e:
		if "object has no attribute" in str(e):
			pass
		else:
			print(e)
			pass
	while True:
		post = login.get_entity("@Shiba_Airdroppbot")
		login.send_message(entity=post,message="🎁 Bonus")
		sleep(3)
		message = login(GetHistoryRequest(peer=post,limit=2,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
		reward = message.messages[1].message
		if "successfully" in reward:
			print(f"  {reward}".replace("👍",f"{p}[{d}{time}{p}]"))
			countdown(int(60*30))
		else:
			print(f"  {p}[{d}{time}{p}] {p}Claim again after 30 minutes {m}!")
			countdown(int(60*30))

# Execute to runing
if __name__=='__main__':
	if len(sys.argv) < 2:
		exit("\n# Example: python %s <Nomor_Telegram> "%sys.argv[0]+"\n")
	else:
		_main(sys.argv[1])
