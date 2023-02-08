import pytest
from selene import have
from selene.support.shared import browser


@pytest.mark.parametrize('browser_open', ["900x940"], indirect=True)
def test_github_mobile_indirect(browser_open):
    browser.element('div>[aria-label="Toggle navigation"]').click()
    browser.element('a[href="/login"]').click()
    browser.element('.auth-form-header').should(have.text("Sign in to GitHub"))


@pytest.mark.parametrize('browser_open', ["1920x1080"], indirect=True)
def test_github_desktop_indirect(browser_open):
    browser.element('a[href="/login"]').click()
    browser.element('.auth-form-header').should(have.text("Sign in to GitHub"))


@pytest.mark.parametrize('width, height', [pytest.param(1920, 1080, id='Browser size: 1920x1080'),
                                           pytest.param(900, 940, id='Browser size: 900x940')
                                           ])
def test_github_desktop(browser_chrome, width, height):
    if width == 900:
        pytest.skip("Мобильный вариант в данном тесте недопустим")
    browser.driver.set_window_size(width, height)
    browser.element('a[href="/login"]').click()
    browser.element('.auth-form-header').should(have.text("Sign in to GitHub"))


@pytest.mark.parametrize('width, height', [pytest.param(1920, 1080, id='Browser size: 1920x1080'),
                                           pytest.param(900, 940, id='Browser size: 900x940')
                                           ])
def test_github_mobile(browser_chrome, width, height):
    if width == 1920:
        pytest.skip("Десктопный вариант в данном тесте недопустим")
    browser.driver.set_window_size(width, height)
    browser.element('div>[aria-label="Toggle navigation"]').click()
    browser.element('a[href="/login"]').click()
    browser.element('.auth-form-header').should(have.text("Sign in to GitHub"))


'''
В чем преимущества и недостатки каждого из подходов?
При переопределилении параметра с помощью indirect мы можем использовать только один параметр, 
а во втором случае мы нагромождаем теcт условиями. 
В зависимости от ситуации, более логично использовать сразу правильные наборы параметров при параметризации.
'''
