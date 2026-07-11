import { useEffect, useState } from "react";

import MainLayout from "../layouts/MainLayout";

import { getRecommendations } from "../services/inventoryService";

function Inventory() {

    const [recommendations, setRecommendations] = useState([]);

    useEffect(() => {

        const fetchRecommendations = async () => {

            try {

                const data = await getRecommendations();

                setRecommendations(data);

            }

            catch (error) {

                console.error(error);

            }

        };

        fetchRecommendations();

    }, []);

    return (

        <MainLayout>

            <h1 className="text-3xl font-bold mb-6">

                Inventory Recommendations

            </h1>

            <div className="overflow-x-auto">

                <table className="min-w-full border border-gray-300">

                    <thead className="bg-gray-100">

                        <tr>

                            <th className="border p-3">

                                Product

                            </th>

                            <th className="border p-3">

                                Store

                            </th>

                            <th className="border p-3">

                                Forecast

                            </th>

                            <th className="border p-3">

                                Current Stock

                            </th>

                            <th className="border p-3">

                                Safety Stock

                            </th>

                            <th className="border p-3">

                                Recommendation

                            </th>

                        </tr>

                    </thead>

                    <tbody>

                        {

                            recommendations.length > 0 ?

                            recommendations.map((item, index) => (

                                <tr key={index}>

                                    <td className="border p-2">

                                        {item.product}

                                    </td>

                                    <td className="border p-2">

                                        {item.store}

                                    </td>

                                    <td className="border p-2">

                                        {item.forecast}

                                    </td>

                                    <td className="border p-2">

                                        {item.current_stock}

                                    </td>

                                    <td className="border p-2">

                                        {item.safety_stock}

                                    </td>

                                    <td className="border p-2 font-semibold">

                                        {item.recommendation}

                                    </td>

                                </tr>

                            ))

                            :

                            <tr>

                                <td
                                    colSpan="6"
                                    className="border p-4 text-center"
                                >

                                    No Recommendations Available

                                </td>

                            </tr>

                        }

                    </tbody>

                </table>

            </div>

        </MainLayout>

    );

}

export default Inventory;