import requests
import argparse
import os 
from dotenv import load_dotenv


def get_conversion_result(token, base_currency, target_currency, amount):
    url =f"https://v6.exchangerateapi.com/v6/{token}/pair/{base_currency}/{target_currency}/{amount}"
    try: 
        response = requests.get(url)
        response.raise_for_status()
        return response.json()["conversion_result"]
    except requests.exceptions.HTTPError as e:
        print(f"Ошибка: {e.response.status_code})")
        return None


def main():
    load_dotenv()
    token = os.getenv("TOKEN")
  
    parser = argparse.ArgumentParser(description="Получение курсов обмена для заданной валюты.")
    parser.add_argument("-cur", "--base_currency", help="Укажите базовую валюту, например: RUB, USD, EUR", required=True, default="RUB")
    parser.add_argument("-tar", "--target_currency", help="Укажите целевую валюту, например: RUB, USD, EUR", required=True, default="USD")
    parser.add_argument("-amo", "--amount", help="Укажие число для конвертации в другую валюту", required=True, type=float, default="1000")
    args = parser.parse_args()
    base_currency = args.base_currency.upper()
    target_currency = args.target_currency.upper()
    amount = args.amount

    conversion_result = get_conversion_result(token, base_currency, target_currency, amount)
    if conversion_result:
        print(f"Конвертированная сумма: {conversion_result} {target_currency}")


if __name__ == "__main__":
    main()





































































