class Environments(dict):

    def return_environments(environment):

        # Data Dictionary of Environments
        environments={
            'Dev': 'https://svcdev.wn.nasinsurance.com/',
            'Demo1': 'https://svcdemo1.wn.nasinsurance.com/',
            'Demo2': 'https://svcdemo2.wn.nasinsurance.com/',
            'Demo3': 'https://svcdemo3.wn.nasinsurance.com/',
            'Demo4': 'https://svcdemo4.wn.nasinsurance.com/',
            'Demo5': 'https://svcdemo5.wn.nasinsurance.com/',
            'Demo6': 'https://svcdemo6.wn.nasinsurance.com/',
            'Demo7': 'https://svcdemo7.wn.nasinsurance.com/',
            'Demo8': 'https://svcdemo8.wn.nasinsurance.com/',
            'Demo9': 'https://svcdemo9.wn.nasinsurance.com/',
            'Fix': 'https://svcfix.wn.nasinsurance.com/',
            'Stage': 'https://svcrel.wn.nasinsurance.com/',
            'QA': 'https://svcqa.wn.nasinsurance.com/',
            'Cust_Demo3': 'https://custdemo3.wn.nasinsurance.com/index.php?c=program.welcome&id=19',
            'Live': 'https://service.wn.nasinsurance.com/'
            }
        return environments[environment]