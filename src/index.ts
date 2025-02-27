import { ChatGroq } from "@langchain/groq";
import { HumanMessage, SystemMessage } from "@langchain/core/messages";
import { ChatPromptTemplate } from "@langchain/core/prompts";

// Initializing a model
const model = new ChatGroq({
  model: "mixtral-8x7b-32768",
  temperature: 0
});

async function main() {
    const systemTemplate = "Translate the following from English into {language}";
    // Generating a prompt template
    const promptTemplate = ChatPromptTemplate.fromMessages([
        ["system", systemTemplate],
        ["user", "{text}"],
      ]);

    // Invoking the prompt template
    const promptValue = await promptTemplate.invoke({
        language: "italian",
        text: "hi"
    })

    const response = await model.invoke(promptValue);
    console.log(response.content);
}

main();