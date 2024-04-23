import allure
import pytest

from page.contacts_page.contacts_data import NEW_REGION, CURRENT_REGION
from page.about_page.AboutActions import AboutActions
from page.about_page.AboutChecks import AboutChecks
from page.contacts_page.ContactsActions import ContactsActions
from page.contacts_page.ContactsChecks import ContactsChecks
from page.downloads_page.DownloadsActions import DownloadsActions
from page.downloads_page.DownloadsChecks import DownloadsChecks
from page.main_page.MainActions import MainActions
from page.main_page.MainChecks import MainChecks
from page.tensor_page.TensorActions import TensorActions
from page.tensor_page.TensorChecks import TensorChecks


@allure.epic("UI тест")
@allure.feature("Тест проверки страницы sbis.ru")
class TestFirstScript:

    @allure.title("Тест проверки блока 'Сила в людях'")
    @pytest.mark.run
    def test_first_script(self,
                          driver,
                          open_browser):
        main_checks = MainChecks(driver)
        main_actions = MainActions(driver)
        contacts_checks = ContactsChecks(driver)
        contacts_actions = ContactsActions(driver)
        tensor_actions = TensorActions(driver)
        tensor_checks = TensorChecks(driver)
        about_checks = AboutChecks(driver)
        about_actions = AboutActions(driver)

        contacts_actions.next_step(1)
        main_checks.check_open_main_page()
        main_actions.click_contacts()

        contacts_actions.next_step(2)
        contacts_checks.check_open_contacts_page()
        contacts_actions.click_banner_tensor()

        contacts_actions.next_step(3)
        contacts_actions.click_next_page()
        tensor_checks.check_logo_exist()
        tensor_checks.check_open_tensor_page()

        tensor_actions.next_step(4)
        tensor_checks.check_power_people_exists()

        tensor_actions.next_step(5)
        tensor_actions.click_more_detail()
        about_checks.check_open_about_page()

        about_actions.next_step(6)
        about_checks.check_working_exists()
        about_checks.check_size_images()

    @allure.title("Тест проверки блока 'Регион'")
    @pytest.mark.run
    def test_second_script(self,
                          driver,
                          open_browser):
        main_checks = MainChecks(driver)
        main_actions = MainActions(driver)
        contacts_checks = ContactsChecks(driver)
        contacts_actions = ContactsActions(driver)

        contacts_actions.next_step(1)
        main_checks.check_open_main_page()
        main_actions.click_contacts()

        contacts_actions.next_step(2)
        #не понятно, что проверять в списке партнеров. Я бы запросил по API список организаций и проверил с экраном
        contacts_checks.check_open_contacts_page()
        contacts_checks.check_region_and_partners(CURRENT_REGION)

        contacts_actions.next_step(3)
        contacts_actions.click_region()
        contacts_actions.choose_new_region(NEW_REGION)

        contacts_actions.next_step(4)
        contacts_checks.check_info_region_in_title()
        contacts_checks.check_info_region_in_url()
        contacts_checks.check_region_and_partners(NEW_REGION)

    @allure.title("Тест проверки размера файла")
    @pytest.mark.run
    def test_third_script(self,
                           driver,
                           open_browser):
        main_checks = MainChecks(driver)
        main_actions = MainActions(driver)
        downloads_actions = DownloadsActions(driver)
        downloads_checks = DownloadsChecks(driver)

        main_actions.next_step(1)
        main_checks.check_open_main_page()

        main_actions.next_step(2)
        main_actions.click_downloads_local_versions()

        downloads_actions.next_step(3)
        downloads_checks.check_open_downloads_page()
        downloads_actions.click_sbis_plagin()
        downloads_checks.check_windows()
        downloads_actions.click_download_file()
        downloads_checks.check_file_downloaded()







