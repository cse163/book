from lxml import etree


def main():
    root = etree.parse("lesson.xml")

    transform = etree.XSLT(etree.parse("edstem.xsl"))

    result = transform(root)
    result.write_output("book_source/source/out.rst")


if __name__ == "__main__":
    main()
