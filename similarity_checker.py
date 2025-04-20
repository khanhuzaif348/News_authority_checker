
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_similarity_score(user_input):
    verified_claim = "COVID-19 vaccines are safe and effective"
    input_emb = model.encode(user_input, convert_to_tensor=True)
    verified_emb = model.encode(verified_claim, convert_to_tensor=True)
    similarity = util.cos_sim(input_emb, verified_emb).item()
    verdict = "Likely Real" if similarity > 0.7 else "Likely Fake"
    return similarity, verdict
