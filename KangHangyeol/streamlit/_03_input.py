import streamlit as st
import pandas as pd

# 사용자 입력을 처리할 수 있는 다양한 요소 제공
st.title('Input Elements')

# 버튼
st.header('Button')

clicked = st.button('Click me!')
if clicked:
    st.write('버튼을 클릭하셨습니다.')

if st.button('안녕'):
    st.write('너도 안녕~')
else:
    st.write('**안녕**을 클릭해보세요.') # 클릭 전 기본값

# callback 함수 : 버튼 클릭시 특정 함수 호출
def foo():
    st.write('함수는 함수입니다.')
st.button('이 버튼을 누르면 문장이 출력됩니다.', on_click=foo)

if st.button('이렇게 하면 아래쪽에 출력되네요.', key = 'unique_button_key'):
    foo()

# 파일 다운로드
students_df = pd.DataFrame({
    'Name' : ['hg', 'yz', 'ng'],
    'Age' : [27, 25, 20],
    'Score' : [99, 98, 92]
})
st.download_button(
    label = '학생 데이터 다운로드',
    data = students_df.to_csv(),
    file_name = 'students.csv',
    mime = 'text/csv' # 파일 형식
)

# 이미지 파일 다운로드
with open('./data/molang.jpg', 'rb') as f:
    st.download_button(
        label = '몰랑이 이미지 다운로드',
        data = f,
        file_name='molang.jpg',
        mime='image/jpeg' # 파일형식
    )

# 텍스트 / 숫자 입력
st.header('텍스트 / 숫자 입력')
name = st.text_input(
    label = '당신의 이름을 입력하세요.',
    placeholder = '이름',
    value = 'hg' # 초기값
)
print(name)
st.write(f'당신의 이름은 :blue[**{name}**]입니다.')

age = st.number_input(
    label = '나이를 입력하세요.',
    min_value = 0,
    max_value = 120,
    step = 2 # +-버튼 step 조정
)
st.write(f'당신의 나이는 :green[**{age}**]세입니다.')

st.header('선택')
# 평점 입력
rating_nums = [1,2,3,4,5]
rating_idx = st.feedback('stars') # thumbs, faces...

if rating_idx is not None:
    st.write(f'당신이 주신 평점은 {rating_nums[rating_idx]}점입니다.')

# 라디오(택1)
mbti = st.radio(
    label = '당신의 MBTI는 무엇입니까?',
    options = ['ISTJ', 'ESTJ', 'INTP', 'INTJ', '모름'],
    index = 4 # 초기값 설정
)
if mbti != '모름':
    st.write(f'당신의 MBTI는 :red[**{mbti}**]입니다.')

# 체크박스(boolean형 체크박스)
checked = st.checkbox('동의하십니까?')
st.write(f"동의여부 : {'동의' if checked else '비동의'}")

# 다중선택
st.multiselect(
    label ='좋아하는 과일을 입력하세요.',
    options = ['사과', '파인애플', '바나나', '키위']
)