from page.BasePage import BasePage


class ScrollHelpers:

    @staticmethod
    def scroll_to_element(driver, locator):
        element = BasePage(driver).find_element(locator)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
