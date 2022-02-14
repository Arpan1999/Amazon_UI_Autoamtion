from selenium.webdriver.common.by import By


class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    addcart = (By.XPATH, "//input[contains(@name,'submit.add-to-cart')]")
    Cart = (By.XPATH, "(//input[@class = 'a-button-input'])[6]")

    def getModelName(self, model_name):
        xpath = "//li[contains(@aria-label,'{name}')]//a".format(name=model_name)
        return self.driver.find_element_by_xpath(xpath)

    def getPriceRange(self, price_range):
        xpath = "//span[contains(text(),'{price}')]".format(price=price_range)
        return self.driver.find_element_by_xpath(xpath)

    def getBattery(self, battery_capacity):
        xpath = "//li[contains(@aria-label,'{battery}')]//a".format(battery=battery_capacity)
        return self.driver.find_element_by_xpath(xpath)

    def getMemory(self, memory_capacity):
        xpath = "//li[contains(@aria-label,'{memory}')]//a".format(memory=memory_capacity)
        return self.driver.find_element_by_xpath(xpath)

    def getRam(self, ram):
        xpath = "(//li[contains(@aria-label,'{capacity}')]//a)[1]".format(capacity=ram)
        return self.driver.find_element_by_xpath(xpath)

    def getmobilename(self):
        xpath = "//div[@data-component-type = 's-search-result']"
        mobile = self.driver.find_elements_by_xpath(xpath)
        for i in range(1, len(mobile)):
            print(self.driver.find_element_by_xpath("//div[@data-component-type = 's-search-result'][" + str(i) + "]//span[contains(@class,'a-size-medium')]").text)

    def selectmobile(self, name):
        xpath = "(//div[@data-component-type = 's-search-result']//span[contains(text(),'{model_name}')])[1]".format(model_name=name)
        self.driver.find_element_by_xpath(xpath).click()
        self.driver.switch_to.window(self.driver.window_handles[1])

    def getprice(self):
        xpath = "(//span[@class = 'a-color-price']/span)[1]"
        price = self.driver.find_element_by_xpath(xpath).text
        return price

    def addtocart(self):
        return self.driver.find_element(*SearchPage.addcart)

    def cart(self):
        return self.driver.find_element(*SearchPage.Cart)