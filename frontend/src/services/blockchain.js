// Mock blockchain service for rewards
let rewards = [];

export const getRewards = () => rewards;

export const addReward = (reward) => {
  rewards.push(reward);
  return rewards;
};
