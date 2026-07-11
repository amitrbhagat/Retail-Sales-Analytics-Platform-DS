import { useEffect, useState } from "react";

import MainLayout from "../layouts/MainLayout";

import { getForecast } from "../services/forecastService";

function Forecast() {

    const [forecast, setForecast] = useState([]);

    useEffect(() => {

        const fetchForecast = async () => {

            try {

                const data = await getForecast();

                setForecast(data);

            }

            catch (error) {

                console.log(error);

            }

        };

        fetchForecast();

    }, []);

    return (

        <MainLayout>

            <h1 className="text-3xl font-bold mb-5">

                Forecast

            </h1>

            <pre>

                {JSON.stringify(forecast, null, 2)}

            </pre>

        </MainLayout>

    );

}

export default Forecast;