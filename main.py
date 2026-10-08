
from curl_cffi import requests
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()
session = requests.Session(impersonate="firefox")

url = "https://unesp.primo.exlibrisgroup.com/primaws/suprimaLogin?lang=pt"

headers = {
    #"Host": "unesp.primo.exlibrisgroup.com",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:153.0) Gecko/20100101 Firefox/153.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    #"Accept-Encoding": "gzip, deflate, br, zstd",
    "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
    "Origin": "https://unesp.primo.exlibrisgroup.com",
    #"Connection": "keep-alive",
    "Referer": "https://unesp.primo.exlibrisgroup.com/discovery/search?vid=55UNESP_INST:UNESP",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    #"Priority": "u=0"
}

data = {
    "authenticationProfile": "LDAP",
    "username": f"{os.getenv("USERNAME")}",
    "password": f"{os.getenv("PASS")}",
    "institution": "55UNESP_INST",
    "view": "55UNESP_INST:UNESP",
    "targetUrl": ""
}

response = session.post(url, headers=headers, data=data)
jwt_token = response.json().get("jwtData")

if response.status_code == 200:
    print("Logado com Sucesso!")

    url = "https://unesp.primo.exlibrisgroup.com/primaws/rest/priv/myaccount/renew_all_loans?&lang=pt"
    headers = {"url = ""User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:153.0) Gecko/20100101 Firefox/153.0",
    "Accept": "application/json, text/plain, */*",
    "Authorization": jwt_token if jwt_token else 'Bearer "<insira_token_aqui>"',
    "Referer": "https://unesp.primo.exlibrisgroup.com/discovery/account?vid=55UNESP_INST:UNESP&section=loans&lang=pt"}

    response = session.get(url, headers=headers)

    print(f"Status Renovação: {response.status_code}")
    print(response.text)
else:
    print("Erro de Login")
