from io import StringIO
from pathlib import Path

import httpx
import pandas as pd


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


class HandleRequestExoplanetArchive:
    def headers(self):
        headers = {
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
            "Accept": "*/*",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PS",
            "Accept-Language": "en-US,en;q=0.9",
            "Cookie": "ISIS=2021.06.11_00.53.06_007798",
        }
        return headers

    def query(self, post_start):
        query = [
            "log=TblView.ExoplanetArchive",
            "workspace=2021.06.11_00.53.06_007798%2FTblView%2F2021.06.23_10.28.28_004066",
            "table=/exodata/kvmexoweb/ExoTables/PS.tbl",
            "pltxaxis=",
            "pltyaxis=",
            "checkbox=1",
            "initialcheckedval=1",
            "splitlabel=0",
            "wsoverride=1",
            "rowLabel=rowlabel",
            "connector=true",
            "dhx_no_header=1",
            "count=250",
            "dhxr1624469339369=1",
        ]
        query.insert(-2, f"posStart={post_start}")
        query_string = "&".join(query)
        return query_string

    def url(self, post_start):
        domain = "https://exoplanetarchive.ipac.caltech.edu"
        path = "cgi-bin/IceTable/nph-iceTbl"
        url = f"{domain}/{path}?{self.query(post_start)}"
        return url

    def get(self, post_start):
        r = httpx.get(self.url(post_start), headers=self.headers())
        return r
