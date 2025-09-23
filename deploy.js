async function main() {
  const OctoImpact = await ethers.getContractFactory("OctoImpact");
  const contract = await OctoImpact.deploy();
  await contract.deployed();
  console.log("OctoImpact deployed to:", contract.address);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
