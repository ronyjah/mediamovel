import csv
import unittest

PAYED_VALUE = 0
BALANCE = 2000  # Amount equivalent to 50 stocks (PAYED_VALUE)
# STOCKS = {'73.41': 50}
STOCK_AMOUNT = 0
VAR_RATE = 15

def loss():
    global VAR_RATE
    return round(VAR_RATE * PAYED_VALUE / 100, 2)

def gain():
    global VAR_RATE
    return round(VAR_RATE * PAYED_VALUE / 100, 2)


def sell_or_buy(stock_price):
    global STOCK_AMOUNT
    global BALANCE
    global PAYED_VALUE
    # print(f"{stock_price} -- {PAYED_VALUE} -- {LOSS} -- {GAIN}")

    # No stocks, buy some
    if stock_price == 0:
        return
    if STOCK_AMOUNT == 0:
        STOCK_AMOUNT = int(BALANCE / stock_price)
        PAYED_VALUE = stock_price
        BALANCE = BALANCE - (STOCK_AMOUNT * PAYED_VALUE)
        print(f"BOUGHT: {STOCK_AMOUNT} for R$ {stock_price} ({BALANCE})")
    else:
        # My stocks are HIGHER
        if PAYED_VALUE > stock_price:
            diff = PAYED_VALUE - stock_price
            if diff >= loss():
                PAYED_VALUE = stock_price
                BALANCE = BALANCE + STOCK_AMOUNT * stock_price
                print(f"LOSS: {STOCK_AMOUNT} for R$ {stock_price} ({BALANCE})")
                STOCK_AMOUNT = 0
            else:
                # pass
                print("WAIT, acceptable loss")
        # My stocks are LOWER
        if PAYED_VALUE < stock_price:
            diff = stock_price - PAYED_VALUE
            if diff >= gain():
                PAYED_VALUE = stock_price
                BALANCE = BALANCE + STOCK_AMOUNT * stock_price
                print(f"GAIN: {STOCK_AMOUNT} for R$ {stock_price} ({BALANCE})")
                STOCK_AMOUNT = 0
            else:
                # pass
                print("WAIT, unacceptable gain")


def main():
    global STOCK_AMOUNT
    global BALANCE
    global PAYED_VALUE

    file = 'BBDC3.SA.1Y.csv' # <<<<<< Nome do arquivo para simular

    print(file)
    print(f"Initial: R${BALANCE}")
    with open(file, newline='') as csvfile:
        bovadb = csv.reader(csvfile)
        header = True
        for row in bovadb:
            if header:
                header = False
                continue

            try:
                open_price = round(float(row[1]), 2)
            except ValueError:
                open_price = 0

            sell_or_buy(open_price)

    if STOCK_AMOUNT > 0:
        BALANCE = BALANCE + STOCK_AMOUNT * PAYED_VALUE

    variation = round((BALANCE - 2000) * 0.05, 2)
    print(f"Result: R${BALANCE} -> {variation}%")


if __name__ == '__main__':
    main()


class StockbotTests(unittest.TestCase):
    def test_sell_or_buy(self):
        self.assertEqual(
            sell_or_buy(PAYED_VALUE - (PAYED_VALUE / 2)), 'SELL')
