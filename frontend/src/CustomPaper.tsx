import { createTheme, Paper } from "@mui/material";

type Props = {
  children: React.ReactNode;
};

export const CustomPaper = (props: Props) => {
  const theme = createTheme();
  return (
    <Paper
      style={{
        padding: "16px",
        textAlign: "center",
        color: theme.palette.text.secondary,
      }}
    >
      {props.children}
    </Paper>
  );
};
