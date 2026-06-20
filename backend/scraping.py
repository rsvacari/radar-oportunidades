import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL_ACOES = "https://www.fundamentus.com.br/buscaavancada.php"
BASE_URL_FIIS = "https://www.fundamentus.com.br/fii_buscaavancada.php"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; RadarOportunidades/1.0)"
}

def _html_to_dataframe(html):
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table", {"class": "resultado"})
    if table is None:
        return pd.DataFrame()

    rows = table.find_all("tr")
    data = []
    headers = [th.get_text(strip=True) for th in rows[0].find_all("th")]

    for row in rows[1:]:
        cols = [td.get_text(strip=True) for td in row.find_all("td")]
        if cols:
            data.append(cols)

    df = pd.DataFrame(data, columns=headers)
    return df

def get_acoes():
    resp = requests.get(BASE_URL_ACOES, headers=HEADERS)
    resp.raise_for_status()
    return _html_to_dataframe(resp.text)

def get_fiis():
    resp = requests.get(BASE_URL_FIIS, headers=HEADERS)
    resp.raise_for_status()
    return _html_to_dataframe(resp.text)
