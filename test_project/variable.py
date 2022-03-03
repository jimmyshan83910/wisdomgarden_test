from datetime import datetime


class test_variable:
    match_item = "ipad"
    match_item_category = "electronic"
    convert_str_to_datetime = "2022.03.01"
    ticket_retry = 1
    get_discount_content = "2022.03.03|0.7|electronic"
    get_discount_purchase_data_dict = {
        'discount_or_not': {},
        'customer_purchase_data': {},
        'ticket': {},
        'account_days': ''
    }
    get_ticket_purchase_data_dict = {
        'discount_or_not': {},
        'customer_purchase_data': {},
        'ticket': {},
        'account_days': ''
    }
    get_each_item = "ipad"
    get_each_item_count = 1
    get_each_purchase_data_dict = {
        'discount_or_not': {},
        'customer_purchase_data': {},
        'ticket': {},
        'account_days': ''
    }
    price_discount_calculate = [{'electronic': 0.7}]
    price_discount_customer_purchase_content = {
        'ipad': 2399,
        'screen': 1799,
        'beer': 300,
        'bread': 45
    }
    price_ticket_calculate = {datetime.strptime('2022.9.10', '%Y.%m.%d').date(): {1000: 200}}
    test_purchase_item = {
        'ipad': 1,
        'screen': 1,
        'beer': 12,
        'bread': 5
    }
