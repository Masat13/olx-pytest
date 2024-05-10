from playwright.sync_api import Playwright, sync_playwright, expect
import time
import allure
from page_objects.main_page import main_page
from page_objects.locators import *

class olx:
    def __init__(self, playwright):
        self.browser = playwright.chromium.launch(headless=True, slow_mo=900)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.main_page = main_page(self.page)

    @allure.step
    def go_to(self, name):
        if name == 'main':
            self.page.goto(f'{url_host}')
        else:
            self.page.goto(f'{url_host}/{name}')
        time.sleep(2)
        if self.page.get_by_test_id("dismiss-cookies-banner").is_visible():
            self.page.get_by_test_id("dismiss-cookies-banner").click()

    @allure.step
    def user_clicks_myProfile(self):
        with self.page.expect_navigation(wait_until='load', timeout=30000):
            self.page.get_by_role("link", name="Ваш профіль").click(no_wait_after=True)

    @allure.step
    def check_login_page_isOpened(self):
        expect(self.page.get_by_text("УвійтиЗареєструватися")).to_be_visible()
        expect(self.page.get_by_text("Електронна пошта чи телефон")).to_be_visible()
        expect(self.page.get_by_text("Пароль", exact=True)).to_be_visible()
        expect(self.page.locator("input[name=\"username\"]")).to_be_visible()
        expect(self.page.locator("input[name=\"password\"]")).to_be_visible()
        expect(self.page.get_by_test_id("login-submit-button")).to_be_visible()

    @allure.step
    def login_with(self, user_creds):
        self.page.locator("input[name=\"username\"]").fill(creds.get(user_creds)['username'])
        self.page.locator("input[name=\"password\"]").fill(creds.get(user_creds)['userpass'])
        self.page.get_by_test_id("login-submit-button").click()

    @allure.step
    def check_fail_login(self):
        expect(self.page.get_by_test_id("login-form").locator("div").filter(
            has_text="Ми не знайшли профіль із цією адресою електронної пошти. Повторіть спробу, використовуючи іншу "
                     "адресу, або створіть профіль").first).to_be_visible()
        expect(self.page.locator("input[name=\"username\"]")).to_have_value(creds.get('wrong_creds')['username']);
        expect(self.page.locator("input[name=\"password\"]")).to_have_value(creds.get('wrong_creds')['userpass']);

    @allure.step
    def check_page_url_is(self, url_name):
        expect(self.page).to_have_url(f'{url_host}/{url_name}')

    @allure.step
    def check_profile_page_isOpened(self):
        expect(self.page).to_have_url('https://www.olx.ua/d/uk/myaccount')
        expect(self.page.get_by_test_id("header-title")).to_be_visible()
        expect(self.page.locator("#mainContent").get_by_text(
            "ОголошенняПовідомленняПлатежі та рахунок OLXШукаю роботуНалаштуванняOLX Доставка")).to_be_visible()
        expect(self.page.get_by_text("Активні Очікуючі Неоплачені Неактивні Відхилені")).to_be_visible()
        expect(self.page.get_by_text("Додати фільтрСортувати")).to_be_visible()

    def close(self):
        self.context.close()
        self.browser.close()

