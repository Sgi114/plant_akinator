import { MainCard } from "./MainCard";
import "./Top.css";
import { TopContent } from "./TopContent";

export const Top = () => {
  return (
    <div className="container">
      <MainCard>
        <TopContent />
      </MainCard>
    </div>
  );
};
