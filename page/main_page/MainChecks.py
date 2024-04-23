import allure

from page.BaseChecks import BaseChecks
from page.main_page.MainPage import MainPage


class MainChecks(BaseChecks, MainPage):

    @allure.step("Проверить открытие главной страницы")
    def check_open_main_page(self):
        self.find_element(self.main_logo)
