from pydantic import BaseModel, Field


class Student(BaseModel):
    name: str = Field(..., alias='שם')
    city: str = Field(..., alias='יישוב')
    grade: str = Field(..., alias='כיתה')
    hebrew: str = Field(..., alias='לשון')
    literature: str = Field(..., alias='ספרות')
    english: str = Field(..., alias='אנגלית')
    bible: str = Field(..., alias='תנך')
    other: str = Field(..., alias='אחר')
    student_value: str = Field(..., alias='ערך תלמיד')
    subjects: str = Field(..., alias='מקצועות')
    contact_number: str = Field(..., alias='טלפון ליצירת קשר')
    teacher: str = Field(..., alias='מורה')
    contacted_by: str = Field(..., alias='יצר קשר')
    subject_details: str = Field(..., alias='נושאי \nלימוד')
    hours: list[str] = Field(..., alias='שעות')
    evacuated_destination: str = Field(..., alias='יעד \nפינוי')
    comments: str = Field(..., alias='הערות \nותיאור')
    time_of_registration: str = Field(..., alias='מועד הירשמות')
    group_leader: str = Field(..., alias='אחראי קבוצה')
    compatibility: fload = Field(..., alias='התאמה')
    amount_used: int = Field(..., alias='כמות ניצול (ההפך מערך אלטרנטיבי)')
    last_lesson: str = Field(..., alias='שיעור אחרון שבוצע')
    previous_lessons: list[str] = Field(..., alias='שיעורים\nשביצע')