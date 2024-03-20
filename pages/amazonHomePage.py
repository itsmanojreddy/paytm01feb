import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.Baseclass import Baseclass
from utility.javascriptmethods import javascriptmethods


class amazonHomePage(Baseclass):
    def __init__(self, driver):
        self.driver = driver

    @property
    def all_dropdown(self):
        return (By.ID, "searchDropdownBox")

    @property
    def search_Suggestions(self):
        return "//*[contains(@class,'s-suggestion-ell')]"

    @property
    def searchbox(self):
        return self.driver.find_element(By.ID, "twotabsearchtextbox")

    @property
    def searchbox_Suggestion(self):
        return (By.XPATH, "//*[contains(@class,'s-suggestion-ell')]")

    def select_All_dropdown(self, val):
        ele = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.all_dropdown))
        sel = Select(ele)
        sel.select_by_visible_text(val)

    def enter_search_value(self, val):
        ele = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.searchbox))
        act = ActionChains(self.driver)
        js = javascriptmethods()
        js.clickjs(self.driver, ele)
        act.move_to_element(ele).click(ele).send_keys(val).perform()

    def click_suggested_Search(self, index):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.searchbox_Suggestion))
        li = self.driver.find_elements(By.XPATH, self.search_Suggestions)
        li[index - 1].click()

        if __name__ == "__main__":
            print(
                "Print inside all the lloooops====================================================================================")
