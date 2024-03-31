from pydantic import BaseModel, Field


class Student(BaseModel):
    name: str = Field(..., serialization_alias='שם')
    city: str = Field(..., serialization_alias='יישוב')
    grade: str = Field(..., serialization_alias='כיתה')
    hebrew: str = Field(..., serialization_alias='לשון')
    literature: str = Field(..., serialization_alias='ספרות')
    english: str = Field(..., serialization_alias='אנגלית')
    bible: str = Field(..., serialization_alias='תנך')
    other: str = Field(..., serialization_alias='אחר')
    student_value: str = Field(..., serialization_alias='ערך תלמיד')
    subjects: str = Field(..., serialization_alias='מקצועות')
    contact_number: str = Field(..., alias='טלפון ליצירת קשר')
    teacher: str = Field(..., serialization_alias='מורה')
    contacted_by: str = Field(..., serialization_alias='יצר קשר')
    subject_details: str = Field(..., serialization_alias='נושאי \nלימוד')
    hours: list[str] = Field(..., serialization_alias='שעות')
    evacuated_destination: str = Field(..., serialization_alias='יעד \nפינוי')
    comments: str = Field(..., serialization_alias='הערות \nותיאור')
    time_of_registration: str = Field(..., serialization_alias='מועד הירשמות')
    group_leader: str = Field(..., serialization_alias='אחראי קבוצה')
    compatibility: float = Field(..., serialization_alias='התאמה')
    amount_used: int = Field(..., serialization_alias='כמות ניצול (ההפך מערך אלטרנטיבי)')
    last_lesson: str = Field(..., serialization_alias='שיעור אחרון שבוצע')
    previous_lessons: list[str] = Field(..., serialization_alias='שיעורים\nשביצע')

