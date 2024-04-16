import streamlit as st
import requests

st.set_page_config(
    page_title="FAQ",
    page_icon="🆀",
)


def send_post_request(user_message):
    url = "https://uaens61u81.execute-api.us-east-1.amazonaws.com/query"
    headers = {"Content-Type": "application/json"}
    payload = {"body": {"user_message": user_message}}

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}"


def save_message(message, role):
    st.session_state["messages"].append({"message": message, "role": role})


def send_message(message, role, save=True):
    with st.chat_message(role):
        st.markdown(message)
    if save:
        save_message(message, role)


def show_messages_history():
    if st.session_state["messages"] != []:
        for message in st.session_state["messages"]:
            send_message(
                message["message"],
                message["role"],
                save=False,
            )


st.title("FAQ")
st.header(":blue[Notice]", divider="rainbow")
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
st.divider()
if "messages" not in st.session_state:

    st.session_state["messages"] = []

send_message("안녕하세요. 무엇이 궁금하신가요?", "ai", save=False)
show_messages_history()
message = st.chat_input("Ask anything about your file...")
if message:
    send_message(message, "human")

    with st.chat_message("ai"):
        with st.spinner("AI 응답 요청중..."):
            ai_response = send_post_request(message)
            ai_message = ai_response["response"]["content"]
            metadata = ai_response["response"]["response_metadata"]
            save_message(ai_message, "ai")
            st.write(ai_message)
            st.write(metadata)
