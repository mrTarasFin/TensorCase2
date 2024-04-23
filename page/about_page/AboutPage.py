from selenium.webdriver.common.by import By
from page.BasePage import BasePage
from page.about_page.about_data import WORKING


class AboutPage(BasePage):

    image = (By.XPATH, '//*[contains(@class, "new_lazy loaded")]')

    title_working = (By.XPATH, f'//h2[text()="{WORKING}"]')

    def get_list_size_images(self, locator):
        list_width, list_height = [], []
        for item in self.find_elements(locator):
            list_width.append(item.get_attribute("width"))
            list_height.append(item.get_attribute("height"))
        return list_width, list_height
