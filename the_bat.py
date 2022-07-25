import requests
from time import sleep
# Bold
BBlack="\033[1;30m"       # Black
BRed="\033[1;31m"         # Red
BGreen="\033[1;32m"       # Green
BYellow="\033[1;33m"      # Yellow
BBlue="\033[1;34m"        # Blue
BPurple="\033[1;35m"      # Purple
BCayn="\033[1;36m"        # Cyan
BWhite="\033[1;37m"       # White
print(BRed+f'''


████████╗██╗  ██╗███████╗
╚══██╔══╝██║  ██║██╔════╝
   ██║   ███████║█████╗  
   ██║   ██╔══██║██╔══╝  
   ██║   ██║  ██║███████╗
   ╚═╝   ╚═╝  ╚═╝╚══════╝

██████╗  █████╗ ████████╗
██╔══██╗██╔══██╗╚══██╔══╝
██████╔╝███████║   ██║   
██╔══██╗██╔══██║   ██║   
██████╔╝██║  ██║   ██║   
╚═════╝ ╚═╝  ╚═╝   ╚═╝   
                         
[1] - info acc
[2] - get following
[3] - get followers 

[4] - exit


''')
c=int(input(f'[+] - Choose : '))




if c ==4:
	exit()
	
	
	
	
user = input(f'[+] - username : ')
pas=input(f'[+] - password : ')
url_l = 'https://www.instagram.com/accounts/login/ajax/'
h = {'accept':'*/*',
'accept-encoding':'gzip, deflate, br',
'accept-language':'ar,en-US;q=0.9,en;q=0.8',
'content-length':'326',
'content-type':'application/x-www-form-urlencoded',
'cookie':'mid=YVvhbgALAAGEYIx5zhMwH4bDBV45; ig_did=648907BC-0061-4C67-AFF5-C72FAA705508; ig_nrcb=1; rur="LDC\05451296553316\0541675250058:01f73352f31122060f419a1c03ef57b01f1db6d027546e0dce91569f7ba529abb34ba7de"; csrftoken=nM9X5ZO6mQsQ2mbsnSVMu2fy8wd5woQe',
'origin':'https://www.instagram.com',
'referer':'https://www.instagram.com/',
'sec-ch-ua':'" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
'x-asbd-id':'198387',
'x-csrftoken':'nM9X5ZO6mQsQ2mbsnSVMu2fy8wd5woQe',
'x-ig-app-id':'936619743392459',
'x-ig-www-claim':'hmac.AR3VqP_m-krwiZnt3-dga6AdX4Ci5cwQwDhvGD_6DT0IRX8c',
'x-instagram-ajax':'ee0117db2fab',
'x-requested-with':'XMLHttpRequest'}
d = {'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1643714074:'+(pas),'username':user,'queryParams':'{}','optIntoOneTap':'false','stopDeletionNonce':'','trustedDeviceRecords':'{}',}
r = requests.post(url_l,headers=h,data=d)
if '"authenticated":true' in r.text:
    
    si = r.cookies['sessionid']
    id = r.cookies['ds_user_id']
    csrftoken=r.cookies['csrftoken']
else:
    print(BRed+' [×] Erorr Login => ',pas)
    exit()
