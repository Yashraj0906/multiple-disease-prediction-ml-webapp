import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np

# loading the saved models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_model = pickle.load(open('heart_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinson Disease Prediction'],
                           icons=['activity', 'heart', 'person'],
                           default_index=0)


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:    
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI Value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    with col2:
        Age = st.text_input('Age of the Person')

    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):
        input_values = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        input_values = np.asarray(input_values, dtype=float).reshape(1, -1)

        diab_prediction = diabetes_model.predict(input_values)

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is Diabetic'
        else:
            diab_diagnosis = 'The person is not Diabetic'

        st.success(diab_diagnosis)


# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
    with col2:    
        sex = st.text_input('Sex (1 = male, 0 = female)')
    with col3:
        cp = st.text_input('Chest Pain Type (0–3)')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholesterol in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic Results (0–2)')
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina (1 = yes; 0 = no)')

    with col1:
        oldpeak = st.text_input('ST Depression Induced by Exercise')
    with col2:
        slope = st.text_input('Slope of the Peak Exercise ST Segment (0–2)')
    with col3:
        ca = st.text_input('Number of Major Vessels Colored by Fluoroscopy (0–3)')

    with col1:
        thal = st.text_input('Thalassemia (1 = normal; 2 = fixed defect; 3 = reversable defect)')

    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        input_values = [age, sex, cp, trestbps, chol, fbs, restecg, thalach,
                        exang, oldpeak, slope, ca, thal]
        input_values = np.asarray(input_values, dtype=float).reshape(1, -1)

        heart_prediction = heart_model.predict(input_values)

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person has Heart Disease'
        else:
            heart_diagnosis = 'The person does not have Heart Disease'

        st.success(heart_diagnosis)


# Parkinson’s Disease Prediction Page
if selected == 'Parkinson Disease Prediction':
    st.title('Parkinson Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col1:
        jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col2:
        jitter_abs = st.text_input('MDVP:Jitter(Abs)')
    with col3:
        rap = st.text_input('MDVP:RAP')

    with col1:
        ppq = st.text_input('MDVP:PPQ')
    with col2:
        ddp = st.text_input('Jitter:DDP')
    with col3:
        shimmer = st.text_input('MDVP:Shimmer')

    with col1:
        shimmer_db = st.text_input('MDVP:Shimmer(dB)')
    with col2:
        apq3 = st.text_input('Shimmer:APQ3')
    with col3:
        apq5 = st.text_input('Shimmer:APQ5')

    with col1:
        mdvp_apq = st.text_input('MDVP:APQ')
    with col2:
        dda = st.text_input('Shimmer:DDA')
    with col3:
        nhr = st.text_input('NHR')

    with col1:
        hnr = st.text_input('HNR')
    with col2:
        rpde = st.text_input('RPDE')
    with col3:
        dfa = st.text_input('DFA')

    with col1:
        spread1 = st.text_input('spread1')
    with col2:
        spread2 = st.text_input('spread2')
    with col3:
        d2 = st.text_input('D2')

    with col1:
        ppe = st.text_input('PPE')

    parkinson_diagnosis = ''

    if st.button('Parkinson Disease Test Result'):
        input_values = [fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp, shimmer,
                        shimmer_db, apq3, apq5, mdvp_apq, dda, nhr, hnr, rpde, dfa,
                        spread1, spread2, d2, ppe]
        input_values = np.asarray(input_values, dtype=float).reshape(1, -1)

        parkinson_prediction = parkinsons_model.predict(input_values)

        if parkinson_prediction[0] == 1:
            parkinson_diagnosis = 'The person has Parkinson\'s Disease'
        else:
            parkinson_diagnosis = 'The person does not have Parkinson\'s Disease'

        st.success(parkinson_diagnosis) 


# to open this 
#python -m streamlit run "C:\Users\Yashraj Kumar\OneDrive\Desktop\Machine Learning\Projects\Multiple Disease Prediction\multiple_disease_prediction.py"

