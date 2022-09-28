import mysql.connector

def connect():
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="hospital"
    )
    cur=conn.cursor()

    cur.execute("CREATE DATABASE IF NOT EXISTS hospital")
    cur.execute("CREATE TABLE IF NOT EXISTS Patients (uhid INTEGER PRIMARY KEY NOT NULL , name VARCHAR(50) NOT NULL, address VARCHAR(30) NOT NULL, phone_number VARCHAR(20) NOT NULL, Gender ENUM('Male','Female','Other') NOT NULL, Nurse_Assigned VARCHAR(20) NOT NULL,Attendent VARCHAR(20) NOT NULL, Date_of_admit Varchar(15),Date_of_departure VARCHAR(15), Status ENUM('Present','Left'))")
    cur.execute("CREATE TABLE IF NOT EXISTS Nurses ( name VARCHAR(50) NOT NULL, address VARCHAR(30) NOT NULL, phone_number VARCHAR(20) NOT NULL, Gender ENUM('Male','Female','Other') NOT NULL, Patient_Assigned VARCHAR(20) NOT NULL,Badge_Number INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT, Status ENUM('ACTIVE','NOT ACTIVE'))")
    cur.execute("CREATE TABLE IF NOT EXISTS doctors (name VARCHAR(50) NOT NULL,  address VARCHAR(30) NOT NULL, phone_number VARCHAR(20) NOT NULL, Gender ENUM('Male','Female','Other') NOT NULL, Speciality VARCHAR(20) NOT NULL,Badge_Number INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT, Status ENUM('ACTIVE','NOT ACTIVE'))")
    conn.commit()
    conn.close()
def insert(name,address,phone_number,Gender,Speciality,Badge_Number,Status):

    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="hospital"
    )
    cur=conn.cursor()
    insertperson = ("INSERT INTO doctors "
                "(name, address ,phone_number,Gender, Speciality , Badge_Number,Status) "
                "VALUES (%s,%s,%s,%s,%s,%s,%s)")
    data_user = (name, address, phone_number,Gender, Speciality, Badge_Number,Status)
    cur.execute(insertperson, data_user)

    conn.commit()
    conn.close()
    connect()
    view()

def view():
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="hospital"
    )
    cur=conn.cursor()
    cur.execute("SELECT * FROM doctors")
    row=cur.fetchall()
    conn.close()
    return row

def search(name="",address="",phone_number="",Speciality="",Gender="",Badge_Number="",Status=""):
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="hospital"
    )
    cur=conn.cursor()
    cur.execute("SELECT * FROM doctors WHERE name=%s OR address=%s OR phone_number=%s  OR  Speciality=%s  OR  Gender=%s  OR  Badge_Number=%s AND Status=%s",(name,address,phone_number,Speciality,Gender,Badge_Number,Status))
    row=cur.fetchall()
    conn.close()
    return row

def delete(Badge_Number):
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="hospital"
    )
    cur=conn.cursor()
    deleteuser=("DELETE FROM doctors WHERE Badge_Number=%s")
    deleteBadge_Number=(Badge_Number,)
    cur.execute(deleteuser,deleteBadge_Number)
    conn.commit()
    conn.close()

def update(name,address,phone_number,Speciality,Gender,Badge_Number,Status):

    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="hospital"
    )
    cur=conn.cursor()
    cur.execute("UPDATE doctors SET name=%s ,address=%s  , phone_number=%s  ,  Speciality=%s  , Gender=%s  , Status=%s  where Badge_Number=%s ",(name,address,phone_number,Speciality,Gender,Status,Badge_Number))
    conn.commit()
    conn.close()

def insertN(name,address,phone_number,Gender,Patient_Assigned,Badge_Number,Status):

    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="hospital"
    )
    cur=conn.cursor()
    insertperson = ("INSERT INTO Nurses "
                "(name, address ,phone_number,Gender, Patient_Assigned , Badge_Number,Status) "
                "VALUES (%s,%s,%s,%s,%s,%s,%s)")
    data_user = (name, address, phone_number,Gender, Patient_Assigned, Badge_Number,Status)
    cur.execute(insertperson, data_user)

    conn.commit()
    conn.close()
    viewN()

