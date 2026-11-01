from functools import lru_cache
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


@lru_cache(maxsize=1)
def get_model():
    return SentenceTransformer("all-MiniLM-L6-v2")


def calculate_semantic_similarity(resume_text, job_description):
    try:
        model = get_model()

        resume_embedding = model.encode(
            [resume_text],
            convert_to_numpy=True,
            normalize_embeddings=True
        )
        job_embedding = model.encode(
            [job_description],
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        similarity = cosine_similarity(
            resume_embedding,
            job_embedding
        )[0][0]

        score = similarity * 100
        return max(0.0, min(score, 100.0))
    except Exception:
        return 0.0