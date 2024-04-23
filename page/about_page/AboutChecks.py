import allure
from helpers.ScrollHelpers import ScrollHelpers
from page.BaseChecks import BaseChecks
from page.about_page.AboutPage import AboutPage
from page.tensor_page.tensor_data import URL_TENSOR


class AboutChecks(BaseChecks, AboutPage):

    @allure.step("Проверить открытия сайта [https://tensor.ru/about]")
    def check_open_about_page(self):
        self.check_open_url(f'{URL_TENSOR}about')

    @allure.step("Проверить заголовок 'Работаем' существует")
    def check_working_exists(self):
        ScrollHelpers.scroll_to_element(self.driver, self.title_working)
        self.check_element_exists(self.title_working)

    @allure.step("Проверить размер всех картинок, должны быть одинаковые")
    def check_size_images(self):
        list_width, list_height = self.get_list_size_images(self.image)
        try:
            assert len(set(list_width)) == 1
            assert len(set(list_height)) == 1
        except Exception:
            raise AssertionError ("Картинки неодинаковые")
