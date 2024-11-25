import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de Mercado Libre (puedes personalizarla según la categoría o región)
url = "https://www.mercadolibre.com.ar/ofertas"

# Encabezados para imitar un navegador
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Realizar la solicitud HTTP
response = requests.get(url, headers=headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extraer las ofertas
    offers = []
    for item in soup.find_all('li', class_='promotion-item'):  # Ajusta el selector según el HTML
        title = item.find('p', class_='promotion-item-title').get_text(strip=True) if item.find('p', class_='promotion-item-title') else "Sin título"
        price = item.find('span', class_='promotion-item-price').get_text(strip=True) if item.find('span', class_='promotion-item-price') else "Sin precio"
        link = item.find('a', href=True)['href'] if item.find('a', href=True) else "Sin enlace"
        offers.append({"Título": title, "Precio": price, "Enlace": link})

    # Guardar en un archivo CSV
    df = pd.DataFrame(offers)
    df.to_csv('ofertas_mercadolibre.csv', index=False)
    print("Ofertas guardadas en ofertas_mercadolibre.csv")
else:
    print(f"Error al acceder a la página: {response.status_code}")
