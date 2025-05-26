import React, { useEffect } from 'react';
import axios from 'axios';

export default function ResultDisplay({ query, onResult, result }) {
  useEffect(() => {
    if (query) {
      axios.post("http://localhost:8000/search", { query })
        .then(res => onResult(res.data.response))
        .catch(err => onResult("Error: " + err.message));
    }
  }, [query]);

  return (
    <div className="bg-gray-100 p-4 mt-4 rounded">
      <h2 className="text-xl font-semibold mb-2">Result:</h2>
      <p>{result}</p>
    </div>
  );
}
