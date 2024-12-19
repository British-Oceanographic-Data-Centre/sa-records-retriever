# this script moves XML records from a given directory - FROM-DIR -
# selected by a simple text match in it - PHRASE -
# and places them into another directory - TO_DIR

from pathlib import Path
from lxml import etree
from utils import NAMESPACES, NAMESPACES_19139

namespaces = {**NAMESPACES, **NAMESPACES_19139}


RECORDS_DIR = Path("/home/nick/work/bodc/sa-records/")
FROM_DIRS = [
    RECORDS_DIR / "records" / "records_000000",
    RECORDS_DIR / "records" / "records_000001",
    RECORDS_DIR / "records" / "records_000002",
    RECORDS_DIR / "records" / "records_000003",
    RECORDS_DIR / "records" / "records_000004",
    RECORDS_DIR / "records" / "records_000005",
    RECORDS_DIR / "records" / "records_000006",
    RECORDS_DIR / "records" / "records_000007",
    RECORDS_DIR / "records" / "records_000008",
    RECORDS_DIR / "records" / "records_000009",
    RECORDS_DIR / "records" / "records_000010",
    RECORDS_DIR / "records" / "records_000011",
    RECORDS_DIR / "records" / "records_000012",
    RECORDS_DIR / "records" / "records_000013",
    RECORDS_DIR / "records" / "records_000014",
    RECORDS_DIR / "records" / "records_000015",
    RECORDS_DIR / "records" / "records_000016",
    RECORDS_DIR / "records" / "records_000017",
    RECORDS_DIR / "records" / "records_000018",
    RECORDS_DIR / "capital",
    RECORDS_DIR / "ifremer",
    RECORDS_DIR / "paleoclimatolog",

]

TO_DIR = Path(RECORDS_DIR / "paleoclimatolog")


# <gco:CharacterString>ARGO</gco:CharacterString
# <gco:CharacterString>CMEMS</gco:CharacterString>
# <gco:CharacterString>AOML</gco:CharacterString>
# <gco:CharacterString>CSIO</gco:CharacterString>
# <gco:CharacterString>NOAA/PMEL</gco:CharacterString>
# <gco:CharacterString>NOAA National Centers for Environmental Information</gco:CharacterString>
# <gco:CharacterString>EMODnet Chemistry </gco:CharacterString>
# <gco:CharacterString>JAMSTEC</gco:CharacterString>
# <gco:CharacterString>VITO NV</gco:CharacterString>
# <gco:CharacterString>NASA Goddard Space Flight Center, Earth Science Data and Information System</gco:CharacterString>
# <gco:CharacterString>Geological Survey Ireland</gco:CharacterString>

i = 0
j = 0
for dir in FROM_DIRS:
    print(dir)
    for record in dir.glob("**/*.xml"):
        print(record)

        # # NEMO Floats
        # txt = record.read_text()
        # if "NEMO Profiling Float - " in txt:
        #     i += 1
        #     print(f"Moved {i}")
        #     record.rename(Path(RECORDS_DIR / "nemo") / record.name)

        # # APEX Floats
        # txt = record.read_text()
        # if "APEX Profiling Float - " in txt:
        #     record.rename(Path(RECORDS_DIR / "apex") / record.name)

        # # Party email matching
        # et = etree.parse(record)
        # party_email = et.xpath(
        #     f"//gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:onlineResource/gmd:CI_OnlineResource/gmd:linkage/gmd:URL/text()",
        #     namespaces=namespaces,
        # )
        #
        # if len(party_email) > 0:
        #     print(party_email[0])
        #     if party_email[0] == "http://marine.copernicus.eu/":
        #         i += 1
        #         record.rename(Path(RECORDS_DIR / "cmems") / record.name)
        #         print(f"moved: {i} CMEMS")
        #     elif party_email[0] == "https://land.copernicus.eu/global/":
        #         j += 1
        #         record.rename(Path(RECORDS_DIR / "cmems-non") / record.name)
        #         print(f"moved: {j} non-CMEMS")

        # # Title matching
        # et = etree.parse(record)
        # title = et.xpath(
        #     f"//gmd:title/gco:CharacterString/text()",
        #     namespaces=namespaces,
        # )
        # if len(title) > 0:
        #     if title[0].startswith("NOAA/WDS Paleoclimatolog"):
        #         i += 1
        #         record.rename(TO_DIR / record.name)
        #         print(f"moved: {i}")

        # # Uppper case file name
        # for l in str(record.name):
        #   if l.isupper():
        #       record.rename(TO_DIR / record.name)
        #       print(f"moved: {i}")
        #       break


"""
Title starts with 'NOAA/WDS Paleoclimatolog' --> paleoclimatlog/
"""