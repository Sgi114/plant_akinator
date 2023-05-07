import { Box, Button, ButtonProps } from "@mui/material";

export const QuestionContent = () => {
  type ControlButtonProps = {
    text: string;
    onClick?: React.MouseEventHandler<HTMLButtonElement>;
  } & ButtonProps;
  const ControlButton = (props: ControlButtonProps) => (
    <Button
      {...props}
      variant={props.variant ?? "contained"}
      size="large"
      onClick={props.onClick}
      sx={{
        fontWeight: 500,
        fontSize: 18,
        borderRadius: 50,
        px: 6,
        py: 1,
        ...props.sx,
      }}
    >
      {props.text}
    </Button>
  );

  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "row",
        alignItems: "start",
      }}
    >
      <ControlButton text="yes" sx={{ mr: 2 }} color="success" />
      <ControlButton text="no" sx={{ mr: 2 }} color="error" />
      {/* FIXME: themeで`neutral`を作ってそれに置き換える 参考サイト：https://mui.com/material-ui/customization/palette/ */}
      <ControlButton text="skip" variant="outlined" color="info" />
    </Box>
  );
};
