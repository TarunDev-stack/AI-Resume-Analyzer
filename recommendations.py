# -----------------------------------
# Skill Priority Levels
# -----------------------------------

HIGH_PRIORITY = {
    "python",
    "java",
    "sql",
    "machine learning",
    "deep learning",
    "data science",
    "tensorflow",
    "pytorch",
    "aws",
    "azure",
    "gcp"
}


MEDIUM_PRIORITY = {
    "pandas",
    "numpy",
    "scikit-learn",
    "docker",
    "kubernetes",
    "spark",
    "power bi",
    "tableau",
    "mongodb",
    "postgresql"
}


# -----------------------------------
# Generate Recommendations
# -----------------------------------

def generate_recommendations(missing_skills):

    recommendations = []

    for skill in missing_skills:

        skill_lower = skill.lower()

        if skill_lower in HIGH_PRIORITY:

            priority = "🔴 High"

        elif skill_lower in MEDIUM_PRIORITY:

            priority = "🟠 Medium"

        else:

            priority = "🟡 Low"

        recommendations.append({
            "skill": skill,
            "priority": priority
        })

    return recommendations