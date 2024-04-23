import allure
from selenium.webdriver.remote.webelement import WebElement

from page.BasePage import BasePage


class BaseActions(BasePage):

    @allure.step("----------------------ШАГ №{number}----------------------")
    def next_step(self, number):
        return self

    @allure.step("Нажать на элемент")
    def click_element(self, locator):
        try:
            element: WebElement = self.find_element(locator)
            element.click()
        except Exception as ex:
            raise AssertionError(f'Ошибка при нажатии на элемент: {ex}')

    @allure.step("Переход на следующую вкладку")
    def next_page(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
