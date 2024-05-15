import allure
import pytest


@allure.title('Negative login with empty data')
def test_negative_register_empty_data(get_env):
    get_env.go_to('main')
    get_env.register_page.clicks_personal_cabinet_and_choose_action('Реєстрація')
    get_env.register_page.verify_register_form_is_opened()
    get_env.user_clicks_button('Продовжити')
    get_env.expected_text_on_the_page_is('Ім\'я має містити від 1 до 32 символів!')
    get_env.expected_text_on_the_page_is('Прізвище має містити від 1 до 32 символів!')
    get_env.expected_text_on_the_page_is('Адреса електронної пошти, здається, недійсна!')
    get_env.expected_text_on_the_page_is('Телефон повинен містити від 3 до 32 символів!')
    get_env.expected_text_on_the_page_is('Адреса електронної пошти, здається, недійсна!')
    get_env.expected_text_on_the_page_is('Пароль повинен містити від 4 до 20 символів!')
    get_env.not_expected_text_on_the_page_is('Підтвердження пароля не відповідає паролю!')






