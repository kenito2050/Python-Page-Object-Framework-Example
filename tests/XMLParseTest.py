from utilities.contract_classes.contract_classes import ContractClasses
from xml.etree import ElementTree as ET

# TODO: NEED TO FIX SO THAT SCRIPT USES STRING VALUE CONTAINED IN contract_class variable
# Access XML to retrieve contract_class
tree = ET.parse('Contract_Classes.xml')
contract_classes_XML = tree.getroot()
contract_class = (contract_classes_XML[0][74].text)
contract_class_int_value = ContractClasses.return_contract_class_values(contract_class)


print (contract_class)
print (contract_class_int_value)

# tree = ET.parse('Resources.xml')
# root = tree.getroot()
#
# print (root[0][0].text)
# print (root[0][1].text)
# print (root[1][0].text)
# print (root[1][1].text)

#username = (root[0][0].text)
#password = (root[0][1].text)

#print (username, password)