def info(u):
  url=f'https://i.instagram.com/api/v1/users/web_profile_info/?username={u}'
  headers={
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'accept-encoding': 'gzip, deflate, br',
  'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
  'cache-control': 'max-age=0',
  'cookie': f'ig_did=37396E22-2BAA-45B4-BE12-2C138F2EE907; ig_nrcb=1; mid=Yoo2NAALAAF_bSUg9E76T9FjnyOg; datr=1w6bYk9s5Fe7mNlwoBvLzX_d; shbid="6501\{id}\0541689888481:01f73c5c447b81316667f3fef03e854ec17819127a3a7cfc708b6d6e3b1375631101f397"; shbts="1658352481\{id}\0541689888481:01f71e2280fe2389aebca035d43296bda632ccf8386b2b0d3dbc3285dce2018e676c77fc"; ds_user_id={id}; csrftoken={csrftoken}; sessionid={si}; rur="NAO/{id}\0541690144166:01f716870c4d087f0dc86549dd21ad03c1b4a998a97bce93ceda73f7ddfef603bcf6b03a"',
  'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'none',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 Instagram 231.0.0.18.113',
  'x-frame-options': 'SAMEORIGIN'
  }
  req=requests.get(url,headers=headers)
  print('\n'*3)
  print('====== started ======')
  print('\n'*3)
  print('\n'*19)
  try:
    print(f'[+] status : '+req.json()['status'])
  except :
    print(f'[+] user not found')
  print('')
  sleep(0.2)
  print(f'[+] user : '+u)
  print('')
  sleep(0.2)
  
  print(f'[+] bio : '+req.json()['data']['user']['biography'])
  print('')
  sleep(0.2)
  print(f'[+] link : '+str(req.json()['data']['user']['external_url']))
  print('')
  sleep(0.2)
  print(f'[+] following :  '+str(req.json()['data']['user']['edge_followed_by']['count']))
  print('')
  sleep(0.2)
  print(f'[+] followers :  '+str(req.json()['data']['user']['edge_follow']['count']))
  print('')
  sleep(0.2)
  print(f'[+] name :  '+str(req.json()['data']['user']['full_name']))
  print('')
  sleep(0.2)
  print(f'[+] id : '+str(req.json()['data']['user']['id']))
  print('')
  sleep(0.2)
  a=str(req.json()['data']['user']['is_business_account'])
  print(f'[+] business account : '+a)
  print('')
  sleep(0.2)
  if a == 'True' :
    print('')
    sleep(0.2)
    print(f'[+] name business : '+str(req.json()['data']['user']['category_name']))
  else:
    pass
  print('')
  sleep(0.2)
  print(f'[+] business email :  '+str(req.json()['data']['user']['business_email']))
  print('')
  sleep(0.2)
  print(f'[+] business number :  '+str(req.json()['data']['user']['business_phone_number']))
  print('')
  sleep(0.2)
  print(f'[+] private : '+str(req.json()['data']['user']['is_private']))
  print('')
  #sleep(2)
  #print('========not important==========')
  print('')
  sleep(0.2)
  print(f'[+] fbid :  '+str(req.json()['data']['user']['fbid']))
  print('')
  sleep(0.2)
  print(f'[+] verified :  '+str(req.json()['data']['user']['is_verified']))
  print('')
  sleep(0.2)
  print(f'[+] clips :  '+str(req.json()['data']['user']['has_clips']))
if c==1:
  u=input(f'[+] - username target : ')
  info(u)




















def get_ing():
  global id
  global si
  global csrftoken
  u=input(f'[+] - username target : ')
  ur=f'https://i.instagram.com/api/v1/users/web_profile_info/?username={u}'
  header={
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'accept-encoding': 'gzip, deflate, br',
  'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
  'cache-control': 'max-age=0',
  'cookie': f'ig_did=37396E22-2BAA-45B4-BE12-2C138F2EE907; ig_nrcb=1; mid=Yoo2NAALAAF_bSUg9E76T9FjnyOg; datr=1w6bYk9s5Fe7mNlwoBvLzX_d; shbid="6501\{id}\0541689888481:01f73c5c447b81316667f3fef03e854ec17819127a3a7cfc708b6d6e3b1375631101f397"; shbts="1658352481\{id}\0541689888481:01f71e2280fe2389aebca035d43296bda632ccf8386b2b0d3dbc3285dce2018e676c77fc"; ds_user_id={id}; csrftoken={csrftoken}; sessionid={si}; rur="NAO/{id}\0541690144166:01f716870c4d087f0dc86549dd21ad03c1b4a998a97bce93ceda73f7ddfef603bcf6b03a"',
  'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'none',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 Instagram 231.0.0.18.113',
  'x-frame-options': 'SAMEORIGIN'
  }
  req=requests.get(ur,headers=header)
  id = str(req.json()['data']['user']['id'])
  print(f'[+] - id : '+id)
  lis=int(input(f'[+] - number of following : '))
  url=f'https://i.instagram.com/api/v1/friendships/{id}/following/?count={lis}'

  
  headers={
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'cookie': f'ig_did=37396E22-2BAA-45B4-BE12-2C138F2EE907; ig_nrcb=1; mid=Yoo2NAALAAF_bSUg9E76T9FjnyOg; datr=1w6bYk9s5Fe7mNlwoBvLzX_d; ds_user_id={id}; shbid="6501\{id}\0541690153954:01f73336d2f16eae237610a06f5bcd1f504113d2f3f5a8272e7a3632b1c49a2b38d996b8"; shbts="1658617954\{id}\0541690153954:01f7daef559297f48fade12c799d37d559c1714e6d5f1c748d113e3afe054482d99ce705"; csrftoken={csrftoken}; sessionid={si}; rur="NAO\{id}\0541690220317:01f7a8da6b0e6b43e92dfc93007569e40f9e2e1b878df993fcb2864254ddd65cdb5e7daf"',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 Instagram 231.0.0.18.113',
    'x-frame-options': 'SAMEORIGIN'
  }
  req=requests.get(url,headers=headers)
  r=req.text
  print('\n'*3)
  print('   ====== started ======')
  print('\n'*3)
  lis=lis+1
  for i in range(1,lis):
      try:
          sleep(0.1)
          a=r.split('"username"')[i]
          b=a.split('","')[0]
          c=b.split(':"')[1]
          #b=str(a.split('","')[0])
          print(f'[{i}] - username : '+c)
      except:
          print('[-] we finished ' )
