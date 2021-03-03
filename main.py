from flask import Flask, render_template, request, jsonify
import requests
import os
from datetime import datetime

BOT_API = os.getenv('BOT_API')
OWNER_ID = os.getenv('OWNER_ID')
app = Flask(__name__)


@app.route("/")
def main():
    header = request.headers.get('cf-connecting-ip')
    url = f"http://ip-api.com/json/{header}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query"
    response = requests.get(url)
    info = response.json()
    
    output = f"""*🥳🥳A new visiter arrived on the website!!🥳🥳*
*Timestamp :* `{datetime.now()}`
*IP Address : {info['query']}*
*Details : *
    *Status :* `{info['status']}`
    *Continent Code :* `{info['continentCode']}`
    *Country :* `{info['country']}`
    *Country Code :* `{info['countryCode']}`
    *Region :* `{info['region']}`
    *Region Name :* `{info['regionName']}`
    *City :* `{info['city']}`
    *District :* `{info['district']}`
    *Zip :* `{info['zip']}`
    *Latitude :* `{info['lat']}`
    *Longitude :* `{info['lon']}`
    *Time Zone :* `{info['timezone']}`
    *Offset :* `{info['offset']}`
    *Currency :* `{info['currency']}`
    *ISP :* `{info['isp']}`
    *Org :* `{info['org']}`
    *As :* `{info['as']}`
    *Asname :* `{info['asname']}`
    *Reverse :* `{info['reverse']}`
    *User is on Mobile :* `{info['mobile']}`
    *Proxy :* `{info['proxy']}`
    *Hosting :* `{info['hosting']}`
    """
    requests.get(f'https://api.telegram.org/bot{BOT_API}/sendmessage?chat_id={OWNER_ID}&text={output}&parse_mode=Markdown')
    return jsonify({"Your IP Address ":info['query'], "Status":"IP successfully tracked."})
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
