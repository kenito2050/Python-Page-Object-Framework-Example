class Environments(dict):

    def return_environments(environment):

        # Data Dictionary of Environments
        environments={
            'Dev': 'https://svcdev.wn.nasinsurance.com/',
            'Demo1': 'https://svcdemo1.wn.nasinsurance.com/',
            'ProdDemo1': 'https://proddemo1.wn.nasinsurance.com/',
            'Demo2': 'https://svcdemo2.wn.nasinsurance.com/',
            'ProdDemo2': 'https://proddemo2.wn.nasinsurance.com/',
            'Demo3': 'https://svcdemo3.wn.nasinsurance.com/',
            'ProdDemo3': 'https://proddemo3.wn.nasinsurance.com/',
            'Demo4': 'https://svcdemo4.wn.nasinsurance.com/',
            'ProdDemo4': 'https://proddemo4.wn.nasinsurance.com/',
            'Demo5': 'https://svcdemo5.wn.nasinsurance.com/',
            'ProdDemo5': 'https://proddemo5.wn.nasinsurance.com/',
            'Demo6': 'https://svcdemo6.wn.nasinsurance.com/',
            'ProdDemo6': 'https://proddemo6.wn.nasinsurance.com/',
            'Demo7': 'https://svcdemo7.wn.nasinsurance.com/',
            'ProdDemo7': 'https://proddemo7.wn.nasinsurance.com/',
            'Demo8': 'https://svcdemo8.wn.nasinsurance.com/',
            'ProdDemo8': 'https://proddemo8.wn.nasinsurance.com/',
            'Demo9': 'https://svcdemo9.wn.nasinsurance.com/',
            'ProdDemo9': 'https://proddemo9.wn.nasinsurance.com/',
            'Stage': 'https://svcstg.wn.nasinsurance.com/',
            'ProdStage': 'https://prodstg.wn.nasinsurance.com/',
            'Fix': 'https://svcfix.wn.nasinsurance.com/',
            'ProdFix': 'https://prodfix.wn.nasinsurance.com/',
            'QA': 'https://svcqa.wn.nasinsurance.com/',
            'Cust_Live': 'https://customer.wn.nasinsurance.com/index.php?c=program.welcome&id=19',
            'Cust_Dev': 'https://custdev.wn.nasinsurance.com/index.php?c=program.welcome&id=19',
            'Cust_Demo3': 'https://custdemo3.wn.nasinsurance.com/index.php?c=program.welcome&id=19',
            'Cust_Demo4': 'https://custdemo4.wn.nasinsurance.com/index.php?c=program.welcome&id=19',
            'Cust_Demo6': 'https://custdemo6.wn.nasinsurance.com/index.php?c=program.welcome&id=19',
            'Cust_QA': 'https://custqa.wn.nasinsurance.com/index.php?c=program.welcome&id=19',
            'Cust_Fix': 'https://custfix.wn.nasinsurance.com/index.php?c=program.welcome&id=19',
            'Cust_Stage': 'https://custstg.wn.nasinsurance.com/index.php?c=program.welcome&id=19',
            'Cust_OS_Upgrade': 'https://custstg.wn.nasinsurance.com/index.php?c=program.welcome&id=19',
            'Retail_Access_Live': 'https://producer.wn.nasinsurance.com/registration',
            'Retail_Access_Stage': 'https://prodstg.wn.nasinsurance.com/registration',
            'Retail_Access_Demo1': 'https://proddemo1.wn.nasinsurance.com/registration',
            'Retail_Access_Demo7': 'https://proddemo7.wn.nasinsurance.com/registration',
            'Live': 'https://service.wn.nasinsurance.com/',
            'ProdLive': 'https://producer.wn.nasinsurance.com/'
            }
        return environments[environment]