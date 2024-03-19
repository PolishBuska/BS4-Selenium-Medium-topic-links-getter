from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome


class DriverFactory:

    @staticmethod
    def create_driver(driver_class, service: Service, options) -> webdriver:
        return driver_class(service=service, options=options, keep_alive=True)


class DriverContainer:
    def __init__(self, driver_factory: DriverFactory,
                 driver_class, service, options):
        self._driver = driver_factory.create_driver(
            driver_class,
            service,
            options
        )

    @property
    def driver(self) -> Chrome:
        return self._driver


class ChromeDriver(DriverContainer):
    def __init__(
            self,
            driver_factory: DriverFactory,
            service,
            options,
    ):
        super().__init__(
            driver_factory,
            webdriver.Chrome,
            service,
            options
        )


def options_factory():

    options = webdriver.ChromeOptions()

    return options


def service_factory(path) -> Service:
    return Service(executable_path=path)


def get_container() -> ChromeDriver:
    driver_factory = DriverFactory()
    return ChromeDriver(
        driver_factory=driver_factory,
        service=service_factory('/usr/bin/chromedriver'),
        options=options_factory()
    )

