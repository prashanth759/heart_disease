from django.shortcuts import render, redirect
from .models import Patient
import joblib

model = joblib.load('trained_model.pkl')
scaler = joblib.load('scaler.pkl')

def index(request):
    if request.method == 'POST':
        age = int(request.POST['age'])
        sex = int(request.POST['sex'])
        cp = int(request.POST['cp'])
        trestbps = int(request.POST['trestbps'])
        chol = int(request.POST['chol'])
        fbs = int(request.POST['fbs'])
        restecg = int(request.POST['restecg'])
        thalach = int(request.POST['thalach'])
        exang = int(request.POST['exang'])
        oldpeak = float(request.POST['oldpeak'])
        slope = int(request.POST['slope'])
        ca = int(request.POST['ca'])
        thal = int(request.POST['thal'])
        
        input_data = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
        if scaler:
            input_data_scaled = scaler.transform(input_data)
        else:
            input_data_scaled = input_data  
        prediction = model.predict(input_data_scaled)        
        result = "Heart Disease Present" if prediction[0] == 0 else "No Heart Disease"
        return render(request, 'result.html', {'result': result})
    return render(request, 'index.html')

def result(request):
    patients = Patient.objects.all()
    return render(request, 'results.html', {'patients': patients})
