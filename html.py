from lxml import etree


def to_etree(html_file):
    try:
        return etree.HTML(html_file)
    except:
        return None