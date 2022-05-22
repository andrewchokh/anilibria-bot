from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup as BS

class Anilibria:
    def __init__(self, url):
        self.url = url
        
    def get_anime_schedule(self):
        r = requests.get(self.url + '/pages/schedule.php')
        html = BS(r.content, 'html.parser')

        anime_list = []

        for e in html.select('.news-block > div > .test'):
            anime_data_list = []

            names = e.select('tr > td > a > div > .schedule-runame')
            links = e.select('tr > td > a')
        
            for i in range(len(names)):
                anime_data_list.append({
                    'name': names[i].text,
                    'link': self.url + links[i]['href'] 
                })
        
            anime_list.append(anime_data_list)

        return anime_list

    # def download_img(self, url):
    #     r = requests.get(url, allow_redirects=True)

    #     a = urlparse(url)
    #     filename = os.path.basename(a.path)
    #     open('temp/' + filename, 'wb').write(r.content)

    #     return filename
