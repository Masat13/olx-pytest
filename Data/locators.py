
REGISTER_FORM = {
    "input_firstname": '//input[@name="firstname"]',
    "input_lastname": '//input[@name="lastname"]',
    "input_email": '//input[@name="email"][@id="input-register-email"]',
    "input_telephone": '//input[@name="telephone"][@id="input-telephone"]',
    "input_password": '//input[@name="password"][@id="input-register-password"]',
    "input_confirm": '//input[@name="confirm"]'
}

LOGIN_FORM = {
    "input_email": '//input[@name="email"][@id="input-email"]',
    "input_password": '//input[@name="password"][@id="input-password"]',
    "invalid_data_alert": '//div[@class="alert alert-danger"][text()=" Попередження: Не відповідає адреса електронної '
                          'пошти та / або пароль."]'
}
