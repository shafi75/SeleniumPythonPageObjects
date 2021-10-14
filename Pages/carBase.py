from Utilities import configreader

class CarBase:
    def __init__(self,driver):
        self.driver=driver

    def getCarTitle(self):
        return self.driver.find_element_by_xpath(configreader.readConfig("locators","carTitle_XPATH")).text

    def getCarNameandPrice(self):
        carNames=self.driver.find_elements_by_xpath(configreader.readConfig("locators","carName_XPATH"))
        carPrice=self.driver.find_elements_by_xpath(configreader.readConfig("locators","carPrice_XPATH"))
        for i in range(len(carPrice)):
            print(('Car name is '+carNames[i].text+"car price is"+carPrice[i].text).encode('utf8'))


