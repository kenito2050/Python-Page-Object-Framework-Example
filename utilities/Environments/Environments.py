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
            'Stage': 'https://svcstg.wn.nasinsurance.com/',
            'Fix': 'https://svcfix.wn.nasinsurance.com/',
            'Old_Stage': 'https://svcrel.wn.nasinsurance.com/',
            'QA': 'https://svcqa.wn.nasinsurance.com/',
            'Cust_Live': 'https://customer.wn.nasinsurance.com/index.php?c=program.welcome&id=19',
            'Cust_Dev': 'https://custdev.wn.nasinsurance.com/index.php?c=program.welcome&id=19',
            'Cust_Demo3': 'https://custdemo3.wn.nasinsurance.com/index.php?c=program.welcome&id=19',
            'Cust_Demo4': 'https://custdemo4.wn.nasinsurance.com/index.php?c=program.welcome&id=19',
            'Cust_Demo6': 'https://custdemo6.wn.nasinsurance.com/index.php?c=program.welcome&id=19',
            'Cust_QA': 'https://custqa.wn.nasinsurance.com/index.php?c=program.welcome&id=19',
            'Cust_Fix': 'https://custfix.wn.nasinsurance.com/index.php?c=program.welcome&id=19',
            'Cust_Stage': 'https://custrel.wn.nasinsurance.com/index.php?c=program.welcome&id=19',
            'Cust_OS_Upgrade': 'https://custstg.wn.nasinsurance.com/index.php?c=program.welcome&id=19',
            'Retail_Access_Live': 'https://producer.wn.nasinsurance.com/registration',
            'Retail_Access_Stage': 'https://prodstg.wn.nasinsurance.com/registration',
            'Retail_Access_Demo7': 'https://proddemo7.wn.nasinsurance.com/registration',
            'Live': 'https://service.wn.nasinsurance.com/'
            }
        return environments[environment]