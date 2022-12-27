import requests, random, time
from colorama import Fore

while True:
    user = ""
 
    for character in random.choices("abcdefghijklmnopqrstuvwxyz1234567890", k=3):
        user = user + character
 
    response = requests.get(f"https://instagram.com/{user}/")

    

    if (response.status_code == 200): #200 alınabilir demektir phiec
        print(Fore.RED + f"Calismiyor: {user}" + Fore.RESET)
    elif (response.status_code == 404): # 404 eror kodudur phiec
        print(Fore.GREEN + f"Yakala: {user}" + Fore.RESET)

    else:
        print("BLOCKED FROM SITE")
        time.sleep(120)
        
