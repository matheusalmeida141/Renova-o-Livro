# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Online Python compiler (interpreter) to run Python online.
import requests


url = 'https://unesp.primo.exlibrisgroup.com/primaws/suprimaLogin?lang=pt'
myobj = {
	"authenticationProfile":"LDAP",
	"username":"teste",
	"password":"teste",
	"institution":"55UNESP_INST",
	"view":"55UNESP_INST:UNESP"
}

header = {"Host": "unesp.primo.exlibrisgroup.com",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
"Accept": "application/json, text/plain, */*",
"Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
"Accept-Encoding": "gzip, deflate, br",
"Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
"Content-Length": "123",
"Origin": "https://unesp.primo.exlibrisgroup.com",
"DNT": "1",
"Connection": "keep-alive",
"Referer": "https://unesp.primo.exlibrisgroup.com/discovery/search?vid=55UNESP_INST:UNESP",
"Cookie": "JSESSIONID='755C3C90E423ABCBC52C37D76B960605.apd01.na04.prod.alma.dc01.hosted.exlibrisgroup.com:1801'; __Secure-UqZBpD3n3naPU21K6FLv5zCTTKpBupZZf92Kuo2FqkGKSg__=v1GOoKgw__B6j; urm_st=1667518169440; urm_se=1667519069440; institute=55UNESP_INST",
"Sec-Fetch-Dest": "empty",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Site": "same-origin",}
#use the 'headers' parameter to set the HTTP headers:
x = requests.post(url, data = myobj, headers = header)

#print(x.json())
print(x.status_code)

obj = x.json()
print(obj['jwtData'])

header = {"Host": "unesp.primo.exlibrisgroup.com",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
"Accept": "application/json, text/plain, */*",
"Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
"Accept-Encoding": "gzip, deflate, br",
"Authorization": "Bearer " + obj['jwtData'],
"DNT": "1",
"Connection": "keep-alive",
"Referer": "https://unesp.primo.exlibrisgroup.com/discovery/account?vid=55UNESP_INST:UNESP&section=loans&lang=pt",
"Cookie": "JSESSIONID='1D5E70E4F0B47EAB20C3F6A561A6BA9F.apd01.na04.prod.alma.dc01.hosted.exlibrisgroup.com:1801'; __Secure-UqZBpD3n3naPU21K6FLv5zCTTKpBupZZf92Kuo2FqkGKSg__=v1GOoKgw__B6j; urm_st=1667862805167; urm_se=1667866405167; institute=55UNESP_INST",
"Sec-Fetch-Dest": "empty",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Site": "same-origin",}

url = "https://unesp.primo.exlibrisgroup.com/primaws/rest/priv/myaccount/renew_all_loans?=&lang=pt"
x = requests.get(url, headers = header)
print(x.text)
print(x.status_code)

