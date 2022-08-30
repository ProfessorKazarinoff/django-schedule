from django.db import models

class Instructor(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, default='', null=True)
    last_name = models.CharField(max_length=200)

    def __str__(self): # new
        return f"{self.first_name} {self.last_name}"

class Course(models.Model):
    code = models.CharField(max_length=10)
    title = models.CharField(max_length=200)

    def __str__(self): # new
        return self.code

class CRN(models.Model):
    code = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    year = models.IntegerField()
    quarter = models.CharField(max_length=2)

    def __str__(self): # new
        return f"{self.course} - CRN {self.code}"

class Timeslot(models.Model):
    crn = models.ForeignKey(CRN, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    day = models.CharField(max_length=20)
    start = models.CharField(max_length=20, default='9:00am')
    end = models.CharField(max_length=20, default='12:00pm')
    campus = models.CharField(max_length=5)
    room = models.CharField(max_length=50)

    def __str__(self): # new
        return f"{self.crn} - {self.day}"
