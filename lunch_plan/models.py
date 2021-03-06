from django.db import models

from order_details.config import DateWeekDay
from reference.models import BaseModel
from work_week.models import Day
from django.contrib.auth.models import User


class DailyPlan(BaseModel):
    user = models.ForeignKey(User)
    date = models.DateField()
    will_have_lunch = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.date}--{self.will_have_lunch}'

    def day(self):
        return f'{DateWeekDay.CHOICES[self.date.weekday()][1]}'
    day.short_description = "Day"


class WeeklyPlan(BaseModel):
    user = models.OneToOneField(User)
    office_lunch_days = models.ManyToManyField(Day)

    def __str__(self):
        return f'{self.user}'

    def admin_names(self):
        days = ', '.join([a.name for a in self.office_lunch_days.all()])
        if days == '':
            days = "None"
        return days
    admin_names.short_description = "Office Lunch Days"
