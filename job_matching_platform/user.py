from mysql.connector import connect

try:
    mydb = connect(
        host="localhost",
        user="root",
        password="root"
    )
except:
    print("cant connect")

finally:
    cur = mydb.cursor()
    cur.execute("USE JOB_MATCHING_PLATFORM")

class user:
    def __init__(self, name, idx):
        self.name = name
        self.idx = idx

    def getId(self):
        return self.idx

    def getName(self):
        return self.name

    def addCourse(self, id, name, hrs):
        data = (id, name, hrs)
        query = "INSERT INTO COURSES(ID, coursename, coursehours) VALUES(%s, %s, %s)"
        print(data)
        cur.execute(query, data)
        mydb.commit()
        print("course has been added")

    def getCourse(self, id):
        query = f"SELECT * FROM COURSES WHERE ID={id}"
        cur.execute(query)
        data = cur.fetchall()
        print(data)

    def getSkills(self, id):
        query = f"SELECT * FROM SKILLS WHERE ID={id}"
        cur.execute(query)
        data = cur.fetchall()
        print(data)
    def addSkills(self, id, skill_name):
        data = (id, skill_name)
        query = "INSERT INTO SKILLS(ID, skillname) VALUES(%s, %s)"
        cur.execute(query, data)
        mydb.commit()
        print("skills has been added")

    def addUser(self, password):
        query = "INSERT INTO USER(ID, name, password) VALUES(%s, %s, %s)"
        data = (self.idx, self.name, password)
        cur.execute(query, data)
        mydb.commit()
        print("user added")

    def deleteCourse(self, id, name):
        query = f"DELETE FROM COURSES WHERE ID='{id}' AND coursename='{name}'"
        cur.execute(query)
        mydb.commit()
        print("deleted")

    def checkUser(self, idx, password):
        query = f"SELECT * FROM USER WHERE ID='{id}' AND password='{password}'"
        cur.execute(query)
        data = cur.fetchall()
        if(len(data) == 0):
            return False
        else:
            return True




class Employer:
    def __init__(self, name, id):
        self.name = name
        self.idx = id
        self.preferred_skills = []

    def addEmployer(self, id, name, password):
        query = "INSERT INTO EMPLOYER(EMPID, name, password) VALUES(%s, %s, %s)"
        data = (id, name, password)
        cur.execute(query, data)
        mydb.commit()
        print("Employee added")


    def getPreferredSills(self, data):
        if data == 'course':
            query = f"SELECT * FROM COURSES WHERE coursename='{data}'"
            cur.execute(query)
            data = cur.fetchall()
            if len(data) > 0:
                for index, val in enumerate(data):
                    print(f"{index}: {val}")
            else:
                print("no user")

        else:
            query = f"SELECT * FROM SKILLS WHERE skillname='{data}'"
            cur.execute(query)
            data = cur.fetchall()
            if len(data) > 0:
                for index, val in enumerate(data):
                    print(f"{index}: {val}")
            else:
                print("no user")

    def addUser(self, id, name):
        id = int(input("Enter the id of the candidate"))
        name = input("Enter name")
        data = (id, name)
        query = "INSERT INTO SELECTED(ID, name) VALUES(%s, %s)"
        cur.execute(query, data)
        mydb.commit()
        print("Inserted into selected table")

    def checkUser(self, id, password):
        query = f"SELECT * FROM EMPLOYER WHERE EMPID='{id}' AND password='{password}'"
        cur.execute(query)
        data = cur.fetchall()
        if(len(data) == 0):
            return False
        else:
            return True

print("Enter 1 for user\n2 for employee")
c1 = int(input("Enter above choice"))

if c1 == 1:
    print("Enter 1 for 1st time user and 2 for regular user")
n = int(input())
if n == 1:
    name = input("Enter name:")
    id = int(input("Enter id"))
    password = input("Enter password")
    user1 = user(name, id)
    user1.addUser(password)
elif n == 2:
    name = input("Enter name")
    id = input("Enter id")
    password = input("Enter password")
    user1 = user(id, password)
    if user1.checkUser(id, password):
        #user exists
        print("Enter 1 to add course")
        print("Enter 2 to add skills")
        print("Enter 3 to fetch all registered courses")
        print("Enter 4 to delete a course")
        n = int(input("Enter above choice:"))
        c = ['java', 'c', 'c++', 'python', 'ML']
        if n == 1:
            print("choose from ", end="")
            for i, j in enumerate(c):
                print(f"{i+1} : {j}")
            choose = int(input("choose above choice:"))
            if len(c) >= choose > 0:
                user1.addCourse(id, c[choose-1], 40)
            else:
                print("not valid")

        elif n == 2:
            skill = input("Enter the skill")
            user1.addSkills(id, skill)

        elif n == 3:
            user1.getCourse(id)

        elif n == 4:
            print("1 to delete java\n2 to delete c\n3 to delete c++\n 4 to delete python")
            ch = int(input("enter above choice:"))
            user1.deleteCourse(id, c[ch-1])

    else:
        print("not a user")

else:
    ch = int(input("Enter the 1 for 1st time Employee\n2 for 2nd time Employee"))
    if ch == 1:
        id = int(input("Enter id"))
        name = input("Enter name")
        password = input("Enter password")
        emp = Employer(id, name)
        emp.addUser(id, name, password)
        emp.getPreferredSills('java')



