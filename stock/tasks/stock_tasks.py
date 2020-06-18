from __future__ import absolute_import, unicode_literals
from celery import task


@task()
def get_latest_stock_data(ticker):
    """
    Method that gets the latest data for a Stock
    :param ticker: Ticker of Stock to get data for
    """
    from stock.services import get_stock_data, stock_price_data_df_to_model

    df = get_stock_data(ticker, period='1d', interval='1m')
    stock_price_data_df_to_model(df)
    print('Added {} minute data'.format(ticker))


@task
def get_day_stock_data(ticker):
    """
    Method that that gets the day data for a Stock
    :param ticker: Stock ticker to get data for
    """
    from stock.services import get_stock_data, stock_price_data_df_to_model

    df = get_stock_data(ticker, period='1d', interval='1d')
    stock_price_data_df_to_model(df)
    print('Added {} day data'.format(ticker))


@task
def get_bulk_day_stock_data(ticker):
    """
    Method that that gets the day data for a Stock
    :param ticker: Stock symbool to get data for
    """
    from stock.services import get_stock_data, bulk_stock_price_data_to_model

    df = get_stock_data(ticker, period='1y', interval='1d')
    bulk_stock_price_data_to_model(df)
    print('Added {} daily data'.format(ticker))