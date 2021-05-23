import requests
import webbrowser
from bs4 import BeautifulSoup

def download_game(download_url):
    payload={}
    headers = {
    'authority': 'uploadhaven.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Microsoft Edge";v="90"',
    'sec-ch-ua-mobile': '?0',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.49',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': f'{download_url}',
    'accept-language': 'es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5',
    'cookie': '_ga=GA1.2.291078755.1619670467; _gid=GA1.2.529339966.1619670467; XSRF-TOKEN=eyJpdiI6IlN6RkZlb0VMdSsxcUZMakVWbzVabGc9PSIsInZhbHVlIjoia0hFbmgrYzExUlhYU3BUeUkxSjVTWW1tTVMxVHc4d1gyU1hcLzlKVXdNZlpvNldcL1ZRSWFCTkFQRVg5c2pCNUE5IiwibWFjIjoiZTcwMWIzN2JiNzU0YzM1ZjA3ZDExZDE0MjJmZDFjYWFjMjVjMGZjZmZkMDNmOTJiZjAyMjUwZWJkMGRhMGU1ZCJ9; uploadhaven_session=eyJpdiI6IjJlRmhYMmNZMEl2TjNraFwvSW5xMGlBPT0iLCJ2YWx1ZSI6IjA1amdMTlZXNk9FYUl0YlRzOWFISDd4YUl5R2IwZ2NmZm1Tc1FlS2hqRXdlZ3RJTHZzMm15dnhycUxBT1VRb2IiLCJtYWMiOiIxMDY2NWRiOWIzYTVkMjQwYzczNWE2M2RkMTNlMDQxY2YzNGZiN2FmZjIzNjZjZDY5OWE5MTRlMmZjZjMxYzY2In0%3D; XSRF-TOKEN=eyJpdiI6InFwanFJOXplNEFVUjRDZGVxMnY3T1E9PSIsInZhbHVlIjoiODZiWjBNSTlpek96MVpuM0xzcEVuWHhVSkMydnRaRTFOc3lOc1BDYVo5WXh2ODJiZkZiQVpKak5MM2Zxc2xkTSIsIm1hYyI6ImU1MDRiZjVhZmU2YzYyZjJjNzNmMzVmY2UyMDViNDdiMGM5MzU5MDQyNDcyNDQzYzFhOTQ1OTQ1ODY2Y2ZhYzQifQ%3D%3D; uploadhaven_session=eyJpdiI6IkJ2c3l3Vk5wS1VpdDJva1U5UlpBTlE9PSIsInZhbHVlIjoiemtsdVdCdHVKT0paZzBKZFhaMTdtUXU3VDdTaXFYRGprdFwvZU04NWJXM1REZEdaZXBQZFEzdzArbXRUa2NCS00iLCJtYWMiOiJjYjI3ZGExNmEzMDQzMDI2MGRjOTJlOTA1N2ZkYzg3MDE4MmU4MWUxYTY2MjYxZmZkMjhiYTZlMGQ4ZmQ3ZTY0In0%3D'
    }

    response = requests.request("GET", download_url, headers=headers, data=payload)
    soup = BeautifulSoup(response.text, 'lxml')
    download_button = soup.find_all(class_="alert alert-success")
    #print(soup)
    print(download_button)

def find_downloadBtn(game_url):
    response = requests.request("GET", game_url)
    soup = BeautifulSoup(response.text, 'lxml')
    download_button = soup.find_all(class_="btn-download")
    shortcut_download = download_button[0]['href']
    print(shortcut_download)
    webbrowser.open(game_url, new=1)
    download_game(shortcut_download)

def main():
    game_download = input("Game to download...")
    url = f"https://steamunlocked.net/?s={game_download}"

    response = requests.request("GET", url)
    soup = BeautifulSoup(response.text, 'lxml')
    games = soup.find_all(class_="cover-item-title")
    print(games)
    i = 0
    for game in games:
        i = i + 1
        print(f'{i}.{game.h1.text}')

    selected_game = int(input("Select a game...")) - 1
    print(f"Selected game {games[selected_game].h1.text}")
    find_downloadBtn(games[selected_game].a['href'])

#download_game('https://uploadhaven.com/download/4ae86e02298ef940aa8c1e8f14cb338c')
main()
