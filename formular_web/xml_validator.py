from lxml import etree


def validateXML(file_name):
    xmlschema_doc = etree.parse('registration.xsd')
    xmlschema = etree.XMLSchema(xmlschema_doc)

    if ".xml" in file_name:
        xml_doc = etree.parse(file_name)
    else:
        xml_doc = etree.parse(file_name + ".xml")
    result = xmlschema.validate(xml_doc)

    return result

