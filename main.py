import requests
token = '2619421814940190'
urls = [
    f'https://www.superheroapi.com/api.php/{token}/search/Hulk',
    f'https://www.superheroapi.com/api.php/{token}/search/Thanos',
    f'https://www.superheroapi.com/api.php/{token}/search/Captain%America',
]
def requests_get(url_all):
    r = (requests.get(url) for url in url_all)
    return r

def parser():
    super_man = []
    for item in requests_get(urls):
        intelligence = item.json()
        try:
            for power_stats in intelligence['results']:
                super_man.append({
                    'name': power_stats['name'],
                    'intelligence': power_stats['powerstats']['intelligence'],
                })
        except KeyError:
            print(f"Проверте ссылки urls: {urls}")

    intelligence_super_hero = 0
    name = ''
    for intelligence_hero in super_man:
        if intelligence_super_hero < int(intelligence_hero['intelligence']):
            intelligence_super_hero = int(intelligence_hero['intelligence'])
            name = intelligence_hero['name']

    print(f"Самый умный -  {name}, его интелект: {intelligence_super_hero}")


parser()
