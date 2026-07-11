import { useState } from "react";

import MainLayout from "../layouts/MainLayout";

import { askAssistant } from "../services/assistantService";

function Assistant() {

    const [question, setQuestion] = useState("");

    const [answer, setAnswer] = useState("");

    const ask = async () => {

        try {

            const response = await askAssistant(question);

            setAnswer(response.answer);

        }

        catch (error) {

            console.log(error);

        }

    };

    return (

        <MainLayout>

            <h1 className="text-3xl font-bold mb-5">

                AI Assistant

            </h1>

            <textarea

                rows="5"

                className="border w-full p-3"

                value={question}

                onChange={(e) =>

                    setQuestion(e.target.value)

                }

            />

            <button

                onClick={ask}

                className="bg-blue-600 text-white px-5 py-2 rounded mt-4"

            >

                Ask

            </button>

            <div className="mt-6">

                <h2 className="font-bold mb-2">

                    Response

                </h2>

                <pre>

                    {answer}

                </pre>

            </div>

        </MainLayout>

    );

}

export default Assistant;