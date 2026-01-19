import streamlit as st
import google.generativeai as genai

# 画面のタイトル
st.title("Gemini Webアプリ")

# APIキーを安全に取得（公開設定時に行います）
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("APIキーが設定されていません。")

# 入力フォーム
user_input = st.text_input("AIに聞きたいことを入力してください")

if st.button("送信"):
    if user_input:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(user_input)
        st.write("### AIの回答:")
        st.success(response.text)