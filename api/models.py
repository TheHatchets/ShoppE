# from django.db import models
# from simplesocial.accounts.models import User
# # Create your models here.
#
# class Student(models.Model):
#     student_tnumber = models.ForeignKey(User, on_delete=models.CASCADE)
#     student_name = models.CharField(max_length=200)
#     student_classification = models.CharField(max_length=9)
#     student_university_attended = models.CharField(max_length=200)
#     student_classes = models.ManyToOneRel(field='class1', 'class2', 'class3', 'class4', 'class5', 'class6',field_name='classes', to='models.name')
#
#     def __str__(self):
#         return self.student_name
#
