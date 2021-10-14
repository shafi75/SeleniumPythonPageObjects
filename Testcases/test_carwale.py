from Testcases.BaseTest import BaseTest
from Pages.HomePage import HomePage
import logging
from Utilities.LogUtil import Logger
from Utilities import dataProvider as dp
from Pages.carBase import CarBase
import time
import pytest

log=Logger(__name__,logging.INFO)

class Test_Carwale(BaseTest):
    @pytest.mark.skip
    def test_goToNewCars(self):
        log.logger.info("******************Inside the NewCar Test**********************")
        home=HomePage(self.driver)
        home.gotoNewCars()
        time.sleep(5)

    @pytest.mark.skip
    @pytest.mark.parametrize("carModel,carTitle",dp.get_data("NewCarsData"))
    def test_SelectCars(self,carModel,carTitle):
        log.logger.info("******************Inside the Select car Test**********************")
        home=HomePage(self.driver)
        car=CarBase(self.driver)
        print(("The car brand is :"+carModel).encode("utf8"))
        if carModel=="BMW":
            home.gotoNewCars().selectBMW()
            actual_title=car.getCarTitle()
            print(("The actual title is: "+actual_title).encode("utf8"))
            assert actual_title==carTitle,"Not on the correct page,title is not matching"
        elif carModel=="Hyundayi":
            home.gotoNewCars().selectHyundayi()
            actual_title = car.getCarTitle()
            print(("The actual title is: " + actual_title).encode("utf8"))
            assert actual_title == carTitle, "Not on the correct page,title is not matching"
        elif carModel=="Toyota":
            home.gotoNewCars().selectToyota()
            actual_title = car.getCarTitle()
            print(("The actual title is: " + actual_title).encode("utf8"))
            assert actual_title == carTitle, "Not on the correct page,title is not matching"
        elif carModel=="Honda":
            home.gotoNewCars().selectHonda()
            actual_title = car.getCarTitle()
            print(("The actual title is: " + actual_title).encode("utf8"))
            assert actual_title == carTitle, "Not on the correct page,title is not matching"
        time.sleep(5)

    @pytest.mark.parametrize("carModel,carTitle", dp.get_data("NewCarsData"))
    def test_SelectCars(self, carModel, carTitle):
        log.logger.info("******************Inside the Select car Test**********************")
        home = HomePage(self.driver)
        car = CarBase(self.driver)
        print(("The car brand is :" + carModel).encode("utf8"))
        if carModel == "BMW":
            home.gotoNewCars().selectBMW()
            actual_title = car.getCarTitle()
            # print(("The actual title is: " + actual_title).encode("utf8"))
            assert actual_title == carTitle, "Not on the correct page,title is not matching"
            car.getCarNameandPrice()
        elif carModel == "Hyundayi":
            home.gotoNewCars().selectHyundayi()
            actual_title = car.getCarTitle()
            print(("The actual title is: " + actual_title).encode("utf8"))
            assert actual_title == carTitle, "Not on the correct page,title is not matching"
            car.getCarNameandPrice()
        elif carModel == "Toyota":
            home.gotoNewCars().selectToyota()
            actual_title = car.getCarTitle()
            print(("The actual title is: " + actual_title).encode("utf8"))
            assert actual_title == carTitle, "Not on the correct page,title is not matching"
            car.getCarNameandPrice()
        elif carModel == "Honda":
            home.gotoNewCars().selectHonda()
            actual_title = car.getCarTitle()
            print(("The actual title is: " + actual_title).encode("utf8"))
            assert actual_title == carTitle, "Not on the correct page,title is not matching"
            car.getCarNameandPrice()
        time.sleep(5)






