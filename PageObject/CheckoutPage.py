
class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def getcheckoutprice(self):
        xpath = "(//span[@id = 'sc-subtotal-amount-buybox']//span)[2]"
        price = self.driver.find_element_by_xpath(xpath).text
        return price
