from selenium.webdriver.common.by import By
from page.tensor_page.tensor_data import POWER_PEOPLE, MORE_DETAILED
from page.BasePage import BasePage


class TensorPage(BasePage):

    title_power_people = (By.XPATH, f'//*[contains(text(), "{POWER_PEOPLE}")]')

    button_more_detail = (By.XPATH, f'//*[@href="/about" and contains(text(), "{MORE_DETAILED}")]')

    logo_tensor = (By.XPATH, '//*[@href="/"]')
