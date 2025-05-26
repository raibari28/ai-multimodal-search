import React, { useState } from 'react';

export default function SearchInput({ onSearch }) {
  const [input, setInput] = useState('');

  return (
    <div className="mb-4">
      <input
        type="text"
        value={input}
        onChange={e => setInput(e.target.value)}
        placeholder="Search with AI..."
        className="border p-2 w-full"
      />
      <button onClick={() => onSearch(input)} className="mt-2 bg-blue-500 text-white p-2">
        Search
      </button>
    </div>
  );
}
