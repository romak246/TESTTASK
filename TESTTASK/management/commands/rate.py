import requests
from django.core.management.base import BaseCommand
from datetime import date

from TESTTASK.models import *


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        today = date.today()

        def currency_rate(valute_name, quoted_valute, date):
            exchange_rate = ExchangeRate()

            def exist_check(valute):

                currency_search = CurrencyName.objects.filter(name=valute)
                currency_name = CurrencyName()


                if currency_search.count() < 1:
                    currency_name.name = valute
                    currency_name.symbol = '*'
                    currency_name.save()


            exist_check(valute_name)
            exist_check(quoted_valute)

            data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()

            currency_object = CurrencyName.objects.get(name=valute_name)
            base_id = currency_object.id
            quoted_object = CurrencyName.objects.get(name=quoted_valute)

            quoted_id = quoted_object.id


            def check(value):
                if value == "RUB":
                    return 1
                base_value = data['Valute'][value]['Value']/data['Valute'][value]['Nominal']
                print(base_value)
                return base_value

            base = check(valute_name)
            quote = check(quoted_valute)
            exchange_rate_res = base/quote
            print(exchange_rate_res)

            sc = ExchangeRate.objects.filter(at=today, base_id=base_id, quoted_id=quoted_id)

            if sc.count() < 1:
                exchange_rate.at = today
                exchange_rate.base_id = base_id
                exchange_rate.quoted_id = quoted_id
                exchange_rate.value = exchange_rate_res
                exchange_rate.save()

            else:
                genre = ExchangeRate.objects.filter(at=today, base_id=base_id, quoted_id=quoted_id).get()
                genre.at = today
                genre.base_id = base_id
                genre.quoted_id = quoted_id
                genre.value = exchange_rate_res
                genre.save()

        currency_names = CurrencyName.objects.values_list('name')
        for base in currency_names:
            for query in currency_names:
                if base == query:
                    continue
                print(query[0], base[0])
                currency_rate(base[0], query[0], today)







