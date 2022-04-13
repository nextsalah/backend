from typing import List
from pydantic import BaseModel

class PrayerTimeDay(BaseModel):        
    date: str
    fajr: str
    sunrise: str
    dhuhr: str
    asr: str
    maghrib: str
    isha: str   
    
          
class PrayerTimeFullYear(BaseModel):
    success: bool = False
    prayertimes: List[PrayerTimeDay] = [{}]
    
    class Config:
        schema_extra = {
            "example": {
                "success": True,
                "prayertimes": [{
                    "date": "2022-01-01",
                    "fajr": "05:00",
                    "sunrise": "06:00",
                    "dhuhr": "12:00",
                    "asr": "15:00",
                    "maghrib": "18:00",
                    "isha": "19:00",}
                ]
            }   
        }
        
        
class VaktijaEULocations(BaseModel):
    class Data(BaseModel):
        class Country(BaseModel):
            id: int
            title: str
            short_code: str
        name: str
        slug: str
        country: Country
    data: List[Data]
        
