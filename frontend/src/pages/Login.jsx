import { useState } from "react";
import { useNavigate } from "react-router-dom";

import { login } from "../services/authService";

function Login() {

    const navigate = useNavigate();

    const [formData, setFormData] = useState({

        username: "",

        password: ""

    });

    const handleChange = (e) => {

        setFormData({

            ...formData,

            [e.target.name]: e.target.value

        });

    };

    const handleSubmit = async (e) => {

        e.preventDefault();

        try {

            const data = await login(formData);

            localStorage.setItem(

                "access",

                data.access

            );

            localStorage.setItem(

                "refresh",

                data.refresh

            );

            navigate("/");

        }

        catch {

            alert("Invalid Credentials");

        }

    };

    return (

        <div className="flex justify-center items-center h-screen">

            <form

                onSubmit={handleSubmit}

                className="border p-8 rounded shadow w-96"

            >

                <h2 className="text-2xl font-bold mb-5">

                    Login

                </h2>

                <input

                    className="border p-2 w-full mb-3"

                    name="username"

                    placeholder="Username"

                    onChange={handleChange}

                />

                <input

                    className="border p-2 w-full mb-5"

                    type="password"

                    name="password"

                    placeholder="Password"

                    onChange={handleChange}

                />

                <button

                    className="bg-blue-600 text-white w-full p-2 rounded"

                >

                    Login

                </button>

            </form>

        </div>

    );

}

export default Login;