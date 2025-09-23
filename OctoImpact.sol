// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract OctoImpact {
    mapping(address => uint) public rewards;

    function rewardUser(address user, uint amount) public {
        rewards[user] += amount;
    }

    function getReward(address user) public view returns (uint) {
        return rewards[user];
    }
}

