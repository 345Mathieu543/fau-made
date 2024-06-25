import unittest
import os
import sqlite3

class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.csv_path = 'csv_files/PedData.csv'
        cls.db_path = '../data/data.sqlite'

        if os.path.exists(cls.csv_path):
            os.remove(cls.csv_path)

        if os.path.exists(cls.db_path):
            os.remove(cls.db_path)

        os.system('./pipeline.sh')

    def test_csv_exists(self):
        message = "The CSV file has not been generated!"
        self.assertTrue(os.path.exists(self.csv_path), message)

    def test_db_exists(self):
        message = "The database does not exist!"
        self.assertTrue(os.path.exists(self.db_path), message)

    def test_db_not_empty(self):
        self.test_db_exists()
        
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        
        cur.execute("SELECT COUNT(*) FROM pedestrians")
        rows = cur.fetchall()
        message = "The pedestrians table is empty!"
        self.assertTrue(rows[0][0] > 0, message)
        
        cur.execute("SELECT COUNT(*) FROM rainmoe")
        rows = cur.fetchall()
        message = "The rainmoe table is empty!"
        self.assertTrue(rows[0][0] > 0, message)
        
        cur.execute("SELECT COUNT(*) FROM rainnue")
        rows = cur.fetchall()
        message = "The rainnue table is empty!"
        self.assertTrue(rows[0][0] > 0, message)
        
        cur.execute("SELECT COUNT(*) FROM tempmoe")
        rows = cur.fetchall()
        message = "The tempmoe table is empty!"
        self.assertTrue(rows[0][0] > 0, message)
        
        cur.execute("SELECT COUNT(*) FROM tempnue")
        rows = cur.fetchall()
        message = "The tempnue table is empty!"
        self.assertTrue(rows[0][0] > 0, message)

        cur.execute("SELECT COUNT(*) FROM data")
        rows = cur.fetchall()
        message = "The data table is empty!"
        self.assertTrue(rows[0][0] > 0, message)

        conn.close()
    
    def test_db_complete(self):
        self.test_db_exists()
        
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        
        cur.execute("SELECT COUNT(*) FROM pedestrians")
        rows = cur.fetchall()
        message = "The pedestrians table has not exactly 550 rows!"
        self.assertTrue(rows[0][0] == 550, message)
        
        cur.execute("SELECT COUNT(*) FROM rainmoe")
        rows = cur.fetchall()
        message = "The rainmoe table has not exactly 550 rows!"
        self.assertTrue(rows[0][0] == 550, message)
        
        cur.execute("SELECT COUNT(*) FROM rainnue")
        rows = cur.fetchall()
        message = "The rainnue table has not exactly 550 rows!"
        self.assertTrue(rows[0][0] == 550, message)
        
        cur.execute("SELECT COUNT(*) FROM tempmoe")
        rows = cur.fetchall()
        message = "The tempmoe table has not exactly 550 rows!"
        self.assertTrue(rows[0][0] == 550, message)
        
        cur.execute("SELECT COUNT(*) FROM tempnue")
        rows = cur.fetchall()
        message = "The tempnue table has not exactly 550 rows!"
        self.assertTrue(rows[0][0] == 550, message)

        cur.execute("SELECT COUNT(*) FROM data")
        rows = cur.fetchall()
        message = "The data table has not exactly 550 rows!"
        self.assertTrue(rows[0][0] == 550, message)

        conn.close()
        
if __name__ == '__main__':
    unittest.main()
