# this script deduplicates multiple, identical peer keywords

from lxml import etree

from pathlib import Path
from utils import NAMESPACES, NAMESPACES_19139

RECORDS_DIR = Path("xml_files/")


if __name__ == "__main__":
    for f in RECORDS_DIR.glob("records*/*.xml"):
        print(f)
        et = etree.parse(f)
        keywords = et.xpath(
            "//gmd:descriptiveKeywords/gmd:MD_Keywords/gmd:keyword",
            namespaces={**NAMESPACES, **NAMESPACES_19139},
        )
        print(f"kw no. orig: {len(keywords)}")
        kw_cache = set()
        for keyword in keywords:
            if len(keyword.getchildren()) == 0:
                continue
            this_kw_text = keyword.getchildren()[0].text
            if this_kw_text in kw_cache:
                keyword.getparent().remove(keyword)
            kw_cache.add(this_kw_text)

        keywords = et.xpath(
            "//gmd:descriptiveKeywords/gmd:MD_Keywords/gmd:keyword",
            namespaces={**NAMESPACES, **NAMESPACES_19139},
        )
        print(f"kw no. reduc: {len(keywords)}")

        # replace the original
        Path.unlink(f)
        et.write(f, pretty_print=True)
