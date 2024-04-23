import allure

from page.BaseActions import BaseActions
from page.main_page.MainPage import MainPage
from helpers.ScrollHelpers import ScrollHelpers


class MainActions(BaseActions, MainPage):

    @allure.step("Нажать на Контакты")
    def click_contacts(self):
        self.find_element(self.contacts).click()

    @allure.step("Нажать в футере 'Скачать локальные версии'")
    def click_downloads_local_versions(self):
        ScrollHelpers.scroll_to_element(self.driver, self.downloads_local_versions)
        self.click_element(self.downloads_local_versions)
