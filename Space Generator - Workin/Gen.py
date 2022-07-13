from xml.dom.minidom import parseString
from colorama import Fore, Style, init
from time import sleep, time
from datetime import datetime
from base64 import b64encode as b
from httpx_socks import SyncProxyTransport
import websocket, json, threading, os, ctypes, random, string, httpx, requests, win32console, config, base64
init()


generated = 0; failed = 0; solved = 0; genstated = time(); avatar_folder = 'Avatars'

class Utils:
    @staticmethod
    def GetProxy():
      with open('data/proxies.txt', "r") as f:
        return "http://" + random.choice(f.readlines()).strip()

    @staticmethod
    def randomc(len):
        return os.urandom(len).hex()[len:]
    
    @staticmethod
    def clearconsole():
        command = 'clear'
        if os.name in ('nt', 'dos'):
            command = 'cls'   
        os.system(command)
    
    @staticmethod
    def GetCookies():
        return f'__dcfduid={Utils.randomc(43)}; __sdcfduid={Utils.randomc(96)}; __stripe_mid={Utils.randomc(18)}-{Utils.randomc(4)}-{Utils.randomc(4)}-{Utils.randomc(4)}-{Utils.randomc(18)}; locale=en-GB; __cfruid={Utils.randomc(40)}-{"".join(random.choice(string.digits) for i in range(10))}'
    
    @staticmethod
    def GetUsername():
        usernames = open("data/usernames.txt", encoding="cp437", failed='ignore').read().splitlines()
        return random.choice(usernames)

class Logger:
    def Success(text):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f'[{Fore.GREEN}+{Fore.WHITE}] {text}')
    
    def Error(text):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f'[{Fore.RED}-{Fore.WHITE}] {text}')


class Solvers:
    @staticmethod
    def hCaptcha(websiteKey, websiteUrl, UserAgent):
           solvedCaptcha = None
           taskId = ""
           taskId = httpx.post(f"https://api.{config.captcha_service}/createTask", json={"clientKey": config.captcha_api_key, "task": { "type": "HCaptchaTaskProxyless",  "websiteURL": websiteUrl, "websiteKey": websiteKey, "userAgent": UserAgent}}, timeout=33).json()
           if taskId.get("errorId") > 0:
                print(f"{Fore.RED}[-] Error While Creating Task - {taskId.get('errorDescription')}!")

           taskId = taskId.get("taskId")
            
           while not solvedCaptcha:
                    captchaData = httpx.post(f"https://api.{config.captcha_service}/getTaskResult", json={"clientKey": config.captcha_api_key, "taskId": taskId}, timeout=30).json()
                    if captchaData.get("status") == "ready":
                        solvedCaptcha = captchaData.get("solution").get("gRecaptchaResponse")
                        return solvedCaptcha
    

class AiSolver:
    @staticmethod
    def hCaptcha(sitekey, url):
        captchakey = httpx.post("http://144.76.107.39:6969/api/v1/captchasolver", json={
            "site_key": sitekey,
            "site_url": url
        }, timeout=None).text
        return captchakey


class WebSocket:
    def Connect(token):
        ws = websocket.WebSocket()
        ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
        response = ws.recv()
        event = json.loads(response)
        auth = {'op': 2, 'd': {'token': token, 'capabilities': 61, 'properties': {'os': 'Windows', 'browser': 'Chrome', 'device': '',  'system_locale': 'en-GB', 'browser_user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36', 'browser_version': '90.0.4430.212', 'os_version': '10', 'referrer': '', 'referring_domain': '', 'referrer_current': '', 'referring_domain_current': '', 'release_channel': 'stable', 'client_build_number': '85108', 'client_event_source': 'null'}, 'presence': {'status': random.choice(['online', 'dnd', 'idle']), 'since': 0, 'activities': [{ "name": "Custom Status", "type": 4, "state": config.custom_status, "emoji": None }], 'afk': False}, 'compress': False, 'client_state': {'guild_hashes': {}, 'highest_last_message_id': '0', 'read_state_version': 0, 'user_guild_settings_version': -1}}};
        ws.send(json.dumps(auth))

