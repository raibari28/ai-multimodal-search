let store = [];

export function addVector(vector, metadata) {
  store.push({ vector, metadata });
}

export function searchVector(queryVec) {
  return store
    .map(item => ({
      score: cosineSimilarity(queryVec, item.vector),
      metadata: item.metadata
    }))
    .sort((a, b) => b.score - a.score)
    .slice(0, 5);
}

function cosineSimilarity(a, b) {
  const dot = a.reduce((sum, val, i) => sum + val * b[i], 0);
  const magA = Math.sqrt(a.reduce((sum, v) => sum + v * v, 0));
  const magB = Math.sqrt(b.reduce((sum, v) => sum + v * v, 0));
  return dot / (magA * magB);
}
