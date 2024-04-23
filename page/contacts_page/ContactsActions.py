import allure

from page.BaseActions import BaseActions
from page.contacts_page.ContactsPage import ContactsPage


class ContactsActions(ContactsPage, BaseActions):

    @allure.step("Нажать на баннер Тензор")
    def click_banner_tensor(self):
        self.click_element(self.banner)

    def click_next_page(self):
        self.next_page()

    @allure.step("Нажать на название региона")
    def click_region(self):
        self.click_element(self.region)

    @allure.step("Выбрать из списка регион {name_region}")
    def choose_new_region(self, name_region):
        self.click_element(self.get_new_region_by_name(name_region))
