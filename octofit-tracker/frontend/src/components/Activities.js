import React, { useState, useEffect } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const codespace = process.env.REACT_APP_CODESPACE_NAME;
    const apiUrl = codespace 
      ? `https://${codespace}-8000.app.github.dev/api/activities/`
      : 'http://localhost:8000/api/activities/';
    
    console.log('Activities - Fetching from:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Activities - Fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const activitiesData = data.results || data;
        setActivities(Array.isArray(activitiesData) ? activitiesData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Activities - Error fetching data:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) return (
    <div className="container mt-5">
      <div className="loading-spinner">
        <div className="spinner-border text-primary" role="status">
          <span className="visually-hidden">Loading activities...</span>
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
        <h1>Activities</h1>
        <p className="text-muted">Track all fitness activities and workouts</p>
      </div>
      
      <div className="mb-3">
        <button className="btn btn-primary">
          <i className="bi bi-plus-circle"></i> Add Activity
        </button>
      </div>

      {activities.length === 0 ? (
        <div className="alert alert-info" role="alert">
          No activities found. Start tracking your fitness journey!
        </div>
      ) : (
        <div className="table-responsive">
          <table className="table table-striped table-hover">
            <thead>
              <tr>
                <th>Activity Type</th>
                <th>Duration</th>
                <th>Calories</th>
                <th>Date</th>
                <th>User</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {activities.map(activity => (
                <tr key={activity._id}>
                  <td>
                    <strong>{activity.activity_type}</strong>
                  </td>
                  <td>{activity.duration} min</td>
                  <td>
                    <span className="badge bg-success">{activity.calories} cal</span>
                  </td>
                  <td>{new Date(activity.date).toLocaleDateString()}</td>
                  <td>{activity.user_email}</td>
                  <td>
                    <button className="btn btn-sm btn-outline-primary me-1">View</button>
                    <button className="btn btn-sm btn-outline-secondary">Edit</button>
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

export default Activities;
