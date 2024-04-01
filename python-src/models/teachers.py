from pydantic import BaseModel, Field


class Teacher(BaseModel):
    name: str
    phone_number: str
    number_of_students: str
    classes_taken: str
    subjetcts: list[str]
    teacher_value: str
    background: str
    contacted_by: str
    comments: str


class TeacherWithHebrewTranslator(BaseModel):
    name: str = Field(..., alias='שם')
    phone_number: str  = Field(..., alias='טלפון')
    number_of_students: str = Field(..., alias="מס' תלמידים")
    classes_taken: str = Field(..., alias='שיעורים שנלקחו')
    subjetcts: str = Field(..., alias='מקצועות')
    teacher_value: str = Field(..., alias='ערך מורה')
    background: str = Field(..., alias='רקע')
    contacted_by: str  = Field(..., alias='מי יצר קשר')
    comments: str = Field(..., alias='הערות אישיות \ אחרי שיחה')
