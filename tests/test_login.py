from conftest import *


@allure.title('Negative login with invalid user')
def test_negative_login(get_env):
    login_page = login(get_env)
    common = common_steps(get_env)
    common.go_to('main')
    common.clicks_personal_cabinet_and_choose_action('Авторизація')
    login_page.verify_login_form_is_opened()
    common.login_with('invalid_user')
    login_page.validate_login_failed()


@allure.title('Positive login')
def test_positive_login(get_env):
    login_page = login(get_env)
    common = common_steps(get_env)
    try:
        common.go_to('main')
        common.clicks_personal_cabinet_and_choose_action('Авторизація')
        login_page.verify_login_form_is_opened()
        common.login_with('valid_user')
        login_page.validate_login_successful()
    # attach screen to test_body allure report
    except Exception:
        common.allure_screenshot_attach()
        raise






