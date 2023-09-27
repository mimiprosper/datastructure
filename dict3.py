# nested dict --> dict inside a dict

students = {

    '01A90X': {
    'firstName' : 'Victor',
    'lastName' : "Uzoma",
    "address" : 'orji rd'
    },

    '02B80Y': {
    'firstName' : 'Ada',
    'lastName' : "Nma",
    "address" : 'Akwa rd'
    },

     '03C70Z': {
    'firstName' : 'ijeome',
    'lastName' : "okeke",
    "address" : 'whetheral rd'
    }
    
}

for studentID, student in students.items():
    print(studentID, student['firstName'], student['lastName'], 'location is', student['address'])
    