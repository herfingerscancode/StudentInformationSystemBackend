from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Marks(models.Model):
    MIDTERM04 = 'MT4'
    TERMINAL = 'TML'
    MIDTERM09 = 'MT9'
    ANNUAL = 'ANL'
    examChoices = [
        (MIDTERM04, 'First MidTerm Exam'),
        (TERMINAL, 'Terminal Exam'),
        (MIDTERM09, 'Second MidTerm Exam'),
        (ANNUAL, 'Annual Exam'),
    ]
    exam = models.CharField(max_length=10, choices=examChoices, default=MIDTERM04)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    english = models.IntegerField(null=True)
    maths = models.IntegerField(null=True)
    kiswahili = models.IntegerField(null=True)
    biology = models.IntegerField(null=True)
    physics = models.IntegerField(null=True)
    chemistry = models.IntegerField(null=True)
    civics = models.IntegerField(null=True)
    history = models.IntegerField(null=True)
    geography = models.IntegerField(null=True)
    gs = models.IntegerField(null=True)
    bam = models.IntegerField(null=True)

    def __str__(self):
        return self.username