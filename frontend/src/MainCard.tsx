import React from "react";
import "./MainCard.css";

type Props = {
  children?: React.ReactNode;
};

export const MainCard = (props: Props) => {
  return <div className="card-container">{props.children}</div>;
};
