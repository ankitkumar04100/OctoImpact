import React, { useEffect, useState } from "react";
import axios from "../services/api";

function Dashboard() {
  const [dashboardData, setDashboardData] = useState({});

  useEffect(() => {
    axios.get("/dashboard")
      .then(res => setDashboardData(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div className="card mb-4">
      <div className="card-header">Dashboard</div>
      <div className="card-body">
        <p>Energy Saved: {dashboardData.energy_saved}</p>
        <p>Water Saved: {dashboardData.water_saved}</p>
        <p>Eco Score: {dashboardData.eco_score}</p>
        <p>AI Insight: {dashboardData.ai_insight}</p>
      </div>
    </div>
  );
}

export default Dashboard;
