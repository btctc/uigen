import { query } from "@anthropic-ai/claude-code";

const prompt = "Look at the src directory and give me a brief summary of what this project does";

for await (const message of query({ prompt })) {
  if (message.type === "result") {
    console.log(message.result);
  }
}