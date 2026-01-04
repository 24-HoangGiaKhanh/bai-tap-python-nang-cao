import xml.dom.minidom

def main():
    doc = xml.dom.minidom.parse("chuong2/cau3.xml")
    names = doc.getElementsByTagName('name')
    for name in names: print(name)

if __name__ == '__main__': main()