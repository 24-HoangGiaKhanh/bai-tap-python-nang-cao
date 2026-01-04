import xml.dom.minidom

def main():
    doc = xml.dom.minidom.parse("chuong2/cau3.xml")
    print(doc.nodeName)
    print(doc.firstChild.tagName)

if __name__ == '__main__': main()