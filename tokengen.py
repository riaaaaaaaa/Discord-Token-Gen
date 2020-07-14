import json,requests,sys,random,time,threading
req = requests.Session()

tcap = 150
proxies = open('proxies.txt','r').read().splitlines()
proxies = [{'https':'http://'+proxy} for proxy in proxies]

def gen():
	proxy = random.choice(proxies)

	r = req.get('https://discord.com/api/experiments', proxies = proxy).json()
	fingerprint = r['fingerprint']
	print('Got fingerprint: '+fingerprint)

	print('Generating token...')
	r = req.post('https://discord.com/api/auth/register', json = {'captcha_key': None ,'consent': True ,'fingerprint': fingerprint,'gift_code_sku_id': None,'username': '[DISCORD] NiggerKiller'}, proxies = proxy).json()
	token = r['token']
	print('Token generated: '+token)

	with open('Tokens.txt', 'a+', encoding='utf-8') as f:
		f.write(token+"\n" )

while 1:
	threads = []
	for _ in range(tcap):
		threads.append(threading.Thread(target=gen))
	for t in threads: t.start()
	for t in threads: t.join()