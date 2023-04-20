import { useState } from "react";
import { Box, Grid, Paper, TextField, Button, Typography } from "@mui/material";
import { CustomPaper } from "./CustomPaper";
import SendIcon from "@mui/icons-material/Send";

export const App = () => {
  const [messageList, setMessageList] = useState<string[]>([]);
  const [newMessage, setNewMessage] = useState("");

  const handleMessageSubmit = () => {
    if (!newMessage.length) {
      return;
    }
    setMessageList((prev) => [...prev, newMessage]);
    setNewMessage("");
  };
  return (
    <Box sx={{ display: "flex", flexDirection: "column", height: "100vh" }}>
      <Grid item xs={12}>
        <CustomPaper>
          <Typography variant="h4">Plant Akinator</Typography>
        </CustomPaper>
      </Grid>
      <Box sx={{ flex: 1, overflow: "auto" }}>
        {messageList.map((message) => (
          <Paper sx={{ padding: "16px", margin: "8px" }}>{message}</Paper>
        ))}
      </Box>
      <Box sx={{ display: "flex", padding: "8px" }}>
        <TextField
          sx={{ flex: 1, marginRight: "8px" }}
          label="メッセージを入力"
          variant="outlined"
          value={newMessage}
          onChange={(e) => setNewMessage(e.target.value)}
        />
        <Button variant="contained" onClick={handleMessageSubmit}>
          <SendIcon />
        </Button>
      </Box>
    </Box>
  );
};
