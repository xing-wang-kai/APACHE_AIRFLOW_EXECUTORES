import yfinance

from airflow.decorators import dag, task
from airflow.macros import ds_add
from pathlib import Path
import pendulum

TICKERS = [
    "BTC",
    "ETH",
    "DOGE",
    "AVAX"
]


@task()
def get_history(ticker, ds=None, ds_nodash=None):
    
    file_path = f'/home/kaiwang/Documents/airflow_celeby/datalake/BRONZE/CRIPTO/{ticker}/{ticker}_{ds_nodash}.csv'
    
    (Path(file_path).parent).mkdir(parents=True, exist_ok=True)
    
    yfinance.Ticker(ticker).history(
                period = "1d",
                interval = '1h',
                start=ds_add(ds, -3),
                end=ds,
                prepost=True
            ).to_csv(file_path)


@dag(
    dag_id='BRONZER_GET_CRIPTOS',
    start_date = pendulum.datetime(2024, 8, 1, tz="UTC"),
    schedule_interval="0 0 * * 2-6"
)
def get_stoncks():
    
    for ticker in TICKERS:
        get_history.override(
            task_id=f"BRONZE_CRIPTO_{ticker}",
        )(ticker)
        
dag = get_stoncks()