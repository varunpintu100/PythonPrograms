import requests
import random

Number = input('Enter the mobile number : ')
Number_code = '+91'+Number
heads = [
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0',
        'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0',
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0",
    'Accept': '*/*'
    },
]
HEADERS = random.choice(heads)
try:
    response = requests.get("https://securedapi.confirmtkt.com/api/platform/register?newOtp=true&mobileNumber="+Number,headers=HEADERS)
    if response.json() == True:
        print("The SMS is sent !!!!")
    else:
        print("The SMS is not sent !!!!!")
except Exception as e:
    print(f"The api couldn't connect : {e}")
try:
    response = requests.post("https://api.nnnow.com/d/api/appDownloadLink",json={"mobileNumber": Number},headers=HEADERS)
    # if response["Status"] == True:
    #     print("The SMS is sent !!!")
    # else:
    #     print("The SMS is not sent !!!!")
except Exception as e:
    print(f"The api couldnt connect : {e}")

