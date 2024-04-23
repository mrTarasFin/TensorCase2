from selenium.webdriver.common.by import By
from page.BasePage import BasePage
from page.main_page.main_data import LOCAL_VERSIONS


class MainPage(BasePage):

    main_logo = (By.XPATH, '//div[@name="logo"]')

    contacts = (By.XPATH, '//li[starts-with(@class, "sbisru-Header__menu-item")]/a[@href="/contacts"]')

    downloads_local_versions = (By.XPATH, f'//li/a[contains(text(), "{LOCAL_VERSIONS}")]')
