from playwright.sync_api import Playwright, sync_playwright, expect
from page_objects.login_page import *
from page_objects.locators import *
import allure


class main_page:
    def __init__(self, page):
        self.page = page

    @allure.step
    def check_main_page_isOpened(self):
        expect(self.page).to_have_url(url_host)
        expect(self.page.get_by_test_id("home-categories-title")).to_contain_text("Роз4діли на сервісі OLX")
        expect(self.page.get_by_test_id("cat-36").locator("span")).to_contain_text("Дитячий світ")
        expect(self.page.get_by_test_id("cat-3").locator("span")).to_contain_text("Запчастини для транспорту")

    @allure.step
    def open_product_category(self, cat_name):
        # Дім і сад
        self.page.locator(f'//span[text()="{cat_name}"]/..').click()
        expect(self.page.get_by_text(
            "Канцтовари / витратні матеріалиМебліПродукти харчування / напоїСад / городПредме")).to_be_visible()

    @allure.step
    def open_product_subcategory(self, subcat_name):
        # Меблі
        self.page.get_by_role("link", name=f"{subcat_name}").click()

    @allure.step
    def check_filter_page_isOpened(self):
        expect(self.page).to_have_url('https://www.olx.ua/uk/dom-i-sad/mebel/')
        expect(self.page.get_by_role("heading", name="Фільтри")).to_be_visible()

    @allure.step
    def select_filter_subcategory(self, subcat_name):
        # Меблі для вітальні
        self.page.locator('//p[text()="Підкатегорія"]/..//div').nth(1).click()
        self.page.get_by_test_id("listing-filters").get_by_text(f"{subcat_name}", exact=True).click()

    @allure.step
    def set_filter_price(self, low_price, high_price):
        self.page.get_by_test_id("range-from-input").fill(f"{low_price}", no_wait_after=True)
        self.page.get_by_test_id("range-to-input").fill(f"{high_price}")
        with self.page.expect_navigation(wait_until='load', timeout=30000):
            self.page.get_by_test_id("range-to-input").press("Enter", no_wait_after=True)

    @allure.step
    def check_green_sofa_search_result(self):
        expect(self.page.get_by_test_id("listing-grid").locator("div").filter(has_text="Диван Б\\У зелений100").nth(
            1)).to_be_visible()