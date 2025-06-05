import React from 'react';
import { useChat } from '../../context/ChatContext';

export default function ResetButton() {
  const { resetChat } = useChat();

  return (
    <button
      onClick={resetChat}
      className="mt-4 bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded"
    >
      Reset Chat
    </button>
  );
}