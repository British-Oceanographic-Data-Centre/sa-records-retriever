from owslib.csw import CatalogueServiceWeb
import lxml.etree as etree
from pathlib import Path


if __name__ == '__main__':
    url = "http://blue-cloud.geodab.eu/gs-service/services/essi/view/fair-ease/csw"

    csw = CatalogueServiceWeb(url, timeout=50)

    total_records = 156717
    batch_size = 100
    start = 0
    dir_size = 10000
    dir_prefix = "records_"
    dir_count = 0

    dir_name = dir_prefix + str(dir_count).zfill(6)
    Path.mkdir(dir_name, exist_ok=True)
    rec_no = 0

    for batch in range(start, total_records, batch_size):
        print(f"starting at {start}")

        csw.getrecords2(
            resulttype="results",
            startposition=start,
            maxrecords=batch_size,
            esn="full",
            outputschema="http://www.isotc211.org/2005/gmd",  # "http://www.opengis.net/cat/csw/2.0.2",
        )

        batch_rec_counter = 0
        for x in csw.records:
            # print(csw.records[x].title)
            content = etree.fromstring(csw.records[x].xml)
            etree.indent(content, space="\t")
            open(f"{dir_name}/{x}.xml", "w").write(etree.tostring(content, pretty_print=True).decode())

            batch_rec_counter += 1
            rec_no = start + batch_rec_counter
            print(f"written rec. no {rec_no}")

            if (start + batch_rec_counter - 2) % dir_size == 0:
                dir_count += 1
                dir_name = dir_prefix + str(dir_count).zfill(6)
                Path.mkdir(dir_name, exist_ok=True)

        print(f"processed records")
        print()

        start = start + batch_size

"""
C4FCB80C939B2B9DC3E9686BCDB67507780799C3
a0e3200f-e640-4521-b251-25c69d81e45e
7be513ae-5089-4c23-806f-9f420ddf1001
"""
