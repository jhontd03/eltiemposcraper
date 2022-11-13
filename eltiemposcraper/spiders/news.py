import scrapy
import os
import datetime

# Se define los xpath
HOME_URL = 'https://www.eltiempo.com/'
XPATH_MENU = '//ul[@class="default-menu"]/li/a/@href'
XPATH_LINK = '//h3/a[(@class="title page-link ") or (@class="title page-link")]/@href'
XPATH_TITLE = '//div/h1[(@class="titulo") or (@class="titulo ")]/text()'
XPATH_EPIGRAPH = '//div[@class="epigraph-container lead"]/h2/text()'
XPATH_BODY = '//div[@class="articulo-contenido"]/div/p[(@class="contenido ") or (@class="contenido")]/text()'

class SpiderElTiempo(scrapy.Spider):

    name = 'news'
    # Se seleccionan solo el dominio eltiempo.com
    allowed_domains = ['eltiempo.com']
    # Se define el url principal
    start_urls = [HOME_URL]

    date = datetime.date.today().strftime('%d-%m-%Y')

    custom_settings = {
        # se configura el formato a exportar
        'FEEDS': {
            f'dataset/news_eltiempo_{date}.json': {
                'format': 'json',
                'overwrite': True,
                'encoding': 'utf-8'
            }
        },
        # Se configura el máximo numero de peticiones concurrentes
        'CONCURRENT_REQUESTS': 1000,
        # Se configura el uso máximo de memoria
        'MEMUSAGE_LIMIT_MB': 2048,
        'MEMUSAGE_NOTIFY_EMAIL': ['jrealpe0@uoc.edu'],
        # Se respetan las reglas del archivo robots.txt
        'ROBOTSTXT_OBEY': True,
        # Se configura el user-agent
        'USER_AGENT': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
        # Se configura el tiempo de espera ante petición al servidor web
        'CLOSESPIDER_TIMEOUT': 10,
        # Se configura la máxima profundid en links a explorar
        'DEPTH_LIMIT': 5,
        # Se genera un retardo de 500ms para cada petición
        'DOWNLOAD_DELAY': 0.5,
    }

    def parse(self, response):
        # Crea directorio donde se almacenará el dataset
        if not os.path.isdir('dataset'):
            os.mkdir('dataset')

        # Se obtiene lista con categoria de noticias
        links_pages = response.xpath(XPATH_MENU).getall()

        sel_pages= ['/opinion', '/economia', '/colombia', 
                '/justicia', '/politica', '/unidad-investigativa']

        # Se seleccionan solo las categorias de interés
        links_pages = [x for x in links_pages if x in sel_pages]

        # Se hace un request a cada link de categoría de noticias
        # y se hace llamado a función parge_page
        for links in links_pages:
            url = response.urljoin(links)
            yield scrapy.Request(url, callback=self.parse_page)

    def parse_page(self, response):
        # Se crea una lista con los links de cada noticia
        links_articles = response.xpath(XPATH_LINK).getall()
        # Se hace requesta a cada link y se hace llamado a la función parse_link
        for url in links_articles:
            yield response.follow(url, callback=self.parse_link, cb_kwargs={'url': response.urljoin(url)})

    def parse_link(self, response, **kwargs):
        # Se obtiene la información correspondiente para cada noticia
        url = kwargs['url']
        category = url.split("/")[3]

        sel_category= ['opinion', 'economia', 'colombia', 
                       'justicia', 'politica', 'unidad-investigativa']

        # Se filtran categorias de interés
        if category in sel_category:
            title =  response.xpath(XPATH_TITLE).get()
            epigraph = response.xpath(XPATH_EPIGRAPH).get()
            # se obtiene el cuerpo de la noticia
            body = response.xpath(XPATH_BODY).getall()
            # Dado que el cuerpo de la noticia tiene múltiples parrafos
            # se concatenan.
            body = ' '.join(body)
            # Se volca la información a fichero json
            yield {
                category: {
                    'title': title,
                    'epigraph': epigraph,
                    'body': body
                }
            }
