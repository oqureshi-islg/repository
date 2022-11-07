#!/usr/bin/env python

import numpy as np
import pandas as pd


def load_df(file_path, file_name):    # read in data file

    df = pd.read_csv(file_path, engine='python')

    return df


def drop_columns(df, drop_cols, file_name, logger=None):

    for col in drop_cols:
        if col in df.columns:
            df = df.drop(col, axis=1)
            
    return df

