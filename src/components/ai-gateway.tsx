import React from 'react';
import './ai-gateway.css';

export default function AIGateway() {
  // Replace these with your actual shared chat links
  const links = {
    notebookLM: "https://notebooklm.google.com/...",
    gemini: "https://gemini.google.com/share/...",
    chatgpt: "https://chatgpt.com/share/...",
  };

  return (
    <div className="ai-gateway-wrapper">
      <div className="gateway-header">
        <h4>Discuss the Monograph</h4>
        <p>Choose your preferred AI to explore the Quantum Braid Dynamics framework, ask questions, or challenge the theorems.</p>
      </div>
      
      <div className="gateway-button-grid">
        {/* NotebookLM Button */}
        <a href={links.notebookLM} target="_blank" rel="noopener noreferrer" className="gateway-btn btn-notebook">
          <div className="btn-icon">
            {/* Simple Document Icon */}
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
          </div>
          <div className="btn-text">
            <span className="btn-title">NotebookLM</span>
            <span className="btn-sub">Best for strict citations</span>
          </div>
        </a>

        {/* Gemini Button */}
        <a href={links.gemini} target="_blank" rel="noopener noreferrer" className="gateway-btn btn-gemini">
          <div className="btn-icon">
            {/* Simple Sparkle/Star Icon */}
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M12 3v18"></path><path d="M3 12h18"></path><path d="m5 5 14 14"></path><path d="m19 5-14 14"></path></svg>
          </div>
          <div className="btn-text">
            <span className="btn-title">Gemini</span>
            <span className="btn-sub">Best for deep context</span>
          </div>
        </a>

        {/* ChatGPT Button (Optional) */}
        <a href={links.chatgpt} target="_blank" rel="noopener noreferrer" className="gateway-btn btn-chatgpt">
          <div className="btn-icon">
             {/* Simple Message Icon */}
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
          </div>
          <div className="btn-text">
            <span className="btn-title">ChatGPT</span>
            <span className="btn-sub">Best for code translation</span>
          </div>
        </a>
      </div>
    </div>
  );
}