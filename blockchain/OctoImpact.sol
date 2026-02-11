// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract OctoImpact {
    struct Reward {
        address user;
        uint256 points;
        string nftURI;
    }

    Reward[] public rewards;
    address public owner;

    event RewardAdded(address indexed user, uint256 points, string nftURI);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    function addReward(address _user, uint256 _points, string memory _nftURI) public onlyOwner {
        rewards.push(Reward(_user, _points, _nftURI));
        emit RewardAdded(_user, _points, _nftURI);
    }

    function getRewardCount() public view returns (uint256) {
        return rewards.length;
    }

    function getReward(uint256 index) public view returns (address, uint256, string memory) {
        require(index < rewards.length, "Index out of bounds");
        Reward memory r = rewards[index];
        return (r.user, r.points, r.nftURI);
    }
}
