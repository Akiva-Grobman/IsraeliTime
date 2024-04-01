from typing import Optional, Union
from pydantic import BaseModel, Field


class StudentLogin(BaseModel):
    name: str
    phone_number: str
    original_city: str
    grade: str
    subjects: list[str]
    comments: str


class Student(BaseModel):
    name: str
    original_city: str
    grade: str
    student_value: str
    subjects: list[str]
    phone_number: str
    teacher: str
    contacted_by: str
    subject_details: str
    available_hours: list[str]
    current_city: str
    comments: str
    time_of_registration: str
    group_leader: str
    compatibility: float
    amount_used: int
    last_lesson: str
    previous_lessons: list[str]


class StudentWithHebrewTranslator(BaseModel):
    name: str = Field(..., alias='שם')
    original_city: str = Field(..., alias='יישוב')
    grade: Optional[str] = Field(None, alias='כיתה')
    student_value: int = Field(..., alias='ערך תלמיד')
    subjects: str = Field(..., alias='מקצועות')
    phone_number: Optional[str] = Field(None, alias='טלפון ליצירת קשר')
    teacher: Optional[str] = Field(None, alias='מורה')
    contacted_by: str = Field(..., alias='יצר קשר')
    # subject_details: str = Field(..., alias='נושאי \nלימוד')
    # available_hours: list[str] = Field(..., alias='שעות')
    # evacuated_destination: str = Field(..., alias='יעד \nפינוי')
    # comments: str = Field(..., alias='הערות \nותיאור')    
    # time_of_registration: str = Field(..., alias='מועד הירשמות')
    # group_leader: str = Field(..., alias='אחראי קבוצה')
    # compatibility: float = Field(..., alias='התאמה')
    # amount_used: int = Field(..., alias='כמות ניצול (ההפך מערך אלטרנטיבי)')
    # last_lesson: str = Field(..., alias='שיעור אחרון שבוצע')
    # previous_lessons: list[str] = Field(..., alias='שיעורים\nשביצע')
