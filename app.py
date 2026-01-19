import streamlit as st
import random

st.title("簡単おみくじアプリ")
st.write("ボタンを押して今日の運勢を占おう！")

if st.button("おみくじを引く"):
    results = ["大吉 🌟", "中吉 ✨", "小吉 🍀", "吉 ☀️", "末吉 🍃", "凶 ☁️"]
    luck = random.choice(results)
    st.header(f"結果は... {luck}")
    
    if "大吉" in luck:
        st.balloons() # 大吉の時だけ風船を飛ばす演出
