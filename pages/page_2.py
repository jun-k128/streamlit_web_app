import streamlit as st

with st.form(key='profile_form'):
        
# テキストボックス
        name = st.text_input('名前')
        adress = st.text_input('住所')

#セレクトボックス / ラジオボタン st.selectbox / st. radio
        age_category = st.selectbox(
                '年齢層',
                ('子ども(18才未満)', '大人（18才以上）'))
        sex_category = st.radio(
                '性別',
                ('男性', '女性'))
#複数選択（戻り値>リスト）
        hobby = st.multiselect(
                '趣味',
                ('スポーツ', '読書', 'プログラミング', 'アニメ・映画', '釣り', '料理'))
       
#ボタン
        submit_btn = st.form_submit_button('送信')
        cancel_btn = st.form_submit_button('キャンセル')
# print(f'submit_btn: {submit_btn}')
# print(f'cancel_btn: {cancel_btn}')
        if submit_btn:
                st.text(f'ようこそ！{name}さん！{adress}に書籍を送りました！')
                st.text(f'年齢層：{age_category}')
                st.text(f'性別：{sex_category}')
                st.text(f'趣味：{", ".join(hobby)}')