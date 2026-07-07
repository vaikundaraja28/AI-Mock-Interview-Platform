import streamlit as st


def load_theme():
    st.markdown("""
<style>

/* ==========================
   HIDE STREAMLIT DEFAULT UI
========================== */

#MainMenu{
visibility:hidden;
}

header{
visibility:hidden;
}

footer{
visibility:hidden;
}

/* ==========================
   GLOBAL APP
========================== */

.stApp{
background:linear-gradient(
135deg,
#020617 0%,
#0F172A 45%,
#111827 100%
);

color:white;
}

.block-container{
padding-top:2rem;
padding-left:4rem;
padding-right:4rem;
max-width:1400px;
}

/* ==========================
   TITLES
========================== */

.title{

font-size:64px;

font-weight:800;

text-align:center;

color:white;

margin-bottom:8px;

}

.subtitle{

font-size:22px;

text-align:center;

color:#94A3B8;

margin-bottom:45px;

}

/* ==========================
   METRIC CARDS
========================== */

.metric-card{

background:rgba(255,255,255,.06);

border:1px solid rgba(255,255,255,.08);

border-radius:22px;

padding:35px;

text-align:center;

backdrop-filter:blur(18px);

transition:.35s;

height:180px;

display:flex;

flex-direction:column;

justify-content:center;

align-items:center;

}

.metric-card:hover{

transform:translateY(-8px);

box-shadow:0 20px 40px rgba(59,130,246,.30);

}

.metric-card h2{

font-size:54px;

margin:0;

font-weight:700;

color:white;

}

.metric-card p{

margin-top:10px;

font-size:22px;

color:#CBD5E1;

}

.metric-card:hover{

transform:translateY(-8px);

box-shadow:0 20px 40px rgba(59,130,246,.20);

}

.metric-card h2{

font-size:48px;

margin-bottom:8px;

color:white;

}

.metric-card p{

font-size:20px;

color:#CBD5E1;

}

/* ==========================
   BUTTONS
========================== */

.stButton > button{

width:100%;

height:72px;

border:none;

border-radius:20px;

font-size:22px;

font-weight:700;

color:white;

background:linear-gradient(
135deg,
#2563EB,
#3B82F6,
#60A5FA
);

transition:all .35s ease;

box-shadow:0 12px 28px rgba(37,99,235,.35);

}

.stButton > button:hover{

transform:translateY(-6px);

background:linear-gradient(
135deg,
#3B82F6,
#60A5FA,
#93C5FD
);

box-shadow:0 20px 45px rgba(37,99,235,.55);

}

.stButton > button:active{

transform:scale(.97);

}

/* ==========================
   ACTION CARDS
========================== */

.action-card{

background:linear-gradient(
135deg,
#1E293B,
#0F172A
);

border:1px solid rgba(255,255,255,.08);

border-radius:24px;

padding:30px;

height:240px;

transition:all .35s ease;

box-shadow:0 10px 30px rgba(0,0,0,.35);

}

.action-card:hover{

transform:translateY(-10px);

box-shadow:0 20px 45px rgba(59,130,246,.30);

}

.action-icon{

font-size:55px;

margin-bottom:18px;

}

.action-title{

font-size:30px;

font-weight:700;

color:white;

margin-bottom:12px;

}

.action-desc{

font-size:18px;

color:#CBD5E1;

line-height:1.6;

}

/* ==========================
   DIVIDERS
========================== */

hr{

border:1px solid rgba(255,255,255,.08);

margin-top:30px;

margin-bottom:30px;

}

/* ==========================
   SCROLLBAR
========================== */

::-webkit-scrollbar{

width:10px;

}

::-webkit-scrollbar-thumb{

background:#3B82F6;

border-radius:20px;

}

::-webkit-scrollbar-track{

background:#111827;

}

</style>
""", unsafe_allow_html=True)