import React, { useState, useEffect } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const codespace = process.env.REACT_APP_CODESPACE_NAME;
    const apiUrl = codespace 
      ? `https://${codespace}-8000.app.github.dev/api/teams/`
      : 'http://localhost:8000/api/teams/';
    
    console.log('Teams - Fetching from:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Teams - Fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const teamsData = data.results || data;
        setTeams(Array.isArray(teamsData) ? teamsData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Teams - Error fetching data:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) return (
    <div className="container mt-5">
      <div className="loading-spinner">
        <div className="spinner-border text-primary" role="status">
          <span className="visually-hidden">Loading teams...</span>
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
        <h1>Teams</h1>
        <p className="text-muted">View and manage fitness teams</p>
      </div>
      
      <div className="mb-4">
        <button className="btn btn-primary">
          <i className="bi bi-people"></i> Create Team
        </button>
      </div>

      {teams.length === 0 ? (
        <div className="alert alert-info" role="alert">
          No teams found. Create your first team to start competing!
        </div>
      ) : (
        <div className="row">
          {teams.map(team => (
            <div key={team._id} className="col-md-4 mb-4">
              <div className="card h-100">
                <div className="card-header">
                  <h5 className="mb-0">{team.name}</h5>
                </div>
                <div className="card-body">
                  <p className="card-text">
                    {team.description || 'No description available'}
                  </p>
                </div>
                <div className="card-footer bg-white border-top">
                  <small className="text-muted">
                    <i className="bi bi-calendar"></i> Created: {new Date(team.created_at).toLocaleDateString()}
                  </small>
                  <div className="mt-2">
                    <button className="btn btn-sm btn-primary me-1">View</button>
                    <button className="btn btn-sm btn-outline-secondary">Edit</button>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default Teams;
