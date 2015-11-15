import sqlite3

mydir = "C:/pythonplay/"

class Course(object):
    def __init__(self, name, credit=0, prof=None):
        self.name, self.credit, self.prof = name,credit,prof

    def __repr__(self):
        return "Course '%s' %d credits by '%s'"%(self.name,self.credit,self.prof)

    def courseConverter(obj):
        return "%s:%s:%s"%(obj.name,obj.credit,obj.prof)


class CoursesDB:
    def __init__(self, loc = ":memory:"):
        self.con = sqlite3.connect(loc)
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS course(name text, credits int, professor text, primary key(name));")

    def insertCourse(self, name, credits=None, profName=None):
        c = self.cur
        try:
            c.execute("INSERT INTO course VALUES(?,?,?);",(name,credits,profName));
        except sqlite3.Error as e:
            print("Error :",e.args[0])
        else:
            print("Inserted")

    def deleteCourse(self, name):
        c = self.cur
        try:
            c.execute("DELETE FROM course WHERE name=?;", (name,));
        except sqlite3.Error as e:
            print("Error :", e.args[0])
        else:
            print("Deleted")

    def printAll(self):
        c = self.cur
        try:
            c.execute("SELECT * FROM course;")
            result = c.fetchall()
            for line in result:
                print(line)
        except sqlite3.Error as e:
            print("Error :", e.args[0])

def main():
    myDB = CoursesDB()
    myDB.insertCourse('Database', 3, 'Sang-gu Lee')
    myDB.insertCourse('Compiler', 3, 'Soo-Muk Moon')
    myDB.insertCourse('Analog')
    myDB.printAll()
            
if __name__=='__main__':
    main()