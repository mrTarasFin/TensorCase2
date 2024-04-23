import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page.base_page_data import URL


class BasePage:
    """
    Класс определяет базовые методы для работы с WebDriver
    """

    def __init__(self, driver, url=URL):
        self.driver = driver
        self.url = url

    def find_element(self, locator, time=15):
        """
        Функция находит элемент на странице по локатору, аргумент time устанавливает время ожидания
        """
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Элемент {locator} не найден'
                                                      )

    def find_elements(self, locator, time=15):
        """
        Функция находит все элементы по локатору, аргумент time устанавливает время ожидания
        """
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f'Элементы {locator} не найдены'
                                                      )

    def expect_load_page(self, title, time=15):
        WebDriverWait(self.driver, time).until(EC.title_is(title))

    def visible_element(self, locator, time=15):
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located((locator)))

    def get_text_element(self, locator):
        try:
            element = self.find_element(locator)
        except Exception:
            raise AssertionError("Не получилось найти элемент")
        return element.text
