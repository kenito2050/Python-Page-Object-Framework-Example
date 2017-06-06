class ContractClasses_Medical(dict):

    def return_contract_class_values(contract_class):

        # Data Dictionary of Contract Classes
        contract_class_values={
        'Medical Group': '1',
        'Office of Physician': '2',
        }
        return contract_class_values[contract_class]