from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    Search = (By.XPATH, "//input[contains(@id,'twotabsearchtextbox')]")

    def SearchBar(self):
        return self.driver.find_element(*HomePage.Search)
