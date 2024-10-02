from pytest import fixture
from playwright.sync_api import Playwright, sync_playwright, expect
from page_objects.common import *
import pytest
import allure


# environment setup
@fixture
def get_env(request):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()

        yield page

        page.close()
        browser.close()


# environment setup with pre-authorized user, like some background step
@fixture
def user_auth(get_env):
    def _user_auth(user_creds):
        common = common_steps(get_env)
        common.go_to('main')
        common.clicks_personal_cabinet_and_choose_action('Авторизація')
        common.login_with(user_creds)
        return common
    yield _user_auth


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get('get_env')

        if page:
            allure.attach(body=page.screenshot(), name='screenshot', attachment_type=allure.attachment_type.PNG)




