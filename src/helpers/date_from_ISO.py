from datetime import datetime

def date_from_ISO(date: str) -> datetime:
  return datetime(*[int(i) for i in date.split('-')])