import pytest  # Импорт библиотеки pytest для создания тестов
from selenium import webdriver  # Импорт webdriver из библиотеки Selenium для управления браузером
from selenium.webdriver.chrome.options import Options
@pytest.fixture  # Декоратор для создания фикстуры
def driver():
    options = Options()
    options.add_argument("--headless")  # запускать в безголовом режиме
    driver = webdriver.Chrome(options=options)  # Инициализация драйвера для браузера Chrome
    driver.maximize_window()  # Максимизация окна браузера
    driver.implicitly_wait(3)  # Установка неявного ожидания для всех элементов (3 секунды)
    yield driver  # Возврат драйвера тестовой функции и приостановка выполнения до завершения теста
    driver.close()  # Закрытие браузера после завершения тестаpytes