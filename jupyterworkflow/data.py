import os
import pandas as pd
from urllib.request import urlretrieve

FREMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_fremont_data(filename='Fremont.csv', url=FREMONT_URL, force_download=False):
    
    """Download and cache the Fremont data
    
    Parameters
    ----------
    filename: string (optional)
        Location to save the data
    url: strint (optional)
        Web location of the data
    force_download: bool (optional)
        if True, force redownload of the data
        
    Returns
    -------
    data: pandas.DataFrame
        Fremont bridge bike data downloaded from seattle.gov website
    """
    if force_download or not os.path.exists(filename):
        urlretrieve(url, 'Fremont.csv')
    data = pd.read_csv('Fremont.csv', index_col='Date')
    
    try:
        data.index = pd.to_datetime(data.index, format='%m/%d/%Y %H:%M:%S %p')
    except TypeError:
        data.index = pd.to_datetime(data.index)
    
    # Rename columns to reduce verbosity
    data.columns = ['East', 'West']
    # Calculate total bike rides as a sum of both column entries
    data['Total'] = data['West'] + data['East']

    return data