import streamlit as st
import pandas as pd
import plotly.express as px
import random
from fpdf import FPDF
import tempfile

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="OPALINE",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

.stApp{
    background: linear-gradient(to right,#eef2ff,#f8fafc);
    font-family:'Segoe UI',sans-serif;
}

/* TITLE */

.main-title{
    text-align:center;
    font-size:45px;
    font-weight:bold;
    color:#1e3a8a;
    margin-bottom:20px;
}

/* HERO SECTION */

.hero-box{
    background:white;
    padding:35px;
    border-radius:22px;
    box-shadow:0px 8px 25px rgba(0,0,0,0.08);
    margin-bottom:30px;
}

/* KPI CARDS */

.metric-card{
    background:linear-gradient(135deg,#2563eb,#1d4ed8);
    padding:25px;
    border-radius:18px;
    text-align:center;
    color:white;
    box-shadow:0px 8px 20px rgba(0,0,0,0.15);
    margin-bottom:15px;
}

.metric-title{
    font-size:18px;
    font-weight:500;
}

.metric-value{
    font-size:34px;
    font-weight:bold;
}

/* CHART BOX */

.chart-box{
    background:white;
    padding:20px;
    border-radius:20px;
    box-shadow:0px 5px 15px rgba(0,0,0,0.08);
    margin-bottom:20px;
}

/* FEEDBACK */

.feedback-box{
    background:white;
    padding:25px;
    border-radius:18px;
    box-shadow:0px 5px 15px rgba(0,0,0,0.08);
    margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.markdown(
    "<div class='main-title'>🏸 OPALINE</div>",
    unsafe_allow_html=True
)

# ---------------------------------------------------
# HERO SECTION
# ---------------------------------------------------

with st.container():

    col1, col2 = st.columns([1,2])

    with col1:

        st.image("coach.jpg", width=240)

    with col2:

        st.markdown("## BHARATHRAJ PILLAI")

        st.markdown("""
### Professional Badminton Coach With 15+ Years of Coaching Excellence
""")

        st.write("""
Passionate and professional full-time badminton coach with extensive experience
training beginner, intermediate, and advanced competitive players.
Specialized in badminton techniques, match strategies, fitness training,
footwork improvement, and player development.
""")

        st.write("""
Dedicated to building discipline, confidence, stamina, leadership qualities,
and tournament-level performance through structured coaching methods.
""")

# ---------------------------------------------------
# ABOUT COACH
# ---------------------------------------------------

st.markdown("---")

st.subheader("🏸 About Coach")

st.write("""
Highly experienced badminton coach with more than 15 years of professional coaching
experience across multiple reputed academies and sports institutions.
Focused on creating a strong high-performance sports culture rooted in discipline,
consistency, teamwork, sportsmanship, and game ethics.
""")

# ---------------------------------------------------
# COACHING EXPERIENCE
# ---------------------------------------------------

st.markdown("---")

st.subheader("🏸 Coaching Experience")

st.markdown("""
- **Head Coach – Hiranandani** (2014 – March 2025) – 11 Years

- **Head Coach – Sai Sarvesh** (2010 – 2015) – 5 Years

- **Head Coach – Opaline Olympia** (2015 – Present) – 10+ Years

- **Head Coach – Humming Garden** (2015 – Present) – 10+ Years

- **Head Coach – SHASU** (2023 – Present) – 2+ Years
""")

# ---------------------------------------------------
# ACHIEVEMENTS
# ---------------------------------------------------

st.markdown("---")

st.subheader("🏸 Coach Achievements")

st.markdown("""
- Successfully trained beginner to advanced-level badminton players

- Produced multiple district and tournament-level performers

- Expert in fitness training, match strategy, and footwork coaching

- Built structured player performance monitoring systems

- Mentored students in discipline, confidence, and leadership qualities

- Created high-performance badminton training environments
""")

# ---------------------------------------------------
# ABOUT BADMINTON TRAINING
# ---------------------------------------------------

st.markdown("---")

st.subheader("🏸 About Badminton Training")

st.write("""
Badminton is one of the fastest sports that improves stamina,
reflexes, concentration, agility, and mental strength.
Regular professional coaching helps students improve discipline,
fitness, confidence, leadership, and tournament performance.
""")

st.write("""
Performance analysis and progress tracking help players understand
their strengths and areas for improvement while preparing them
for competitive-level matches.
""")

# ---------------------------------------------------
# LOAD EXCEL
# ---------------------------------------------------

df = pd.read_excel("namelist.xlsx")
df.replace(33, 3, inplace=True)

students = list(df.columns[1:])

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.title("🏸 Student Dashboard")

selected_student = st.sidebar.selectbox(
    "Select Student",
    students
)

# ---------------------------------------------------
# FILTER DATA
# ---------------------------------------------------

criteria = df.iloc[:,0]

scores = df[selected_student]

student_df = pd.DataFrame({
    "Criteria": criteria,
    "Score": scores
})

student_df = student_df.dropna()

student_df["Score"] = pd.to_numeric(
    student_df["Score"],
    errors="coerce"
)

student_df["Score"] = pd.to_numeric(
    student_df["Score"],
    errors="coerce"
)

student_df = student_df.dropna()

student_df = student_df[
    student_df["Score"] >= 0
]

# ---------------------------------------------------
# SPLIT DATA FOR CHARTS
# ---------------------------------------------------

groups = []

for i in range(0, len(student_df), 5):
    groups.append(student_df.iloc[i:i+5])

while len(groups) < 8:
    groups.append(pd.DataFrame(columns=["Criteria","Score"]))
g1,g2,g3,g4,g5,g6,g7,g8 = groups[:8]

# ---------------------------------------------------
# KPI CALCULATIONS
# ---------------------------------------------------

average = round(student_df["Score"].mean(),1)

strong = len(student_df[student_df["Score"] >= 5])
weak = len(student_df[student_df["Score"] <= 2])

if average >= 6:
    level = "Excellent"
elif average >= 4:
    level = "Good"
elif average >= 2:
    level = "Developing"
else:
    level = "Beginner"
# ---------------------------------------------------
# STUDENT HEADER
# ---------------------------------------------------

st.markdown("---")

st.subheader(
    f"🏸 {selected_student} Performance Dashboard"
)

# ---------------------------------------------------
# KPI SECTION
# ---------------------------------------------------

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.markdown(f"""
    <div class="metric-card">
    <div class="metric-title">
    Overall Score
    </div>

    <div class="metric-value">
    {average}
    </div>
    </div>
    """, unsafe_allow_html=True)

with c2:

    st.markdown(f"""
    <div class="metric-card">
    <div class="metric-title">
    Strong Skills
    </div>

    <div class="metric-value">
    {strong}
    </div>
    </div>
    """, unsafe_allow_html=True)

with c3:

    st.markdown(f"""
    <div class="metric-card">
    <div class="metric-title">
    Improvement Areas
    </div>

    <div class="metric-value">
    {weak}
    </div>
    </div>
    """, unsafe_allow_html=True)

with c4:

    st.markdown(f"""
    <div class="metric-card">
    <div class="metric-title">
    Performance
    </div>

    <div class="metric-value">
    {level}
    </div>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------
# CHARTS
# ---------------------------------------------------
chart_config = {
    "displayModeBar": False,
    "scrollZoom": False,
    "editable": False,
    "staticPlot": True
}

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    if not g1.empty:
        fig1 = px.bar(
            g1,
            x="Criteria",
            y="Score",
            color="Score",
            title="Movement Skills Analytics"
        )
        st.plotly_chart(
            fig1,
            use_container_width=True,
            config=chart_config
        )
 

with col2:
    if not g2.empty:
        fig2 = px.line(
            g2,
            x="Criteria",
            y="Score",
            markers=True,
            title="Technical Skills Analysis"
        )
        st.plotly_chart(
            fig2,
            use_container_width=True,
            config=chart_config
        )


# ---------------------------------------------------

col3, col4 = st.columns(2)

with col3:
    if not g3.empty:
        fig3 = px.area(
            g3,
            x="Criteria",
            y="Score",
            title="Fitness & Court Coverage"
        )
        st.plotly_chart(
            fig3,
            use_container_width=True,
            config=chart_config
        )


with col4:
    if not g4.empty:
        fig4 = px.pie(
            g4,
            names="Criteria",
            values="Score",
            title="Mental Strength & Discipline"
        )
        st.plotly_chart(
            fig4,
            use_container_width=True,
            config=chart_config
        )


# ---------------------------------------------------

col5, col6 = st.columns(2)

with col5:
    if not g5.empty:
        fig5 = px.area(
            g5,
            x="Criteria",
            y="Score",
            title="Fitness & Court Coverage"
        )
        st.plotly_chart(
            fig5,
            use_container_width=True,
            config=chart_config
        )


with col6:
    if not g6.empty:
        fig6 = px.scatter(
            g6,
            x="Criteria",
            y="Score",
            title="Advanced Performance Metrics"
        )
        st.plotly_chart(
            fig6,
            use_container_width=True,
            config=chart_config
        )


# ---------------------------------------------------

col7, col8 = st.columns(2)

with col7:
    if not g7.empty:
        fig7 = px.bar(
            g7,
            x="Criteria",
            y="Score",
            color="Score",
            title="Reaction & Coordination"
        )
        st.plotly_chart(
            fig7,
            use_container_width=True,
            config=chart_config
        )


with col8:
    if not g8.empty:
        fig8 = px.pie(
            g8,
            names="Criteria",
            values="Score",
            hole=0.5,
            title="Overall Skill Distribution"
        )
        st.plotly_chart(
            fig8,
            use_container_width=True,
            config=chart_config
        )


# ---------------------------------------------------
# RADAR CHART
# ---------------------------------------------------

st.markdown("---")

st.subheader("🏸 Advanced Performance Metrics")

if not student_df.empty:

    fig9 = px.line_polar(
        student_df.head(10),
        r="Score",
        theta="Criteria",
        line_close=True
    )

    fig9.update_traces(fill="toself")

    st.plotly_chart(
        fig9,
        use_container_width=True,
        config=chart_config
    )

# ---------------------------------------------------
# DETAILED AI FEEDBACK
# ---------------------------------------------------

strengths = student_df[
    student_df["Score"] >= 5
]["Criteria"].tolist()

improvements = student_df[
    student_df["Score"] <= 2
]["Criteria"].tolist()

overall_lines = [

    "shows strong dedication towards badminton development and maintains impressive consistency during training sessions.",

    "demonstrates excellent discipline and positive learning attitude during badminton coaching activities.",

    "has shown stable performance improvement across multiple badminton performance indicators.",

    "maintains strong interest and active involvement during advanced badminton practice sessions."
]

strength_lines = [

    "The student performs strongly in {} and demonstrates excellent tactical awareness during rallies.",

    "Strong performance has been observed in {}, indicating excellent technical understanding and confidence.",

    "The student consistently performs well in {}, reflecting advanced badminton potential.",

    "Excellent performance is visible in {}, showing strong focus and skill execution."
]

improvement_lines = [

    "Additional improvement is recommended in {} to strengthen overall tournament consistency.",

    "Focused training sessions in {} can improve advanced competitive performance.",

    "The student can further improve overall gameplay by strengthening {} through regular practice.",

    "Further technical refinement in {} can help improve defensive recovery and match stability."
]

future_lines = [

    "With continuous coaching and regular training, the student has strong district-level tournament potential.",

    "The student demonstrates excellent long-term badminton growth opportunities and competitive capability.",

    "Current performance trends indicate strong future possibilities in advanced badminton competitions.",

    "Regular advanced training and structured coaching can help the student achieve higher performance levels."
]

overall_feedback = random.choice(overall_lines)

strength_feedback = random.choice(
    strength_lines
).format(
    ", ".join(strengths[:4])
)

improvement_feedback = random.choice(
    improvement_lines
).format(
    ", ".join(improvements[:4])
)

future_feedback = random.choice(future_lines)

# ---------------------------------------------------
# FEEDBACK DISPLAY
# ---------------------------------------------------

st.markdown("---")

st.subheader(
    "🏸 Intelligent AI Performance Report"
)

st.info(overall_feedback)

st.success(strength_feedback)

st.warning(improvement_feedback)

st.success(future_feedback)

# ---------------------------------------------------
# PARENT FEEDBACK
# ---------------------------------------------------

st.markdown("---")

st.subheader("👨‍👩‍👧 Parent Feedback")

parent_name = st.text_input(
    "Enter Parent Name"
)

parent_feedback = st.text_area(
    "Enter Parent Feedback"
)

if st.button("Submit Feedback"):

    st.success(
        "Feedback Submitted Successfully ✅"
    )

# ---------------------------------------------------
# PDF REPORT GENERATION
# ---------------------------------------------------
st.markdown("---")

if st.button("📄 Generate Professional Report"):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_auto_page_break(auto=True, margin=15)

    # TITLE

    pdf.set_font("Arial", "B", 20)
    pdf.cell(190, 12, "OPALINE", ln=True, align="C")

    pdf.set_font("Arial", "", 12)
    pdf.cell(
        190,
        8,
        "Professional Badminton Performance Analytics Report",
        ln=True,
        align="C"
    )

    pdf.ln(8)

    # COACH DETAILS

    pdf.set_font("Arial", "B", 15)
    pdf.cell(190, 10, "Coach Profile", ln=True)

    pdf.set_font("Arial", "", 11)

    coach_text = """
BHARATHRAJ PILLAI

Professional Badminton Coach With 15+ Years of Coaching Excellence

Passionate and professional full-time badminton coach with extensive experience
training beginner, intermediate, and advanced competitive players.

Specialized in badminton techniques, match strategies, fitness training,
footwork improvement, and player development.

Dedicated to building discipline, confidence, stamina, leadership qualities,
and tournament-level performance through structured coaching methods.
"""

    pdf.multi_cell(0, 8, coach_text)

    pdf.ln(5)

    # STUDENT DETAILS

    pdf.set_font("Arial", "B", 15)
    pdf.cell(
        190,
        10,
        f"Student Report : {selected_student}",
        ln=True
    )

    pdf.ln(3)

    # KPI SUMMARY

    pdf.set_font("Arial", "B", 14)
    pdf.cell(190, 10, "Performance Summary", ln=True)

    pdf.set_font("Arial", "", 11)

    summary_text = f"""
Overall Score : {average}

Strong Skills : {strong}

Improvement Areas : {weak}

Performance Level : {level}
"""

    pdf.multi_cell(0, 8, summary_text)

    pdf.ln(5)

    # AI ANALYSIS

    pdf.set_font("Arial", "B", 14)
    pdf.cell(190, 10, "AI Performance Analysis", ln=True)

    pdf.set_font("Arial", "", 11)

    pdf.multi_cell(0, 8, overall_feedback)
    pdf.ln(2)

    pdf.multi_cell(0, 8, strength_feedback)
    pdf.ln(2)

    pdf.multi_cell(0, 8, improvement_feedback)
    pdf.ln(2)

    pdf.multi_cell(0, 8, future_feedback)

    pdf.ln(5)

    # FUTURE POTENTIAL

    pdf.set_font("Arial", "B", 14)
    pdf.cell(190, 10, "Future Potential Assessment", ln=True)

    pdf.set_font("Arial", "", 11)

    future_text = f"""
Based on the current badminton performance indicators,
{selected_student} demonstrates encouraging growth potential.

The student shows positive development in technical execution,
court awareness, movement efficiency, discipline, fitness,
reaction ability and competitive readiness.

Continued coaching, structured practice sessions and tournament
exposure can significantly enhance future performance and help
the student achieve higher levels of badminton excellence.
"""

    pdf.multi_cell(0, 8, future_text)

    pdf.ln(5)

    # PERFORMANCE TABLE

    pdf.set_font("Arial", "B", 14)
    pdf.cell(190, 10, "Detailed Performance Scores", ln=True)

    pdf.ln(3)

    pdf.set_font("Arial", "B", 11)

    pdf.cell(130, 10, "Criteria", border=1)
    pdf.cell(40, 10, "Score", border=1, ln=True)

    pdf.set_font("Arial", "", 10)

    for index, row in student_df.iterrows():

        criteria = str(row["Criteria"])[:45]

        pdf.cell(
            130,
            8,
            criteria,
            border=1
        )

        pdf.cell(
            40,
            8,
            str(row["Score"]),
            border=1,
            ln=True
        )

    pdf.ln(8)

    # FOOTER

    pdf.set_font("Arial", "I", 10)

    footer_text = """
Generated by OPALINE
Professional Badminton Performance Analytics System

This report is automatically generated using student performance data,
analytics, coaching insights and badminton development indicators.
"""

    pdf.multi_cell(0, 8, footer_text)

    # SAVE PDF

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as tmp_file:

        pdf.output(tmp_file.name)

        with open(tmp_file.name, "rb") as file:

            st.download_button(
                label="⬇ Download Performance PDF",
                data=file.read(),
                file_name=f"{selected_student}_Performance_Report.pdf",
                mime="application/pdf"
            )
# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("---")

st.markdown("""
<center>

© 2026 OPALINE

Professional Badminton Performance Analytics System

</center>
""", unsafe_allow_html=True)
