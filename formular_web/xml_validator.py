from lxml import etree


def validateXML():
    xmlschema_doc = etree.parse('registration.xsd')
    xmlschema = etree.XMLSchema(xmlschema_doc)

    xml_doc = etree.parse('registration.xml')
    result = xmlschema.validate(xml_doc)

    return result

