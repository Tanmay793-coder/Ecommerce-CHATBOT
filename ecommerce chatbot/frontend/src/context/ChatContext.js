import React, { createContext, useContext, useState, useEffect } from 'react';
import api from '../services/api';

const ChatContext = createContext();

export function useChat() {
  return useContext(ChatContext);
}

export function ChatProvider({ children }) {
  const [messages, setMessages] = useState([]);
  const [sessionStart] = useState(new Date().toISOString());

  useEffect(() => {
    // Load previous session messages
    const savedMessages = localStorage.getItem('chatMessages');
    if (savedMessages) {
      try {
        setMessages(JSON.parse(savedMessages));
      } catch (e) {
        console.error('Failed to load chat messages');
      }
    }
  }, []);

  const saveMessages = (msgs) => {
    localStorage.setItem('chatMessages', JSON.stringify(msgs));
  };

  const sendMessage = async (text) => {
    const userMessage = {
      text,
      isUser: true,
      timestamp: new Date().toISOString()
    };
    
    const newMessages = [...messages, userMessage];
    setMessages(newMessages);
    saveMessages(newMessages);
    
    try {
      const response = await api.post('/chat', { 
        message: text,
        sessionStart 
      });
      
      const botResponse = {
        text: response.data.message,
        isUser: false,
        timestamp: new Date().toISOString(),
        products: response.data.products
      };
      
      const updatedMessages = [...newMessages, botResponse];
      setMessages(updatedMessages);
      saveMessages(updatedMessages);
    } catch (error) {
      const errorResponse = {
        text: "Sorry, I'm having trouble connecting. Please try again.",
        isUser: false,
        timestamp: new Date().toISOString()
      };
      
      const updatedMessages = [...newMessages, errorResponse];
      setMessages(updatedMessages);
      saveMessages(updatedMessages);
    }
  };

  const resetChat = () => {
    setMessages([]);
    saveMessages([]);
  };

  const value = {
    messages,
    sendMessage,
    resetChat
  };

  return (
    <ChatContext.Provider value={value}>
      {children}
    </ChatContext.Provider>
  );
}