import re
import requests
from bs4 import BeautifulSoup as BS4

URL = 'https://jut.su/'

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15",
}

def get_html(url, params=''):
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()  
    return response

def extract_image_url(style):
    match = re.search(r"url\('([^']+)'\)", style)
    return match.group(1) if match else "No image"

def get_data(html):
    bs = BS4(html, 'html.parser')
    items = bs.find_all('div', class_='all_anime')  
    jutsu_list = []

    for item in items:
        title_div = item.find('div', class_='aablock')  
        title = title_div.get_text(strip=True) if title_div else "No title"

        image_div = item.find('div', class_="all_anime_image")
        if image_div and 'style' in image_div.attrs:
            image = extract_image_url(image_div['style'])
        else:
            image = "No image"

        tooltip_div = item.find('div', class_='all_anime_tooltip')
        tooltip = tooltip_div['title'] if tooltip_div and 'title' in tooltip_div.attrs else "No tooltip"

        jutsu_list.append({
            'title': title,
            'image': image,
            'tooltip': tooltip
        })
    return jutsu_list

def parsing():
    response = get_html('https://jut.su/anime/')
    return get_data(response.text)

print(parsing())
