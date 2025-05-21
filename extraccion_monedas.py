import requests
import pandas as pd
from datetime import datetime

# Monedas a consultar
monedas = ['USD-BRL', 'EUR-BRL', 'BTC-BRL']
url = f"https://economia.awesomeapi.com.br/last/{','.join(monedas)}"

# Hacer la petición a la API
response = requests.get(url)
data = response.json()

# Procesar los datos
normalizados = []

for par in monedas:
    base, destino = par.split('-')
    key = base + destino
    info = data[key]

    normalizados.append({
        'moneda_base': base,
        'moneda_destino': destino,
        'valor_compra': float(info['bid']),
        'valor_venta': float(info['ask']),
        'fecha_hora': datetime.utcfromtimestamp(int(info['timestamp'])).strftime('%Y-%m-%d %H:%M:%S')
    })

# Convertir a DataFrame
df = pd.DataFrame(normalizados)

# Guardar en CSV
df.to_csv('datos_monedas.csv', index=False)

print("Datos guardados exitosamente en datos_monedas.csv")
