import React from 'react';
import { ArrowUpRight, Wallet } from 'lucide-react';
import { useTonConnectModal, useTonConnectUI } from '@tonconnect/ui-react';

const ConnectWalletBox = () => {
  const { state, open, close } = useTonConnectModal();

  return (
    <div className="bg-gradient-to-r from-[#9333EA] via-[#3B82F6] to-[#16A34A] rounded-xl my-0.5 px-0.5 flex items-center justify-between">
      <button
        onClick={open}
        className="py-1 px-2 rounded-xl hover:bg-primary/20 transition-all flex items-center flex-row"
      >
        <Wallet className="mr-2 stroke-white" />
        <h3 className="text-white text-sm font-semibold">Connect wallet</h3>
      </button>
    </div>
  );
};

export default ConnectWalletBox;
