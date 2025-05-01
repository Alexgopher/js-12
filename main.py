import logging
import mysql.connector
import requests
from datetime import datetime

formatter = logging.Formatter('[%(levelname)s] %(asctime)s %(message)s', datefmt="%Y-%m-%d %H:%M:%S")
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

SITES = [
    "congress.gov",
    "gov.uk",
    "govtrack.us",
    "house.gov",
    "regulations.gov",
    "senate.gov",
    "service-public.fr",
    "archives.gov/federal-register",
    "assemblee-nationale.fr",
    "bgbl.de",
    "bundesanzeiger.de",
    "bundesrat.de",
    "bundestag.de",
    "bundesverfassungsgericht.de",
    "camera.it",
    "canlii.org",
    "cbo.gov",
    "commons.parliament.uk",
    "conseil-constitutionnel.fr",
    "conseil-etat.fr",
    "consultant.ru",
    "cortecostituzionale.it",
    "council.gov.ru",
    "courts.go.jp",
    "digital.go.jp",
    "dip.bundestag.de",
    "duma.gov.ru",
    "e-gov.go.jp",
    "federalregister.gov",
    "gao.gov",
    "garant.ru",
    "gazette.gc.ca",
    "gazzettaufficiale.it",
    "gesetze-im-internet.de",
    "giustizia-amministrativa.it",
    "giustizia.it",
    "gov.uk/government/publications",
    "government.ru",
    "governo.it",
    "govinfo.gov",
    "gpo.gov",
    "hansard.parliament.uk",
    "japaneselawtranslation.go.jp",
    "journal-officiel.gouv.fr",
    "juris.de",
    "kanpou.npb.go.jp",
    "kantei.go.jp",
    "kremlin.ru",
    "ksrf.ru",
    "laws-lois.justice.gc.ca",
    "legifrance.gouv.fr",
    "legislation.gov.uk",
    "loc.gov",
    "lords.parliament.uk",
    "minjust.gov.ru",
    "moj.go.jp",
    "ncsl.org",
    "niassembly.gov.uk",
    "normattiva.it",
    "openparliament.ca",
    "ourcommons.ca",
    "parl.ca",
    "parl.ca/legisinfo",
    "parlamento.it",
    "parliament.scot",
    "parliament.uk",
    "pco-bcp.gc.ca",
    "pravo.gov.ru",
    "reginfo.gov",
    "rg.ru",
    "sangiin.go.jp",
    "senat.fr",
    "senato.it",
    "sencanada.ca",
    "senedd.wales",
    "shugiin.go.jp",
    "soumu.go.jp",
    "thegazette.co.uk",
    "vie-publique.fr",
    "vsrf.ru",
    "whitehouse.gov"]


response = requests.get("https://api.congress.gov")

config = {
    'host': '*.beget.tech',  # Хост базы данных
    'user': '*_news',  # Имя пользователя
    'password': 'n3w5_c0ll3ctor',  # Пароль
    'db': '*_news',  # Имя базы данных вместо 'database'
    'autocommit': True  # Автоматический коммит транзакций
}


