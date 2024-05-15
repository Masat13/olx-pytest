from playwright.sync_api import expect
import allure
from Data import locators


class login_page:
    def __init__(self, page):
        self.page = page


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
        for input_name in locators.REGISTER_FORM.keys():
            expect(self.page.locator(locators.REGISTER_FORM.get(input_name))).to_be_visible()
        expect(self.page.get_by_role("button", name="Продовжити")).to_be_visible()

    @allure.step
    def fill_register_form_input(self, input_name, text):
        self.page.locator(locators.REGISTER_FORM.get(input_name)).fill(text)


    @allure.step
    def fill_all_register_form_inputs(self, text):
        for input_name in locators.REGISTER_FORM.keys():
            self.fill_register_form_input(input_name, text)





