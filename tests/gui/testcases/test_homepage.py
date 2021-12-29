import config
import unittest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from pages.home_page import HomePage


class TestHomepage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        ser = Service(executable_path=r"/Users/sachinchaudhary/PycharmProjects/api_gui_unit_testing_fw/drivers/"
                                      r"chrome/mac/chromedriver")
        cls.driver = webdriver.Chrome(service=ser)
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
