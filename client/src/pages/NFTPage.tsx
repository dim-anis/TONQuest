import React from 'react';
import BottomMenu from '../components/BottomMenu';

const NFTPage = () => {
  return (
    <div className="min-h-screen relative bg-gradient-to-b from-black via-[#00a1ff] to-black flex flex-col items-center min-w-[432px]">
      <h2 className="text-xl font-bold">NFT Page</h2>
      <BottomMenu isNFTPage={true} />
    </div>
  );
};

export default NFTPage;
