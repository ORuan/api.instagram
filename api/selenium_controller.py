from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium import webdriver
import requests, io, pdb, pdb, time, os, json, sys
import chromedriver_autoinstaller

class SearchInsta():
    def __init__(self, username):
        self.username = username

    def config(self):
        try:
            os.system('export INSTALL=True')
        except:
            print('O ambiente não permite a definição de variaveis de ambiente')
                
        path_install = chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")
        options.add_argument('--no-sandbox')
        options.add_argument(r"user-data-dir=./driver/data")
        return webdriver.Chrome(
                        chrome_options=options,
                        executable_path=path_install
                    )

    """
        try:
            os.environ['INSTALL']
        except:
            driver = config()
    """
    def selenium_get_username(self):
        user_agent = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36'}
        req = requests.get(f'https://www.instagram.com/web/search/topsearch/?context=blended&query={self.username}', headers=user_agent)
        content = req.json()
        users_unique = content['users']
    #profile_pic_url
        def filter_data(accounts):
            results = dict()
            result = list()
            result.append(accounts['user']['username'])
            result.append(accounts['user']['profile_pic_url'])
            result.append(accounts['user']['mutual_followers_count'])  
            return result


        resultss = map(filter_data,users_unique)
        return json.dumps(list(resultss))
