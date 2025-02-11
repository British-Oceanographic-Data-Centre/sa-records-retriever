"""
Retrieves - downloads via CSW calls - XML records from Blue Cloud

Currently downloads 150,000+ records.

"""

from owslib.csw import CatalogueServiceWeb
import lxml.etree as etree
from pathlib import Path


if __name__ == "__main__":
    url = "http://blue-cloud.geodab.eu/gs-service/services/essi/view/fair-ease/csw"

    csw = CatalogueServiceWeb(url, timeout=50)

    batch_size = 100
    offset = 0
    dir_size = 10000
    base_dir = Path("xml_files")
    dir_count = 1
    dir_name = base_dir / f"records_{str(dir_count).zfill(6)}"

    Path.mkdir(dir_name, exist_ok=True)
    rec_no = 0

    while True:
        print(f"starting at {offset}")

        csw.getrecords2(
            resulttype="results",
            startposition=offset,
            maxrecords=batch_size,
            esn="full",
            outputschema="http://www.isotc211.org/2005/gmd",  # "http://www.opengis.net/cat/csw/2.0.2",
        )
        if len(csw.records) == 0:
            print("No more records to process.")
            break
        batch_rec_counter = 0
        for x in csw.records:
            # print(csw.records[x].title)
            content = etree.fromstring(csw.records[x].xml)
            etree.indent(content, space="\t")

            # cater for file names with '/' in them
            if "/" in x:
                Path.mkdir(Path(dir_name) / Path(x.split("/")[0]), exist_ok=True)
            open(dir_name / f"{x}.xml", "w").write(
                etree.tostring(content, pretty_print=True).decode()
            )

            batch_rec_counter += 1
            rec_no = offset + batch_rec_counter
            print(f"written rec. no {rec_no}")

            if (offset + batch_rec_counter - 2) % dir_size == 0:
                dir_count += 1
                dir_name = base_dir / f"records_{str(dir_count).zfill(6)}"
                Path.mkdir(dir_name, exist_ok=True)

        offset = offset + batch_size
    print("Processing complete.")
