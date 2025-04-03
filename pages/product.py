from selenium.webdriver.common.by import By  # Импорт класса By для указания способа поиска элементов (по сути не нужен)

class ProductPage:
    def __init__(self, driver):
        self.driver = driver  # Инициализация драйвера для использования в методах класса

    def check_title_is(self, title):
        page_title = self.driver.find_element(By.CSS_SELECTOR, "h2")  # ПОИСК элемента заголовка (h2) на странице с помощью CSS-селектора
        assert page_title.text == title  # Проверка, что текст заголовка соответствует переданному значению `title`