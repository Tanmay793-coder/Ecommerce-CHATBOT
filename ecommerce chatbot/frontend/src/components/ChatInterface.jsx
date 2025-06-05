import React, { useState, useEffect, useRef } from 'react';
import { useChat } from '../context/ChatContext';
import MessageBubble from './UI/MessageBubble';
import ProductCard from './ProductCard';
import ResetButton from './UI/ResetButton';
import { useAuth } from '../context/AuthContext';

export default function ChatInterface() {
  const { messages, sendMessage } = useChat();
  const { logout } = useAuth();
  const [input, setInput] = useState('');
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (input.trim() !== '') {
      sendMessage(input);
      setInput('');
    }
  };

  return (
    <div className="flex flex-col h-screen bg-gray-100">
      <div className="bg-blue-600 text-white p-4 flex justify-between items-center">
        <h1 className="text-xl font-bold">E-commerce Assistant</h1>
        <button 
          onClick={logout}
          className="bg-red-500 hover:bg-red-700 text-white font-bold py-1 px-3 rounded"
        >
          Logout
        </button>
      </div>
      
      <div className="flex-1 overflow-y-auto p-4">
        {messages.map((msg, idx) => (
          <React.Fragment key={idx}>
            <MessageBubble text={msg.text} isUser={msg.isUser} />
            {msg.products && (
              <div className="mt-2 mb-4">
                <p className="text-gray-600 mb-2">Here are some products you might like:</p>
                <div className="flex flex-wrap">
                  {msg.products.map(p => (
                    <ProductCard key={p.id} product={p} />
                  ))}
                </div>
              </div>
            )}
          </React.Fragment>
        ))}
        <div ref={messagesEndRef} />
      </div>
      
      <form onSubmit={handleSubmit} className="bg-white p-4 border-t">
        <div className="flex">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Type your message..."
            className="flex-1 border rounded-l-lg p-2"
            autoFocus
          />
          <button
            type="submit"
            className="bg-blue-500 hover:bg-blue-600 text-white px-4 rounded-r-lg"
          >
            Send
          </button>
        </div>
      </form>
      
      <div className="p-4 bg-white border-t">
        <ResetButton />
        <div className="mt-2 text-sm text-gray-500">
          Session started at: {new Date().toLocaleTimeString()}
        </div>
      </div>
    </div>
  );
}