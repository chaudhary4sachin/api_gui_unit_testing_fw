from selenium.webdriver.chrome.options import Options
import config
import unittest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from pages.home_page import HomePage


class TestHomepage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        ser = Service(executable_path=r"../../../drivers/chrome/mac/chromedriver")
        options = Options()
        options.add_argument("--headless")
        options.add_argument("window-size=1400,1500")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("start-maximized")
        options.add_argument("enable-automation")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-dev-shm-usage")
        cls.driver = webdriver.Chrome(service=ser, options=options)
        cls.driver.get(url=config.app_url)
        cls.driver.maximize_window()
        cls.homepage = HomePage(cls.driver)

    def test_home_page_title(self):
        self.assertEqual("BlazeDemo", self.homepage.get_page_title())

    def test_reserve_page_title(self):
        self.homepage.select_departure_city('Paris')
        self.homepage.select_destination_city('Rome')
        self.homepage.click_find_flights_btn()
        self.assertEqual("BlazeDemo - reserve", self.homepage.get_page_title())

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