def viewN():
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="hospital"
    )
    cur=conn.cursor()
    cur.execute("SELECT * FROM Nurses")
    row=cur.fetchall()
    conn.close()
    return row

def searchN(name="",address="",phone_number="",Patient_Assigned="",Gender="",Badge_Number="",Status=""):
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="hospital"
    )
    cur=conn.cursor()
    cur.execute("SELECT * FROM Nurses WHERE name=%s OR address=%s OR phone_number=%s  OR  Patient_Assigned=%s  OR  Gender=%s  OR  Badge_Number=%s AND Status=%s",(name,address,phone_number,Patient_Assigned,Gender,Badge_Number,Status))
    row=cur.fetchall()
    conn.close()
    return row

def deleteN(Badge_Number):
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="hospital"
    )
    cur=conn.cursor()
    deleteuser=("DELETE FROM Nurses WHERE Badge_Number=%s")
    deleteBadge_Number=(Badge_Number,)
    cur.execute(deleteuser,deleteBadge_Number)
    conn.commit()
    conn.close()

def updateN(name,address,phone_number,Patient_Assigned,Gender,Badge_Number,Status):

    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="hospital"
    )
    cur=conn.cursor()
    cur.execute("UPDATE Nurses SET name=%s ,address=%s  , phone_number=%s  ,  Patient_Assigned=%s  , Gender=%s  , Status=%s  where Badge_Number=%s ",(name,address,phone_number,Patient_Assigned,Gender,Status,Badge_Number))
    conn.commit()
    conn.close()

def insertP(uhid,name,address,phone_number,Nurse_Assigned,Attendent,Gender,Date_of_admit,Date_of_departure,Status):

    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="hospital"
    )
    cur=conn.cursor()
    insertperson = ("INSERT INTO Patients "
                "(uhid ,name, address ,phone_number,Gender, Nurse_Assigned,Attendent,Date_of_admit,Date_of_departure,Status) "
                "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    data_user = (uhid,name, address, phone_number,Gender, Nurse_Assigned,Attendent,Date_of_admit,Date_of_departure,Status)
    cur.execute(insertperson, data_user)

    conn.commit()
    conn.close()
    viewP()

def viewP():
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="hospital"
    )
    cur=conn.cursor()
    cur.execute("SELECT * FROM Patients")
    row=cur.fetchall()
    conn.close()
    return row

def searchP(uhid="",name="",address="",phone_number="",Nurse_Assigned="",Attendent="",Gender="",Date_of_admit="",Date_of_departure="",Status=""):
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="hospital"
    )
    cur=conn.cursor()
    cur.execute("SELECT * FROM Patients WHERE uhid=%s OR name=%s OR address=%s OR phone_number=%s  OR  Nurse_Assigned=%s OR Attendent=%s  OR  Gender=%s  OR Date_of_admit=%s OR Date_of_departure=%s AND Status=%s",(uhid,name,address,phone_number,Nurse_Assigned,Attendent,Gender,Date_of_admit,Date_of_departure,Status))
    row=cur.fetchall()
    conn.close()
    return row

def deleteP(uhid):
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="hospital"
    )
    cur=conn.cursor()
    deleteuser=("DELETE FROM Patients WHERE uhid=%s")
    deleteuhid=(uhid,)
    cur.execute(deleteuser,deleteuhid)
    conn.commit()
    conn.close()

def updateP(uhid,name,address,phone_number,Nurse_Assigned,Attendent,Gender,Date_of_admit,Date_of_departure,Status):

    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="hospital"
    )
    cur=conn.cursor()
    cur.execute("UPDATE Patients SET name=%s ,address=%s  , phone_number=%s  ,  Nurse_Assigned=%s,Attendent=%s  , Gender=%s  ,Date_of_admit=%s,Date_of_departure=%s, Status=%s  where uhid=%s ",(name,address,phone_number,Nurse_Assigned,Attendent,Gender,Date_of_admit,Date_of_departure,Status,uhid))
    conn.commit()
    conn.close()




connect()