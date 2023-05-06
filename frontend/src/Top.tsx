import { MainCard } from "./MainCard";
import "./Top.css";
import lamp_majin from "./lamp_majin.png";

export const Top = () => {
  return (
    <div className="container">
      {/* <div className="top-panel"></div>
      <div className="center-panel">
        <img
          src={lamp_majin}
          alt="Akinator"
          // style={{ paddingTop: 10, paddingBottom: 10 }}
          height={300}
        />
        <div className="akinator-bubble">やあ、私はアキネイターです</div>
        <button className="akinator-button">プレイする</button>
      </div>
      <div className="bottom-panel"></div> */}
      <MainCard>
        <h2 className="card-title">PlantAkinator</h2>
        <img src={lamp_majin} alt="Card Image" className="card-image" />
        <button className="card-button">Button</button>
      </MainCard>
    </div>
  );
};
