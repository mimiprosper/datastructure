# dict with list
languages = {
    'onyedika' : ['java', 'c++', 'go'],
    'john' : ['php', 'ruby', 'c', 'dart'],
    'uche' : ['go', 'js', 'c#', 'java'],
    'tobe' : ['swift', 'solidity', 'c++', 'php', 'js'],
    'romeo' : ['c#', 'go', 'solidity']
}

for name, language in languages.items():
    print(name, end = ' : ')
    for lang in language:
        print(lang, end = ' ')
    print('')

#for name, language in languages.items():
    # get the names and first item in the list
    # print(name, language[0])

