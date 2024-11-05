import streamlit as st

# 페이지 제목
st.title('처음 만난 Stramlit😁hahaha')

# 헤더
st.header('This is header')

# 서브헤더
st.subheader('This is subheader')

# 텍스트
st.text('안녕하세요. 저는 일반 텍스트입니다.ㅋㅋㅋ')

# 마크다운
st.markdown('''**목록**을 *보여드리겠습니다.*
1. meat
2. pizza
3. bacon
''')

# write 매직메소드
# 전달된 데이터의 특성에 따라 자동 포매팅된다
# markdown, html, dataframe, chart 등 모두 가능
st.write('***write**은 **마크다운** 문법을 지원합니다.')
st.write('<mark>저는 html 작성도 가능해요...</mark>', unsafe_allow_html=True) # html태그로 처리
st.write('텍스트의 컬러를 지정할 수 있습니다. :red[노을], :blue[바다], :green[나뭇잎]')

# metric 지표 등 시각화
st.metric(label = '**온도**', value = '10℃', delta = '-3.7℃')
st.metric(label = '**AAPL**',  value = '$1027', delta = '-$55')

# 컬럼 사용
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label = 'USD', value = '1310', delta = '+11')
with col2:
    st.metric(label = 'KRW', value = '1000', delta = '0')
with col3:
    st.metric(label = 'JPY', value = '887', delta = '-9')
