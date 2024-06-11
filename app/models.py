# app/models.py
from .user import create_user_table
from .student import create_student_table
from .level import create_level_table

def initialize_db():
    create_user_table()
    create_student_table()
    create_level_table()
