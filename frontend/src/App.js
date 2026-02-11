import React from "react";
import Navbar from "./components/Navbar";
import Dashboard from "./components/Dashboard";
import Rewards from "./components/Rewards";
import Footer from "./components/Footer";

function App() {
  return (
    <div>
      <Navbar />
      <div className="container mt-5">
        <Dashboard />
        <Rewards />
      </div>
      <Footer />
    </div>
  );
}

export default App;
