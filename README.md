# Challenge - Analytics Engineer Administration Risk & Compliance

## Descripción

Este proyecto consiste en una aplicación que consume datos financieros de una API pública ([AwesomeAPI - API de Moedas](https://docs.awesomeapi.com.br/api-de-moedas)), realiza la normalización de las cotizaciones de monedas extranjeras (USD/BRL, EUR/BRL, BTC/BRL) y almacena la información para consultas futuras.

---

## Estructura del Proyecto

- `extraccion_monedas.py`: Script principal encargado de extraer, transformar y guardar los datos.  
- `datos_monedas.csv`: Archivo de salida que contiene los datos normalizados en formato CSV.  
- `README.md`: Este archivo de documentación.

---

## Tecnologías Utilizadas

- Python 3.x  
- Requests (para consumir la API)  
- Pandas (para la manipulación y normalización de datos)  
- CSV (para almacenamiento en archivo plano)  

---

## Cómo Ejecutar

1. Asegurarse de tener Python 3 instalado.

2. Instalar las dependencias necesarias:
    pip install requests pandas
   
3. Ejecutar el script principal:
  python extraccion_monedas.py

4. El script extraerá las cotizaciones de USD/BRL, EUR/BRL y BTC/BRL desde la API pública, normalizará los datos y los guardará en el archivo datos_monedas.csv. 

---

Estructura de los Datos Normalizados
Los datos se almacenan con los siguientes campos:

| Campo          | Descripción                                                           |
| -------------- | --------------------------------------------------------------------- |
| moeda\_base    | Moneda base (ej. USD, EUR, BTC)                                       |
| moeda\_destino | Moneda destino (ej. BRL)                                              |
| valor\_compra  | Valor de compra de la moneda                                          |
| valor\_venda   | Valor de venta de la moneda                                           |
| data\_hora     | Fecha y hora de la cotización, en formato UTC (`yyyy-MM-dd HH:mm:ss`) |


Observaciones
La fecha y hora fueron normalizadas a UTC para mantener consistencia temporal.

Se utilizó un archivo CSV para facilitar la manipulación y análisis posterior.

Se recomienda revisar el script para ajustar rutas o parámetros en caso de modificaciones.

¡Gracias por la revisión!




