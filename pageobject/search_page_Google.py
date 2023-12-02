from selenium.webdriver.common.by import By

from utlities import constants


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(constants.Google_URL)

    def Homepage(self):

        # self.driver.get("https:google.com")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

        # GOOGLE
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.ID, "APjFqb").send_keys("hot w")
        dropdownLists = self.driver.find_elements(By.XPATH, "//ul[@class='G43f7e']/li")

        print("Total sugestion are :", dropdownLists)
#Transversing through the elements each and every and verifying those are present or not
        for ele in dropdownLists:

            print("Suggestion as : ", ele.text)
            if ele.text == 'hot wheels':
                ele.click()
                break



