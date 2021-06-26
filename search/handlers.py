from pathlib import PurePath
import pandas as pd
from dynaconf import settings
from typing import Union


class HandleExoplanetArchive:
    def __init__(self):
        self.file = (
            PurePath(settings.BASE_DIR)
            .joinpath("search")
            .joinpath("data")
            .joinpath("exoplanets.csv")
        )
        self.dataframe: Union[pd.DataFrame, None] = None

    def read(self):
        self.dataframe = pd.read_csv(self.file, skiprows=96)
        return self

    def normalize(self):
        for column in self.dataframe.columns:
            if self.dataframe[column].dtype == "object":
                self.dataframe[column] = self.dataframe[column].fillna("")
            else:
                self.dataframe[column] = self.dataframe[column].fillna(0)
        return self

    def records(self):
        records = self.dataframe.to_dict("records")
        return records
