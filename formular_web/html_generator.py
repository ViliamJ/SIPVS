from lxml import etree


def generateHTML(xml, xslt):
    xslt_doc = etree.parse(xslt)
    xslt_transformer = etree.XSLT(xslt_doc)

    source_doc = etree.parse(xml)
    output_doc = xslt_transformer(source_doc)

    xml_file = "default.html"
    if ".xml" in xml:
        xml_file = xml.split(".")[0]

    new_file_name = xml_file + ".html"
    output_doc.write(f"templates/{new_file_name}", pretty_print=True)

    return new_file_name

