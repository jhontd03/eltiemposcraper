[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7317125.svg)](https://doi.org/10.5281/zenodo.7317125)

# Desvelando el Pulso de Colombia: Extracción de Datos y Análisis de Noticias con Scrapy

![map accident](https://github.com/jhontd03/eltiemposcraper/blob/master/img/daily_news.png "daily_news")

## [Contenido](#Contenido)

- [Introducci�n](#Introducc�n)
- [Instalaci�n](#Instalaci�n)
- [Requisitos](#Requisitos)
- [Uso](#Uso)
- [Estructura del repositorio](#Estructura-del-repositorio)
- [Resultados](#Resultados)
- [Autor](#Autor)

## Introducci�n

El presente proyecto es una aplicaci�n de la t�cnica de webscraping, para la obtenci�n de noticias en el diario [El Tiempo](https://www.eltiempo.com/).

Su desarrollo se enmarca en la pr�ctica 1 de la asignatura Tipolog�a y ciclo de vida de datos del [Mater Universitario en Ciencia de Datos](https://estudios.uoc.edu/es/masters-universitarios/data-science/presentacion) de la Universitat Oberta de Catalunya.

## Instalaci�n

## Requisitos

Para la ejecuci�n del programa es necesario instalar la version de python 3.8.x y para usuarios de windows, un emulador de la terminal de comandos similar al bash de linux 

Instale [python](https://www.python.org/downloads/) y [cmder](https://cmder.app/)

## Uso

Clone el presente repositorio cree un entorno virtual, instale las librerias y ejecute el c�digo Python directamente.

```
git clone https://github.com/jhontd03/eltiemposcraper.git
cd eltiemposcraper
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
pip install scrapy
cd eltiemposcraper
scrapy crawl news
```

## Estructura del repositorio

El �rbol de directorios del repositorio es el siguiente:
```
.
+---scrapy.cfg
�   
+---dataset
�       news_eltiempo_11-11-2022.json
�       
+---eltiemposcraper
    �   items.py
    �   middlewares.py
    �   pipelines.py
    �   settings.py
    �   __init__.py
    �   
    +---spiders
    �   �   news.py
    �   �   __init__.py
    �   �   
    �   +---__pycache__
    �           news.cpython-38.pyc
    �           __init__.cpython-38.pyc
    �           
    +---__pycache__
            settings.cpython-38.pyc
            __init__.cpython-38.pyc

```

## Resultados

Se obtuvo un archivo json que contiene 234 noticias correspondientes al 11 de noviembre de 2022, en las categorias: econom�a, pol�tica, justicia, unidad investigativa y opini�n, cada noticia contiene el t�tulo, ep�grafe y el cuerpo.

[Ver dataset obtenido](https://github.com/jhontd03/eltiemposcraper/tree/master/dataset)

## Autor

Jhon Jairo Realpe

jrealpe0@uoc.edu
