
import time
from pages.homepage import HomePage
from pages.product import ProductPage

def test_open_galagy_s6(driver):
    homepage = HomePage(driver)  # Инициализация объекта HomePage
    homepage.open()  # Открытие главной страницы
    homepage.click_galaxy_s6()  # Клик по элементу "Samsung galaxy s6"
    # driver.get('https://www.demoblaze.com/')  # Альтернативный способ открытия страницы
    # galaxy_s6 = driver.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]')  # Поиск элемента по XPath
    # galaxy_s6.click()  # Клик по элементу
    product_page = ProductPage(driver)  # Инициализация объекта ProductPage
    product_page.check_title_is("Samsung galaxy s6")  # Проверка заголовка страницы
    # title = driver.find_element(By.CSS_SELECTOR, "h2")  # Поиск заголовка по CSS-селектору
    # assert title.text == "Samsung galaxy s6"  # Проверка текста заголовка


def test_two_monitors(driver):
    homepage = HomePage(driver)  # Инициализация объекта HomePage
    homepage.open()  # Открытие главной страницы
    # driver.get('https://www.demoblaze.com/')  # Альтернативный способ открытия страницы
    homepage.click_monitor()  # Клик по элементу "Monitors"
    # monitor_link = driver.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')  # Поиск элемента по CSS-селектору
    # monitor_link.click()  # Клик по элементу
    time.sleep(2)  # Пауза для загрузки страницы
    homepage.check_products_count(2)  # Проверка количества товаров на странице
    # monitors = driver.find_elements(By.CSS_SELECTOR, '.card')  # Поиск всех элементов с классом 'card'
    # assert len(monitors) == 2  # Проверка количества найденных элементов