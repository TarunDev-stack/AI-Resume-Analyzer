import re


# -----------------------------------
# Skills Database
# -----------------------------------

SKILLS = [
    # Programming Languages
    "python",
    "java",
    "c",
    "c++",
    "javascript",
    "typescript",
    "r",

    # Web Development
    "html",
    "css",
    "react",
    "react.js",
    "node.js",
    "express",
    "next.js",

    # Data Science
    "machine learning",
    "deep learning",
    "data science",
    "data analysis",
    "data analytics",
    "statistics",
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "scikit-learn",
    "sklearn",

    # AI / NLP
    "artificial intelligence",
    "natural language processing",
    "nlp",
    "computer vision",
    "generative ai",
    "large language model",
    "llm",
    "transformers",
    "hugging face",
    "tensorflow",
    "keras",
    "pytorch",
    "opencv",
    "spacy",
    "nltk",

    # Databases
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "oracle",
    "sqlite",
    "database",

    # Cloud
    "aws",
    "azure",
    "google cloud",
    "gcp",
    "cloud computing",

    # DevOps
    "docker",
    "kubernetes",
    "git",
    "github",
    "gitlab",
    "jenkins",
    "ci/cd",

    # Big Data
    "spark",
    "hadoop",
    "apache spark",
    "kafka",

    # BI / Visualization
    "tableau",
    "power bi",
    "excel",

    # Other
    "rest api",
    "api",
    "linux",
    "flask",
    "django",
    "streamlit"
]


# -----------------------------------
# Skill Extraction Function
# -----------------------------------

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        # Escape special characters
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text):

            found_skills.append(skill)

    return sorted(
        list(set(found_skills))
    )