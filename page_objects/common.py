from page_objects.auth_register_page import *
from Data.creds import *
from Data.locators import *


class common_steps:
    def __init__(self, page):
        self.page = page

    @allure.step
    def go_to(self, name):
        if name == 'main':
            self.page.goto(f'{HOSTS["frontoffice"]}')
        else:
            self.page.goto(f'{HOSTS["frontoffice"]}/{name}')

    @allure.step
    def clicks_personal_cabinet_and_choose_action(self, button):
        # Реєстрація, Авторизація
        self.page.get_by_role("button", name="Особистий кабінет").click()
        self.page.get_by_role("link", name=button).click()

    @allure.step
    def login_with(self, user_creds):
        users = {
            'invalid_user': {'username': 'someusrname@gmail.com', 'userpass': '1111111'},
            'valid_user': {'username': 'hurylov.maksym@gmail.com', 'userpass': 'QAutomation1!'}
        }
        allure.attach(str(users.get(user_creds)['username']), name="User Credentials", attachment_type=allure.attachment_type.TEXT)
        self.page.locator(LOGIN_FORM.get('input_email')).fill(users.get(user_creds)['username'])
        self.page.locator(LOGIN_FORM.get('input_password')).fill(users.get(user_creds)['userpass'])
        self.user_clicks_button('Увійти')

    @allure.step
    def check_page_url_is(self, url_name):
        expect(self.page).to_have_url(f'{HOSTS["frontoffice"]}/{url_name}')

    @allure.step
    def user_clicks_button(self, button_name):
        self.page.get_by_role("button", name=button_name).click(force=True)

    @allure.step
    def expected_text_on_the_page_is(self, text):
        expect(self.page.locator(f'text={text}').first).to_be_visible()

    @allure.step
    def not_expected_text_on_the_page_is(self, text):
        expect(self.page.locator(f'text={text}').first).not_to_be_visible()

    @allure.step
    def reload_page(self):
        self.page.reload()

    def allure_screenshot_attach(self):
        allure.attach(body=self.page.screenshot(), name='screenshot', attachment_type=allure.attachment_type.PNG)

