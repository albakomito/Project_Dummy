#Imports
import pandas as pd
import os
import streamlit as st
import numpy as np
import datetime as dt
from twelvedata import TDClient
from opensea import OpenseaAPI
from opensea import utils
from MCForecastTools import MCSimulation


#All Functions


#Opensea API Key
opensea_api = OpenseaAPI(apikey="7913a9c0377249d2998900d7ce6d38b3")

#Twelve Data API Key
td = TDClient(apikey="d1d0c43b0fb445518d1435c2b90c9cdc") 

#Cryptocurrency DF Function
def create_ts(user_inputc, td):
        ts = td.time_series(
            symbol = user_inputc,
            exchange = "Binance",
            interval = '1day',
            outputsize=5000,
            start_date = '2017-12-31',
            end_date = '2022-03-31',
            timezone="America/New_York",
            )
        crypto_df = ts.as_pandas().sort_index()
        crypto_df = crypto_df.round(2)
        return crypto_df



#NFT DF Function
def pull_nft_stats(user_input, opensea_api):
    contract = opensea_api.contract(asset_contract_address = user_input)
    name = contract['collection']['slug']
    nft_stats = opensea_api.collection_stats(collection_slug = name)
    nft_stats_df = pd.DataFrame.from_dict(nft_stats)
    nft_stats_df = nft_stats_df[['stats']].round(decimals = 2)
    return(nft_stats_df)

#NFT Socials Function
def get_socials(name, telegram, twitter, instagram, discord, website):
    st.subheader(f'{name} Socials')
    st.write(f'Website: {website}')
    st.write(f'Discord: {discord}')
    st.write(f'Twitter: {twitter}')
    st.write(f'Telegram: {telegram}')
    st.write(f'Instagram: {instagram}')      




#Cryptocurrency Library

#BTC DataFrame
btc = td.time_series(
        symbol = 'BTC/USD',
        exchange = "Binance",
        interval = '1day',
        outputsize=5000,
        start_date = '2017-12-31',
        end_date = '2022-03-31',
        timezone="America/New_York",
        )
btc_df = btc.as_pandas().sort_index()
btc_df = btc_df.round(2)
        
    #ETH DataFrame
eth = td.time_series(
        symbol = 'ETH/USD',
        exchange = "Binance",
        interval = '1day',
        outputsize=5000,
        start_date = '2017-12-31',
        end_date = '2022-03-31',
        timezone="America/New_York",
        )
eth_df = eth.as_pandas().sort_index()
eth_df = eth_df.round(2)

#XRP DataFrame
xrp = td.time_series(
        symbol = 'XRP/USD',
        exchange = "Binance",
        interval = '1day',
        outputsize=5000,
        start_date = '2017-12-31',
        end_date = '2022-03-31',
        timezone="America/New_York",
        )
xrp_df = xrp.as_pandas().sort_index()
xrp_df = xrp_df.round(2)

#BNB DataFrame
bnb = td.time_series(
        symbol = 'BNB/USD',
        exchange = "Binance",
        interval = '1day',
        outputsize=5000,
        start_date = '2017-12-31',
        end_date = '2022-03-31',
        timezone="America/New_York",
        )
bnb_df = bnb.as_pandas().sort_index()
bnb_df = bnb_df.round(2)

#SOL DataFrame
sol = td.time_series(
        symbol = 'SOL/USD',
        exchange = "Binance",
        interval = '1day',
        outputsize=5000,
        start_date = '2017-12-31',
        end_date = '2022-03-31',
        timezone="America/New_York",
        )
sol_df = sol.as_pandas().sort_index()
sol_df = sol_df.round(2)

#ADA DataFrame
ada = td.time_series(
        symbol = 'ADA/USD',
        exchange = "Binance",
        interval = '1day',
        outputsize=5000,
        start_date = '2017-12-31',
        end_date = '2022-03-31',
        timezone="America/New_York",
        )
ada_df = ada.as_pandas().sort_index()
ada_df = ada_df.round(2)

#LUNA DataFrame
luna = td.time_series(
        symbol = 'LUNAt/USD',
        exchange = "Binance",
        interval = '1day',
        outputsize=5000,
        start_date = '2017-12-31',
        end_date = '2022-03-31',
        timezone="America/New_York",
        )
luna_df = luna.as_pandas().sort_index()
luna_df = luna_df.round(2)

