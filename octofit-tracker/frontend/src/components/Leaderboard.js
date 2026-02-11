import React, { useState, useEffect } from 'react';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const codespace = process.env.REACT_APP_CODESPACE_NAME;
    const apiUrl = codespace 
      ? `https://${codespace}-8000.app.github.dev/api/leaderboard/`
      : 'http://localhost:8000/api/leaderboard/';
    
    console.log('Leaderboard - Fetching from:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Leaderboard - Fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const leaderboardData = data.results || data;
        setLeaderboard(Array.isArray(leaderboardData) ? leaderboardData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Leaderboard - Error fetching data:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) return (
    <div className="container mt-5">
      <div className="loading-spinner">
        <div className="spinner-border text-primary" role="status">
          <span className="visually-hidden">Loading leaderboard...</span>
        </div>
      </div>
    </div>
  );
  
  if (error) return (
    <div className="container mt-5">
      <div className="alert alert-danger" role="alert">
        <h4 className="alert-heading">Error!</h4>
        <p>{error}</p>
      </div>
    </div>
  );

  return (
    <div className="container mt-5">
      <div className="page-header">
        <h1>Leaderboard</h1>
        <p className="text-muted">See who's leading the fitness challenge</p>
      </div>

      {leaderboard.length === 0 ? (
        <div className="alert alert-info" role="alert">
          No leaderboard data available yet. Start logging activities to compete!
        </div>
      ) : (
        <div className="table-responsive">
          <table className="table table-striped table-hover">
            <thead>
              <tr>
                <th>Rank</th>
                <th>User</th>
                <th>Total Points</th>
                <th>Team</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {leaderboard.map((entry, index) => (
                <tr key={entry._id || index} className={index < 3 ? 'table-warning' : ''}>
                  <td>
                    {index === 0 && <span className="badge bg-warning text-dark">🥇</span>}
                    {index === 1 && <span className="badge bg-secondary">🥈</span>}
                    {index === 2 && <span className="badge bg-danger">🥉</span>}
                    {index >= 3 && <span className="badge bg-light text-dark">{index + 1}</span>}
                  </td>
                  <td>
                    <strong>{entry.user_email}</strong>
                  </td>
                  <td>
                    <span className="badge bg-success">{entry.total_points || 0} pts</span>
                  </td>
                  <td>
                    {entry.team ? (
                      <span className="badge bg-primary">{entry.team}</span>
                    ) : (
                      <span className="badge bg-secondary">No team</span>
                    )}
                  </td>
                  <td>
                    <button className="btn btn-sm btn-outline-primary">View Profile</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default Leaderboard;
