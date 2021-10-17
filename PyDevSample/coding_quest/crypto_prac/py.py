import requests
import json
import os
t= requests.get("https://api.coingecko.com/api/v3/simple/price?ids=ripple&vs_currencies=inr&include_last_updated_at=true").text
t= json.loads(t)
price =(int(t["ripple"]["inr"]))
os.system(f"notify-send")