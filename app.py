import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Movie Recap Script Generator", page_icon="🎬")
st.title("🎬 Movie Recap Script Generator (မြန်မာဘာသာ)")

api_key = st.text_input("Gemini API Key ထည့်ပါ:", type="password")
movie_title = st.text_input("ရုပ်ရှင် သို့မဟုတ် ဇာတ်လမ်းအမည်:")
genre = st.selectbox("ဇာတ်လမ်း အမျိုးအစား:", ["Suspense / Thriller", "Action", "Romance", "Horror", "Sci-Fi", "Drama", "Comedy"])
duration = st.select_slider("Script အရှည် (မိနစ်):", options=["3 မိနစ်", "5 မိနစ်", "10 မိနစ်"])

if st.button("🚀 Script ထုတ်ယူမည်"):
    if not api_key:
        st.error("ကျေးဇူးပြု၍ Gemini API Key ထည့်ပေးပါ။")
    elif not movie_title:
        st.warning("ရုပ်ရှင် သို့မဟုတ် ဇာတ်လမ်းအမည် ထည့်ပေးပါ။")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            prompt = f"ကျေးဇူးပြု၍ '{movie_title}' ဆိုသည့် {genre} ရုပ်ရှင်အတွက် TikTok/YouTube Movie Recap ပြုလုပ်ရန် {duration} စာခန့်ရှိသော စိတ်ဝင်စားဖွယ် မြန်မာလို Movie Recap Script တစ်ခု ရေးပေးပါ။ Voiceover ပြောရန် အသံထွက်ဇာတ်ညွှန်း အပြည့်အစုံ ပါဝင်ရပါမည်။"
            
            with st.spinner("Script ရေးသားနေပါသည်... ခဏစောင့်ပါ..."):
                response = model.generate_content(prompt)
                st.success("ဖန်တီးမှု အောင်မြင်ပါသည်။")
                st.markdown(response.text)
        except Exception as e:
            st.error(f"Error ဖြစ်ပွားပါသည်: {e}")
