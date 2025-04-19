class BasePage:
    def __init__(self, page, base_url="https://testpages.eviltester.com/styled/dynamic-buttons-disabled.html"):
        self.page = page
        self.base_url = base_url

    def go_to_site(self):
        self.page.goto(self.base_url)

    def find_element(self, locator: str, timeout: int = 10000):
        return self.page.wait_for_selector(locator, timeout=timeout)
