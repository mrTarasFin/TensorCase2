import allure

from page.BaseChecks import BaseChecks
from page.tensor_page.TensorPage import TensorPage
from page.tensor_page.tensor_data import URL_TENSOR


class TensorChecks(BaseChecks, TensorPage):

    @allure.step("Проверить открытие страницы")
    def check_open_tensor_page(self):
        self.check_open_url(URL_TENSOR)

    @allure.step("Проверить логотип существует")
    def check_logo_exist(self):
        self.check_element_exists(self.logo_tensor)

    @allure.step("Проверить заголовок 'Сила в людях' существует")
    def check_power_people_exists(self):
        self.check_element_exists(self.title_power_people)

