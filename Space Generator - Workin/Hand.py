from%20xml.dom.minidom%20import%20parseString%0Afrom%20colorama%20import%20Fore%2C%20Style%2C%20init%0Afrom%20time%20import%20sleep%2C%20time%0Afrom%20datetime%20import%20datetime%0Afrom%20base64%20import%20b64encode%20as%20b%0Afrom%20httpx_socks%20import%20SyncProxyTransport%0Aimport%20websocket%2C%20json%2C%20threading%2C%20os%2C%20ctypes%2C%20random%2C%20string%2C%20httpx%2C%20requests%2C%20win32console%2C%20config%0Ainit()%0A%0A%0Agenerated%20%3D%200%3B%20failed%20%3D%200%3B%20solved%20%3D%200%3B%20genstated%20%3D%20time()%0A%0Aclass%20Utils%3A%0A%20%20%20%20%40staticmethod%0A%20%20%20%20def%20GetProxy()%3A%0A%20%20%20%20%20%20with%20open(%27data%2Fproxies.txt%27%2C%20%22r%22)%20as%20f%3A%0A%20%20%20%20%20%20%20%20return%20%22http%3A%2F%2F%22%20%2B%20random.choice(f.readlines()).strip()%0A%0A%20%20%20%20%40staticmethod%0A%20%20%20%20def%20randomc(len)%3A%0A%20%20%20%20%20%20%20%20return%20os.urandom(len).hex()%5Blen%3A%5D%0A%20%20%20%20%0A%20%20%20%20%40staticmethod%0A%20%20%20%20def%20clearconsole()%3A%0A%20%20%20%20%20%20%20%20command%20%3D%20%27clear%27%0A%20%20%20%20%20%20%20%20if%20os.name%20in%20(%27nt%27%2C%20%27dos%27)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20command%20%3D%20%27cls%27%20%20%20%0A%20%20%20%20%20%20%20%20os.system(command)%0A%20%20%20%20%0A%20%20%20%20%40staticmethod%0A%20%20%20%20def%20GetCookies()%3A%0A%20%20%20%20%20%20%20%20return%20f%27__dcfduid%3D%7BUtils.randomc(43)%7D%3B%20__sdcfduid%3D%7BUtils.randomc(96)%7D%3B%20__stripe_mid%3D%7BUtils.randomc(18)%7D-%7BUtils.randomc(4)%7D-%7BUtils.randomc(4)%7D-%7BUtils.randomc(4)%7D-%7BUtils.randomc(18)%7D%3B%20locale%3Den-GB%3B%20__cfruid%3D%7BUtils.randomc(40)%7D-%7B%22%22.join(random.choice(string.digits)%20for%20i%20in%20range(10))%7D%27%0A%20%20%20%20%0A%20%20%20%20%40staticmethod%0A%20%20%20%20def%20GetUsername()%3A%0A%20%20%20%20%20%20%20%20usernames%20%3D%20open(%22data%2Fusernames.txt%22%2C%20encoding%3D%22cp437%22%2C%20failed%3D%27ignore%27).read().splitlines()%0A%20%20%20%20%20%20%20%20return%20random.choice(usernames)%0A%0Aclass%20Logger%3A%0A%20%20%20%20def%20Success(text)%3A%0A%20%20%20%20%20%20%20%20now%20%3D%20datetime.now()%0A%20%20%20%20%20%20%20%20current_time%20%3D%20now.strftime(%22%25H%3A%25M%3A%25S%22)%0A%20%20%20%20%20%20%20%20print(f%27%5B%7BFore.GREEN%7D%2B%7BFore.WHITE%7D%5D%20%7Btext%7D%27)%0A%20%20%20%20%0A%20%20%20%20def%20Error(text)%3A%0A%20%20%20%20%20%20%20%20now%20%3D%20datetime.now()%0A%20%20%20%20%20%20%20%20current_time%20%3D%20now.strftime(%22%25H%3A%25M%3A%25S%22)%0A%20%20%20%20%20%20%20%20print(f%27%5B%7BFore.RED%7D-%7BFore.WHITE%7D%5D%20%7Btext%7D%27)%0A%0A%0Aclass%20Solvers%3A%0A%20%20%20%20%40staticmethod%0A%20%20%20%20def%20hCaptcha(websiteKey%2C%20websiteUrl%2C%20UserAgent)%3A%0A%20%20%20%20%20%20%20%20%20%20%20solvedCaptcha%20%3D%20None%0A%20%20%20%20%20%20%20%20%20%20%20taskId%20%3D%20%22%22%0A%0A%20%20%20%20%20%20%20%20%20%20%20taskId%20%3D%20httpx.post(f%22https%3A%2F%2Fapi.%7Bconfig.captcha_service%7D%2FcreateTask%22%2C%20json%3D%7B%22clientKey%22%3A%20config.captcha_api_key%2C%20%22task%22%3A%20%7B%20%22type%22%3A%20%22HCaptchaTaskProxyless%22%2C%20%20%22websiteURL%22%3A%20websiteUrl%2C%20%22websiteKey%22%3A%20websiteKey%2C%20%22userAgent%22%3A%20UserAgent%7D%7D%2C%20timeout%3D30).json()%0A%20%20%20%20%20%20%20%20%20%20%20if%20taskId.get(%22errorId%22)%20%3E%200%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print(f%22%7BFore.RED%7D%5B-%5D%20Error%20While%20Creating%20Task%20-%20%7BtaskId.get(%27errorDescription%27)%7D!%22)%0A%0A%20%20%20%20%20%20%20%20%20%20%20taskId%20%3D%20taskId.get(%22taskId%22)%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20while%20not%20solvedCaptcha%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20captchaData%20%3D%20httpx.post(f%22https%3A%2F%2Fapi.%7Bconfig.captcha_service%7D%2FgetTaskResult%22%2C%20json%3D%7B%22clientKey%22%3A%20config.captcha_api_key%2C%20%22taskId%22%3A%20taskId%7D%2C%20timeout%3D30).json()%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20captchaData.get(%22status%22)%20%3D%3D%20%22ready%22%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20solvedCaptcha%20%3D%20captchaData.get(%22solution%22).get(%22gRecaptchaResponse%22)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20solvedCaptcha%0A%0Aclass%20WebSocket%3A%0A%20%20%20%20def%20Connect(token)%3A%0A%20%20%20%20%20%20%20%20ws%20%3D%20websocket.WebSocket()%0A%20%20%20%20%20%20%20%20ws.connect(%27wss%3A%2F%2Fgateway.discord.gg%2F%3Fv%3D6%26encoding%3Djson%27)%0A%20%20%20%20%20%20%20%20response%20%3D%20ws.recv()%0A%20%20%20%20%20%20%20%20event%20%3D%20json.loads(response)%0A%20%20%20%20%20%20%20%20auth%20%3D%20%7B%27op%27%3A%202%2C%20%27d%27%3A%20%7B%27token%27%3A%20token%2C%20%27capabilities%27%3A%2061%2C%20%27properties%27%3A%20%7B%27os%27%3A%20%27Windows%27%2C%20%27browser%27%3A%20%27Chrome%27%2C%20%27device%27%3A%20%27%27%2C%20%20%27system_locale%27%3A%20%27en-GB%27%2C%20%27browser_user_agent%27%3A%20%27Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F90.0.4430.212%20Safari%2F537.36%27%2C%20%27browser_version%27%3A%20%2790.0.4430.212%27%2C%20%27os_version%27%3A%20%2710%27%2C%20%27referrer%27%3A%20%27%27%2C%20%27referring_domain%27%3A%20%27%27%2C%20%27referrer_current%27%3A%20%27%27%2C%20%27referring_domain_current%27%3A%20%27%27%2C%20%27release_channel%27%3A%20%27stable%27%2C%20%27client_build_number%27%3A%20%2785108%27%2C%20%27client_event_source%27%3A%20%27null%27%7D%2C%20%27presence%27%3A%20%7B%27status%27%3A%20random.choice(%5B%27online%27%2C%20%27dnd%27%2C%20%27idle%27%5D)%2C%20%27since%27%3A%200%2C%20%27activities%27%3A%20%5B%7B%20%22name%22%3A%20%22Custom%20Status%22%2C%20%22type%22%3A%204%2C%20%22state%22%3A%20config.custom_status%2C%20%22emoji%22%3A%20None%20%7D%5D%2C%20%27afk%27%3A%20False%7D%2C%20%27compress%27%3A%20False%2C%20%27client_state%27%3A%20%7B%27guild_hashes%27%3A%20%7B%7D%2C%20%27highest_last_message_id%27%3A%20%270%27%2C%20%27read_state_version%27%3A%200%2C%20%27user_guild_settings_version%27%3A%20-1%7D%7D%7D%3B%0A%20%20%20%20%20%20%20%20ws.send(json.dumps(auth))%0A%0Aclass%20Generator%3A%0A%20%20%20%20def%20__init__(self)%3A%0A%20%20%20%20%20%20%20%20try%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20self.invite%20%3D%20config.invite_code%0A%20%20%20%20%20%20%20%20%20%20%20%20self.super_properties%20%3D%20b(json.dumps(%7B%22os%22%3A%22Windows%22%2C%22browser%22%3A%22Firefox%22%2C%22device%22%3A%22%22%2C%22system_locale%22%3A%22en-US%22%2C%22browser_user_agent%22%3A%22Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64%3B%20rv%3A94.0)%20Gecko%2F20100101%20Firefox%2F94.0%22%2C%22browser_version%22%3A%2294.0%22%2C%22os_version%22%3A%2210%22%2C%22referrer%22%3A%22%22%2C%22referring_domain%22%3A%22%22%2C%22referrer_current%22%3A%22%22%2C%22referring_domain_current%22%3A%22%22%2C%22release_channel%22%3A%22stable%22%2C%22client_build_number%22%3A9999%2C%22client_event_source%22%3A%20%27null%27%7D%2C%20separators%3D(%27%2C%27%2C%20%27%3A%27)).encode()).decode()%0A%20%20%20%20%20%20%20%20%20%20%20%20self.headers%20%3D%20%7B%22Accept%22%3A%20%22*%2F*%22%2C%20%22Accept-Language%22%3A%20%22en-US%22%2C%20%22Connection%22%3A%20%22keep-alive%22%2C%20%22Content-Type%22%3A%20%22application%2Fjson%22%2C%20%22DNT%22%3A%20%221%22%2C%20%22Host%22%3A%20%22discord.com%22%2C%20%22Referer%22%3A%20f%22https%3A%2F%2Fdiscord.com%2Finvite%2F%7Bself.invite%7D%22%2C%20%22Sec-Fetch-Dest%22%3A%20%22empty%22%2C%20%22Sec-Fetch-Mode%22%3A%20%22cors%22%2C%20%22Sec-Fetch-Site%22%3A%20%22same-origin%22%2C%20%22TE%22%3A%20%22trailers%22%2C%20%22User-Agent%22%3A%20%22Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64%3B%20rv%3A95.0)%20Gecko%2F20100101%20Firefox%2F95.0%22%2C%20%22X-Discord-Locale%22%3A%20%22en-US%22%2C%20%22X-Super-Properties%22%3A%20self.super_properties%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20self.transport%20%3D%20SyncProxyTransport.from_url(Utils.GetProxy())%0A%20%20%20%20%20%20%20%20%20%20%20%20self.session%20%3D%20httpx.Client(headers%3Dself.headers%2C%20cookies%3D%7B%22locale%22%3A%20%22en-US%22%7D%2C%20transport%3Dself.transport)%0A%20%20%20%20%20%20%20%20%20%20%20%20self.session.headers%5B%22X-Fingerprint%22%5D%20%3D%20self.session.get(%22https%3A%2F%2Fdiscord.com%2Fapi%2Fv9%2Fexperiments%22%2C%20timeout%3D30).json()%5B%22fingerprint%22%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20self.session.headers%5B%22Origin%22%5D%20%3D%20%22https%3A%2F%2Fdiscord.com%22%0A%20%20%20%20%20%20%20%20%20%20%20%20self.GenerateToken()%0A%20%20%20%20%20%20%20%20except%20Exception%20as%20e%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20pass%0A%0A%20%20%20%20def%20GenerateToken(self)%3A%0A%20%20%20%20%20%20%20%20global%20generated%2C%20solved%2C%20failed%0A%0A%20%20%20%20%20%20%20%20self.username%20%3D%20Utils.randomc(4)%20%2B%20random.choice(%5B%27%20%7C%20.gg%2Fspacemembers%27%5D)%0A%20%20%20%20%20%20%20%20self.fingerprint%20%3D%20self.session.headers%5B%22X-Fingerprint%22%5D%0A%20%20%20%20%20%20%20%20self.captcha%20%3D%20Solvers.hCaptcha(%274c672d35-0701-42b2-88c3-78380b0db560%27%2C%20%27https%3A%2F%2Fdiscord.com%2F%27%2C%20%22Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F101.0.4951.54%20Safari%2F537.36%22)%0A%20%20%20%20%20%20%20%20solved%20%2B%3D%201%0A%20%20%20%20%20%20%20%20win32console.SetConsoleTitle(f%27Space%20Generator%20%7C%20Genned%20%3A%20%7Bgenerated%7D%20%7C%20Solved%20%3A%20%7Bsolved%7D%20%7C%20Failed%20%3A%20%7Bfailed%7D%20%7C%20Speed%20%7Bround(generated%20%2F%20((time()%20-%20genstated)%20%2F%2060))%7D%2Fmin%27)%0A%0A%20%20%20%20%20%20%20%20try%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20self.payload%20%3D%20%7B%20%22fingerprint%22%3A%20self.session.headers%5B%22X-Fingerprint%22%5D%2C%20%22username%22%3A%20self.username%2C%20%22invite%22%3A%20self.invite%2C%20%22gift_code_sku_id%22%3A%20None%2C%20%22captcha_key%22%3A%20self.captcha%2C%20%22Consent%22%3A%20True%20%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20self.response%20%3D%20self.session.post(%27https%3A%2F%2Fdiscord.com%2Fapi%2Fv9%2Fauth%2Fregister%27%2C%20json%3Dself.payload)%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20self.response.status_code%20%3D%3D%20201%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20generated%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20win32console.SetConsoleTitle(f%27Space%20Generator%20%7C%20Genned%20%3A%20%7Bgenerated%7D%20%7C%20Solved%20%3A%20%7Bsolved%7D%20%7C%20Failed%20%3A%20%7Bfailed%7D%20%7C%20Speed%20%7Bround(generated%20%2F%20((time()%20-%20genstated)%20%2F%2060))%7D%2Fmin%27)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.token%20%3D%20self.response.json()%5B%27token%27%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20Logger.Success(f%27Generated%20Token%20%3A%20%7Bself.token%7D....%27)%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.email%20%3D%20Utils.randomc(8)%2B%22%40outlook.io%22%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20payload%20%3D%20%7B%20%27email%27%3A%20self.email%2C%20%27password%27%3A%20%27Void7331%40%27%2C%20%27date_of_birth%27%3A%20%271998-01-05%27%2C%20%27bio%27%3A%20config.tokens_bio%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20headsss%20%3D%20%7B%20%27accept%27%3A%20%27*%2F*%27%2C%20%27accept-encoding%27%3A%20%27gzip%2C%20deflate%27%2C%20%27accept-language%27%3A%20%27en-US%27%2C%20%27authorization%27%3A%20self.token%2C%20%27cookie%27%3A%20Utils.GetCookies()%2C%20%27content-type%27%3A%20%27application%2Fjson%27%2C%20%27origin%27%3A%20%27https%3A%2F%2Fdiscordapp.com%27%2C%20%27referer%27%3A%20%27https%3A%2F%2Fdiscordapp.com%2Fchannels%2F%40me%27%2C%20%27sec-fetch-dest%27%3A%20%27empty%27%2C%20%27sec-fetch-mode%27%3A%20%27cors%27%2C%20%27sec-fetch-site%27%3A%20%27same-origin%27%2C%20%27sec-gpc%27%3A%20%271%27%2C%20%27user-agent%27%3A%20%27Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F102.0.5005.61%20Safari%2F537.36%27%2C%20%27x-debug-options%27%3A%20%27bugReporterEnabled%27%2C%20%27x-super-properties%27%3A%20%27eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMi4wLjUwMDUuNjEgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwMi4wLjUwMDUuNjEiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6Imh0dHBzOi8vZGlzY29yZC5jb20vbG9naW4%2FcmVkaXJlY3RfdG89JTJGY2hhbm5lbHMlMkYlNDBtZSIsInJlZmVycmluZ19kb21haW4iOiJkaXNjb3JkLmNvbSIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMzA4MzIsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9%27%20%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20resp%20%3D%20self.session.patch(%27https%3A%2F%2Fdiscord.com%2Fapi%2Fv9%2Fusers%2F%40me%27%2C%20json%3Dpayload%2C%20headers%3Dheadsss).json()%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print(resp)%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20try%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20with%20open(%27output%2Ftokens.txt%27%2C%20%27a%27)%20as%20fp%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20fp.write(resp%5B%27token%27%5D%20%2B%20%22%5Cn%22)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20config.online_tokens%20%3D%3D%20True%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20WebSocket.Connect(resp%5B%27token%27%5D)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20except%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20with%20open(%27data%2Ftokens.txt%27%2C%20%27a%27)%20as%20fp%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20fp.write(self.token%20%2B%20%22%5Cn%22)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20config.online_tokens%20%3D%3D%20True%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20WebSocket.Connect(resp%5B%27token%27%5D)%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20failed%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20win32console.SetConsoleTitle(f%27Space%20Generator%20%7C%20Genned%20%3A%20%7Bgenerated%7D%20%7C%20Solved%20%3A%20%7Bsolved%7D%20%7C%20Failed%20%3A%20%7Bfailed%7D%20%7C%20Speed%20%7Bround(generated%20%2F%20((time()%20-%20genstated)%20%2F%2060))%7D%2Fmin%27)%0A%0A%20%20%20%20%20%20%20%20except%20Exception%20as%20e%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20failed%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20win32console.SetConsoleTitle(f%27Space%20Generator%20%7C%20Genned%20%3A%20%7Bgenerated%7D%20%7C%20Solved%20%3A%20%7Bsolved%7D%20%7C%20Failed%20%3A%20%7Bfailed%7D%20%7C%20Speed%20%7Bround(generated%20%2F%20((time()%20-%20genstated)%20%2F%2060))%7D%2Fmin%27)%0A%0Aclass%20SpaceGenerator%3A%0A%20%20%20%20def%20start()%3A%0A%20%20%20%20%20%20%20%20os.system(%27mode%20122%2C24%27)%0A%20%20%20%20%20%20%20%20win32console.SetConsoleTitle(f%27%5BSpace%20Generator%5D%20-%20Main%20Menu%27)%0A%20%20%20%20%20%20%20%20print(f%22%22%22%0A%20____%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20____%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20_%20%20%20%20%20%20%20%20%20%20%20%20%20%0A%2F%20___%7C%20_%20__%20%20%20__%20_%20%20___%20___%20%20%20%2F%20___%7C%20___%20_%20__%20%20%20___%20_%20__%20__%20_%7C%20%7C_%20___%20%20_%20__%20%20%20%20%20%20%20%20%20%20%20%20%20%2CMMM8%26%26%26.%20%20%0A%5C___%20%5C%7C%20%27_%20%5C%20%2F%20_%60%20%7C%2F%20__%2F%20_%20%5C%20%7C%20%7C%20%20_%20%2F%20_%20%5C%20%27_%20%5C%20%2F%20_%20%5C%20%27__%2F%20_%60%20%7C%20__%2F%20_%20%5C%7C%20%27__%7C%20%20%20%20%20%20%20_...MMMMM88%26%26%26%26..._%20%20%0A%20___)%20%7C%20%7C_)%20%7C%20(_%7C%20%7C%20(_%7C%20%20__%2F%20%7C%20%7C_%7C%20%7C%20%20__%2F%20%7C%20%7C%20%7C%20%20__%2F%20%7C%20%7C%20(_%7C%20%7C%20%7C%7C%20(_)%20%7C%20%7C%20%20%20%20%20%20%20.%3A%3A%27%27%27MMMMM88%26%26%26%26%26%26%27%27%27%3A%3A.%0A%7C____%2F%7C%20.__%2F%20%5C__%2C_%7C%5C___%5C___%7C%20%20%5C____%7C%5C___%7C_%7C%20%7C_%7C%5C___%7C_%7C%20%20%5C__%2C_%7C%5C__%5C___%2F%7C_%7C%20%20%20%20%20%20%20%3A%3A%20%20%20%20%20MMMMM88%26%26%26%26%26%26%20%20%20%20%20%3A%3A%0A%20%20%20%20%20%20%7C_%7C%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%27%3A%3A....MMMMM88%26%26%26%26%26%26....%3A%3A%27%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%60%27%27%27%27MMMMM88%26%26%26%26%27%27%27%27%60%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%27MMM8%26%26%26%27%20%20%0A%20%20%20%20%20%20%20%20%22%22%22)%0A%20%20%20%20%20%20%20%20threads%20%3D%20int(input(%27%5BSpace%5D%20Enter%20The%20Number%20Of%20Threads%20%3A%20%27))%0A%20%20%20%20%20%20%20%20win32console.SetConsoleTitle(f%27%5BSpace%20Generator%5D%20-%20Started....%27)%0A%20%20%20%20%20%20%20%20for%20i%20in%20range(threads)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20t%20%3D%20threading.Thread(target%3DGenerator)%0A%20%20%20%20%20%20%20%20%20%20%20%20t.start()%0A%0ASpaceGenerator.start()