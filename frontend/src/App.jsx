import React, { useState } from 'react';
import SearchInput from './components/SearchInput';
import ResultDisplay from './components/ResultDisplay';

function App() {
  const [query, setQuery] = useState('');
  const [result, setResult] = useState('');

  return (
    <div className="p-4 font-sans">
      <h1 className="text-3xl font-bold mb-4">AI Multimodal Search Agent</h1>
      <SearchInput onSearch={setQuery} />
      <ResultDisplay query={query} onResult={setResult} result={result} />
    </div>
  );
}
export default App;
