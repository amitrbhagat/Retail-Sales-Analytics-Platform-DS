import { useState } from "react";

import MainLayout from "../layouts/MainLayout";

import { askAssistant } from "../services/assistantService";

function Assistant() {

    const [question, setQuestion] = useState("");

    const [answer, setAnswer] = useState("");

    const [loading, setLoading] = useState(false);

    const handleAsk = async () => {

        if (!question.trim()) {

            alert("Enter a question.");

            return;

        }

        try {

            setLoading(true);

            const data = await askAssistant(question);

            setAnswer(data.answer);

        }

        catch (error) {

            console.log(error);

            alert("Unable to get response.");

        }

        finally {

            setLoading(false);

        }

    };

    return (

        <MainLayout>

            <h1 className="text-3xl font-bold mb-6">

                AI Business Assistant

            </h1>

            <textarea

                rows="5"

                className="border rounded w-full p-3"

                placeholder="Ask a business question..."

                value={question}

                onChange={(e) =>
                    setQuestion(e.target.value)
                }

            />

            <button

                onClick={handleAsk}

                className="bg-blue-600 text-white px-5 py-2 rounded mt-4"

            >

                {

                    loading

                    ?

                    "Thinking..."

                    :

                    "Ask AI"

                }

            </button>

            <div className="mt-8">

                <h2 className="text-xl font-semibold mb-3">

                    Response

                </h2>

                <div className="border rounded p-4 bg-gray-50 min-h-[120px]">

                    {

                        answer ||

                        "The AI response will appear here."

                    }

                </div>

            </div>

        </MainLayout>

    );

}

export default Assistant;