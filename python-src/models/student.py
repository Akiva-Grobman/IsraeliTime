import datetime
from typing import Optional, Union
from pydantic import BaseModel, Field, validator, Extra, field_validator


class StudentLogin(BaseModel):
    name: str
    phone_number: str
    original_city: str
    current_city: str
    grade: str
    subjects: list[str]
    comments: Optional[str] = None
    time_of_registration: datetime.datetime = Field(default_factory=datetime.datetime.now)


class Student(BaseModel):
    name: str
    phone_number: str
    original_city: str
    current_city: str
    grade: str
    subjects: list[str]
    comments: Optional[str]
    time_of_registration: datetime.datetime
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
    identifier: Optional[int] = Field(default=0)

    @field_validator("time_of_registration", mode="before")
    def strip_nanosedonds(cls, v):
        return datetime.datetime.fromisoformat(v['$date'])


class StudentWithHebrewTranslator(BaseModel):
    name: str = Field(..., alias='שם')
    phone_number: Optional[str] = Field(None, alias='טלפון ליצירת קשר')
    original_city: str = Field(..., alias='יישוב')
    current_city: Optional[str] = Field(None, alias='יעד \nפינוי')
    grade: Optional[str] = Field(None, alias='כיתה')
    subjects: list[str] = Field(..., alias='מקצועות')

    @field_validator("subjects", mode="before")
    def strip_nanosedonds(cls, v):
        return v.split(',')

    # teacher: Optional[str] = Field(None, alias='מורה')
    # contacted_by: str = Field(..., alias='יצר קשר')
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
