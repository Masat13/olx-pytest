from conftest import *
import pytest


# In this suit main target is to run it in parallel mode using @pytest.mark.parallel, 2/3 tests should fail
@allure.title('Green parallel test')
@pytest.mark.parallel
def test_parallel_green(user_auth):
    common = user_auth('valid_user')
    common.expected_text_on_the_page_is('Рекомендовані')
    common.expected_text_on_the_page_is('категорії')


@allure.title('Red by text parallel test')
@pytest.mark.parallel
def test_parallel_red_1(user_auth):
    common = user_auth('valid_user')
    common.expected_text_on_the_page_is('Some crazy cat')


@allure.title('Red by url parallel test')
@pytest.mark.parallel
def test_parallel_red_2(user_auth):
    common = user_auth('valid_user')
    common.check_page_url_is('pizza/sushi')
