from selenium.webdriver.common.by import By
from page.BasePage import BasePage
from page.downloads_page.downloads_data import *


class DownloadsPage(BasePage):

    title_downloads_page = (By.XPATH, f'//h1[contains(text(), "{TITLE_PAGE}")]')

    sbis_plagin = (By.XPATH, f'//div[@data-id="plugin"]')

    windows = (By.XPATH, f'//div[@data-id="default"]')

    downloads_link = (By.XPATH, f'//h3[text()="{TYPE_DISTRIBUTION}"]/../following-sibling::div//a')
