import streamlit as st
from random import choice

hands = ["グー","チョキ","パー"]

st.title("岸部露伴とジャンケン")
st.caption("君、僕とジャンケンをしないか？")

st.subheader("露伴を負かせ")
st.text("ボタンを押して出す")

gu_btn = st.button("グー")
choki_btn = st.button("チョキ")
pa_btn = st.button("パー")

hand = choice(hands)
if gu_btn == True:
    st.text("ぐはあああ")
    if hand == "パー":
        st.text("意外ッ！それはパーッ！")
        st.text("サイコーの気分だねッ、ガキ負かすのは")
    elif hand == "グー":
        st.text("意外ッ！それはグーッ！")
        st.text("僕と同じ波長を感じるよ")
    else:
        st.text("意外ッ！それはチョキッ！")
        st.text("チッ、僕の負けだ")
if choki_btn ==True:
    st.text("ぐわあああ")
    if hand == "パー":
        st.text("意外ッ！それはパーッ！")
        st.text("チッ、僕の負けだ")
    elif hand == "チョキ":
        st.text("意外ッ！それはグーッ！")
        st.text("僕と同じ波長を感じるよ")
    else:
        st.text("意外ッ！それはチョキッ！")
        st.text("サイコーの気分だねッ、ガキ負かすのは")
if pa_btn == True:
    st.text("ぶった、ぶったね？2度もぶった！親父にもぶたれたことないのに！")
    if hand == "パー":
        st.text("意外ッ！それはパーッ！")
        st.text("僕と同じ波長を感じるよ")
    elif hand == "チョキ":
        st.text("意外ッ！それはグーッ！")
        st.text("チッ、僕の負けだ")
    else:
        st.text("意外ッ！それはチョキッ！")
        st.text("サイコーの気分だねッ、ガキ負かすのは")