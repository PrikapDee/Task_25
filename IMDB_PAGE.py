from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


class Imdb:
    #  create driver object of chrome driver class
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # create wait object of webdriver class to use explict time
    wait = WebDriverWait(driver, 10)

    # Locators
    name_locator = "//label//span[1]//div[text()='Name']"
    name_search_box_locator = "//div[@class='ipc-textfield__container']//input[@placeholder='e.g. Audrey Hepburn']"
    Birth_date_locator = "//label//span//div[text()='Birth date']"
    result_locator = "//button//span[text()='See results']"
    start_date_locator = "//input[@data-testid='birthDate-start']"
    end_date_locator = "//input[@data-testid='birthDate-end']"
    search_data = "aamir khan"
    start_date = "05/10/1975"
    end_date = "05/10/1990"

    def __init__(self, imdb_url):
        self.url = imdb_url

    # login method
    def login(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            return True

        except Exception as e:
            print(e)
            return False

    # method to search results with name and birthdate
    def search_name_Birthdate(self):
        try:
            self.login()
            self.driver.execute_script('window.scrollBy(0, 500)')
            # use of explict wait that wait till selenium get element clickable
            name = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.name_locator)))
            name.click()
            # use of explict wait ,once element is located
            search_box = self.wait.until(EC.presence_of_element_located((By.XPATH, self.name_search_box_locator)))

            search_box.send_keys(self.search_data)
            Birth_date = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Birth_date_locator)))
            Birth_date.click()
            # use of explict wait that wait till selenium get element located
            start_date = self.wait.until(EC.presence_of_element_located((By.XPATH, self.start_date_locator)))
            start_date.send_keys(self.start_date)

            end_date = self.wait.until(
                EC.presence_of_element_located((By.XPATH, self.end_date_locator)))
            end_date.send_keys(self.end_date)
            result_box = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.result_locator)))
            result_box.click()

            return True

        except NoSuchElementException as e:
            print(e)
            return False
        finally:
            self.driver.quit()


if __name__ == "__main__":
    url = "https://www.imdb.com/search/name/"
    obj1 = Imdb(url)
    obj1.search_name_Birthdate()
