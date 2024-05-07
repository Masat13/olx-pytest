def test_login_negative(olx_env):
    olx_env.go_to('main')
    olx_env.user_clicks_myProfile()
    olx_env.check_login_page_isOpened()
    olx_env.login_with('wrong_creds')
    olx_env.check_fail_login()


def test_login_positive(olx_env):
    olx_env.go_to('main')
    olx_env.user_clicks_myProfile()
    olx_env.check_login_page_isOpened()
    olx_env.login_with('correct_creds')
    olx_env.check_profile_page_isOpened()


def test_furniture_filter(olx_auth):
    olx_auth.go_to('main')
    olx_auth.main_page.check_main_page_isOpened()
    olx_auth.main_page.open_product_category('Дім і сад')
    olx_auth.main_page.open_product_subcategory('Меблі')
    olx_auth.main_page.check_filter_page_isOpened()
    olx_auth.main_page.select_filter_subcategory('Меблі для вітальні')
    olx_auth.main_page.set_filter_price('100', '200')
    olx_auth.main_page.check_green_sofa_search_result()

