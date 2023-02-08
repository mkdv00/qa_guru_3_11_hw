import pytest
from selene.support.shared import browser


@pytest.fixture(params=["1920x1080", "900x940"])
def browser_open(request):
    if request.param == "1920x1080":
        browser.config.window_width = int(request.param.split('x')[0])
        browser.config.window_height = int(request.param.split('x')[1])
    else:
        browser.config.window_width = int(request.param.split('x')[0])
        browser.config.window_height = int(request.param.split('x')[1])
    browser.open('https://github.com')


@pytest.fixture()
def browser_chrome():
    browser.open('https://github.com')