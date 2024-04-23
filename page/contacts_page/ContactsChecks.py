import allure
from page.BaseChecks import BaseChecks
from page.contacts_page.ContactsPage import ContactsPage
from page.contacts_page.contacts_data import TEXT_URL, NEW_REGION, TITLE


class ContactsChecks(ContactsPage, BaseChecks):

    @allure.step("Проверить открытия страницы Контакты")
    def check_open_contacts_page(self):
        self.check_element_exists(self.title_contacts_page)

    @allure.step("Проверить текущий регион и список партнеров")
    def check_region_and_partners(self, current_region):
        self.check_element_text_by_current_text(self.region, current_region)
        self.check_element_exists(self.list_partner)

    @allure.step("Проверить название региона в url")
    def check_info_region_in_url(self):
        self.check_text_in_url(TEXT_URL)

    @allure.step("Проверить название региона в заголовке страницы")
    def check_info_region_in_title(self):
        self.expect_load_page(TITLE)
