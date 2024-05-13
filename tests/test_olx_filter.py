import allure
from pytest import mark


@allure.title('some like main page and filter test')
@mark.filter1
def test_furniture_filter(olx_auth):
    olx_auth.go_to('main')
    olx_auth.main_page.check_main_page_isOpened()
    olx_auth.main_page.open_product_category('Дім і сад')
    olx_auth.main_page.open_product_subcategory('Меблі')
    olx_auth.main_page.check_filter_page_isOpened()
    olx_auth.main_page.select_filter_subcategory('Меблі для вітальні')
    olx_auth.main_page.set_filter_price('100', '200')
    olx_auth.main_page.check_green_sofa_search_result()

