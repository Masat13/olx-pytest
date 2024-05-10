from pytest import fixture, hookimpl
from playwright.sync_api import Playwright, sync_playwright, expect
from page_objects.login_page import olx
import allure

@fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright

@fixture
def olx_env(get_playwright, request):
    site = olx(get_playwright)
    yield site
    site.close()

@fixture
def olx_auth(olx_env):
    olx_env.go_to('main')
    olx_env.user_clicks_myProfile()
    olx_env.login_with('correct_creds')
    yield olx_env


@fixture(scope='function', autouse=True)
def make_screenshots(request, olx_env):
    yield
    if hasattr(olx_env, 'page') and olx_env.page:
        allure.attach(body=olx_env.page.screenshot(), name='screenshot', attachment_type=allure.attachment_type.PNG)




