import streamlit as st

# ==================================================
# 1. 페이지 기본 설정
# ==================================================
st.set_page_config(
    page_title="MBTI 포켓몬 단짝 찾기 💛",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ==================================================
# 2. 디자인 CSS
# ==================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Jua&family=Noto+Sans+KR:wght@400;500;700;900&display=swap');

:root {
    --cream: #fff9ed;
    --yellow: #ffe59a;
    --yellow-dark: #f4c84b;
    --brown: #5c4935;
    --pink: #ffe6df;
    --green: #e6f2d9;
}

.stApp {
    background: var(--cream);
    color: var(--brown);
    font-family: 'Noto Sans KR', sans-serif;
}

.block-container {
    max-width: 900px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3 {
    color: var(--brown) !important;
    font-family: 'Jua', 'Noto Sans KR', sans-serif !important;
}

.hero {
    text-align: center;
    padding: 24px 10px 28px;
}

.hero-tag {
    display: inline-block;
    background: var(--yellow);
    border-radius: 30px;
    padding: 7px 18px;
    font-size: 14px;
    font-weight: 900;
    letter-spacing: 1px;
}

.hero-title {
    font-family: 'Jua', sans-serif;
    font-size: clamp(34px, 7vw, 52px);
    line-height: 1.35;
    margin: 20px 0 12px;
    color: var(--brown);
}

.hero-desc {
    color: #826e55;
    font-size: 17px;
    line-height: 1.9;
}

.section-heading {
    font-family: 'Jua', sans-serif;
    font-size: 25px;
    margin: 15px 0 8px;
}

.section-desc {
    color: #8c7860;
    margin-bottom: 20px;
    font-size: 15px;
}

div.stButton > button {
    width: 100%;
    min-height: 52px;
    border: 2px solid #f0e3c8;
    border-radius: 15px;
    background: #fffdf7;
    color: #5c4935;
    font-size: 17px;
    font-weight: 900;
    transition: all 0.15s ease;
}

div.stButton > button:hover {
    border-color: #edc64f;
    background: #fff0bd;
    color: #5c4935;
    transform: translateY(-2px);
}

div.stButton > button:focus {
    box-shadow: 0 0 0 3px #ffe59a;
    border-color: #d9ac35;
    color: #5c4935;
}

.pokemon-card {
    background: white;
    border: 2px solid #f0e4ca;
    border-radius: 28px;
    padding: 26px 24px;
    text-align: center;
    box-shadow: 0 8px 0 rgba(210, 182, 126, 0.12);
    margin-top: 10px;
}

.result-tag {
    display: inline-block;
    padding: 7px 17px;
    background: var(--yellow);
    border-radius: 30px;
    font-size: 14px;
    font-weight: 900;
}

.pokemon-name {
    font-family: 'Jua', sans-serif;
    font-size: clamp(30px, 6vw, 42px);
    margin: 12px 0 4px;
    color: var(--brown);
    word-break: keep-all;
}

.pokemon-en {
    color: #90795b;
    font-size: 17px;
    font-weight: 700;
}

.type-pill {
    display: inline-block;
    background: #fff1c8;
    border-radius: 20px;
    padding: 6px 14px;
    margin: 12px 4px 4px;
    font-size: 15px;
    font-weight: 800;
}

.info-box {
    background: #fff8e8;
    border-radius: 18px;
    padding: 18px 20px;
    margin-top: 17px;
    text-align: left;
    line-height: 1.9;
    color: #5c4935;
}

.info-title {
    font-family: 'Jua', sans-serif;
    font-size: 20px;
    margin-bottom: 8px;
}

.match-box {
    background: var(--green);
    border-radius: 18px;
    padding: 18px;
    margin-top: 16px;
    text-align: center;
}

.match-box p {
    line-height: 1.9;
    margin-bottom: 0;
}

.footer-note {
    color: #a08c73;
    text-align: center;
    font-size: 13px;
    margin-top: 25px;
    line-height: 1.8;
}

div[data-testid="stImage"] img {
    object-fit: contain;
}

@media (max-width: 600px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }
    .hero-title {
        font-size: 35px;
    }
    .pokemon-card {
        padding: 20px 14px;
    }
}
</style>
""", unsafe_allow_html=True)


# ==================================================
# 3. 포켓몬 데이터
# 이미지: PokéAPI sprites 저장소의 공식 아트워크
# ==================================================
POKEMON = {
    "INTJ": {
        "name": "뮤츠", "en": "Mewtwo", "id": 150,
        "types": ["에스퍼"],
        "feature": "뛰어난 지능과 강력한 집중력을 가진 포켓몬",
        "reason": "큰 그림을 먼저 보고 전략적으로 생각하는 모습이 닮았어요. "
                  "혼자 깊이 고민하고 목표를 향해 나아가는 INTJ에게 어울려요.",
        "partner": "ENFP",
        "partner_name": "피카츄",
    },
    "INTP": {
        "name": "메타몽", "en": "Ditto", "id": 132,
        "types": ["노말"],
        "feature": "다른 포켓몬으로 변신할 수 있는 신비로운 포켓몬",
        "reason": "호기심이 많고 다양한 가능성을 탐구하는 모습이 닮았어요. "
                  "틀에 얽매이지 않는 생각과 유연한 사고가 매력적이에요.",
        "partner": "ENTJ",
        "partner_name": "리자몽",
    },
    "ENTJ": {
        "name": "리자몽", "en": "Charizard", "id": 6,
        "types": ["불꽃", "비행"],
        "feature": "강한 힘과 자신감으로 하늘을 나는 포켓몬",
        "reason": "목표를 향해 과감하게 도전하는 모습이 닮았어요. "
                  "리더십과 추진력을 발휘해 어려운 일에도 도전하는 타입이에요.",
        "partner": "INTP",
        "partner_name": "메타몽",
    },
    "ENTP": {
        "name": "루카리오", "en": "Lucario", "id": 448,
        "types": ["격투", "강철"],
        "feature": "파동을 감지해 주변의 움직임을 알아차리는 포켓몬",
        "reason": "새로운 방법을 찾고 상황에 따라 재치 있게 대응하는 모습이 닮았어요. "
                  "호기심과 도전 정신으로 색다른 해결책을 발견해요.",
        "partner": "INFJ",
        "partner_name": "가디안",
    },
    "INFJ": {
        "name": "가디안", "en": "Gardevoir", "id": 282,
        "types": ["에스퍼", "페어리"],
        "feature": "소중한 사람을 지키려는 마음이 강한 포켓몬",
        "reason": "다른 사람의 마음을 섬세하게 이해하는 모습이 닮았어요. "
                  "깊은 공감 능력과 소중한 사람을 지키려는 따뜻함이 있어요.",
        "partner": "ENTP",
        "partner_name": "루카리오",
    },
    "INFP": {
        "name": "이브이", "en": "Eevee", "id": 133,
        "types": ["노말"],
        "feature": "여러 모습으로 진화할 수 있는 가능성 가득한 포켓몬",
        "reason": "자신만의 가치관과 풍부한 상상력을 소중히 여기는 모습이 닮았어요. "
                  "다양한 가능성을 품고 자기만의 길을 찾아가는 타입이에요.",
        "partner": "ENFJ",
        "partner_name": "님피아",
    },
    "ENFJ": {
        "name": "님피아", "en": "Sylveon", "id": 700,
        "types": ["페어리"],
        "feature": "리본 모양 촉수로 마음을 전하는 다정한 포켓몬",
        "reason": "주변 사람을 응원하고 따뜻한 분위기를 만드는 모습이 닮았어요. "
                  "다른 사람의 장점을 발견하고 함께 성장하는 걸 좋아해요.",
        "partner": "INFP",
        "partner_name": "이브이",
    },
    "ENFP": {
        "name": "피카츄", "en": "Pikachu", "id": 25,
        "types": ["전기"],
        "feature": "전기를 모으고 친구들과 모험을 즐기는 포켓몬",
        "reason": "호기심이 많고 새로운 경험을 즐기는 모습이 닮았어요. "
                  "밝은 에너지와 톡톡 튀는 아이디어로 주변을 즐겁게 해요.",
        "partner": "INTJ",
        "partner_name": "뮤츠",
    },
    "ISTJ": {
        "name": "거북왕", "en": "Blastoise", "id": 9,
        "types": ["물"],
        "feature": "강력한 물대포를 지닌 든든한 포켓몬",
        "reason": "책임감 있게 맡은 일을 끝까지 해내는 모습이 닮았어요. "
                  "차분하고 꾸준하게 자신의 역할을 지키는 믿음직한 타입이에요.",
        "partner": "ESFP",
        "partner_name": "꼬부기",
    },
    "ISFJ": {
        "name": "해피너스", "en": "Blissey", "id": 242,
        "types": ["노말"],
        "feature": "다른 포켓몬을 보살피는 상냥한 포켓몬",
        "reason": "주변 사람을 세심하게 챙기고 배려하는 모습이 닮았어요. "
                  "작은 변화도 잘 알아차리고 행동으로 마음을 전해요.",
        "partner": "ESFP",
        "partner_name": "꼬부기",
    },
    "ESTJ": {
        "name": "윈디", "en": "Arcanine", "id": 59,
        "types": ["불꽃"],
        "feature": "용감하고 믿음직스러운 전설적인 포켓몬",
        "reason": "해야 할 일을 빠르게 정리하고 책임감 있게 행동하는 모습이 닮았어요. "
                  "강한 실행력과 든든한 태도로 주변에 믿음을 줘요.",
        "partner": "ISFP",
        "partner_name": "치라치노",
    },
    "ESFJ": {
        "name": "푸린", "en": "Jigglypuff", "id": 39,
        "types": ["노말", "페어리"],
        "feature": "노래로 주변을 사로잡는 사랑스러운 포켓몬",
        "reason": "사람들과 어울리고 모두가 즐거운 분위기를 만드는 모습이 닮았어요. "
                  "따뜻한 관심과 친근함으로 주변에 행복을 전해요.",
        "partner": "ISFP",
        "partner_name": "치라치노",
    },
    "ISTP": {
        "name": "메타그로스", "en": "Metagross", "id": 376,
        "types": ["강철", "에스퍼"],
        "feature": "네 개의 뇌를 가진 뛰어난 계산 능력의 포켓몬",
        "reason": "복잡한 문제도 침착하게 분석하는 모습이 닮았어요. "
                  "직접 시도하고 실용적인 해결책을 찾아내는 능력이 돋보여요.",
        "partner": "ESTP",
        "partner_name": "갸라도스",
    },
    "ISFP": {
        "name": "치라치노", "en": "Cinccino", "id": 573,
        "types": ["노말"],
        "feature": "부드러운 털과 깔끔한 감각을 지닌 포켓몬",
        "reason": "자신만의 취향과 감각을 소중히 여기는 모습이 닮았어요. "
                  "섬세하고 조용하지만 좋아하는 것에는 진심을 다하는 타입이에요.",
        "partner": "ESFJ",
        "partner_name": "푸린",
    },
    "ESTP": {
        "name": "갸라도스", "en": "Gyarados", "id": 130,
        "types": ["물", "비행"],
        "feature": "압도적인 힘과 대담함을 가진 포켓몬",
        "reason": "생각만 하기보다 직접 도전하고 경험하는 모습이 닮았어요. "
                  "빠른 판단력과 과감한 행동력으로 예상 밖의 상황에도 대응해요.",
        "partner": "ISTP",
        "partner_name": "메타그로스",
    },
    "ESFP": {
        "name": "꼬부기", "en": "Squirtle", "id": 7,
        "types": ["물"],
        "feature": "장난기 많고 친구들과 어울리기를 좋아하는 포켓몬",
        "reason": "지금 이 순간을 즐기고 사람들과 추억을 만드는 모습이 닮았어요. "
                  "밝은 에너지와 유쾌함으로 평범한 하루도 즐겁게 만들어요.",
        "partner": "ISTJ",
        "partner_name": "거북왕",
    },
}

MBTI_TYPES = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP",
]

# ==================================================
# 4. 제목
# ==================================================
st.markdown("""
<div class="hero">
    <div class="hero-tag">✨ POKÉMON BEST FRIEND ✨</div>
    <div class="hero-title">내 MBTI의<br>단짝 포켓몬은?</div>
    <div class="hero-desc">
        나와 성격이 닮은 포켓몬을 찾아봐요!<br>
        MBTI를 선택하면 특별한 단짝이 나타나요 💛
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="section-heading">🌼 나의 MBTI를 선택해 주세요</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="section-desc">'
    '16가지 유형 중 하나를 누르면 단짝 포켓몬을 만날 수 있어요.'
    '</div>',
    unsafe_allow_html=True,
)

