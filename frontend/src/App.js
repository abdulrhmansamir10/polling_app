import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

// The URL for our backend API. Note that we use the service name 'backend'
// from our docker-compose file, not 'localhost'. Docker's internal DNS handles this.

function App() {
  const [pollData, setPollData] = useState({});

  // Function to fetch the latest poll data from the backend
  const fetchPollData = async () => {
    try {
      const response = await axios.get('/api/poll');
      setPollData(response.data);
    } catch (error) {
      console.error("Error fetching poll data:", error);
    }
  };

  // Function to handle a vote
  const handleVote = async (option) => {
    try {
      await axios.post('/api/vote', { vote: option });
      fetchPollData(); // Refresh data after voting
    } catch (error) {
      console.error("Error submitting vote:", error);
    }
  };

  // useEffect hook to fetch data when the component mounts
  useEffect(() => {
    fetchPollData();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Vote for Your Favorite Language</h1>
        <div className="poll-container">
          {Object.keys(pollData).map((option) => (
            <div key={option} className="poll-option">
              <p>{option.charAt(0).toUpperCase() + option.slice(1)}: {pollData[option]} votes</p>
              <button onClick={() => handleVote(option)}>Vote</button>
            </div>
          ))}
        </div>
      </header>
    </div>
  );
}

export default App;
