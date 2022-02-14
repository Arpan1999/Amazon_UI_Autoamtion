import time

import pytest
from selenium.webdriver import Keys

from PageObject.CheckoutPage import CheckoutPage
from PageObject.HomePage import HomePage
from PageObject.SearchPage import SearchPage
from Utilities.BaseClass import BaseClass


class TestFile(BaseClass):
    def test_booking(self):
        log = self.getLogger()
        log.info("start")
        searchbar = HomePage(self.driver)
        searchbar.SearchBar().send_keys("mobile")
        searchbar.SearchBar().send_keys(Keys.RETURN)
        modelname = SearchPage(self.driver)
        modelname.getModelName("Samsung").click()
        pricerange = SearchPage(self.driver)
        pricerange.getPriceRange("₹10,000 - ₹20,000").click()
        batterycapacity = SearchPage(self.driver)
        batterycapacity.getBattery("4000 mAh & More").click()
        time.sleep(3)
        memorycapacity = SearchPage(self.driver)
        memorycapacity.getMemory("128 GB").click()
        time.sleep(3)
        ram = SearchPage(self.driver)
        ram.getRam("6 GB").click()
        mobilename = SearchPage(self.driver)
        mobilename.getmobilename()
        time.sleep(3)
        mobile = SearchPage(self.driver)
        mobile.selectmobile(
            "Samsung Galaxy M32 (Black, 6GB RAM, 128GB Storage) 6 Months Free Screen Replacement for Prime")
        time.sleep(5)
        price = SearchPage(self.driver)
        amount = price.getprice()
        print(amount)
        time.sleep(5)
        addcart = SearchPage(self.driver)
        addcart.addtocart().click()
        time.sleep(5)
        cartitem = SearchPage(self.driver)
        cartitem.cart().click()
        time.sleep(5)
        checkoutamount = CheckoutPage(self.driver)
        total = checkoutamount.getcheckoutprice()
        print(total)
