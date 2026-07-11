import { useEffect, useState } from "react";

import MainLayout from "../layouts/MainLayout";

import { getDashboardAnalytics } from "../services/analyticsService";

function Analytics() {

    const [analytics, setAnalytics] = useState({});

    useEffect(() => {

        const fetchAnalytics = async () => {

            try {

                const data = await getDashboardAnalytics();

                setAnalytics(data);

            }

            catch (error) {

                console.log(error);

            }

        };

        fetchAnalytics();

    }, []);

    return (

        <MainLayout>

            <h1 className="text-3xl font-bold mb-5">

                Analytics

            </h1>

            <pre>

                {JSON.stringify(analytics, null, 2)}

            </pre>

        </MainLayout>

    );

}

export default Analytics;