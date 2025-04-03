from selenium.webdriver.common.by import By  # Импорт класса By для указания способа поиска элементов

class HomePage:
    def __init__(self, driver):
        self.driver = driver  # Инициализация драйвера для использования в методах класса

    def open(self):
        self.driver.get('https://www.demoblaze.com/')  # Открытие главной страницы сайта

    def click_galaxy_s6(self):
        galaxy_s6 = self.driver.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]')  # Поиск элемента "Samsung galaxy s6" по XPath
        galaxy_s6.click()  # Клик по найденному элементу

    def click_monitor(self):
        monitor_link = self.driver.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')  # Поиск элемента "Monitors" по CSS-селектору
        monitor_link.click()  # Клик по найденному элементу

    def check_products_count(self, count):
        monitors = self.driver.find_elements(By.CSS_SELECTOR, '.card')  # Поиск всех элементов с классом 'card' (карточки товаров)
        assert len(monitors) == count  # Проверка, что количество найденных элементов равно заданному значению