class ContractClasses_Medical(dict):

    def return_contract_class_values(contract_class):

        # Data Dictionary of Contract Classes
        contract_class_values={
        'Healthcare Facilities': '1',
        'Medical Group': '2',
        'Office of Physician': '3',
        'Offices of Dentists': '4',
        }
        return contract_class_values[contract_class]