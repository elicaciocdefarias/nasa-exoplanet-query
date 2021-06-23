import aiohttp
import asyncio


class Main:
    async def run(self):
        async with aiohttp.ClientSession() as session:
            params = [
                ("log", "TblView.ExoplanetArchive"),
                (
                    "workspace",
                    "2021.06.11_00.53.06_007798%2FTblView%2F2021.06.23_10.28.28_004066",
                ),
                ("table", "/exodata/kvmexoweb/ExoTables/PS.tbl"),
                ("pltxaxis", ""),
                ("pltyaxis", ""),
                ("checkbox", "1"),
                ("initialcheckedval", "1"),
                ("splitlabel", "0"),
                ("wsoverride", "1"),
                ("rowLabel", "rowlabel"),
                ("connector", "true"),
                ("dhx_no_header", "1"),
                ("posStart", "112"),
                ("count", "250"),
                ("dhxr1624469339369", "1"),
            ]
            url = (
                "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/IceTable/nph-iceTbl"
            )
            async with session.get(url, params=params) as response:
                r = response.text
                print(r)

    async def __call__(self):
        return await self.run()


def cli():
    main = Main()
    asyncio.run(main())
