from pathlib import Path
import pandas as pd
from io import StringIO


class HandleFile:
    table_init = 96
    number_columns = 92
    suffix = ".csv"

    def __init__(self, file):
        self.file = file
        self.string_io = StringIO(self.file.read().decode("utf-8"))

    def _dataframe(self):
        df = pd.read_csv(
            self.string_io,
            skiprows=self.table_init,
        )
        self.string_io.seek(0)
        return df

    def is_type_csv(self):
        return Path(self.file.name).suffix == self.suffix

    def structure_is_valid(self):
        return len(self._dataframe().columns) == self.number_columns

    def records(self):
        records = self._dataframe().to_dict("records")
        return records
