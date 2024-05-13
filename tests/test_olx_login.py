import allure
from pytest import mark


@allure.title('Some negative login tets')
@mark.login1
def test_login_negative(olx_env):
    olx_env.go_to('main')
    olx_env.user_clicks_myProfile()
    olx_env.check_login_page_isOpened()
    olx_env.login_with('wrong_creds')
    olx_env.check_fail_login()


@allure.title('Some positive login tets')
@mark.login2
def test_login_positive(olx_env):
    olx_env.go_to('main')
    olx_env.user_clicks_myProfile()
    olx_env.check_login_page_isOpened()
    olx_env.login_with('correct_creds')
    olx_env.check_profile_page_isOpened()


