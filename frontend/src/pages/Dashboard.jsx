import { useEffect, useState } from "react";

import MainLayout from "../layouts/MainLayout";

import { getDashboardAnalytics } from "../services/analyticsService";

function Dashboard() {

    const [analytics, setAnalytics] = useState({});

    useEffect(() => {

        const fetchDashboard = async () => {

            const data = await getDashboardAnalytics();

            setAnalytics(data);

        };

        fetchDashboard();

    }, []);

    return (

        <MainLayout>

            <h1 className="text-3xl font-bold mb-5">

                Dashboard

            </h1>

            <pre>

                {JSON.stringify(

                    analytics,

                    null,

                    2

                )}

            </pre>

        </MainLayout>

    );

}

export default Dashboard;