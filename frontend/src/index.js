// PASTE THIS CODE INTO frontend/src/index.js

import React from 'react';
import ReactDOM from 'react-dom/client';
import './App.css'; // Or your main css file
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);