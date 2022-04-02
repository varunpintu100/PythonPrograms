import main
import logging
with open('../Log/app.log', 'w'): # This code is used to clear the log file every time it uses up
    pass
logging.basicConfig(filename="../Log/app.log", level=logging.DEBUG)
def WebDriver(BrowserName: str):
    BrowserName = BrowserName.casefold()
    if BrowserName == "firefox":
        driver = main.webdriver.Firefox(executable_path=r"C:\Users\varunpintu\eclipse-workspace\Automation_Application\Drivers\geckodriver.exe")
        driver.maximize_window()
        logging.debug("----------------------- ! FireFox Browser is invoked ! ----------------------")
        return driver
    if BrowserName == 'chrome':
        driver = main.webdriver.Chrome(executable_path=r"C:\Users\varunpintu\eclipse-workspace\Automation_Application\Drivers\chromedriver.exe")
        driver.maximize_window()
        logging.debug("----------------------- ! Chrome Browser is invoked ! ----------------------")
        return driver
    else:
        return "Browser with such name doesnt exists !!"