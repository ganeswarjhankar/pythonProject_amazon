from selenium.webdriver.common.by import By

from utlities import constants


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(constants.AMAZON_URL)

    def Amazon_Homepage(self):

        # self.driver.get("https:google.com")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

        # amazon
        self.driver.implicitly_wait(20)

        # AMAZON
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.ID,"twotabsearchtextbox").send_keys("hot wheels")
        dropdownLists= self.driver.find_elements(By.XPATH,"//div[@class='left-pane-results-container']/div")

        print("Total sugestion are :", dropdownLists)
#Transversing through the elements each and every and verifying those are present or not
        for ele in dropdownLists:

            print("Suggestion as : ", ele.text)
            if ele.text == 'hot wheels':
                ele.click()
                break



