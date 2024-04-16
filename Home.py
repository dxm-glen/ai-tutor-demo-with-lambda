import streamlit as st

st.set_page_config(
    page_title="AI Tutor DEMO",
    page_icon="🏫",
)

st.title("AI Tutor DEMO")

st.header(":blue[Chat]", divider="rainbow")
st.caption(":blue[AWS Bedrock] 기반 질의응답 챗봇입니다!")
st.caption(
    ":blue[마지막 답변]에 대해서 :blue[사용 모델]과 :blue[토큰] 정보를 제공합니다."
)
st.caption("제가 알고 있는 :blue[기반 정보(knowledge base)]는 다음과 같습니다.")
st.caption(
    ":blue[입학 FAQ(html)] : FAQ_TOP11, 입학안내(공통), 신입학, 편입학, 위탁교육, 시간제, 등록금, 학사, 수업시험 등"
)
st.caption(":blue[Wine & Dine 제대로 알기 수업(txt)] : WD1222_02_01.txt ~ 02_04.text")
st.caption(":blue[미래반도체 수업 커리큘럼(txt)] : 강의자, 강의내용 등 커리큘럼 내용")

st.header(":blue[Quiz]", divider="rainbow")
st.caption(":blue[과목 선택] 후, :blue[퀴즈 생성] 버튼을 눌러서 퀴즈를 생성합니다.")
st.caption(
    "선택지를 :blue[고른 후] 하단 :blue[정답 확인] 버튼을 통해 정답을 확인합니다."
)
st.caption(
    "선택지를 :blue[변경 후] 하단 :blue[정답 확인] 다시 정답을 확인 할 수 있습니다."
)
st.caption(
    ":blue[새로운 퀴즈 생성]이 필요할 떄는 다시 :blue[퀴즈 생성] 버튼을 눌러주세요."
)
