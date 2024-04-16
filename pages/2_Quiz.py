import streamlit as st
import requests
import os

st.set_page_config(
    page_title="Quiz",
    page_icon="🧐",
)
st.title("Quiz")
st.header(":blue[Notice]", divider="rainbow")
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
st.caption(
    ":blue[퀴즈 생성 오류 시] 다시 :blue[퀴즈 생성] 버튼을 눌러주세요. :blue[ai가 생성한 json 형식 오류]가 발생하는 경우가 간헐적있습니다."
)
st.divider()


def send_post_request(topic):
    url = "https://ywd37tyo8h.execute-api.us-east-1.amazonaws.com/query"
    headers = {"Content-Type": "application/json"}
    payload = {"body": {"topic": topic}}

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}"


col1, col2 = st.columns(2)

with col1:
    option = st.selectbox(
        "어떤 내용에 대한 퀴즈를 생성하실건가요?",
        ("Wine & Dine", "미래반도체 커리큘럼"),
        index=None,
        placeholder="과목 선택 대기중...",
    )

with col2:
    st.write("선택된 과목:", option)

    # 새로운 퀴즈 요청을 위한 버튼
    if st.button("퀴즈 생성"):
        with st.spinner("퀴즈 생성 중..."):
            st.session_state["quiz_data"] = send_post_request(option)

st.divider()

if "quiz_data" in st.session_state and st.session_state["quiz_data"]:
    ai_response = st.session_state["quiz_data"]
    response = ai_response["response"]
    with st.form("questions_form"):
        for question in response["questions"]:
            st.write(question["question"])
            value = st.radio(
                "정답을 고르세요.",
                [answer["answer"] for answer in question["answers"]],
                index=None,
                key=f'question_{question["question"]}',
            )

        if st.form_submit_button("정답 확인", type="primary"):
            # 정답 확인 로직
            for question in response["questions"]:
                correct_answer = next(
                    (answer for answer in question["answers"] if answer["correct"]),
                    None,
                )
                user_answer = st.session_state[f'question_{question["question"]}']
                if user_answer == correct_answer["answer"]:
                    st.success(f"Correct! {question['question']}")
                else:
                    st.error(f"Wrong! {question['question']}")
