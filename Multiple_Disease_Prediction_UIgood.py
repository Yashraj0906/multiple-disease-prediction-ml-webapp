import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import matplotlib.pyplot as plt
import time

# Loading saved models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_model = pickle.load(open('heart_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# Custom CSS styling
st.markdown("""
    <style>
        .stButton>button {
            background-color: #4B8BBE;
            color: white;
            font-size: 16px;
            border-radius: 8px;
            padding: 10px 20px;
        }
        .stTextInput>div>div>input {
            border-radius: 6px;
            padding: 8px;
        }
        footer {
            visibility: hidden;
        }
    </style>
    """, unsafe_allow_html=True)

# Custom header
st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>🧠 Multiple Disease Prediction System</h1>", unsafe_allow_html=True)
st.markdown("---")

# Tab layout
tab1, tab2, tab3 = st.tabs(["🩸 Diabetes Prediction", "❤️ Heart Disease", "🧠 Parkinson's Prediction"])

# --- Diabetes Prediction ---
with tab1:
    st.subheader("Enter Patient Details for Diabetes Test")

    with st.expander("🔍 Fill the following parameters"):
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

    if st.button('🔎 Predict Diabetes'):
        try:
            input_values = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
            input_values = np.asarray(input_values, dtype=float).reshape(1, -1)

            with st.spinner('Analyzing...'):
                time.sleep(1)
                diab_prediction = diabetes_model.predict(input_values)

            if diab_prediction[0] == 1:
                diab_diagnosis = '🚨 The person is Diabetic'
                st.error(diab_diagnosis)
            else:
                diab_diagnosis = '✅ The person is not Diabetic'
                st.success(diab_diagnosis)

            # Bar chart
            st.subheader("📊 Input Summary")
            fig, ax = plt.subplots()
            ax.bar(['Glucose', 'BloodPressure', 'BMI'], [float(Glucose), float(BloodPressure), float(BMI)])
            st.pyplot(fig)

        except:
            st.warning("⚠️ Please fill all fields correctly with numeric values.")

# --- Heart Disease Prediction ---
with tab2:
    st.subheader("Enter Patient Details for Heart Disease Test")

    with st.expander("🔍 Fill the following parameters"):
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
            restecg = st.text_input('Resting ECG (0–2)')
        with col2:
            thalach = st.text_input('Max Heart Rate Achieved')
        with col3:
            exang = st.text_input('Exercise Induced Angina (1 = yes; 0 = no)')
        with col1:
            oldpeak = st.text_input('ST Depression')
        with col2:
            slope = st.text_input('Slope of ST Segment (0–2)')
        with col3:
            ca = st.text_input('Major Vessels Colored (0–3)')
        with col1:
            thal = st.text_input('Thalassemia (1=normal, 2=fixed defect, 3=reversible defect)')

    heart_diagnosis = ''

    if st.button('🔎 Predict Heart Disease'):
        try:
            input_values = [age, sex, cp, trestbps, chol, fbs, restecg, thalach,
                            exang, oldpeak, slope, ca, thal]
            input_values = np.asarray(input_values, dtype=float).reshape(1, -1)

            with st.spinner('Analyzing...'):
                time.sleep(1)
                heart_prediction = heart_model.predict(input_values)

            if heart_prediction[0] == 1:
                heart_diagnosis = '❤️ The person has Heart Disease'
                st.error(heart_diagnosis)
            else:
                heart_diagnosis = '✅ The person does not have Heart Disease'
                st.success(heart_diagnosis)

        except:
            st.warning("⚠️ Please fill all fields correctly with numeric values.")

# --- Parkinson’s Disease Prediction ---
with tab3:
    st.subheader("Enter Metrics for Parkinson’s Prediction")

    with st.expander("🔍 Fill the following voice parameters"):
        col1, col2, col3 = st.columns(3)

        fo = st.text_input('MDVP:Fo(Hz)')
        fhi = st.text_input('MDVP:Fhi(Hz)')
        flo = st.text_input('MDVP:Flo(Hz)')
        jitter_percent = st.text_input('MDVP:Jitter(%)')
        jitter_abs = st.text_input('MDVP:Jitter(Abs)')
        rap = st.text_input('MDVP:RAP')
        ppq = st.text_input('MDVP:PPQ')
        ddp = st.text_input('Jitter:DDP')
        shimmer = st.text_input('MDVP:Shimmer')
        shimmer_db = st.text_input('MDVP:Shimmer(dB)')
        apq3 = st.text_input('Shimmer:APQ3')
        apq5 = st.text_input('Shimmer:APQ5')
        mdvp_apq = st.text_input('MDVP:APQ')
        dda = st.text_input('Shimmer:DDA')
        nhr = st.text_input('NHR')
        hnr = st.text_input('HNR')
        rpde = st.text_input('RPDE')
        dfa = st.text_input('DFA')
        spread1 = st.text_input('spread1')
        spread2 = st.text_input('spread2')
        d2 = st.text_input('D2')
        ppe = st.text_input('PPE')

    parkinson_diagnosis = ''

    if st.button("🔎 Predict Parkinson's Disease"):
        try:
            input_values = [fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp, shimmer,
                            shimmer_db, apq3, apq5, mdvp_apq, dda, nhr, hnr, rpde, dfa,
                            spread1, spread2, d2, ppe]
            input_values = np.asarray(input_values, dtype=float).reshape(1, -1)

            with st.spinner('Analyzing...'):
                time.sleep(1)
                parkinson_prediction = parkinsons_model.predict(input_values)

            if parkinson_prediction[0] == 1:
                parkinson_diagnosis = "🧠 The person has Parkinson's Disease"
                st.error(parkinson_diagnosis)
            else:
                parkinson_diagnosis = "✅ The person does not have Parkinson's Disease"
                st.success(parkinson_diagnosis)

        except:
            st.warning("⚠️ Please fill all fields correctly with numeric values.")

# Footer
st.markdown("---")
st.markdown("🔬 Built with ❤️ by **Yashraj Kumar** | [GitHub](https://github.com/Yashraj0906)")

