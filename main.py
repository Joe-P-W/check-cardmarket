import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class CardMarket(webdriver.Chrome):
    def __init__(self, *options):

        chrome_options = Options()
        for option in options:
            chrome_options.add_argument(option)

        chrome_options.add_argument("--start-maximized")

        super().__init__(executable_path="driver/chromedriver.exe", options=chrome_options)

    def __enter__(self):
        self.get("https://www.cardmarket.com/en/Magic")

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


if __name__ == "__main__":
    with CardMarket() as driver:
        time.sleep(5)