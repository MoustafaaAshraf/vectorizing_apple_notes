import sqlite3
import os

class AppleNotesExtractor:
    def __init__(self, db_path=None):
        self.db_path = db_path or os.path.expanduser("~/Library/Group Containers/group.com.apple.notes/NoteStore.sqlite")

    def extract(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT ZNOTE.ZTITLE, ZNOTEBODY.ZCONTENT FROM ZICNOTEDATA "
                       "LEFT JOIN ZNOTE ON ZICNOTEDATA.ZNOTE = ZNOTE.Z_PK "
                       "LEFT JOIN ZNOTEBODY ON ZNOTEBODY.ZBODY = ZICNOTEDATA.Z_PK")
        
        notes = cursor.fetchall()
        conn.close()
        
        return notes