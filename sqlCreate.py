import sqlite3 as sql

class Database:
    def __init__(self,db):
        self.conn=sql.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Etudiant (
            idEtudiant  INTEGER  NOT NULL PRIMARY KEY,
            IdFiliereFk INTEGER   NOT NULL,
            nom TEXT NOT NULL , 
            prenom TEXT NOT NULL, 
            age INTEGER NOT NULL,
            FOREIGN KEY (IdFiliereFk)
                REFERENCES Filiere (idFiliere))''')
        self.conn.commit()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Filiere (
            idFiliere INTEGER   NOT NULL PRIMARY KEY, 
            nomFiliere  TEXT NOT NULL)''')
        self.conn.commit()
    
    def fetch1(self):
        self.cur.execute("SELECT * FROM Etudiant")
        rows=self.cur.fetchall()
        return rows
    def fetch2(self):
        self.cur.execute("SELECT * FROM Filiere")
        rows=self.cur.fetchall()
        return rows    

    def insertEtu(self, idEtudiant, Idfiliere, lname, fname,age):
        self.cur.execute("INSERT INTO Etudiant VALUES( ?, ?, ?, ?, ?)",(idEtudiant, Idfiliere, lname, fname,age))
        self.conn.commit()

    def insertFel(self, Idfiliere, nomFiliere):
        self.cur.execute("INSERT INTO Filiere VALUES(?,?)",(Idfiliere, nomFiliere))
        self.conn.commit()

    def removeEtu(self, idEtudiant):
        self.cur.execute("DELETE FROM Etudiant WHERE idEtudiant=?",(idEtudiant,))
        self.conn.commit()
    
    def removeFel(self, Idfiliere):
        self.cur.execute("DELETE FROM Filiere WHERE Idfiliere=?",(Idfiliere,))
        self.conn.commit()

    def updateEtud(self, idEtudiant, Idfiliere, lname, fname,age):
        self.cur.execute("UPDATE Etudiant SET IdfiliereFK=?, nom=?, prenom=?,age=? WHERE idEtudiant=?",(Idfiliere, lname, fname,age,idEtudiant))
        self.conn.commit()
    
    def updateFel(self, Idfiliere, nomFiliere):
        self.cur.execute("UPDATE Filiere SET nomFiliere=? WHERE Idfiliere=?",(nomFiliere, Idfiliere))
        self.conn.commit()

    def inFiliere(self,IdfiliereFK):
        self.cur.execute("SELECT * FROM Filiere WHERE IdFiliere=?",(IdfiliereFK,))
        rows=self.cur.fetchone()
        if rows[0]!=None:
            return True
        else: return False
    
    def __del__(self):
        self.conn.close()