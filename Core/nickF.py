from colorama import Fore
import requests

snm = {"Instagram": "instagram.com/", "VK": "vk.com/", "Twitter": "twitter.com/",
"OK": "ok.ru/", "Facebook": "www.facebook.com/", "Telegram": "t.me/", 
"TikTok": "www.tiktok.com/@", "Mamba": "www.mamba.ru/", "Badoo": "badoo.com/profile/", 
"Patreon": "patreon.com/", "TamTamChat": "tt.me/", "Teletype": "teletype.in/@"}



vh = {"YouTube": "youtube.com/user/", 
"Twitch": "twitch.tv/", "Pornhub": "rt.pornhub.com/users/", "Red Tube": "ru.redtube.com/users/", "Xvideos": "www.xvideos.com/profiles/"}



games = {"Steam": "steamcommunity.com/id/", "Ubisoft": "club.ubisoft.com/profile/", 
"Chess": "www.chess.com/ru/member/", "Xbox": "account.xbox.com/profile?gamertag=", "Warface": "wfts.su/profile/",
"Faceit": "www.faceit.com/ru/players/"}


money = {"DonationAlerts": "www.donationalerts.com/r", "Qiwi": "qiwi.me/", "PayPal": "paypal.me/"}

forums = {"Anime planet": "anime-planet.com/users/", "Linux": "www.linux.org/members/", 
"Bitcoinforum": "bitcoinforum.com/profile/", "Scala lang": "users.scala-lang.org/u/",
 "Pikabu": "pikabu.ru/@", "Signalusers": "community.signalusers.org/u/"

}



other = {"Github": "github.com/", "Ebay": "www.ebay.com/usr/", "Gitlab": "gitlab.com/", 
"AskFM": "ask.fm/", 
"PyPi": "pypi.org/user/", "Wikipedia": "wikipedia.org/wiki/user:", "Pastebin": "pastebin.com/u/", 
"Metacritic": "metacritic.com/user/", "OpenStreetMap": "www.openstreetmap.org/user/", 
"Pinboard": "pinboard.in/u:", "Pinkbike": "pinkbike.com/u/",
"Seoclerks": "www.seoclerks.com/user/"}

prot = "https://"

def osint(dict, nick):
  for key, site in dict.items():
	  url = prot + site + nick
	  try:
	   r = requests.get(url)
	
	   if r.status_code == 200:
	       print(Fore.GREEN + "found " + key + ": " + url)
	   else:
		   print(Fore.RED + key + " not found")
	  except:
	   print(Fore.YELLOW + "request error for " + key) 




