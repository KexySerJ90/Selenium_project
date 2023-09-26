from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = By.CSS_SELECTOR, "#login_link"


class LoginPageLocators:
    MAIL_ENTER=By.NAME,"login-username"
    PASSWORD_ENTER=By.NAME,"login-username"
    BTN_ENTER=By.NAME,"login_submit"
    MAIL_REG=By.NAME,"registration-email"
    PASSWORD_REG1=By.NAME,"registration-password1"
    PASSWORD_REG2=By.NAME,"registration-password2"
    BTN_REG=By.NAME,"registration_submit"

class ProductPageLocators:
    BTN_ADD_TO_COURT=By.CLASS_NAME,"btn-add-to-basket"
    PRODUCT_NAME = (By.CSS_SELECTOR, "div h1")
    ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, "div.alertinner > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alert div p strong")
