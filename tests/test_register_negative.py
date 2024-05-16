import pytest
from conftest import *


@allure.title('Negative register with empty data')
def test_negative_register_empty_data(get_env):
    register_page = register(get_env)
    common = common_steps(get_env)
    common.go_to('main')
    common.clicks_personal_cabinet_and_choose_action('Реєстрація')
    register_page.verify_register_form_is_opened()
    common.user_clicks_button('Продовжити')
    common.expected_text_on_the_page_is('Ім\'я має містити від 1 до 32 символів!')
    common.expected_text_on_the_page_is('Прізвище має містити від 1 до 32 символів!')
    common.expected_text_on_the_page_is('Адреса електронної пошти, здається, недійсна!')
    common.expected_text_on_the_page_is('Телефон повинен містити від 3 до 32 символів!')
    common.expected_text_on_the_page_is('Адреса електронної пошти, здається, недійсна!')
    common.expected_text_on_the_page_is('Пароль повинен містити від 4 до 20 символів!')
    common.not_expected_text_on_the_page_is('Підтвердження пароля не відповідає паролю!')


@allure.title('Negative register with invalid data')
def test_negative_register_invalid_data(get_env):
    register_page = register(get_env)
    common = common_steps(get_env)
    common.go_to('main')
    common.clicks_personal_cabinet_and_choose_action('Реєстрація')
    register_page.fill_all_register_form_inputs('x')
    common.user_clicks_button('Продовжити')
    common.not_expected_text_on_the_page_is('Ім\'я має містити від 1 до 32 символів!')
    common.not_expected_text_on_the_page_is('Прізвище має містити від 1 до 32 символів!')
    common.expected_text_on_the_page_is('Адреса електронної пошти, здається, недійсна!')
    common.expected_text_on_the_page_is('Телефон повинен містити від 3 до 32 символів!')
    common.expected_text_on_the_page_is('Адреса електронної пошти, здається, недійсна!')
    common.expected_text_on_the_page_is('Пароль повинен містити від 4 до 20 символів!')
    register_page.fill_register_form_input('input_confirm', 'xxx')
    common.user_clicks_button('Продовжити')
    common.expected_text_on_the_page_is('Підтвердження пароля не відповідає паролю!')





