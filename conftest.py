from pytest import fixture
from playwright.sync_api import Playwright, sync_playwright, expect
from page_objects.common import *


@fixture
def get_env(request):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()

        yield page

        page.close()
        browser.close()


@fixture
def user_auth(get_env):
    def _user_auth(user_creds):
        common = common_steps(get_env)
        common.go_to('main')
        common.clicks_personal_cabinet_and_choose_action('Авторизація')
        common.login_with(user_creds)
        return common
    yield _user_auth


# attach screen to Tear down allure report
@fixture(scope='function', autouse=True)
def make_screenshots(request, get_env):
    yield
    if hasattr(get_env, 'page') and get_env.page:
        allure.attach(body=get_env.page.screenshot(), name='screenshot', attachment_type=allure.attachment_type.PNG)




