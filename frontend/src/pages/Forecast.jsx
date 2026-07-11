import { useEffect, useState } from "react";

import MainLayout from "../layouts/MainLayout";

import { getForecast } from "../services/forecastService";

function Forecast() {

    const [forecasts, setForecasts] = useState([]);

    useEffect(() => {

        const fetchForecasts = async () => {

            try {

                const data = await getForecast();

                setForecasts(data);

            }

            catch (error) {

                console.error(error);

            }

        };

        fetchForecasts();

    }, []);

    return (

        <MainLayout>

            <h1 className="text-3xl font-bold mb-6">

                Sales Forecast

            </h1>

            <div className="overflow-x-auto">

                <table className="min-w-full border border-gray-300">

                    <thead className="bg-gray-100">

                        <tr>

                            <th className="border p-3">ID</th>

                            <th className="border p-3">Product ID</th>

                            <th className="border p-3">Store ID</th>

                            <th className="border p-3">Forecast Date</th>

                            <th className="border p-3">Predicted Sales</th>

                            <th className="border p-3">Model</th>

                            <th className="border p-3">Confidence</th>

                        </tr>

                    </thead>

                    <tbody>

                        {

                            forecasts.length > 0 ?

                            forecasts.map((forecast) => (

                                <tr key={forecast.id}>

                                    <td className="border p-2">

                                        {forecast.id}

                                    </td>

                                    <td className="border p-2">

                                        {forecast.product}

                                    </td>

                                    <td className="border p-2">

                                        {forecast.store}

                                    </td>

                                    <td className="border p-2">

                                        {forecast.forecast_date}

                                    </td>

                                    <td className="border p-2">

                                        {forecast.predicted_sales}

                                    </td>

                                    <td className="border p-2">

                                        {forecast.model_name}

                                    </td>

                                    <td className="border p-2">

                                        {forecast.confidence_score}

                                    </td>

                                </tr>

                            ))

                            :

                            <tr>

                                <td
                                    colSpan="7"
                                    className="border p-4 text-center"
                                >

                                    No Forecast Records Found

                                </td>

                            </tr>

                        }

                    </tbody>

                </table>

            </div>

        </MainLayout>

    );

}

export default Forecast;