class Generator:
    def __init__(self):
        try:
            self.invite = config.invite_code
            self.super_properties = b(json.dumps({"os":"Windows","browser":"Firefox","device":"","system_locale":"en-US","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0","browser_version":"94.0","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":9999,"client_event_source": 'null'}, separators=(',', ':')).encode()).decode()
            self.headers = {"Accept": "*/*", "Accept-Language": "en-US", "Connection": "keep-alive", "Content-Type": "application/json", "DNT": "1", "Host": "discord.com", "Referer": f"https://discord.com/invite/{self.invite}", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "TE": "trailers", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0", "X-Discord-Locale": "en-US", "X-Super-Properties": self.super_properties}
            self.transport = SyncProxyTransport.from_url(Utils.GetProxy())
            self.session = httpx.Client(headers=self.headers, cookies={"locale": "en-US"}, transport=self.transport)
            self.session.headers["X-Fingerprint"] = self.session.get("https://discord.com/api/v9/experiments", timeout=30).json()["fingerprint"]
            self.session.headers["Origin"] = "https://discord.com"
            self.GenerateToken()
        except Exception as e:
            print(e)

    def GenerateToken(self):
        global generated, solved, failed

        self.username = Utils.randomc(4) + random.choice([' | .gg/spacemembers'])
        self.fingerprint = self.session.headers["X-Fingerprint"]
        self.captcha = AiSolver.hCaptcha('4c672d35-0701-42b2-88c3-78380b0db560', 'https://discord.com/')#Solvers.hCaptcha('4c672d35-0701-42b2-88c3-78380b0db560', 'https://discord.com/', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0')#
        if self.captcha.startswith('P0_'):
            solved += 1
            win32console.SetConsoleTitle(f'Space Generator | Genned : {generated} | Solved : {solved} | Failed : {failed} | Speed {round(generated / ((time() - genstated) / 60))}/min')

            try:
                self.payload = { "fingerprint": self.session.headers["X-Fingerprint"], "username": self.username, "invite": self.invite, "gift_code_sku_id": None, "captcha_key": self.captcha, "Consent": True }
                self.response = self.session.post('https://discord.com/api/v9/auth/register', json=self.payload)
                print(self.response.json())
                if self.response.status_code == 201:
                    generated += 1
                    win32console.SetConsoleTitle(f'Space Generator | Genned : {generated} | Solved : {solved} | Failed : {failed} | Speed {round(generated / ((time() - genstated) / 60))}/min')
                    self.token = self.response.json()['token']
                    Logger.Success(f'Generated Token : {self.token}....')

                    avatarfile = random.choice(os.listdir(avatar_folder)); avatar = avatar_folder+'\\' + avatarfile; image_data = base64.b64encode(open(f"{avatar}", "rb").read()).decode('ascii')
                    
                    self.avatar = image_data
                    self.email = Utils.randomc(8)+"@outlook.io"
                    payload = { 'email': self.email, 'password': 'Void7331@', 'date_of_birth': '1998-01-05', 'bio': f"*{httpx.get('https://free-quotes-api.herokuapp.com', timeout=30).json()['quote']}*", 'avatar': self.avatar}
                    headsss = { "Authorization": self.token, "accept": "*/*", "accept-language": "en-US", "connection": "keep-alive", "DNT": "1", 'origin': 'https://discord.com', 'referer': 'https://discordapp.com/channels/@me', "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin", "TE": "Trailers", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36", "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMi4wLjUwMDUuMTE1IFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiIxMDIuMC41MDA1LjExNSIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMzIxMDgsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"}
                    resp = self.session.patch('https://discord.com/api/v9/users/@me', json=payload, headers=headsss)


                    try:
                        with open('output/tokens.txt', 'a') as fp:
                            fp.write(resp['token'] + "\n")
                    
                        if config.online_tokens == True:
                            WebSocket.Connect(resp['token'])
                    except:
                        with open('data/tokens.txt', 'a') as fp:
                            fp.write(self.token + "\n")
                    
                        if config.online_tokens == True:
                            WebSocket.Connect(resp['token'])
                else:
                    failed += 1
                    win32console.SetConsoleTitle(f'Space Generator | Genned : {generated} | Solved : {solved} | Failed : {failed} | Speed {round(generated / ((time() - genstated) / 60))}/min')

            except Exception as e:
                failed += 1
                win32console.SetConsoleTitle(f'Space Generator | Genned : {generated} | Solved : {solved} | Failed : {failed} | Speed {round(generated / ((time() - genstated) / 60))}/min')

class SpaceGenerator:
    def start():
        os.system('mode 122,24')
        win32console.SetConsoleTitle(f'[Space Generator] - Main Menu')
        print(f"""
 ____                          ____                           _             
/ ___| _ __   __ _  ___ ___   / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __             ,MMM8&&&.  
\___ \| '_ \ / _` |/ __/ _ \ | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|       _...MMMMM88&&&&..._  
 ___) | |_) | (_| | (_|  __/ | |_| |  __/ | | |  __/ | | (_| | || (_) | |       .::'''MMMMM88&&&&&&'''::.
|____/| .__/ \__,_|\___\___|  \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|       ::     MMMMM88&&&&&&     ::
      |_|                                                                       '::....MMMMM88&&&&&&....::'           
                                                                                   `''''MMMMM88&&&&''''`
                                                                                         'MMM8&&&'  
        """)
        threads = int(input('[Space] Enter The Number Of Threads : '))
        win32console.SetConsoleTitle(f'[Space Generator] - Started....')
        for i in range(threads):
            t = threading.Thread(target=Generator)
            t.start()

SpaceGenerator.start()