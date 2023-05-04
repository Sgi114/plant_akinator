import "./Top.css";
import lamp_majin from "./lamp_majin.png";

export const Top = () => {
  return (
    <div className="container">
      <div className="top-panel"></div>
      <div className="center-panel">
        <div className="akinator-image">
          <img
            src={lamp_majin}
            alt="Akinator"
            style={{ marginTop: 10, marginBottom: 10 }}
          />
          <div className="akinator-bubble">やあ、私はアキネイターです</div>
        </div>
        <button className="akinator-button">プレイする</button>
      </div>
      <div className="bottom-panel"></div>
    </div>
  );
};
