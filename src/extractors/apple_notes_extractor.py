import sqlite3
import os


class AppleNotesExtractor:
    """
    A class for extracting notes from the Apple Notes SQLite database.

    Attributes:
        db_path (str): The path to the SQLite database file.
    """

    def __init__(self, db_path=None):
        """
        Initializes a new instance of the AppleNotesExtractor class.

        Args:
            db_path (str, optional): The path to the SQLite database file.
                If not provided, the default path will be used.
                Defaults to None.

        Raises:
            FileNotFoundError: If no SQLite database is found at the specified path.
            PermissionError: If read permissions are required for the SQLite
                database file.
        """
        self.db_path = db_path or os.path.expanduser(
            "~/Library/Group Containers/group.com.apple.notes/NoteStore.sqlite"
        )
        if not os.path.isfile(self.db_path):
            raise FileNotFoundError(f"No SQLite database found at {self.db_path}")
        if not os.access(self.db_path, os.R_OK):
            raise PermissionError(
                f"Read permissions for SQLite database at {self.db_path} are required"
            )

    def extract(self):
        """
        Extracts notes from the SQLite database.

        Returns:
            list: A list of tuples containing the title and content of each note.

        Raises:
            Exception: If there is an error while extracting notes from
                the SQLite database.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            cursor.execute(
                "SELECT ZNOTE.ZTITLE, ZNOTEBODY.ZCONTENT FROM ZICNOTEDATA "
                "LEFT JOIN ZNOTE ON ZICNOTEDATA.ZNOTE = ZNOTE.Z_PK "
                "LEFT JOIN ZNOTEBODY ON ZNOTEBODY.ZBODY = ZICNOTEDATA.Z_PK"
            )

            notes = cursor.fetchall()
            conn.close()

            return notes
        except sqlite3.OperationalError as e:
            raise Exception("Failed to extract notes from SQLite database") from e
