import allure
import pytest
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from settings import Settings

load_dotenv()
URL = os.getenv("URL")



def options() -> Options:
    options = Options()
    settings = Settings()
    options.add_experimental_option(
        "prefs",
        {"download.default_directory": os.getenv(fr'{settings.ROOT_DIR}\downloads')}
    )
    return options


@allure.title("Настройка драйвера")
@pytest.fixture()
def driver():
    driver_service = Service(ChromeDriverManager().install())
    web_driver = webdriver.Chrome(service=driver_service, options=options())
    web_driver.maximize_window()
    yield web_driver
    web_driver.quit()


@allure.title("Открытие страницы браузера")
@pytest.fixture
def open_browser(driver):
    return driver.get(url=URL)
