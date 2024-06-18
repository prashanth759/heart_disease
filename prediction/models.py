# Create your models here.
from django.db import models

class Patient(models.Model):
    age = models.IntegerField()
    sex = models.IntegerField(choices=((0, 'Female'), (1, 'Male')))
    cp = models.IntegerField(choices=((0, 'Typical Angina'), (1, 'Atypical Angina'), (2, 'Non-Anginal Pain'), (3, 'Asymptomatic')))
    trestbps = models.IntegerField()
    chol = models.IntegerField()
    fbs = models.IntegerField(choices=((0, 'No'), (1, 'Yes')))
    restecg = models.IntegerField(choices=((0, 'Normal'), (1, 'ST-T Wave Abnormality'), (2, 'Left Ventricular Hypertrophy')))
    thalach = models.IntegerField()
    exang = models.IntegerField(choices=((0, 'No'), (1, 'Yes')))
    oldpeak = models.FloatField()
    slope = models.IntegerField(choices=((0, 'Upsloping'), (1, 'Flat'), (2, 'Downsloping')))
    ca = models.IntegerField()
    thal = models.IntegerField(choices=((0, 'Normal'), (1, 'Fixed Defect'), (2, 'Reversible Defect')))
    result = models.CharField(max_length=50, blank=True)


