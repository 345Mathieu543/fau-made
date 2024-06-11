import unittest
import os
import sqlite3

class TestStringMethods(unittest.TestCase):

    def test_csv_exists(self):
        scv_path = 'csv_files/PedData.csv'

        if os.path.exists(scv_path):
            os.remove(scv_path)

        os.system('python3 ./pipeline1.py')

        message = "The CSV file has not been generated!"
        
        self.assertTrue(os.path.exists(scv_path), message)

    def test_db_exists(self):
        db_path = '../data/data.sqlite'

        if os.path.exists(db_path):
            os.remove(db_path)

        os.system('./pipeline.sh')

        message = "The database does not exist!"
        
        self.assertTrue(os.path.exists(db_path), message)

    def test_db_not_empty(self):
        db_path = '../data/data.sqlite'

        self.test_db_exists()
        
        conn = sqlite3.connect(db_path)
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
        
if __name__ == '__main__':
    unittest.main()
