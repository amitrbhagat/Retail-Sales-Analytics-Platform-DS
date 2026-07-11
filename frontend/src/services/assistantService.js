import api from "./api";

export const askAssistant = async (question) => {

    const response = await api.post(

        "ai/chat/",

        {

            question

        }

    );

    return response.data;

};