import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def driver():
    driver = webdriver.Chrome()

    yield driver
    driver.quit()


def test_zeelo_is_opened(driver):
    driver.get("https://app.zeelo.co/my-zeelo")
    assert


def test_google_search(driver):
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    # search_box.send_keys("pytest")
    # search_box.send_keys(Keys.RETURN)
    # search_box.submit()
    assert "Google" in driver.title
    # assert 1, 1


def test_python_work(driver):
    driver.get("http://www.python.org")
    # assert "Python" in driver.title
    elem = driver.find_element(By.NAME, "q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
