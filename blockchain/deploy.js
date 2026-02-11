// blockchain/deploy.js
const hre = require("hardhat");

async function main() {
    const OctoImpact = await hre.ethers.getContractFactory("OctoImpact");
    const octoImpact = await OctoImpact.deploy();
    await octoImpact.deployed();
    console.log("OctoImpact deployed to:", octoImpact.address);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
      console.error(error);
      process.exit(1);
  });
