from conftest import *
import pytest


@allure.title('Green parallel test')
@pytest.mark.parallel
def test_parallel_green(user_auth):
    common = user_auth('valid_user')
    try:
        common.expected_text_on_the_page_is('Рекомендовані')
        common.expected_text_on_the_page_is('категорії')
    # attach screen to test_body allure report
    except Exception:
        common.allure_screenshot_attach()
        raise


@allure.title('Red by text parallel test')
@pytest.mark.parallel
def test_parallel_red(user_auth):
    common = user_auth('valid_user')
    try:
        common.expected_text_on_the_page_is('Some crazy cat')
    # attach screen to test_body allure report
    except Exception:
        common.allure_screenshot_attach()
        raise


@allure.title('Red by url parallel test')
@pytest.mark.parallel
def test_positive_login(user_auth):
    common = user_auth('valid_user')
    try:
        common.check_page_url_is('pizza/sushi')
    # attach screen to test_body allure report
    except Exception:
        common.allure_screenshot_attach()
        raise






