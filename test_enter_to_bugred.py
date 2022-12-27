from playwright.sync_api import Page


def test_enter_to_reqres(page: Page):
    page.goto('http://users.bugred.ru/user/login/index')
    page.fill('input#name', 'test1234' )
    page.fill('input#email', 'test1234@gmail.com')
    page.fill('input#password', 'test1234')
    page.click('input#act_register_now')