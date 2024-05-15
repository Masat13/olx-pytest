from pytest import fixture, hookimpl
from playwright.sync_api import Playwright, sync_playwright, expect
from page_objects.common import common_page
import allure


@fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture
def get_env(get_playwright, request):
    site = common_page(get_playwright)
    yield site
    site.close()


@fixture
def user_auth(get_env):
    get_env.go_to('main')
    get_env.user_clicks_myProfile()
    get_env.login_with('correct_creds')
    yield get_env


@fixture(scope='function', autouse=True)
def make_screenshots(request, get_env):
    yield
    if hasattr(get_env, 'page') and get_env.page:
        allure.attach(body=get_env.page.screenshot(), name='screenshot', attachment_type=allure.attachment_type.PNG)




