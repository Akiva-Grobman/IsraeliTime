from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel, Field, validator, Extra


class StudentLogin(BaseModel):
    name: str
    phone_number: str
    original_city: str
    current_city: str
    grade: str
    subjects: list[str]
    comments: str
    time_of_registration: datetime = Field(default_factory=datetime.now)


class Student(BaseModel):
    name: str
    phone_number: str
    original_city: str
    current_city: str
    grade: str
    subjects: list[str]
    comments: str
    time_of_registration: datetime
    student_value: Optional[str] = None
    teacher: Optional[str] = None
    contacted_by: Optional[str] = None
    subject_details: Optional[str] = None
    available_hours: Optional[list[str]] = None
    group_leader: Optional[str] = None
    compatibility: Optional[float] = None
    amount_used: Optional[int] = None
    last_lesson: Optional[str] = None
    previous_lessons: Optional[list[str]] = None


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
