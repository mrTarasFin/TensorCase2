import os

import allure

from page.BaseChecks import BaseChecks
from page.downloads_page.DownloadsPage import DownloadsPage
from settings import Settings


class DownloadsChecks(BaseChecks, DownloadsPage):

    @allure.step("Проверка открытия окна загрузок")
    def check_open_downloads_page(self):
        self.check_element_exists(self.title_downloads_page)

    def check_windows(self):
        self.check_element_visible(self.windows)

    @allure.step("Проверить размер скаченного файла")
    def check_file_downloaded(self):
        settings = Settings()
        name_file = os.listdir(f'{settings.ROOT_DIR}\\downloads')
        size_file = os.path.getsize(f'{settings.ROOT_DIR}\\downloads\\{name_file[0]}')
        assert 7.5 <= size_file/1000 >= 7
