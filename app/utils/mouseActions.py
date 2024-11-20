from selenium.webdriver import ActionChains


def click(driver, element):
    ActionChains(driver).click(element).perform()
