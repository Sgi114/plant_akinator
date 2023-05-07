import React, { useState } from "react";
import "./Question.css";

export const Question = () => {
  const [question, setQuestion] = useState<string>(
    "Do you think of a real or fictional character?"
  );

  const handleAnswer = (answer: string): void => {
    // TODO: implement logic for handling answer
  };

  return (
    <div className="akinator-container">
      <div className="akinator-question">{question}</div>
      <div className="akinator-options">
        <button
          className="akinator-option"
          onClick={() => handleAnswer("real")}
        >
          Real
        </button>
        <button
          className="akinator-option"
          onClick={() => handleAnswer("fictional")}
        >
          Fictional
        </button>
      </div>
    </div>
  );
};
