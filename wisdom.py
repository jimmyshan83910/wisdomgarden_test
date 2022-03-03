import datetime


class ShoppingCart():
    def __init__(self):
        self.item_category = {
            'electronic': ['ipad', 'iphone', 'screen', 'laptop', 'keyboard'],
            'food': ['bread', 'cookies', 'cake', 'beef', 'fish', 'vegetable'],
            'necessary': ['paper＿napkin', 'storage_box', 'coffee＿cup', 'umbrella'],
            'wine': ['beer', 'white_wine', 'vodka']
        }
        self.price = {'ipad': 2399, 'screen': 1799, 'beer': 25, 'bread': 9, 'vegetable': 5.98, 'paper＿napkin': 3.2}
        self.today = datetime.date.today()
        self.total_price = 0

    def match_item_category(self, item, category):
        if category in self.item_category.keys():
            return 1 if item in self.item_category[category] else 0

    def convert_str_to_datetime(self, date):
        return datetime.datetime.strptime(date, "%Y.%m.%d").date()

    def ticket_retry(self, retry):
        return 1 if retry else 0

    def get_discount_content(self, discount_format, purchase_data_dict):
        discount_format = discount_format.split('|')
        discount_date = self.convert_str_to_datetime(discount_format[0])
        if discount_date == self.today:
            if discount_date in purchase_data_dict['discount_or_not'].keys():
                purchase_data_dict['discount_or_not'][discount_date].append(
                    {discount_format[2]: float(discount_format[1])})
            else:
                temp_dict = {discount_date: [{discount_format[2]: float(discount_format[1])}]}
                purchase_data_dict['discount_or_not'].update(temp_dict)
        else:
            print("輸入的折扣日期錯誤，故不會折扣在總價格上")

    def get_ticket_content(self, purchase_data_dict):
        ticket_format = input("請輸入優惠券資訊的格式 -> 到期日 滿xxx 折xxx: ")
        ticket_format = ticket_format.split(' ')

        ticket_expired = self.convert_str_to_datetime(ticket_format[0])
        if ticket_expired >= self.today:
            temp_dict = {ticket_expired: {int(ticket_format[1]): int(ticket_format[2])}}
            purchase_data_dict['ticket'].update(temp_dict)
        else:
            retry = input("不好意思，您的優惠券已超過使用期限，要重新輸入其他優惠券嗎 y/n？")
            while True:
                if retry == 'y':
                    return 1
                elif retry == 'n':
                    return 0
                else:
                    print("輸入格式錯誤，請再輸入一次。 要輸入其他優惠券嗎 y/n？")
                    continue
        return 0

    def get_each_item_total_price(self, item, item_count, purchase_data_dict):
        temp_dict = {}
        temp_dict[item] = item_count * self.price[item]
        purchase_data_dict['customer_purchase_data'].update(temp_dict)

    def price_discount_calculate(self, discount_content, customer_purchase_content):
        for category, disc in discount_content[0].items():
            for item in customer_purchase_content:
                if self.match_item_category(item, category):
                    final_price = customer_purchase_content[item] * disc
                    customer_purchase_content[item] = final_price

    def price_ticket_calculate(self, ticket_content):
        for date in ticket_content:
            if self.total_price >= int(next(iter(ticket_content[date]))):
                self.total_price -= list(ticket_content[date].values())[0]

    def final_purchase_total_price(self, purchase_data_dict):
        # 將最終的折扣、優惠券內容，納入購物車總價格進行計算
        discount_content = None
        if purchase_data_dict['discount_or_not']:
            discount_content = purchase_data_dict['discount_or_not'][self.today]

        customer_purchase_content = purchase_data_dict['customer_purchase_data']
        ticket_content = purchase_data_dict['ticket']

        if discount_content:
            self.price_discount_calculate(discount_content, customer_purchase_content)

        for price in customer_purchase_content.values():
            self.total_price += price

        if ticket_content:
            self.price_ticket_calculate(ticket_content)

        self.total_price = '{:.2f}'.format(self.total_price)

        # 最終價格
        print("您所購買的商品價格為: ", self.total_price)

    def purchase_content_handler(self, cases):
        # 定義購物車資料格式
        purchase_data_dict = {
            'discount_or_not': {},
            'customer_purchase_data': {},
            'ticket': {},
            'account_days': ''
        }

        # 整理所有促銷資料
        while True:
            try:
                discount_format = input("請輸入促銷資訊，格式為 -> 日期|折扣|產品品類。沒有促銷或者輸入完促銷請輸入'n': ")
                if discount_format and discount_format != "n":
                    shopping_cart.get_discount_content(discount_format, purchase_data_dict)
                elif discount_format == "n":
                    break
                else:
                    raise ValueError

                continue_message = input("是否繼續輸入更多折扣資訊 y/n？")
                if continue_message == 'y':
                    continue
                elif continue_message == "n":
                    break
                else:
                    raise ValueError

            except (ValueError, IndexError, TypeError):
                print("輸入格式錯誤，請重新輸入一次！")
                continue

        if not purchase_data_dict['discount_or_not']:
            purchase_data_dict['discount_or_not'] = ''

        # 整理顧客優惠券資料
        while True:
            try:
                ticket_or_not = input("是否使用優惠券 y/n？")
                if ticket_or_not == 'y':
                    retry = shopping_cart.get_ticket_content(purchase_data_dict)
                    if self.ticket_retry(retry):
                        continue
                    else:
                        break
                elif ticket_or_not == 'n':
                    purchase_data_dict['ticket'] = ''
                    break
                else:
                    raise ValueError
            except (ValueError, IndexError, TypeError):
                print("輸入格式錯誤，請重新輸入一次！")
                continue

        # 計算購物車內每一物品總價格。數量*單價 = 總價格
        for item, item_count in cases.items():
            shopping_cart.get_each_item_total_price(item, item_count, purchase_data_dict)

        # 結算日期
        purchase_data_dict['account_days'] = self.today

        # 將整理後的折扣、優惠券、購物車總價格，傳入進行計算
        self.final_purchase_total_price(purchase_data_dict)


if __name__ == '__main__':
    # 選擇Cases
    while True:
        which_case = input("請輸入要使用'case_a' or 'case_b': ")
        cases = {
            'case_a': {'ipad': 1, 'screen': 1, 'beer': 12, 'bread': 5},
            'case_b': {'vegetable': 3, 'paper＿napkin': 8}
        }

        if which_case in cases.keys():
            cases = cases[which_case]
            break
        else:
            print("格式錯誤，請再輸入一次")
            continue

    # 購物車類別
    shopping_cart = ShoppingCart()
    shopping_cart.purchase_content_handler(cases)