# ==================================================
# 5. MBTI 선택 버튼 16개
# ==================================================
if "selected_mbti" not in st.session_state:
    st.session_state.selected_mbti = None

if "celebrate" not in st.session_state:
    st.session_state.celebrate = False

for row_start in range(0, len(MBTI_TYPES), 4):
    cols = st.columns(4, gap="small")

    for col_index, mbti in enumerate(
        MBTI_TYPES[row_start:row_start + 4]
    ):
        with cols[col_index]:
            if st.button(
                f"💛 {mbti}",
                key=f"mbti_{mbti}",
                use_container_width=True,
            ):
                st.session_state.selected_mbti = mbti
                st.session_state.celebrate = True

# ==================================================
# 6. 선택 결과 출력
# ==================================================
selected = st.session_state.selected_mbti

if selected:
    data = POKEMON[selected]

    # 처음 선택한 순간에만 축하 효과 실행
    if st.session_state.celebrate:
        st.balloons()
        st.toast(
            f"축하해요! {data['name']}가 단짝으로 찾아왔어요! 🎉",
            icon="🎉",
        )
        st.session_state.celebrate = False

    st.markdown("---")

    st.markdown(
        f'<div style="text-align:center; margin:20px 0;">'
        f'<span class="result-tag">🎉 {selected}의 단짝 포켓몬</span>'
        f'<h2 style="font-size:25px; margin-top:14px;">'
        f'운명의 단짝을 찾았어요!</h2>'
        f'</div>',
        unsafe_allow_html=True,
    )

    # 인터넷 이미지 주소
    image_url = (
        "https://raw.githubusercontent.com/PokeAPI/sprites/"
        "master/sprites/pokemon/other/official-artwork/"
        f"{data['id']}.png"
    )

    # 포켓몬 이미지와 이름
    st.markdown('<div class="pokemon-card">', unsafe_allow_html=True)

    image_col, detail_col = st.columns([1, 1.2], gap="large")

    with image_col:
        st.image(
            image_url,
            caption=f"{data['name']} · {data['en']}",
            use_container_width=True,
        )

    with detail_col:
        st.markdown(
            f'<div class="pokemon-name">{data["name"]}</div>'
            f'<div class="pokemon-en">{data["en"]}</div>',
            unsafe_allow_html=True,
        )

        type_html = "".join(
            f'<span class="type-pill">✨ {pokemon_type} 타입</span>'
            for pokemon_type in data["types"]
        )
        st.markdown(type_html, unsafe_allow_html=True)

        st.markdown(
            f'<div class="info-box">'
            f'<div class="info-title">🌟 포켓몬 특징</div>'
            f'{data["feature"]}'
            f'</div>',
            unsafe_allow_html=True,
        )

    st.markdown(
        f'<div class="info-box">'
        f'<div class="info-title">💛 나와 어울리는 이유</div>'
        f'{data["reason"]}'
        f'</div>',
        unsafe_allow_html=True,
    )

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(
        f'<div class="match-box">'
        f'<div class="info-title">🤝 함께하면 좋은 유형</div>'
        f'<h2 style="margin:5px 0;">{data["partner"]}</h2>'
        f'<p>이 유형과 함께하면 서로의 다른 장점을 발견하고 '
        f'새로운 경험을 나눌 수 있어요.</p>'
        f'<p>💫 궁합은 재미를 위한 추천이에요!</p>'
        f'</div>',
        unsafe_allow_html=True,
    )

    st.write("")

    if st.button(
        "🔄 다른 MBTI로 다시 찾기",
        use_container_width=True,
        type="primary",
    ):
        st.session_state.selected_mbti = None
        st.session_state.celebrate = False
        st.rerun()

else:
    st.markdown("""
    <div class="info-box" style="text-align:center; margin-top:22px;">
        <div class="info-title">🐣 단짝 포켓몬이 기다리고 있어요!</div>
        마음에 드는 MBTI 버튼을 눌러보세요.<br>
        어떤 포켓몬이 나올까요? ✨
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="footer-note">
    💛 포켓몬과 MBTI의 매칭은 재미를 위한 창작 결과예요.<br>
    포켓몬 이미지 출처: PokéAPI Sprites 저장소
</div>
""", unsafe_allow_html=True)
