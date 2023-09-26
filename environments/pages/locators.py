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

