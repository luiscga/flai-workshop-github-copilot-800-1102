import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const codespace = process.env.REACT_APP_CODESPACE_NAME;
    const apiUrl = codespace 
      ? `https://${codespace}-8000.app.github.dev/api/workouts/`
      : 'http://localhost:8000/api/workouts/';
    
    console.log('Workouts - Fetching from:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Workouts - Fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        setWorkouts(Array.isArray(workoutsData) ? workoutsData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Workouts - Error fetching data:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) return (
    <div className="container mt-5">
      <div className="loading-spinner">
        <div className="spinner-border text-primary" role="status">
          <span className="visually-hidden">Loading workouts...</span>
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
        <h1>Workouts</h1>
        <p className="text-muted">Browse recommended workout routines</p>
      </div>
      
      <div className="mb-3">
        <button className="btn btn-primary">
          <i className="bi bi-plus-circle"></i> Create Workout
        </button>
      </div>

      {workouts.length === 0 ? (
        <div className="alert alert-info" role="alert">
          No workouts found. Create your first workout routine!
        </div>
      ) : (
        <div className="table-responsive">
          <table className="table table-striped table-hover">
            <thead>
              <tr>
                <th>Workout Name</th>
                <th>Description</th>
                <th>Duration</th>
                <th>Difficulty</th>
                <th>Target Muscles</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {workouts.map(workout => (
                <tr key={workout._id}>
                  <td>
                    <strong>{workout.name}</strong>
                  </td>
                  <td>{workout.description || 'No description available'}</td>
                  <td>{workout.duration} min</td>
                  <td>
                    {workout.difficulty === 'Easy' && <span className="badge bg-success">Easy</span>}
                    {workout.difficulty === 'Medium' && <span className="badge bg-warning text-dark">Medium</span>}
                    {workout.difficulty === 'Hard' && <span className="badge bg-danger">Hard</span>}
                    {!workout.difficulty && <span className="badge bg-secondary">N/A</span>}
                  </td>
                  <td>{workout.target_muscles || 'N/A'}</td>
                  <td>
                    <button className="btn btn-sm btn-outline-primary me-1">View</button>
                    <button className="btn btn-sm btn-outline-success">Start</button>
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

export default Workouts;
