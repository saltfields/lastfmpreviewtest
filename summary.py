import requests
import json
import sys

user = sys.argv[1]

apiUrl = "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&limit=1&user="+user+"&api_key=YOURAPIKEY&format=json"
response = requests.get(apiUrl)
r = response.json()
if ("@attr" in r["recenttracks"]["track"][0]) :
  nowplaying = "(currently listening)"
else :
  tIndex = int(str(r["recenttracks"]["track"][0]["date"]["#text"]).find(","))
  hr = int(str(r["recenttracks"]["track"][0]["date"]["#text"])[tIndex+2:tIndex+4])
  hr-=7
  day = int(str(r["recenttracks"]["track"][0]["date"]["#text"])[0:tIndex-8])
  if hr < 0:
    hr+=24
    day -=1
  nowplaying = "(played on " + str(day) + str(r["recenttracks"]["track"][0]["date"]["#text"])[tIndex-9:tIndex+2] + str(hr) + str(r["recenttracks"]["track"][0]["date"]["#text"])[tIndex+4:tIndex+7] + " PST)"
  #print(str(r["recenttracks"]["track"][0]["date"]["#text"]))
 
print("\nmost recent play: " + str(r["recenttracks"]["track"][0]["name"]) + " by " + str(r["recenttracks"]["track"][0]["artist"]["#text"]) + " " + nowplaying)

apiUrl = "http://ws.audioscrobbler.com/2.0/?method=user.gettopartists&user="+user+"&period=overall&limit=5&api_key=YOURAPIKEY&format=json"
response = requests.get(apiUrl)
r = response.json()

print("\ntop artists")
print("#/////////#")
print("1. " + str(r["topartists"]["artist"][0]["name"]) + " (" + str(r["topartists"]["artist"][0]["playcount"]) + " plays)")
print("2. " + str(r["topartists"]["artist"][1]["name"]) + " (" + str(r["topartists"]["artist"][1]["playcount"]) + " plays)")
print("3. " + str(r["topartists"]["artist"][2]["name"]) + " (" + str(r["topartists"]["artist"][2]["playcount"]) + " plays)")
print("4. " + str(r["topartists"]["artist"][3]["name"]) + " (" + str(r["topartists"]["artist"][3]["playcount"]) + " plays)")
print("5. " + str(r["topartists"]["artist"][4]["name"]) + " (" + str(r["topartists"]["artist"][4]["playcount"]) + " plays)")