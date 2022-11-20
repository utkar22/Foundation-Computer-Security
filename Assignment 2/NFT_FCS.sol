// SPDX-License-Identifier: MIT
// This is a pragma directive that tells the compiler to use solidity versions 0.8.6 or higher
pragma solidity 0.8.6;

// I import the 0xcert/ethereum-erc721 contracts.
// For this assignment,  I have used the ERC 721 standard.  
import "https://github.com/0xcert/ethereum-erc721/src/contracts/tokens/nf-token-metadata.sol";
import "https://github.com/0xcert/ethereum-erc721/src/contracts/ownership/ownable.sol";


// I create a new Smart Contract called ourNFT2. This extends the Contracts NFTokenMetadata and
// Ownable
contract ourNFT2 is NFTokenMetadata, Ownable {
 
  // This is the constructor of the Smart Contract. This is called when we deploy the Smart
  // Contract. It sets the name of the NFT to "CattoNFT", and the Symbol to "NYC"
  // Catto - because the picture is of a cute catto
  // NYC - because I clicked this photo on New Year's, and this is a Catto
  constructor() {
    nftName = "CattoNFT";
    nftSymbol = "NYC";
  }
 
  // This function mints the NFT.
  // minter_address- this is the address of the metamask wallet who is minting the NFT
  // 
  function mint_nft(address minter_address, uint256 token_id, string calldata uri) external onlyOwner {
    //This function mints the NFT on the blockchain
    super._mint(minter_address, token_id);
    //This function connects the blockchain with the uri of the image. The image is hosted
    // outside the blockchain, on IPFS
    super._setTokenUri(token_id, uri);
  }
 
}

// References:
// https://www.quicknode.com/guides/smart-contract-development/how-to-create-and-deploy-an-erc-721-nft
// https://medium.com/geekculture/mint-an-nft-and-erc-721-smart-contract-easy-step-by-step-4fafff151fbe
