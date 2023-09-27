AccountNumbers = {
    
    "0120340000" : {
        'firstName' : 'john',
        'lastName' : 'ofor',
        'address' : 'orji rd',
        'accountType' : 'saving account',
        'accountBalance' : '200'
    },
    
    "0120350000" : {
        'firstName' : 'jane',
        'lastName' : 'stellar',
        'address' : 'royce rd',
        'accountType' : 'current account',
        'accountBalance' : '500'
    },
    
    "0120360000" : {
        'firstName' : 'chidi',
        'lastName' : 'udo',
        'address' : 'market rd',
        'accountType' : 'fixed deposit account',
        'accountBalance' : '10000'
    },
    
     "0120370000" : {
        'firstName' : 'chidi',
        'lastName' : 'okeke',
        'address' : 'market rd',
        'accountType' : 'savings account',
        'accountBalance' : '10000'
    },
     
     "0120390000" : {
        'firstName' : 'kelechi',
        'lastName' : 'chukwu',
        'address' : 'greg rd',
        'accountType' : 'current account',
        'accountBalance' : '10000000'
    },
     
}

for accountNumber, customer in AccountNumbers.items():
    print(accountNumber, customer['firstName'], customer['lastName'], customer['accountType'], 'has an account balance : ',  customer['accountBalance'])

