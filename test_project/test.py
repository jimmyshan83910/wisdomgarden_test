import unittest
from schema import Schema
from variable import TestVariable
import datetime


class TestStringMethods(unittest.TestCase):
    def test_match_item_category(self):
        Schema(str).validate(TestVariable.match_item)
        Schema(str).validate(TestVariable.match_item_category)

    def test_convert_str_to_datetime(self):
        date = TestVariable.convert_str_to_datetime.split('.')
        year = date[0]
        month = date[1]
        day = date[2]
        Schema(str).validate(year)
        Schema(str).validate(month)
        Schema(str).validate(day)

    def test_ticket_retry(self):
        Schema(int).validate(TestVariable.ticket_retry)

    def test_get_discount_content(self):
        data_list = TestVariable.get_discount_content.split('|')
        date = data_list[0]
        discount = data_list[1]
        category = data_list[2]

        Schema(str).validate(date)
        Schema(str).validate(discount)
        Schema(str).validate(category)

        Schema({
            'discount_or_not': {},
            'customer_purchase_data': {},
            'ticket': {},
            'account_days': ''
        }).validate(TestVariable.get_discount_purchase_data_dict)

    def test_get_ticket_content(self):
        Schema({
            'discount_or_not': {},
            'customer_purchase_data': {},
            'ticket': {},
            'account_days': ''
        }).validate(TestVariable.get_ticket_purchase_data_dict)

    def test_get_each_item_total_price(self):
        Schema(str).validate(TestVariable.get_each_item)
        Schema(int).validate(TestVariable.get_each_item_count)
        Schema({
            'discount_or_not': {},
            'customer_purchase_data': {},
            'ticket': {},
            'account_days': ''
        }).validate(TestVariable.get_each_purchase_data_dict)

    def test_price_discount_calculate(self):
        for test_key, test_value in TestVariable.price_discount_calculate[0].items():
            Schema(str).validate(test_key)
            Schema(float).validate(test_value)

        for test_key, test_value in TestVariable.price_discount_customer_purchase_content.items():
            Schema(str).validate(test_key)
            Schema(int).validate(test_value)

    def test_price_ticket_calculate(self):
        for test_key, test_value in TestVariable.price_ticket_calculate.items():
            Schema(datetime.date).validate(test_key)
            for key, value in test_value.items():
                Schema(int).validate(key)
                Schema(int).validate(value)

    def test_purchase_content_handler(self):
        for test_key, test_value in TestVariable.test_purchase_item.items():
            Schema(str).validate(test_key)
            Schema(int).validate(test_value)


if __name__ == '__main__':
    unittest.main()
