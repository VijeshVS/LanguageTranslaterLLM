"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
const groq_1 = require("@langchain/groq");
const messages_1 = require("@langchain/core/messages");
const prompts_1 = require("@langchain/core/prompts");
// Initializing a model
const model = new groq_1.ChatGroq({
    model: "mixtral-8x7b-32768",
    temperature: 0
});
function main() {
    return __awaiter(this, void 0, void 0, function* () {
        const systemTemplate = "Translate the following from English into {language}";
        // Generating a prompt template
        const promptTemplate = prompts_1.ChatPromptTemplate.fromMessages([
            ["system", systemTemplate],
            ["user", "{text}"],
        ]);
        // Invoking the prompt template
        const promptValue = yield promptTemplate.invoke({
            language: "italian",
            text: "hi"
        });
        console.log(new messages_1.HumanMessage("hello"));
        const response = yield model.invoke(promptValue);
        console.log(response.content);
    });
}
main();
