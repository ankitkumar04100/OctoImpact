import React, { useEffect, useState } from "react";
import { getRewards, addReward } from "../services/blockchain";

function Rewards() {
  const [rewards, setRewards] = useState([]);

  useEffect(() => {
    setRewards(getRewards());
  }, []);

  const handleAddReward = () => {
    addReward({
      user: "0xDemoUser",
      points: 100,
      nft_uri: "https://demo-nft-uri"
    });
    setRewards(getRewards());
  };

  return (
    <div className="card mb-4">
      <div className="card-header">Rewards</div>
      <div className="card-body">
        <button className="btn btn-success mb-3" onClick={handleAddReward}>
          Add Reward
        </button>
        <ul>
          {rewards.map((r, index) => (
            <li key={index}>
              User: {r.user} | Points: {r.points} | NFT: {r.nft_uri}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default Rewards;
