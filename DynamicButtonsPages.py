from BaseApp import BasePage

class DynamicButtonsLocator:
    BUTTON_START = "button#button00"
    BUTTON_ONE = "button#button01"
    BUTTON_TWO = "button#button02"
    BUTTON_THREE = "button#button03"
    TEXT_ALL_CLICKED = "xpath=//p[contains(text(), 'All Buttons Clicked')]"

class SearchHelper(BasePage):

    def click_start(self):
        self.page.click(DynamicButtonsLocator.BUTTON_START)

    def click_one(self):
        self.page.click(DynamicButtonsLocator.BUTTON_ONE)

    def click_two(self):
        self.page.click(DynamicButtonsLocator.BUTTON_TWO)

    def click_three(self):
        self.page.click(DynamicButtonsLocator.BUTTON_THREE)

    def is_all_buttons_clicked_displayed(self):
        try:
            element = self.find_element(DynamicButtonsLocator.TEXT_ALL_CLICKED)
            return element.is_visible()
        except:
            return False
