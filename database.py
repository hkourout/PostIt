import sqlite3
import constants

class Database:
    def __init__(self, **kwargs):
        self.filename = kwargs.get('filename')
        self.table = kwargs.get('table')

    def sql_do(self, sql, *params):
        self._db.execute(sql, params)
        self._db.commit()

    def insert(self, values):
        keys = ",".join(constants.POSTIT_PARAMETERS)
        print(values)
        self._db.execute('insert into {} ({}) values (?, ?, ?, ?, ?, ?, ?, ?, ?)'.format(constants.TABLE_NAME, keys), values)
        self._db.commit()

    def retrieve(self, value):
        cursor = self._db.execute('select * from {} where message like ? or \
                            author like ? or \
                            date like ? or \
                            style like ? or \
                            categorie like ?'.format(self._table), [f"%{value}%" for _ in range(5)])
        return [dict(row) for row in cursor.fetchall() ]
    
    def retrieve_value_of_key(self, key, value):
        cursor = self._db.execute('select * from {} where {} like ?'.format(self._table, key), [f"%{value}%"])
        return [dict(row) for row in cursor.fetchall() ]

    def update(self, id, key, value):
        self._db.execute('update {} set {} = ? where image = ?'.format(self._table, key), (value, id))
        self._db.commit()

    def delete(self, id):
        self._db.execute('delete from {} where image = ?'.format(self._table), (id,))
        self._db.commit()

    def disp_rows(self):
        cursor = self._db.execute('select * from {} order by t1'.format(self._table))
        for row in cursor:
            print('  {}: {}'.format(row['t1'], row['i1']))

    def get_row(self):
        cursor = self._db.execute('select * from {} '.format(self._table))
        return cursor
    
    def get_sorted_row(self, key):
        cursor = self._db.execute('select * from {} order by {} '.format(self._table, key))
        return cursor
        
    def __iter__(self):
        cursor = self._db.execute('select * from {} '.format(self._table))
        for row in cursor:
            yield dict(row)

    @property
    def filename(self): return self._filename
    @filename.setter
    def filename(self, fn):
        self._filename = fn
        self._db = sqlite3.connect(fn)
        self._db.row_factory = sqlite3.Row
    @filename.deleter
    def filename(self): self.close()
    @property
    def table(self): return self._table
    @table.setter
    def table(self, t): self._table = t
    @table.deleter
    def table(self): self._table = 'test'

    def close(self):
            self._db.close()
            del self._filename

def main():
    db = Database(filename = constants.DATABASE_NAME, table = constants.TABLE_NAME)
    db.sql_do(constants.CREATE_TABLE)

    print('Create rows')
    db.insert(("author11", "message1", "style1", "date1", "color1", "position1", "angle1", "categorie1"))
    db.insert(("author2", "message2", "style2", "date2", "color2", "position2", "angle2", "categorie2"))
    db.insert(("author3", "message3", "style3", "date3", "color3", "position3", "angle3", "categorie3"))
    #for row in db: print(row)

    print('Retrieve rows')
    print(db.retrieve_value_of_key("author", "11"))
    print(db.retrieve_value_of_key("message", "test"))
    print(db.retrieve_value_of_key("date", 'date3'))
    print('Update rows')     

    db.update(6,"message","TEST")
    db.update(6,"date","12 Décmebre 2014")
    #for row in db: print(row)

    print('Delete rows')
    db.delete(6)
    db.delete(7)
    for row in db: print(row)

if __name__ == "__main__": main()