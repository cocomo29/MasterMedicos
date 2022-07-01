class MedicalList:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()

    def customQuery(self,query):
        data = self.cursor.execute(query)
        return (col[0] for col in data.description), data.fetchall()
    def insert(self, data):
        self.cursor.execute(
            """INSERT INTO MedicineList (
      [GenericName]
      ,[MedicineType]
      ,[MarketName]
      ,[Route]
      ,[Potency]
      ,[Status]) VALUES (?, ?, ?, ?, ?, ?)""",
            data
        )
        self.cursor.commit()

    def update(self, data, id):
        self.cursor.execute(
            """UPDATE MedicineList SET
        [GenericName] = ?
        ,[MedicineType] = ?
        ,[MarketName] = ?
        ,[Route] = ?
        ,[Potency] = ?
        ,[Status] = ? WHERE [MedicineId] = ?""",
            data + (id,)
        )
        self.cursor.commit()

    def delete(self, id):
        self.cursor.execute(
            "DELETE FROM MedicineList WHERE [MedicineId] = ?",
            id
        )
        self.cursor.commit()

    def fetch(self, id):
        self.cursor.execute(
            "SELECT * FROM MedicineList WHERE [MedicineId] = ?",
            id
        )
        return self.cursor.fetchone()

    def read(self):
        self.cursor.execute("SELECT * FROM MedicineList")
        return self.cursor.fetchall()

class MedicineRoute:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()

    def insert(self, data):
        self.cursor.execute(
            """INSERT INTO MedicineRoute (
      [RouteType]
      ,[status]) VALUES (?, ?)""",
            data
        )
        self.cursor.commit()

    def update(self, data, id):
        self.cursor.execute(
            """UPDATE MedicineRoute SET
        [RouteType] = ?
        ,[status] = ? WHERE [RouteId] = ?""",
            data + (id,)
        )
        self.cursor.commit()

    def delete(self, id):
        self.cursor.execute(
            "DELETE FROM MedicineRoute WHERE [RouteId] = ?",
            id
        )
        self.cursor.commit()

    def fetch(self, id):
        self.cursor.execute(
            "SELECT * FROM MedicineRoute WHERE [RouteId] = ?",
            id
        )
        return self.cursor.fetchone()

    def read(self):
        self.cursor.execute("SELECT * FROM MedicineRoute")
        return self.cursor.fetchall()

class MedicineType:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()

    def insert(self, data):
        self.cursor.execute(
            """INSERT INTO MedicineType (
      [MedicineType],[status]) VALUES (?,?)""",
            data
        )
        self.cursor.commit()

    def update(self, data, id):
        self.cursor.execute(
            """UPDATE MedicineType SET
        [MedicineType] = ?, [status] = ? WHERE [MedicineTypeId] = ?""",
            data + (id,)
        )
        self.cursor.commit()

    def delete(self, id):
        self.cursor.execute(
            "DELETE FROM MedicineType WHERE [MedicineTypeId] = ?",
            id
        )
        self.cursor.commit()

    def fetch(self, id):
        self.cursor.execute(
            "SELECT * FROM MedicineType WHERE [MedicineTypeId] = ?",
            id
        )
        return self.cursor.fetchone()

    def read(self):
        self.cursor.execute("SELECT * FROM MedicineType")
        return self.cursor.fetchall()