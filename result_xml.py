import xml.etree.ElementTree as ET


def search_in_xml(file_path, group=None, number=None):

    tree = ET.parse('groups.xml')
    root = tree.getroot()


    results = []

    for record in root.findall('record'):
        record_group = record.find('group').text if record.find('group') is not None else None
        record_number = record.find('number').text if record.find('number') is not None else None

        # Перевірка на відповідність
        if (group is None or record_group == group) and (number is None or record_number == str(number)):
            results.append(record)

    return results


file_path = "data.xml"
results = search_in_xml(file_path, group="A", number=3)

# Вивід результатів
for record in results:
    print(ET.tostring(record, encoding='unicode'))
