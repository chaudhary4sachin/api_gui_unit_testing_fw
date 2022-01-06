from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.departure_city_dd = driver.find_element(By.XPATH, '//select[@name=\'fromPort\']')
        self.destination_city_dd = driver.find_element(By.XPATH, '//select[@name=\'toPort\']')
        self.find_flights_button = driver.find_element(By.XPATH, '//input[@class=\'btn btn-primary\']')


    def get_page_title(self):
        return self.driver.title


    def select_departure_city(self, city):
        select = Select(self.departure_city_dd)
        select.select_by_value(city)
        return True

    def select_destination_city(self, city):
        select = Select(self.destination_city_dd)
        select.select_by_value(city)
        return True

    def click_find_flights_btn(self):
        self.find_flights_button.click()
