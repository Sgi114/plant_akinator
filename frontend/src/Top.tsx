import "./Top.css";
import lamp_majin from "./lamp_majin.png";

export const Top = () => {
  return (
    <div className="akinator-container">
      <div className="akinator-image">
        <img src={lamp_majin} alt="Akinator" />
        <div className="akinator-bubble">やあ、私はアキネイターです</div>
      </div>
      <button className="akinator-button">プレイする</button>
    </div>
  );
};
