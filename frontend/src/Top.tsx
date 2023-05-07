import { Box, Button, Typography } from "@mui/material";
import { MainCard } from "./MainCard";
import "./Top.css";
import lamp_majin from "./lamp_majin.png";

export const Top = () => {
  const characterMessageList = [
    "やあ、私は植物アキネーター。\n私が分からないバイオなんて、アキネーター失格じゃない？？",
    "こんにちは！\n植物を制す者は、バイオを制す。",
  ];

  // 指定範囲の整数をランダムに返す
  const getRandomInt = (max: number) => {
    return Math.floor(Math.random() * max);
  };

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
        {/* <h1 className="card-title">PlantAkinator</h1> */}
        <Typography variant="h2" gutterBottom style={{ fontWeight: 600 }}>
          PlantAkinator
        </Typography>
        <Box
          sx={{
            display: "flex",
            flexDirection: "row",
            alignItems: "start",
            // justifyContent: "center",
          }}
        >
          <img src={lamp_majin} alt="character" className="card-image" />
          <Box
            sx={{
              position: "relative",
              // bottom: "auto",
              top: 80,
              left: -30,
              // height: 100,
              // transform: "translateX(-50%)",
              backgroundColor: "white",
              border: "1px solid black",
              borderRadius: 5,
              padding: 1.5,
            }}
          >
            {characterMessageList[getRandomInt(characterMessageList.length)]
              .split("\n")
              .map((text) => (
                <>
                  {text}
                  <br />
                </>
              ))}
          </Box>
        </Box>
        {/* <button className="card-button">Button</button> */}
        <Button
          variant="contained"
          size="large"
          sx={{
            fontWeight: 600,
            fontSize: 20,
            borderRadius: 50,
            px: 8,
            py: 2,
          }}
        >
          Play
        </Button>
      </MainCard>
    </div>
  );
};
