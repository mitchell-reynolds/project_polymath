# Project Polymath
A project to synthesize & generate artwork. 

The first major exploration covers neural style transfer. 
Later explorations will range from GANs, Image Transformers and so on.

## QUICKSTART
```
touch .env

conda create --name polymath python=3.6.4
conda activate polymath
conda install -n polymath nb_conda_kernels
conda install -c conda-forge python-dotenv
pip install -r requirements.txt
```

## General Workflow 
Most Python Scripts will have this structure. 

```
import sys
import logging
import pandas as pd
from pathlib import Path
from dotenv import find_dotenv, load_dotenv

sys.path.append("..")
from data_connector import init_connection, read_sql


def _YOUR_FUNCTION_():
    """
    _YOUR_DECRIPTION_IN_ENGLISH_
    :return:

    """

    # Initialize connection into the MDW
    print("init connection")
    conn = init_connection()

    # Pull in the data with a relative path
    print("Pulling Data")
    _YOUR_SQL_ = read_sql("./sql/_YOUR_SQL_FILE.sql")
    _YOUR_DF_ = pd.read_sql_query(_YOUR_SQL_, conn)

    # Close the connection once finished
    conn.close()

    # _DO_OTHER_THINGS_

    return


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    _YOUR_FUNCTION_()

```
