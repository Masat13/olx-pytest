from pytest import fixture, hookimpl
from playwright.sync_api import Playwright, sync_playwright, expect
import allure
from page_objects.common import *




@fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture
def get_env(request, get_playwright):
    browser = get_playwright.chromium.launch(headless=True)
    page = browser.new_page()

    yield page

    page.close()
    browser.close()


@fixture
def user_auth(get_env):
    # common = common_steps(get_env)
    get_env.go_to('main')
    get_env.user_clicks_myProfile()
    get_env.login_with('correct_creds')
    yield get_env


@fixture(scope='function', autouse=True)
def make_screenshots(request, get_env):
    yield
    if hasattr(get_env, 'page') and get_env.page:
        allure.attach(body=get_env.page.screenshot(), name='screenshot', attachment_type=allure.attachment_type.PNG)




