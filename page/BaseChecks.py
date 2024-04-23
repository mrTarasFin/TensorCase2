import allure
from selenium.common import NoSuchElementException

from page.BasePage import BasePage


class BaseChecks(BasePage):

    @allure.step("Проверить открытие ссылки {current_url}")
    def check_open_url(self, current_url: str):
        """
        Функция получает url адрес страницы
        """
        try:
            get_url = self.driver.current_url
            assert str(get_url) == current_url
        except Exception as ex:
            raise AssertionError (f"Не получилось получить ссылку сайта\n"
                                  f"ОШИБКА: {ex}")

    @allure.step("Проверить элемент существует")
    def check_element_exists(self, locator):
        try:
            self.find_element(locator)
        except NoSuchElementException:
            raise "Элемент не найден"

    @allure.step("Проверить текст элемента с заданным текстом")
    def check_element_text_by_current_text(self, locator, current_text):
        try:
            text = self.find_element(locator).text
            assert text == current_text
        except Exception:
            raise AssertionError(f'Текст не совпадает\n'
                                 f'Ожидаемый текст: {current_text}\n'
                                 f'Фактический текст: {text}')

    @allure.step("Проверить в url содержиться текст {text}")
    def check_text_in_url(self, text):
        try:
            get_url = self.driver.current_url
            assert text in get_url
        except Exception as ex:
            raise AssertionError(f'В {get_url} нет совпадений по тексту {text}')

    @allure.step("Проверить видимость элемента")
    def check_element_visible(self, locator):
        try:
            self.visible_element(locator)
        except Exception:
            raise AssertionError("Элемент не виден на странице")
