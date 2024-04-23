import allure

from page.BaseActions import BaseActions
from page.downloads_page.DownloadsPage import DownloadsPage


class DownloadsActions(BaseActions, DownloadsPage):

    @allure.step("Нажать на СБИС плагин")
    def click_sbis_plagin(self):
        self.click_element(self.sbis_plagin)

    @allure.step("Нажать на операционную систему Windows")
    def click_windows_os(self):
        self.click_element(self.windows)

    @allure.step("Нажать на ссылку для скачивания файла")
    def click_download_file(self):
        self.click_element(self.downloads_link)
