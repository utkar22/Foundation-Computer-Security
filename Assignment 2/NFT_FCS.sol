// SPDX-License-Identifier: MIT
// This is a pragma directive that tells the compiler to use solidity versions 0.8.6 or higher
pragma solidity 0.8.6;

// I import the 0xcert/ethereum-erc721 contracts.  
import "https://github.com/0xcert/ethereum-erc721/src/contracts/tokens/nf-token-metadata.sol";
import "https://github.com/0xcert/ethereum-erc721/src/contracts/ownership/ownable.sol";


// I create a new Smart Contract called ourNFT. This extends the Contracts NFTokenMetadata and
// Ownable
contract ourNFT is NFTokenMetadata, Ownable {
 
  // This is the constructor of the Smart Contract. This is called when we deploy the Smart
  // Contract. It sets the name of the NFT to "Synth NFT", and the Symbol to "SYN"
  constructor() {
    nftName = "Synth NFT";
    nftSymbol = "SYN";
  }
 
  function mint(address minter_address, uint256 token_id, string calldata uri) external onlyOwner {
    super._mint(minter_address, token_id);
    super._setTokenUri(token_id, uri);
  }
 
}

// References:
// https://www.quicknode.com/guides/smart-contract-development/how-to-create-and-deploy-an-erc-721-nft
// https://medium.com/geekculture/mint-an-nft-and-erc-721-smart-contract-easy-step-by-step-4fafff151fbe
