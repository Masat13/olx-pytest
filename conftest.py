from pytest import fixture
from playwright.sync_api import Playwright, sync_playwright, expect
from page_objects.login_page import olx

@fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright

@fixture
def olx_env(get_playwright):
    site = olx(get_playwright)
    yield site
    site.close()

@fixture
def olx_auth(olx_env):
    olx_env.go_to('main')
    olx_env.user_clicks_myProfile()
    olx_env.login_with('correct_creds')
    yield olx_env