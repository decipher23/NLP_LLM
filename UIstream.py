import streamlit as st
import pandas as pd

from project_sentiment2 import predict_sentiment
from spam_or_not2 import predict_spam
from detect_language2 import detect_language
from newsclassify2 import classify_news
from language_translation2 import translate_text

# ----------------------------------------
# Page Configuration
# ----------------------------------------

st.set_page_config(
    page_title="AI NLP Toolkit",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI LLM Toolkit")
st.markdown("### Powered by OPENAI")

# ----------------------------------------
# Sidebar
# ----------------------------------------

option = st.sidebar.radio(
    "Choose Module",
    (
        "🏠 Home",
        "😊 Sentiment Analysis",
        "🚫 Spam Detection",
        "🌍 Language Detection",
        "📰 News Classification",
        "🌐 Machine Translation"
    )
)

# ----------------------------------------
# Home
# ----------------------------------------

if option == "🏠 Home":

    st.header("Welcome 👋")

    st.info("""
This application contains five AI modules.

✅ Sentiment Analysis

✅ Spam Detection

✅ Language Detection

✅ News Classification

✅ Machine(Language) Translation
""")

# ----------------------------------------
# Sentiment
# ----------------------------------------

elif option == "😊 Sentiment Analysis":
    st.header("😊 Sentiment Analysis")

    review = st.text_area("Enter Review")

    if st.button("Analyze Sentiment"):

        if review.strip():

            result = predict_sentiment(review)

            st.success(f"Sentiment : {result.sentiment}")
            st.write(f"Confidence : {result.prob:.2f}")

        else:

            st.warning("Please enter a review.")

    uploaded_file = st.file_uploader("Upload CSV and Excel file only",type=["csv","xlsx"])
    if uploaded_file is not None:
        if uploaded_file.name.endswith(".csv"): 
            df = pd.read_csv(uploaded_file,header=None)
        else:
            df = pd.read_excel(uploaded_file,header=None)
        df.columns=["message"]
        results = []
        for msg in df["message"]:
            result = predict_sentiment(msg)
            results.append({"Message": msg,"Prediction":result.sentiment,"Confidence":result.prob})

        result_df = pd.DataFrame(results)
        st.dataframe(result_df)          
        csv = result_df.to_csv(index=False)
        st.download_button(label="📥 Download Results",data=csv,file_name="prediction_results.csv",mime="text/csv")
# ----------------------------------------
# Spam
# ----------------------------------------

elif option == "🚫 Spam Detection":

    st.header("🚫 Spam Detection")

    message = st.text_area("Enter Message")

    if st.button("Detect Spam"):

        if message.strip():

            result = predict_spam(message)

            st.success(f"Prediction : {result.spam}")
            st.write(f"Confidence : {result.prob:.2f}")

        else:

            st.warning("Please enter a message.")
    
    uploaded_file = st.file_uploader("Upload CSV and Excel file only",type=["csv","xlsx"])
    if uploaded_file is not None:
        if uploaded_file.name.endswith(".csv"): 
            df = pd.read_csv(uploaded_file,header=None)
        else:
            df = pd.read_excel(uploaded_file,header=None)
        df.columns=["message"]
        results = []
        for msg in df["message"]:
            result = predict_spam(msg)
            results.append({"Message": msg,"Prediction":result.spam,"Confidence":result.prob})

        result_df = pd.DataFrame(results)
        st.dataframe(result_df)          
        csv = result_df.to_csv(index=False)
        st.download_button(label="📥 Download Results",data=csv,file_name="prediction_results.csv",mime="text/csv")
# ----------------------------------------
# Language Detection
# ----------------------------------------

elif option == "🌍 Language Detection":

    st.header("🌍 Language Detection")

    text = st.text_area("Enter Text")

    if st.button("Detect Language"):

        if text.strip():

            result = detect_language(text)

            st.success(f"Language : {result.language}")
            st.write(f"Confidence : {result.prob:.2f}")

        else:

            st.warning("Please enter text.")
    
    uploaded_file = st.file_uploader("Upload CSV and Excel file only",type=["csv","xlsx"])
    if uploaded_file is not None:
        if uploaded_file.name.endswith(".csv"): 
            df = pd.read_csv(uploaded_file,header=None)
        else:
            df = pd.read_excel(uploaded_file,header=None)
        df.columns=["message"]
        results = []
        for msg in df["message"]:
            result = detect_language(msg)
            results.append({"Message": msg,"Prediction":result.language,"Confidence":result.prob})

        result_df = pd.DataFrame(results)
        st.dataframe(result_df)          
        csv = result_df.to_csv(index=False)
        st.download_button(label="📥 Download Results",data=csv,file_name="prediction_results.csv",mime="text/csv")        

# ----------------------------------------
# News Classification
# ----------------------------------------

elif option == "📰 News Classification":

    st.header("📰 News Classification")

    news = st.text_area("Paste News")

    if st.button("Classify News"):

        if news.strip():

            result = classify_news(news)

            st.success(f"Category : {result.news}")
            st.write(f"Confidence : {result.prob:.2f}")

        else:

            st.warning("Please enter news.")
    
    uploaded_file = st.file_uploader("Upload CSV and Excel file only",type=["csv","xlsx"])
    if uploaded_file is not None:
        if uploaded_file.name.endswith(".csv"): 
            df = pd.read_csv(uploaded_file,header=None)
        else:
            df = pd.read_excel(uploaded_file,header=None)
        df.columns=["message"]
        results = []
        for msg in df["message"]:
            result = classify_news(msg)
            results.append({"Message": msg,"Prediction":result.news,"Confidence":result.prob})

        result_df = pd.DataFrame(results)
        st.dataframe(result_df)          
        csv = result_df.to_csv(index=False)
        st.download_button(label="📥 Download Results",data=csv,file_name="prediction_results.csv",mime="text/csv")        

# ----------------------------------------
# Translation
# ----------------------------------------

elif option == "🌐 Machine Translation":

    st.header("🌐 Machine Translation")

    text = st.text_area("Enter Text")

   
    result = translate_text(text)   # Sirf detect kare
    st.text(f"Detected Language:{result.lang_detect}")
    target = st.selectbox(
        "Translate To",
        [
            "English",
            "Hindi",
            "French",
            "German",
            "Japanese",
            "Spanish",
            "Mandarin",
            "Korean"
            
        ]
    )
    
    if st.button("Translate"):
        if text.strip():

            result = translate_text(text,target)
            
            st.success(result.translated)
            st.text(result.prob)

        else:

            st.warning("Please enter text.")
            