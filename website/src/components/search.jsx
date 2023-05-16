import React, { useState, useEffect } from 'react';
import axios from 'axios';

const SearchComponent = ({baseAPIUrl}) => {
  const [searchQuery, setSearchQuery] = useState('');
  const [searchResults, setSearchResults] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const delayDebounceFn = setTimeout(() => {
      if (searchQuery.trim() !== '') {
        search();
      } else {
        setSearchResults([]);
      }
    }, 1000);

    return () => clearTimeout(delayDebounceFn);
  }, [searchQuery]);

  const search = async () => {
    setLoading(true);

    try {
      const response = await axios.get(`${baseAPIUrl}/api/search?query=${searchQuery}`);
      console.log(response)
      setSearchResults(response.data);
      setLoading(false);
    } catch (error) {
      console.error('Error occurred during search:', error);
      setLoading(false);
    }
  };

  const handleSearchChange = (e) => {
    setSearchQuery(e.target.value);
  };

  return (
    <div>
      <SearchBox onChange={handleSearchChange} />
      {loading ? (
        <div>Loading...</div>
      ) : (
        <SearchResults results={searchResults} />
      )}
    </div>
  );
};

const SearchBox = ({ onChange }) => {
  return (
    <input
      type="text"
      placeholder="Search..."
      onChange={onChange}
    />
  );
};

const SearchResults = ({ results }) => {
  return (
    <ul>
      {results.map((result) => (
        <li key={result._id}>{result._source.Book_Title}</li>
      ))}
    </ul>
  );
};

export default SearchComponent;
