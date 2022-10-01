from lxml import etree


def generateHTML(xml, xslt):
    xslt_doc = etree.parse(xslt)
    xslt_transformer = etree.XSLT(xslt_doc)

    source_doc = etree.parse(xml)
    output_doc = xslt_transformer(source_doc)

    output_doc.write("templates/generated_HTML.html", pretty_print=True)

