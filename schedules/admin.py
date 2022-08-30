from django.contrib import admin

from .models import Instructor, Course, CRN, Timeslot

admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(CRN)
admin.site.register(Timeslot)