if c==2:
  get_ing()






def get_ers():
  global id
  global si
  global csrftoken
  u=input(f'[+] - username target :  ')
  ur=f'https://i.instagram.com/api/v1/users/web_profile_info/?username={u}'
  header={
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'accept-encoding': 'gzip, deflate, br',
  'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
  'cache-control': 'max-age=0',
  'cookie': f'ig_did=37396E22-2BAA-45B4-BE12-2C138F2EE907; ig_nrcb=1; mid=Yoo2NAALAAF_bSUg9E76T9FjnyOg; datr=1w6bYk9s5Fe7mNlwoBvLzX_d; shbid="6501\{id}\0541689888481:01f73c5c447b81316667f3fef03e854ec17819127a3a7cfc708b6d6e3b1375631101f397"; shbts="1658352481\{id}\0541689888481:01f71e2280fe2389aebca035d43296bda632ccf8386b2b0d3dbc3285dce2018e676c77fc"; ds_user_id={id}; csrftoken={csrftoken}; sessionid={si}; rur="NAO/{id}\0541690144166:01f716870c4d087f0dc86549dd21ad03c1b4a998a97bce93ceda73f7ddfef603bcf6b03a"',
  'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'none',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 Instagram 231.0.0.18.113',
  'x-frame-options': 'SAMEORIGIN'
  }
  req=requests.get(ur,headers=header)
  id = str(req.json()['data']['user']['id'])
  print(f'[+] - id : '+id)
  lis=int(input(f'[+] - number of followers : '))
  url=f'https://i.instagram.com/api/v1/friendships/{id}/followers/?count={lis}'

  
  headers={
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'cookie': f'ig_did=37396E22-2BAA-45B4-BE12-2C138F2EE907; ig_nrcb=1; mid=Yoo2NAALAAF_bSUg9E76T9FjnyOg; datr=1w6bYk9s5Fe7mNlwoBvLzX_d; ds_user_id={id}; shbid="6501\{id}\0541690153954:01f73336d2f16eae237610a06f5bcd1f504113d2f3f5a8272e7a3632b1c49a2b38d996b8"; shbts="1658617954\{id}\0541690153954:01f7daef559297f48fade12c799d37d559c1714e6d5f1c748d113e3afe054482d99ce705"; csrftoken={csrftoken}; sessionid={si}; rur="NAO\{id}\0541690220317:01f7a8da6b0e6b43e92dfc93007569e40f9e2e1b878df993fcb2864254ddd65cdb5e7daf"',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 Instagram 231.0.0.18.113',
    'x-frame-options': 'SAMEORIGIN'
  }
  req=requests.get(url,headers=headers)
  r=req.text
  print('\n'*3)
  print('   ====== started ======')
  print('\n'*3)
  lis=lis+1
  for i in range(1,lis):
      try:
          sleep(0.1)
          a=r.split('"username"')[i]
          b=a.split('","')[0]
          c=b.split(':"')[1]
          #b=str(a.split('","')[0])
          print(f'[{i}] - username : '+c)
      except:
          print('[-] we finished ' )
       
  
if c==3:
  get_ers()

  
    
      


        









