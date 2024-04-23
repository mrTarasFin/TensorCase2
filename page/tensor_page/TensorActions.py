import allure

from page.BaseActions import BaseActions
from page.tensor_page.TensorPage import TensorPage
from helpers.ScrollHelpers import ScrollHelpers


class TensorActions(TensorPage, BaseActions):

    @allure.step("Нажать на Подробнее")
    def click_more_detail(self):
        ScrollHelpers.scroll_to_element(self.driver, self.button_more_detail)
        self.click_element(self.button_more_detail)
