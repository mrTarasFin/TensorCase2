from selenium.webdriver.common.by import By
from page.BasePage import BasePage


class ContactsPage(BasePage):

    title_contacts_page = (By.XPATH, '//h2[text()="Контакты"]')

    banner = (By.XPATH, '//a[@href="https://tensor.ru/"]')

    region = (By.XPATH, '//span[starts-with(@class, "sbis_ru-Region-Chooser ml")]/span')

    list_partner = (By.XPATH, '//div[contains(@class, "sbisru-Contacts-List__col ws-flex-shrink-1 ws-flex-grow-1")]')

    @staticmethod
    def get_new_region_by_name(name_region):
        return (By.XPATH, f'//li/span[contains(@title, "{name_region}")]')
