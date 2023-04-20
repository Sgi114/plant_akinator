import React, { useState } from "react";
import {
  Box,
  Grid,
  TextField,
  Button,
  Typography,
  ListItemText,
  ListItem,
  List,
} from "@mui/material";
import { styled } from "@mui/system";
import { CustomPaper } from "./CustomPaper";

export const App = () => {
  const ChatArea = styled(CustomPaper)(({ theme }) => ({
    height: "400px",
    overflowY: "auto",
    marginBottom: "10px",
  }));

  const [messages, setMessages] = useState<string[]>([]);
  const [newMessage, setNewMessage] = useState("");

  const handleMessageSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setMessages([...messages, newMessage]);
    setNewMessage("");
  };
  return (
    <Box style={{ flexGrow: 1 }}>
      <Grid container spacing={3}>
        <Grid item xs={12}>
          <CustomPaper>
            <Typography variant="h4">Plant Akinator</Typography>
          </CustomPaper>
        </Grid>
        <Grid item xs={12} md={8}>
          <ChatArea>
            <List>
              {messages.map((message, index) => (
                <ListItem key={index}>
                  <ListItemText primary={message} />
                </ListItem>
              ))}
            </List>
          </ChatArea>
          <CustomPaper>
            <form onSubmit={handleMessageSubmit}>
              <TextField
                fullWidth
                label="Type your message here"
                variant="outlined"
                value={newMessage}
                onChange={(e) => setNewMessage(e.target.value)}
              />
              <Button
                type="submit"
                variant="contained"
                color="primary"
                style={{ marginLeft: "10px" }}
              >
                Send
              </Button>
            </form>
          </CustomPaper>
        </Grid>
        <Grid item xs={12} md={4}>
          <CustomPaper>
            <Typography variant="h6">ChatGPT Help</Typography>
            <Typography variant="body1">
              Type your message in the text box at the bottom of the screen and
              click "Send" to send the message to ChatGPT.
            </Typography>
          </CustomPaper>
        </Grid>
      </Grid>
    </Box>
  );
};
