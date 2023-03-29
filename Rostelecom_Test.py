
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pytest


path_driver = r"E:\Note\JN\chromedriver.exe"  # Путь до драйвера
s = Service(path_driver)
chrome_driver = webdriver.Chrome(service=s)
chrome_driver.get('https://b2c.passport.rt.ru/')
chrome_driver.maximize_window()
sleep(5)

# Страница содержит два блока . Правый должен содержать слоган


def test_two_blocks():
    right_element = chrome_driver.find_element(By.ID, "page-left")
    what_is = 0
    try:
        what_is = right_element.find_element(By.CLASS_NAME, "what-is__title")
        assert 'Личный кабинет' == what_is.text
    except NoSuchElementException as e:
        pass
    if not what_is:
        assert 0, 'В правой части должен быть слоган'


# Проверка наименований Tab
def test_button_tab_name():
    phone = chrome_driver.find_element(By.ID, "t-btn-tab-phone").text
    assert phone == 'Телефон'
    mail = chrome_driver.find_element(By.ID, "t-btn-tab-mail").text
    assert mail == 'Почта'
    login = chrome_driver.find_element(By.ID, "t-btn-tab-login").text
    assert login == 'Логин'
    ls = chrome_driver.find_element(By.ID, "t-btn-tab-ls").text
    assert ls == 'Лицевой счёт'


# Проверка что по умолчанию  телефон
def test_default_tab():
    element_by_id = chrome_driver.find_element(
        By.ID, "t-btn-tab-phone").text
    element_by_class = chrome_driver.find_element(
        By.CLASS_NAME, "rt-tab--active").text
    assert element_by_id == element_by_class == 'Телефон'


# Проверка изменений плейсхолдера при нажатии на кнопки
def test_placeholder_tab():
    # Телефон
    chrome_driver.find_element(By.ID, "t-btn-tab-phone").click()
    placeholder = chrome_driver.find_element(
        By.CLASS_NAME, "rt-input__placeholder").text
    assert placeholder == 'Мобильный телефон'
# Почта
    chrome_driver.find_element(By.ID, "t-btn-tab-mail").click()
    placeholder = chrome_driver.find_element(
        By.CLASS_NAME, "rt-input__placeholder").text
    assert placeholder == 'Электронная почта'
# Логин
    chrome_driver.find_element(By.ID, "t-btn-tab-login").click()
    placeholder = chrome_driver.find_element(
        By.CLASS_NAME, "rt-input__placeholder").text
    assert placeholder == 'Логин'
# Лицевой счет
    chrome_driver.find_element(By.ID, "t-btn-tab-ls").click()
    placeholder = chrome_driver.find_element(
        By.CLASS_NAME, "rt-input__placeholder").text
    assert placeholder == 'Лицевой счёт'


# Проверка что появляются валидные ошибки если поля не заполнены и нажимаем кнопку "Войти"


def test_check_error_message():
    # Телефон
    chrome_driver.find_element(By.ID, "t-btn-tab-phone").click()
    chrome_driver.find_element(By.NAME, "login").click()
    error_message = chrome_driver.find_element(
        By.CLASS_NAME, "rt-input-container__meta--error").text
    assert error_message == 'Введите номер телефона'
# Почта
    chrome_driver.find_element(By.ID, "t-btn-tab-mail").click()
    chrome_driver.find_element(By.NAME, "login").click()
    error_message = chrome_driver.find_element(
        By.CLASS_NAME, "rt-input-container__meta--error").text
    assert error_message == 'Введите адрес, указанный при регистрации'
# Логин
    chrome_driver.find_element(By.ID, "t-btn-tab-login").click()
    chrome_driver.find_element(By.NAME, "login").click()
    error_message = chrome_driver.find_element(
        By.CLASS_NAME, "rt-input-container__meta--error").text
    assert error_message == 'Введите логин, указанный при регистрации'
# Лицевой счет
    chrome_driver.find_element(By.ID, "t-btn-tab-ls").click()
    chrome_driver.find_element(By.NAME, "login").click()
    error_message = chrome_driver.find_element(
        By.CLASS_NAME, "rt-input-container__meta--error").text
    assert error_message == 'Введите номер вашего лицевого счета'


# Проверка текста ошибки при вводе неверных данных и нажатия кнопки войти
# @pytest.mark.skip(reason="no way of currently testing this")
def test_view_error_message():
    chrome_driver.find_element(
        By.ID, "username").send_keys('some_login')
    chrome_driver.find_element(
        By.ID, "password").send_keys('some_password')
    chrome_driver.find_element(By.NAME, "login").click()
    error_message = chrome_driver.find_element(
        By.ID, "form-error-message").text
    assert error_message == 'Неверный логин или пароль'


# Переход ссылка забыли пароль
def test_forgot_password():
    chrome_driver.find_element(
        By.ID, "forgot_password").click()
    sleep(3)
    title = chrome_driver.find_element(
        By.CLASS_NAME, "card-container__title").text
    assert title == 'Восстановление пароля'

    chrome_driver.back()

    # chrome_driver.close()
