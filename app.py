import streamlit as st

st.title("(261112) Practice")
st.subheader("1. 식 전개하기")
st.latex(r"(x+y)^2")

a,b,c = st.tabs(["Q1","Q2","Q3"])
with a:
    st.write("Q1")
    options = [
    r"$x^2+y^2$",
    r"$x^2+xy+y^2$",
    r"$x^2-2xy+y^2$",
    r"$x^2+2xy+y^2$",
    ]

    with st.form("forms1"):
        # 1. 선택한 값을 변수(choice)에 저장
        choice1 = st.radio(
            "위의 수식을 전개한 식을 선택하시오",
            options,
            index=None,
        )
        st.session_state.choice1 = choice1
        submit_button1 = st.form_submit_button("제출")

    # 2. 제출 버튼 클릭 시 선택지별 맞춤 피드백 제공 (폼 바깥에 배치하면 화면이 더 깔끔합니다)
    if submit_button1:
        if st.session_state.choice1 is None:
            st.warning("⚠️ 답을 먼저 선택한 후 제출 버튼을 눌러주세요.")
        elif st.session_state.choice1 == options[3]:  # 정답: x^2 + 2xy + y^2
            st.success("🎉 정답입니다! $(x+y)(x+y)$를 분배법칙으로 정확히 전개했습니다.")
            st.balloons()
        elif st.session_state.choice1 == options[0]:  # 오답 1: x^2 + y^2
            st.error("❌ 아쉽습니다! 가장 흔히 하는 실수예요. 지수를 각각 분배하는 것이 아니라 $(x+y)(x+y)$를 전개해야 하므로 가운데 항이 생깁니다.")
        elif st.session_state.choice1 == options[1]:  # 오답 2: x^2 + xy + y^2
            st.error("❌ 거의 다 왔습니다! 분배법칙을 쓰면 $xy$ 항이 두 번 더해지므로 가운데 항의 계수를 다시 확인해 보세요.")
        else : # 오답 3: x^2 - 2xy + y^2
            st.error("❌ 부호를 다시 확인해 보세요! 선택한 식은 $(x-y)^2$을 전개한 결과입니다.")
with b:
    st.write("Q2")
    option2 = [
    r"$2-3-(-3)$",
    r"$4+(-2)$",
    r"$-2-(-1)+3$",
    r"$1+3-(-2)$",
    r"$1-3-(-4)$",]
        
    with st.form("forms2"):
        choice2 = st.radio(
            "다음 중 계산했을 때 $2$가 나오지 **않는** 식을 고르시오!",
            option2,
            index=None
        )
        submit_button2 = st.form_submit_button("제출")

    if submit_button2:
        if choice2 is None:
            st.warning("답을 선택한 후 제출 버튼을 눌러주세요.")
        elif choice2 == option2[3]:  # 정답: x^2 + 2xy + y^2
            st.success("🎉 정답입니다! $1+3=4$에서 $-2$를 뺐으니, 정수의 뺄셈 규칙에 따라 $4$에다 $2$를 더한 것이 되어, 4번째 수식의 결과는 $6$이 됩니다!")
            st.balloons()
        else  : # 오답 3: x^2 - 2xy + y^2
            st.error("❌ 부호를 다시 확인해 보세요! **음수**를 **뺐을 때** 어떻게 바뀌는지 기억해보세요!")

with c:
    st.write("Q3")

    with st.expander("***<눈>***", expanded=False):
        st.write("""
                    눈은 살아 있다
                    떨어진 눈은 살아있다
                    마당 위에 떨어진 눈은 살아있다

                    기침을 하자
                    젊은 詩人이여 기침을 하자
                    눈 위에 대고 기침을 하자
                    눈더러 보라고 마음놓고 마음놓고
                    기침을 하자

                    눈은 살아있다
                    죽음을 잊어버린 靈魂과 肉體를 위하여
                    눈은 새벽이 지나도록 살아있다

                    기침을 하자
                    젊은 詩人이여 기침을 하자
                    눈을 바라보며
                    밤새도록 고인 가슴의 가래라도
                    마음껏 뱉자
                    """)

    count=0
    if st.button("+1"):
        st.session_state.count+=1

        st.write(st.session_state.count)

import streamlit as st


st.title("11/12 실습")


# 초기화
if "saved_a1" not in st.session_state:
    st.session_state.saved_a1 = ""
if "saved_a2" not in st.session_state:
    st.session_state.saved_a2 = ""


with st.form("forms3"):
    a1 = st.number_input("a1")
    s1 = st.form_submit_button("제출 1")


if s1:
    st.session_state.saved_a1 = a1


with st.form("forms4"):
    a2 = st.number_input("a2")
    s2 = st.form_submit_button("제출 2")


if s2:
    st.session_state.saved_a2 = a2  

a1 = st.session_state.saved_a1
a2 = st.session_state.saved_a2
st.divider()
st.write("기억된 a1:", a1)
st.write("기억된 a2:", a2)
st.write(a1+a2)
