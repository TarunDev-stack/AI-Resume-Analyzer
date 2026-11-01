def calculate_match(resume_skills, job_description, all_skills):
    job_description = job_description.lower()

    job_skills = []

    for skill in all_skills:
        if skill.lower() in job_description:
            job_skills.append(skill)

    if not job_skills:
        return 0, [], []

    matched_skills = [
        skill for skill in job_skills
        if skill in resume_skills
    ]

    missing_skills = [
        skill for skill in job_skills
        if skill not in resume_skills
    ]

    score = (len(matched_skills) / len(job_skills)) * 100

    return score, matched_skills, missing_skills