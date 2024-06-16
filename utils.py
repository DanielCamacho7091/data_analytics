import os
import json
import pandas as pd

def import_kaggle_data(dataset_path, kaggle_json_path):

    # Carga las credenciales desde el archivo kaggle.json
    with open(kaggle_json_path, 'r') as file:
        kaggle_credentials = json.load(file)

    os.environ['KAGGLE_USERNAME'] = kaggle_credentials['username']
    os.environ['KAGGLE_KEY'] = kaggle_credentials['key']

    from kaggle.api.kaggle_api_extended import KaggleApi

    # Autentica con Kaggle
    api = KaggleApi()
    api.authenticate()

    # Descarga el dataset
    api.dataset_download_files(dataset_path, path='./data', unzip=True)

    message = 'Datos descargados con éxito por medio de la API de Kaggle'
    print(message)

    # Leer data
    df = pd.read_csv('data/energy_dataset_.csv')

    return df
