import { useEffect, useState } from "react";

import MainLayout from "../layouts/MainLayout";

import { getDashboardAnalytics } from "../services/analyticsService";

function Dashboard() {

    const [analytics, setAnalytics] = useState({});

    useEffect(() => {

        const fetchDashboard = async () => {

            try {

                const data = await getDashboardAnalytics();

                setAnalytics(data);

            }

            catch (error) {

                console.log(error);

            }

        };

        fetchDashboard();

    }, []);

    return (

        <MainLayout>

            <h1 className="text-3xl font-bold mb-6">

                Dashboard

            </h1>

            <div className="grid grid-cols-1">

                <div className="bg-white shadow rounded p-6">

                    <h2 className="text-lg font-semibold">

                        Total Revenue

                    </h2>

                    <p className="text-3xl mt-3">

                        ₹ {analytics.total}

                    </p>

                </div>

            </div>

        </MainLayout>

    );

}

export default Dashboard;