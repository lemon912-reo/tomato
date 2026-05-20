import streamlit as st
import pandas as pd
import joblib

# =========================
# 페이지 기본 설정
# =========================
st.set_page_config(
    page_title="착과율 예측 시스템",
    page_icon="🍅",
    layout="centered"
)

# =========================
# 모델 불러오기
# =========================
# 예시: 저장된 모델 파일명
# rf_model.pkl 파일이 같은 폴더에 있어야 함
rf_model = joblib.load("tomato_model.pkl")

# =========================
# 제목 영역
# =========================
st.markdown("""
    <h1 style='text-align: center; color: #2E8B57;'>
        🍅 스마트팜 착과율 예측 시스템
    </h1>
""", unsafe_allow_html=True)

st.markdown("""
<div style="
    background-color:#F5FFF7;
    padding:20px;
    border-radius:15px;
    border:1px solid #DDEEDD;
    margin-bottom:20px;
">
<h4>📌 환경 데이터를 입력하면 AI가 착과율을 예측합니다.</h4>
</div>
""", unsafe_allow_html=True)

# =========================
# 입력 UI
# =========================
st.subheader("🌡️ 환경 데이터 입력")

col1, col2, col3 = st.columns(3)

with col1:
    temp = st.number_input(
        "내부온도 (℃)",
        min_value=0.0,
        max_value=50.0,
        value=25.0,
        step=0.1
    )

with col2:
    humidity = st.number_input(
        "내부습도 (%)",
        min_value=0.0,
        max_value=100.0,
        value=70.0,
        step=0.1
    )

with col3:
    soil_temp = st.number_input(
        "지온 (℃)",
        min_value=0.0,
        max_value=50.0,
        value=22.0,
        step=0.1
    )

st.markdown("<br>", unsafe_allow_html=True)

# =========================
# 예측 버튼
# =========================
if st.button("🔍 착과율 예측하기", use_container_width=True):

    # 입력 데이터를 DataFrame으로 변환
    input_data = pd.DataFrame(
        [[temp, humidity, soil_temp]],
        columns=['내부온도', '내부습도', '지온']
    )

    # 예측
    predicted = rf_model.predict(input_data)

    result = predicted[0]

    st.markdown("<br>", unsafe_allow_html=True)

    # 결과 카드 UI
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, #E8FFF1, #D8F3DC);
        padding:30px;
        border-radius:20px;
        text-align:center;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    ">
        <h2 style="color:#2E8B57;">📈 예측 결과</h2>
        <h1 style="font-size:60px; color:#1B5E20;">
            {result:.1f}%
        </h1>
        <p style="font-size:18px;">
            예상 착과율입니다.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # 진행 바 표시
    st.progress(min(int(result), 100))

# =========================
# 하단 설명
# =========================
st.markdown("---")

st.caption("AI 기반 스마트팜 환경 분석 시스템")