import streamlit as st
import requests
import json

def apply_rtl():
    st.markdown(
        """
        <style>
        body {
            direction: rtl;
            text-align: right;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Function to gather user input
def get_user_input(language='en'):
    if language == 'en':
        # English labels
        age_label = 'Age'
        sex_label = 'Sex (1 = Male, 0 = Female)'
        cp_label = 'Chest Pain Type (0 = Typical Angina, 1 = Atypical Angina, 2 = Non-anginal Pain, 3 = Asymptomatic)'
        trestbps_label = 'Resting Blood Pressure (in mm Hg)'
        chol_label = 'Cholesterol Level (in mg/dl)'
        fbs_label = 'Fasting Blood Sugar > 120 mg/dl (1 = True, 0 = False)'
        restecg_label = 'Resting Electrocardiographic Results (0 = Normal, 1 = ST-T Abnormality, 2 = LVH)'
        thalach_label = 'Maximum Heart Rate Achieved'
        exang_label = 'Exercise Induced Angina (1 = Yes, 0 = No)'
        oldpeak_label = 'ST Depression Induced by Exercise'
        slope_label = 'Slope of Peak Exercise ST Segment (0 = Upsloping, 1 = Flat, 2 = Downsloping)'
        ca_label = 'Number of Major Vessels (0-4) Colored by Fluoroscopy'
        thal_label = 'Thalassemia (0 = Normal, 1 = Fixed Defect, 2 = Reversible Defect)'
    else:
        # Arabic labels
        age_label = 'العمر'
        sex_label = 'الجنس (1 = ذكر, 0 = أنثى)'
        cp_label = 'نوع ألم الصدر (0 = ذبحة نموذجية, 1 = ذبحة غير نموذجية, 2 = ألم غير ذبحي, 3 = بدون أعراض)'
        trestbps_label = 'ضغط الدم أثناء الراحة (بالمليمتر الزئبقي)'
        chol_label = 'مستوى الكوليسترول (ملغ/دل)'
        fbs_label = 'سكر الدم الصائم > 120 ملغ/دل (1 = صحيح, 0 = خطأ)'
        restecg_label = 'نتائج مخطط كهربية القلب (0 = طبيعي, 1 = تشوه ST-T, 2 = تضخم البطين الأيسر)'
        thalach_label = 'أقصى معدل لضربات القلب تم تحقيقه'
        exang_label = 'الذبحة الصدرية الناتجة عن التمرين (1 = نعم, 0 = لا)'
        oldpeak_label = 'الانخفاض في ST الناتج عن التمرين'
        slope_label = 'ميل الجزء العلوي لموجة ST أثناء التمرين (0 = تصاعدي, 1 = مسطح, 2 = تنازلي)'
        ca_label = 'عدد الأوعية الدموية الرئيسية (0-4) الملونة بواسطة الفحص الفلوري'
        thal_label = 'الثلاسيميا (0 = طبيعي, 1 = عيب ثابت, 2 = عيب قابل للتغيير)'

    # Inputs
    age = st.number_input(age_label, min_value=28, max_value=77, value=30)
    sex = st.selectbox(sex_label, [0, 1])
    cp = st.selectbox(cp_label, [0, 1, 2, 3])
    trestbps = st.number_input(trestbps_label, min_value=80, max_value=200, value=120)
    chol = st.number_input(chol_label, min_value=100, max_value=600, value=200)
    fbs = st.selectbox(fbs_label, [0, 1])
    restecg = st.selectbox(restecg_label, [0, 1, 2])
    thalach = st.number_input(thalach_label, min_value=60, max_value=220, value=150)
    exang = st.selectbox(exang_label, [0, 1])
    oldpeak = st.number_input(oldpeak_label, min_value=0.0, max_value=6.0, value=1.0, step=0.1)
    slope = st.selectbox(slope_label, [0, 1, 2])
    ca = st.number_input(ca_label, min_value=0, max_value=4, value=0)
    thal = st.selectbox(thal_label, [0, 1, 2])

    user_data = {
        'age': age, 'sex': sex, 'cp': cp, 'trestbps': trestbps, 'chol': chol,
        'fbs': fbs, 'restecg': restecg, 'thalach': thalach, 'exang': exang,
        'oldpeak': oldpeak, 'slope': slope, 'ca': ca, 'thal': thal
    }

    return user_data

# Main function for Streamlit app
def main():

    # Language selection (English or Arabic)
    language = st.selectbox("Select Language / اختر اللغة", options=["English", "العربية"])
    lang_code = 'en' if language == "English" else 'ar'
    
    # Apply RTL layout if Arabic is selected
    if lang_code == 'ar':
        apply_rtl()
        
    if lang_code == 'en':
         st.title("Heart Diagnosis Assistant @Powered by AI")
    if lang_code == 'ar':
         st.title("مساعد تشخيص القلب @مدعوم بالذكاء الاصطناعي")
    # Display the description based on the selected language
    if lang_code == 'en':
        st.write("""
            The **Heart Diagnosis Assistant** is an AI-powered application designed to help you assess your heart health.
            It analyzes your input data (such as age, cholesterol levels, and more) to provide a prediction on the likelihood of heart disease.
            This tool is meant to offer insights into heart health, and to assist medical advice.
        """)
    else:
        st.write("""
            **مساعد تشخيص القلب** هو تطبيق مدعوم بالذكاء الاصطناعي تم تصميمه لمساعدتك في تقييم صحة قلبك.
            يقوم التطبيق بتحليل البيانات التي تدخلها (مثل العمر ومستوى الكوليسترول والمزيد) لتقديم تنبؤ حول احتمالية الإصابة بأمراض القلب.
            هذه الأداة تهدف إلى تقديم رؤى حول صحة القلب، وهي مساعدة لنصائح الطبية.
        """)
    
    # Gather input data from user based on selected language
    user_input = get_user_input(language=lang_code)

    # When user clicks 'Predict' button, send data to Flask API
    if st.button("Predict" if lang_code == 'en' else "توقع"):
        url = 'http://127.0.0.1:5000/predict'  # AI_server API URL
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=json.dumps(user_input), headers=headers)

        if response.status_code == 200:
            prediction = response.json()

            # Display prediction and confidence based on the selected language
            if lang_code == 'en':
                st.write(f"Prediction: {prediction['message']}")
                st.write(f"Probability of Heart Disease: {prediction['confidence']:.2%}")
            else:
                st.write(f"التوقع: {prediction['message']}")
                st.write(f"احتمالية الإصابة بأمراض القلب: {prediction['confidence']:.2%}")
        else:
            # Error message based on the selected language
            if lang_code == 'en':
                st.write("Error: Could not connect to AI Server.")
            else:
                st.write("خطأ: لا يمكن الاتصال بخادم الذكاء الاصطناعي.")


if __name__ == "__main__":
    main()
