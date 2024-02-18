 from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

# Создание экземпляра ChromeOptions
chrome_options = Options()
# Установка режима без GUI (если нужно, раскомментируйте следующую строку)
# chrome_options.add_argument("--headless")

# Создание экземпляра Chrome WebDriver с использованием опций и автоматическим управлением драйвером
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Указание URL целевой веб-страницы
url = "https://www.olx.kz/hobbi-otdyh-i-sport/sport-otdyh/"

# Открытие веб-страницы
driver.get(url)

# Ожидание загрузки страницы
driver.implicitly_wait(10)

# Получение исходного кода страницы после выполнения JavaScript
html_content = driver.page_source

# Создание объекта BeautifulSoup для парсинга HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Поиск всех рекламных объявлений с пометкой "ТОП"
top_ads = soup.find_all("div", {"data-testid": "adCard-featured"})

# Инициализация списков для хранения названий и ссылок на рекламные объявления
top_ads_titles = []
top_ads_links = []

# Извлечение названий и ссылок на рекламные объявления
for ad in top_ads:
    # Ваш код предполагает, что у родственного элемента <a> есть текст и href.
    # Необходимо убедиться, что такой элемент существует, прежде чем извлекать оттуда данные.
    ad_link_element = ad.find_previous("a")
    if ad_link_element and ad_link_element.has_attr('href'):
        title = ad_link_element.text.strip()
        link = ad_link_element['href']
        top_ads_titles.append(title)
        top_ads_links.append(link)

# Вывод названий и ссылок на рекламные объявления
for title, link in zip(top_ads_titles, top_ads_links):
    print("Название:", title)
    print("Ссылка:", link)

# Закрытие экземпляра WebDriver после использования
driver.quit()
