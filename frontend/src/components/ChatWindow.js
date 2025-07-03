import React, { useState, useEffect, useRef } from 'react';
import Message from './Message';
import './ChatWindow.css';

const ChatWindow = () => {
  const [messages, setMessages] = useState([{ text: 'Hello! How can I help with MOSDAC data today?', sender: 'bot' }]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const handleSend = async () => {
    if (input.trim() === '') return;
    const newMessages = [...messages, { text: input, sender: 'user' }];
    setMessages(newMessages);
    setInput('');
    setIsLoading(true);
    try {
      const response = await fetch('http://localhost:8000/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: input }),
      });
      const data = await response.json();
      setMessages([...newMessages, { text: data.reply, sender: 'bot' }]);
    } catch (error) {
      setMessages([...newMessages, { text: 'Error connecting to the backend.', sender: 'bot' }]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !isLoading) handleSend();
  };

  return (
    <div className="chat-window">
      <div className="message-list">
        {messages.map((msg, index) => <Message key={index} text={msg.text} sender={msg.sender} />)}
        {isLoading && <Message text="..." sender="bot" />}
        <div ref={messagesEndRef} />
      </div>
      <div className="input-area">
        <input type="text" value={input} onChange={(e) => setInput(e.target.value)} onKeyPress={handleKeyPress} placeholder="Ask about satellites or products..." disabled={isLoading} />
        <button onClick={handleSend} disabled={isLoading}>Send</button>
      </div>
    </div>
  );
};
export default ChatWindow;