from django.db.backends.utils import logger

from exchange.services import NYSE, NASDAQ, LSE, SEHK
from exchange.models import Exchange
from exchange.tasks import bulk_get_exchanges_day_data, bulk_get_exchanges_minute_data, get_exchanges_day_data, \
    get_exchanges_minute_data


def create_exchanges():
    """ Creates all exchanges """
    logger.info('Creating Exchanges...')
    NASDAQ().create_exchange()
    NYSE().create_exchange()
    LSE().create_exchange()
    SEHK().create_exchange()
    logger.info('Created Exchanges')


def create_nasdaq_stocks():
    """ Creates all NASDAQ listed stocks """
    logger.info('Adding NASDAQ Stocks...')
    NASDAQ().create_stocks()
    logger.info('Added NASDAQ Stocks')


def create_nyse_stocks():
    """ Creates all NYSE listed stocks """
    logger.info('Adding NYSE Stocks...')
    NYSE().create_stocks()
    logger.info('Added NYSE Stocks')


def create_lse_stocks():
    """ Creates all LSE listed stocks """
    logger.info('Adding LSE Stocks...')
    LSE().create_stocks()
    logger.info('Added LSE Stocks')


def create_all_exchange_stocks():
    """ Creates all exchange stocks """
    logger.info('Adding all exchange stocks...')
    create_nasdaq_stocks()
    create_nyse_stocks()
    create_lse_stocks()
    logger.info('Added all exchange stocks')


def seed_exchange_stocks_day_data(exchange_symbol):
    """ Creates all exchange Stocks day data """
    logger.info('Adding {} stocks day price data...'.format(exchange_symbol))
    bulk_get_exchanges_day_data(exchange_symbol)
    logger.info('Added {} stocks day price data'.format(exchange_symbol))


def seed_exchange_stocks_minute_data(exchange_symbol):
    """ Creates all exchange Stocks minute data """
    logger.info('Adding {} stocks minute price data...'.format(exchange_symbol))
    bulk_get_exchanges_minute_data(exchange_symbol)
    logger.info('Added {} stocks minute price data'.format(exchange_symbol))


def seed_exchange_stocks_data():
    exchanges = Exchange.objects.all()
    for exchange in exchanges:
        seed_exchange_stocks_day_data(exchange.symbol)
        # Not implementing stock minute data yet
        # seed_exchange_stocks_minute_data(exchange.symbol)


def refresh_exchange_stocks_day_data(exchange_symbol):
    logger.info('Refreshing {} stocks minute data'.format(exchange_symbol))
    get_exchanges_day_data(exchange_symbol)
    logger.info('Refreshed {} day data'.format(exchange_symbol))


def refresh_exchange_stocks_minute_data(exchange_symbol):
    logger.info('Refreshing {} stocks minute data'.format(exchange_symbol))
    get_exchanges_minute_data(exchange_symbol)
    logger.info('Refreshed {} minute data'.format(exchange_symbol))


def refresh_exchange_stocks_data():
    exchanges = Exchange.objects.all()
    for exchange in exchanges:
        refresh_exchange_stocks_day_data(exchange.symbol)
        # Not implementing stock minute data yet
        # refresh_exchange_stocks_minute_data(exchange.symbol)

