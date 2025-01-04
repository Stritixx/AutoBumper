import tls_client, platform, random, secrets, json, uuid, time, os
from pystyle import Colorate, Colors
from colorama import Fore, Style
from datetime import datetime



color_reset = Style.RESET_ALL
color_magenta = Fore.MAGENTA
color_yellow = Fore.YELLOW
color_green = Fore.GREEN
color_red = Fore.RED






def company_name():
    print(Colorate.Horizontal(Colors.purple_to_blue, f'''
                              
                              
	                    	          ________ _____  ________  ___________ __________________ 
	                    	          ___  __ )__  / / /___   |/  /___  __ \___  ____/___  __ |
	                    	         __  __  |_  / / / __  /|_/ / __  /_/ /__  __/   __  /_/ /
	                    	         _  /_/ / / /_/ /  _  /  / /  _  ____/ _  /___   _  _, _/ 
	                    	         /_____/  \____/   /_/  /_/   /_/      /_____/   /_/ |_|\n\n\n																														
    ''', 1)
)
    



	
def check_system():
    os_name = platform.system()

    if os_name == "Windows":
        system = "windows"

    elif os_name == "Linux":
        system = "linux"

    elif os_name == "Darwin":
        system = "darwin"

    return system





def cls():
    system = check_system()

    if system == "windows":
        os.system('cls')

    else:
        os.system('clear')





def discordHeaders(token):
	headers = {
        'accept': '*/*',
        'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': token,
        'content-type': 'application/json',
        'origin': 'https://discord.com',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        'x-discord-locale': 'pl',
        'x-discord-timezone': 'Europe/Warsaw',
    }

	return headers





def bumper(tls_session, token, guild_id, channel_id, server_name):
	payload = {
		"type": 2,
		"application_id": "302050872383242240",
		"guild_id": guild_id,
		"channel_id": channel_id,
		"session_id": str(uuid.uuid4()),
		"data": {
            "version": "1051151064008769576",
            "id": "947088344167366698",
            "name": "bump",
        },
        "nonce": str(secrets.randbelow(10**19) + 10**18),	
	}


	rr = tls_session.post("https://discord.com/api/v9/interactions", headers = discordHeaders(token), json = payload)


	if rr.status_code == 204:
		print(f'{color_magenta}{datetime.now().strftime("%H:%M:%S")}{color_reset} [{color_green}/{color_reset}] {color_yellow}>> {color_reset} Used {color_green}bump{color_reset} command on {server_name}!')


	else:
		print(f'{color_magenta}{datetime.now().strftime("%H:%M:%S")}{color_reset} [{color_red}/{color_reset}] {color_yellow}>> {color_reset} Can\'t bump server: {color_red}{server_name}!{color_reset}')







cls()
company_name()




while True:
	with open('./config/config.json') as file:
		data = json.load(file)


		time.sleep(random.randint(1, 300))


		for server in data:
			server_name = server['server_name']
			guild_id = server['server_id']
			channel_id = server['channel_id']
			token = server['token']


			tls_session = tls_client.Session(
				client_identifier = "chrome_120",
				random_tls_extension_order = True,
			)


			tls_session.get("https://discord.com")
			cookies = tls_session.cookies.get_dict()
			tls_session.cookies.update(cookies)


			bumper(tls_session, token, guild_id, channel_id, server_name)
                  
			time.sleep(random.randint(1, 10))