from django.db import models

# Create your models here.


'''
As we talked last time, our models are to be written here. I'll give a brief description of each model and what fields should 
be in the model. I'll also point out who is to do it.

Note:
It may be useful to know that most fields ( CharField and IntegerField especially have a choice argument that is very useful when dealing
with Data that is limited to some choices 

Example for the case of sex, since there are only two choices, it's convenient to specify the choices.

How to do it,

declare your choices list in a variable, this is the syntax
This should be written inside of a class
sex_choices = (
('M', 'Male'),
('F', 'Female')
) 


Then the field 
sex = models.CharField(max_length=1, choices=sex_choices)

This is probably new to you, but we can take that as a special dictionary in which the M to be the value that will 
be entered in the database and the 'Male' to be what will be shown to the user as a Choice.

the same method can be used for Combination, level and Class fields

I'll elaborate more on this when we meet :)


'''


class Student(models.Model):
    """
    This contains the extra fields for Student with are not in the user class.
    Fields
    - Sex
    - Level
    - Combination (should be blank for O level)
    - Class
    - Registration Status (Boolean)

    Coder: Stanley

    """



    pass

class Result(models.Model):
    """
    This model contains results for each student for each subject and exam
    Fields
    - Student (ForeignKey)
    - Type of exam (example Terminal)
    - Date of exam (Any date within the exam, preferably the first date)
    - English
    - Mathematics
    - Physics
    - Chemistry
    - Biology
    - Civics
    - History
    - Geography
    - General studies
    - Basic Applied Mathematics
    - Kiswahili


Remember: If a student does not study the subject, it should be left blank

Coder: Nguse And Catherine
    """