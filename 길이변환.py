import sys

# 1. Streamlit이 설치되어 있는지 확인 (웹용)
try:
    import streamlit as st
    is_web = True
except ImportError:
    is_web = False

def calculate(inch):
    return inch * 25.4

# --- 실행 부분 ---
if is_web:
    # 웹사이트로 접속했을 때 보여줄 화면
    st.title("📏 인치 변환기 (Web)")
    inch_val = st.number_input("인치를 입력하세요:", min_value=0.0)
    if inch_val > 0:
        st.success(f"{calculate(inch_val):.2f} mm입니다.")
else:
    # VS Code 터미널에서 실행했을 때 보여줄 화면
    print("📏 인치 변환기 (Terminal)")
    try:
        inch_val = float(input("인치를 입력하세요: "))
        print(f"결과: {calculate(inch_val):.2f} mm")
    except ValueError:
        print("숫자만 입력해주세요!")
