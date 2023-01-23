str = input("enter code: ")

graduation = {
            'uq': "MCA",
            'ub': "MBA",
            'ue': "B-TECH"
}
year = {
             '19': '2019',
             '20': '2020',
             '21': '2021'
}
course = {
             'ca': 'COMPUTER APPLICATIONS',
             'ca6': 'MCA',
             'ca4': 'BCA'
         }
degree = {
    '4': 'UG',
    '6': 'PG'
}
eveodd = {
    'a': "even",
    'b': "odd"
}

print(f"{str[8:9].lower()}st subject in {course[str[4:6].lower()]} Branch {eveodd[str[9:10].lower()]} semester {degree[str[7:8].lower()]} course with {str[8:9].lower()} credits initroduced in {year[str[2:4].lower()]}")



