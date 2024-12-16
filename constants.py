from datetime import datetime
DATABASE_NAME = "postit_db"
TABLE_NAME = "postit"
CREATE_TABLE = """CREATE TABLE IF NOT EXISTS """+TABLE_NAME+""" (
            id INTEGER PRIMARY KEY, 
            author text NOT NULL, 
            message text NOT NULL, 
            style text NOT NULL, 
            date DATE, 
            color text NOT NULL, 
            image text NOT NULL, 
            position text NOT NULL, 
            angle text NOT NULL, 
            categorie text NOT NULL
        );"""

# author, message, style, date, color, position, angle, categorie
POSTIT_PARAMETERS = ["author", "message", "style", "date", "color", "image", "position", "angle", "categorie"]

BLACK_COLOR = "#000000"
WHITE_COLOR = "#FFFFFF"
BRUSH_FONT = "Brush\ Script\ MT 14 normal italic"

TODAY_DATE = datetime.now().strftime("%Y-%m-%d")
TODAY_DAY = int(datetime.now().strftime("%d"))
TODAY_MONTH = int(datetime.now().strftime("%m"))
TODAY_YEAR = int(datetime.now().strftime("%Y"))