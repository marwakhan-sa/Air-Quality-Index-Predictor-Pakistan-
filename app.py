import streamlit as st
import joblib
import numpy as np

model = joblib.load('model/aqi_model.pkl')
le = joblib.load('model/label_encoder.pkl')

st.set_page_config(page_title="Pakistan AQI Predictor", page_icon="🌿", layout="centered")

st.markdown("""
    <style>
        /* Background */
        .stApp { background-color: #f0f7f0; }

        /* Hide streamlit default header */
        header { visibility: hidden; }

        /* Hero section */
        .hero {
            background: linear-gradient(135deg, #1b4332, #2d6a4f);
            border-radius: 24px;
            padding: 2.5rem 2rem;
            text-align: center;
            margin-bottom: 2rem;
        }
        .hero-title {
            color: #d8f3dc;
            font-size: 3.2rem;
            font-weight: 800;
            margin: 0;
            letter-spacing: -0.5px;
        }
        .hero-sub {
            color: #95d5b2;
            font-size: 1rem;
            margin-top: 0.5rem;
        }
        .hero-badge {
            display: inline-block;
            background: #52b788;
            color: #1b4332;
            font-size: 0.75rem;
            font-weight: 700;
            padding: 4px 14px;
            border-radius: 50px;
            margin-bottom: 1rem;
            letter-spacing: 1px;
            text-transform: uppercase;
        }

        /* Cards */
        .card {
            background: white;
            border-radius: 20px;
            padding: 1.8rem;
            border: 1px solid #d8f3dc;
            margin-bottom: 1.2rem;
        }
        .card-title {
            font-size: 0.8rem;
            font-weight: 700;
            color: #52b788;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            margin-bottom: 1rem;
        }

        /* Slider labels */
        .pollutant-label {
            font-size: 0.95rem;
            font-weight: 600;
            color: #1b4332;
            margin-bottom: 0.2rem;
        }
        .pollutant-desc {
            font-size: 0.78rem;
            color: #74c69d;
            margin-bottom: 0.5rem;
        }

        /* Sliders */
        .stSlider [data-baseweb="slider"] {
            margin-top: -0.5rem;
        }

        /* Predict button */
        .stButton > button {
            background: linear-gradient(135deg, #2d6a4f, #52b788) !important;
            color: white !important;
            border: none !important;
            border-radius: 50px !important;
            padding: 0.75rem 2rem !important;
            font-size: 1rem !important;
            font-weight: 600 !important;
            width: 100% !important;
            transition: all 0.3s ease !important;
            letter-spacing: 0.5px;
        }
        .stButton > button:hover {
            opacity: 0.9 !important;
            transform: translateY(-1px) !important;
        }

        /* Result box */
        .result-box {
            border-radius: 20px;
            padding: 2rem;
            text-align: center;
            margin-top: 1.5rem;
            border: 1px solid rgba(0,0,0,0.06);
        }
        .result-emoji { font-size: 3rem; margin-bottom: 0.5rem; }
        .result-label { font-size: 0.85rem; font-weight: 600; letter-spacing: 1px; text-transform: uppercase; opacity: 0.7; }
        .result-value { font-size: 2rem; font-weight: 800; margin: 0.3rem 0; }
        .result-desc { font-size: 0.9rem; opacity: 0.8; margin-top: 0.5rem; }

        /* AQI level colors */
        .good { background: #d8f3dc; color: #1b4332; }
        .moderate { background: #fff9c4; color: #5c4a00; }
        .sensitive { background: #ffe8cc; color: #7a3e00; }
        .unhealthy { background: #ffd6d6; color: #7a0000; }
        .very-unhealthy { background: #e8d5f5; color: #3d0066; }
        .hazardous { background: #2c2c2c; color: #f5f5f5; }

        /* Stats row */
        .stat-box {
            background: #f0f7f0;
            border-radius: 14px;
            padding: 1rem;
            text-align: center;
            border: 1px solid #d8f3dc;
        }
        .stat-value { font-size: 1.4rem; font-weight: 700; color: #2d6a4f; }
        .stat-label { font-size: 0.75rem; color: #74c69d; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; }

        /* Footer */
        .footer {
            text-align: center;
            color: #95d5b2;
            font-size: 0.8rem;
            margin-top: 2rem;
            padding-bottom: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="hero">
        <div class="hero-badge">🌿 Pakistan</div>
        <div class="hero-title">Air Quality Predictor</div>
        <div class="hero-sub">Enter pollutant levels to instantly predict the AQI category</div>
    </div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="stat-box"><div class="stat-value">307</div><div class="stat-label">Cities</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="stat-box"><div class="stat-value">6</div><div class="stat-label">AQI Levels</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="stat-box"><div class="stat-value">100%</div><div class="stat-label">Accuracy</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


st.markdown('<div class="card"><div class="card-title">Pollutant Levels</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="pollutant-label">CO AQI</div><div class="pollutant-desc">Carbon Monoxide</div>', unsafe_allow_html=True)
    co = st.slider("CO", 0, 500, 1, label_visibility="collapsed")

    st.markdown('<div class="pollutant-label">Ozone AQI</div><div class="pollutant-desc">Ground-level Ozone</div>', unsafe_allow_html=True)
    ozone = st.slider("Ozone", 0, 500, 50, label_visibility="collapsed")

with col2:
    st.markdown('<div class="pollutant-label">NO2 AQI</div><div class="pollutant-desc">Nitrogen Dioxide</div>', unsafe_allow_html=True)
    no2 = st.slider("NO2", 0, 500, 1, label_visibility="collapsed")

    st.markdown('<div class="pollutant-label">PM2.5 AQI</div><div class="pollutant-desc">Fine Particulate Matter</div>', unsafe_allow_html=True)
    pm25 = st.slider("PM2.5", 0, 500, 100, label_visibility="collapsed")

st.markdown('</div>', unsafe_allow_html=True)

_, btn_col, _ = st.columns([1, 2, 1])
with btn_col:
    predict = st.button("Predict Air Quality")

if predict:
    input_data = np.array([[co, ozone, no2, pm25]])
    prediction = model.predict(input_data)
    category = le.inverse_transform(prediction)[0]

    style_map = {
        'Good':                           ('good',          '🌿', 'Good',              'Air quality is satisfactory. Safe for everyone.'),
        'Moderate':                       ('moderate',      '🌤', 'Moderate',           'Acceptable quality. Unusually sensitive people should consider limiting outdoor activity.'),
        'Unhealthy for Sensitive Groups': ('sensitive',     '⚠', 'Sensitive Groups',   'Children, elderly, and sensitive individuals should reduce outdoor exposure.'),
        'Unhealthy':                      ('unhealthy',     '😷', 'Unhealthy',          'Everyone may experience health effects. Limit prolonged outdoor activity.'),
        'Very Unhealthy':                 ('very-unhealthy','🚨', 'Very Unhealthy',     'Health alert! Everyone should avoid outdoor activity.'),
        'Hazardous':                      ('hazardous',     '☠', 'Hazardous',          'Emergency conditions. Stay indoors and avoid all outdoor exposure.')
    }

    css_class, emoji, label, description = style_map.get(category, ('moderate', '🌤️', category, ''))

    st.markdown(f"""
        <div class="result-box {css_class}">
            <div class="result-label">Predicted AQI Category</div>
            <div class="result-value">{label}</div>
            <div class="result-desc">{description}</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="footer">Built with Pakistan AQI Data · Random Forest Model · Streamlit</div>', unsafe_allow_html=True)