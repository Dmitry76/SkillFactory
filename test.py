# ДЛЯ ЧИСЛОВЫХ ЗНАЧЕНИЙ
import pandas as pd
football = pd.read_csv("c:\ОБМЕН\data_sf.csv")
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(football[football.Age>35][["Name", "Age", "Club", "Wage"]].describe())