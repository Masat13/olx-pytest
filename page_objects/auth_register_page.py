from playwright.sync_api import expect
import allure
from Data.locators import *


class login:
    def __init__(self, page):
        self.page = page

    @allure.step
    def verify_login_form_is_opened(self):
        expect(self.page.locator(".account-login")).to_be_visible()
        expect(self.page.get_by_role("heading", name="Повернення клієнта")).to_be_visible()
        expect(self.page.get_by_text("Я клієнт, що повертається")).to_be_visible()
        expect(self.page.locator('//label[text()="Електронна адреса"]')).to_be_visible()
        expect(self.page.locator('//div[@class="form-group"]//label[text()="Пароль"]')).to_be_visible()
        expect(self.page.get_by_role("button", name="Увійти")).to_be_visible()
        expect(self.page.get_by_role("button", name="Створити аккаунт")).to_be_visible()

    @allure.step
    def validate_login_failed(self):
        expect(self.page.locator(".account-login")).to_be_visible()
        expect(self.page.locator(LOGIN_FORM.get("invalid_data_alert"))).to_be_visible()

    @allure.step
    def validate_login_successful(self):
        expect(self.page.get_by_text("Вітаємо! Вхід успішний×")).to_be_visible()
        self.page.get_by_role("button", name="Особистий кабінет").click()
        expect(self.page.locator("#top-links")).to_be_visible()


class register:
    def __init__(self, page):
        self.page = page

    @allure.step
    def verify_register_form_is_opened(self):
        expect(self.page.locator(".account-register")).to_be_visible()
        expect(self.page.get_by_role("heading", name="Увійти або створити акаунт")).to_be_visible()
        expect(self.page.get_by_text("Ваші особисті дані")).to_be_visible()
        expect(self.page.get_by_text("Група клієнтів")).to_be_visible()
        expect(self.page.locator('//label[text()="Ім\'я"]')).to_be_visible()
        expect(self.page.locator('//label[text()="Прізвище"]')).to_be_visible()
        expect(self.page.locator('//label[text()="Телефон"]')).to_be_visible()
        expect(self.page.locator('//label[text()="Телефон"]')).to_be_visible()
        expect(self.page.locator('//label[text()="Пароль"][@for="input-register-password"]')).to_be_visible()
        expect(self.page.locator('//label[text()="Підтвердження пароля"]')).to_be_visible()
        for input_name in REGISTER_FORM.keys():
            expect(self.page.locator(REGISTER_FORM.get(input_name))).to_be_visible()
        expect(self.page.get_by_role("button", name="Продовжити")).to_be_visible()

    @allure.step
    def fill_register_form_input(self, input_name, text):
        self.page.locator(REGISTER_FORM.get(input_name)).fill(text)

    @allure.step
    def fill_all_register_form_inputs(self, text):
        for input_name in REGISTER_FORM.keys():
            self.fill_register_form_input(input_name, text)





