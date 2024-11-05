# 터미널에서 streamlit run '파일경로'
import streamlit as st
import pandas as pd

st.title('Hello')

# dataframe 생성
st.header('DataFrame')
students_df = pd.DataFrame({
    'Name' : ['hg', 'yz', 'ng'],
    'Age' : [27, 25, 20],
    'Score' : [99, 98, 92]
})

# dataframe(검색, 확장, 정렬 등 기능 있음)
# container 너비에 맞춰 확장
st.dataframe(students_df, use_container_width=True)
st.write(students_df)

# csv 불러오기
fish_df = pd.read_csv('./data/fish.csv')
st.dataframe(fish_df)

# 데이터 편집기
st.header('Data Editor')
movie_df = pd.DataFrame({
    'Title' : ['쇼생크탈출', '인셉션', '테넷'],
    'Rating' : [4.8, 4.7, 4.6],
    'Recommend' : [True, True, False]
})
edited_movie_df = st.data_editor(movie_df)
print(edited_movie_df)

# 최고 평점의 영화 출력
# idxmax는 최대값의 행인덱스 반환
favorite_movie_row = edited_movie_df.iloc[edited_movie_df['Rating'].idxmax()]
favorite_movie_title = (favorite_movie_row['Title'])
st.markdown(f'당신이 가장 좋아하는 영화는 :red[{favorite_movie_title}]입니다.')

# table(정적 테이블)
st.header('Table')
st.table(students_df)



