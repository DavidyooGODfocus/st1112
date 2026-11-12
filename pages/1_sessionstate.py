import streamlit as st

st.title("정수와 유리수의 덧셈과 뺄셈")
A,B,C = st.tabs(["복습하기","활동하기","연습하기"])

with A:
    st.subheader("저번 시간에 배운 걸 떠올려봅시다!")


with B:
    st.write("")


with C:
    option2 = [
    r"$2-3-(-3)$",
    r"$4+(-2)$",
    r"$-2-(-1)+3$",
    r"$1+3-(-2)$",
    r"$1-3-(-4)$",]
        
    with st.form("forms2"):
        choice2 = st.radio(
            "다음 중 계산했을 때 $2$가 나오지 **않는** 식을 고르시오~",
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