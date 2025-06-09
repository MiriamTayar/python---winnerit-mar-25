class BasePage:
    def __init__(self, url: str, end_point: str = "/"):
        self._url = url
        self.__end_point = end_point

    def get_url(self) -> str:
        return self._url

    def get_end_point(self) -> str:
        return self.__end_point

    def click_element(self, element: str):
        print(f"Click on {element}")

    def get_text(self, element: str):
        return f"Text for {element}"

    def who_am_i(self):
        print("I am BasePage")


class LoginPage(BasePage):
    def __init__(self, url: str, end_point: str, main_user: str):
        super().__init__(url, end_point)
        self.main_user = main_user

    def get_main_user(self):
        return self.main_user


    def who_am_i(self):
        print("I am LoginPage")

    def print_super_info(self):
        print(f"Info: {self._url}")
        print(f"Info: {self.get_end_point()}")


base_page = BasePage("https://www.saucedemo.com")
print(base_page.get_url())
print(base_page.get_end_point())
base_page.who_am_i()


login_page = LoginPage("https://www.saucedemo.com/login", "/login", "standard_user")
print(login_page.get_url())
print(login_page.get_end_point())
print(login_page.get_main_user())
login_page.click_element("test")
print(login_page.get_text("test"))
login_page.who_am_i()
login_page.print_super_info()