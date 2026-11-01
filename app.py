import streamlit as st

from resume_parser import extract_text_from_pdf
from skill_extractor import extract_skills, SKILLS
from matcher import calculate_match
from semantic_matcher import calculate_semantic_similarity
from recommendations import generate_recommendations


# -----------------------------------
# Page Configuration
# -----------------------------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)


# -----------------------------------
# Title
# -----------------------------------

st.title("🤖 AI Resume Analyzer & Job Matcher")

st.write(
    "Upload your resume and enter a job description "
    "to analyze your compatibility with the role."
)


# -----------------------------------
# Resume Upload
# -----------------------------------

uploaded_file = st.file_uploader(
    "📄 Upload your Resume",
    type=["pdf"]
)


# -----------------------------------
# Job Description
# -----------------------------------

job_description = st.text_area(
    "💼 Paste the Job Description",
    height=250,
    placeholder=(
        "Example:\n"
        "We are looking for a Data Scientist with experience "
        "in Python, SQL, Machine Learning, Pandas, NumPy, "
        "Scikit-learn, TensorFlow and AWS."
    )
)


# -----------------------------------
# Analyze Button
# -----------------------------------

if st.button("🔍 Analyze Resume", type="primary"):

    if uploaded_file is None:

        st.warning("⚠️ Please upload your resume PDF.")

    elif not job_description.strip():

        st.warning("⚠️ Please enter a job description.")

    else:

        # -----------------------------------
        # Extract Resume Text
        # -----------------------------------

        with st.spinner("📄 Reading your resume..."):

            resume_text = extract_text_from_pdf(
                uploaded_file
            )

        if not resume_text.strip():

            st.error(
                "❌ Could not extract text from the PDF."
            )

        else:

            # -----------------------------------
            # Extract Skills
            # -----------------------------------

            resume_skills = extract_skills(
                resume_text
            )


            # -----------------------------------
            # Skill Matching
            # -----------------------------------

            skill_score, matched, missing = calculate_match(
                resume_skills,
                job_description,
                SKILLS
            )


            # -----------------------------------
            # AI Semantic Matching
            # -----------------------------------

            with st.spinner(
                "🤖 AI is analyzing your resume..."
            ):

                semantic_score = calculate_semantic_similarity(
                    resume_text,
                    job_description
                )


            # -----------------------------------
            # Overall Score
            # -----------------------------------

            overall_score = (
                (skill_score * 0.60)
                + (semantic_score * 0.40)
            )

            overall_score = min(
                max(overall_score, 0),
                100
            )


            # -----------------------------------
            # Match Category
            # -----------------------------------

            if overall_score >= 80:

                category = "🟢 Excellent Match"

            elif overall_score >= 60:

                category = "🟡 Good Match"

            elif overall_score >= 40:

                category = "🟠 Moderate Match"

            else:

                category = "🔴 Low Match"


            # -----------------------------------
            # Generate Recommendations
            # -----------------------------------

            recommendations = generate_recommendations(
                missing
            )


            # -----------------------------------
            # Results
            # -----------------------------------

            st.divider()

            st.header("📊 Resume Analysis")


            # -----------------------------------
            # Overall Score
            # -----------------------------------

            st.subheader("🎯 Overall Job Match")

            st.metric(
                "Overall Match Score",
                f"{overall_score:.1f}%"
            )

            st.progress(
                float(overall_score) / 100
            )

            st.write(
                f"**{category}**"
            )


            # -----------------------------------
            # Individual Scores
            # -----------------------------------

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "🛠️ Skill Match",
                    f"{skill_score:.1f}%"
                )

            with col2:

                st.metric(
                    "🤖 AI Semantic Match",
                    f"{semantic_score:.1f}%"
                )


            # -----------------------------------
            # Skills Detected
            # -----------------------------------

            st.subheader(
                "🛠️ Skills Detected in Resume"
            )

            if resume_skills:

                st.success(
                    " • ".join(resume_skills)
                )

            else:

                st.warning(
                    "No known skills were detected."
                )


            # -----------------------------------
            # Matching Skills
            # -----------------------------------

            st.subheader(
                "✅ Matching Skills"
            )

            if matched:

                for skill in matched:

                    st.write(
                        "✅",
                        skill
                    )

            else:

                st.info(
                    "No matching skills were found."
                )


            # -----------------------------------
            # Missing Skills
            # -----------------------------------

            st.subheader(
                "❌ Missing Skills"
            )

            if missing:

                for skill in missing:

                    st.write(
                        "❌",
                        skill
                    )

            else:

                st.success(
                    "🎉 You have all the detected job skills!"
                )


            # -----------------------------------
            # Skill Recommendations
            # -----------------------------------

            st.subheader(
                "📚 Recommended Skills to Learn"
            )

            if recommendations:

                for item in recommendations:

                    st.write(
                        f"{item['priority']}  "
                        f"**{item['skill']}**"
                    )

            else:

                st.success(
                    "🎉 No major skill gaps detected!"
                )


            # -----------------------------------
            # Resume Text
            # -----------------------------------

            with st.expander(
                "📄 View Extracted Resume Text"
            ):

                st.text_area(
                    "Resume Content",
                    resume_text,
                    height=400
                )