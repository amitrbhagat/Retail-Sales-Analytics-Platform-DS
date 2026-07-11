import { useState } from "react";

import MainLayout from "../layouts/MainLayout";

function Reports() {

    const [report] = useState({

        totalRevenue: "Available in Dashboard",

        forecast: "Available in Forecast",

        inventory: "Available in Inventory",

        aiAssistant: "Available in AI Assistant"

    });

    const exportReport = () => {

        const content = `
Retail Sales Analytics Report

=================================

Revenue
-------
${report.totalRevenue}

Forecast
--------
${report.forecast}

Inventory
---------
${report.inventory}

AI Assistant
------------
${report.aiAssistant}
`;

        const blob = new Blob(
            [content],
            {
                type: "text/plain"
            }
        );

        const url = window.URL.createObjectURL(blob);

        const link = document.createElement("a");

        link.href = url;

        link.download = "Retail_Report.txt";

        link.click();

        window.URL.revokeObjectURL(url);

    };

    return (

        <MainLayout>

            <h1 className="text-3xl font-bold mb-6">

                Reports

            </h1>

            <div className="bg-white shadow rounded p-6">

                <p className="mb-4">

                    Download a simple business report.

                </p>

                <button

                    onClick={exportReport}

                    className="bg-green-600 text-white px-5 py-2 rounded"

                >

                    Download Report

                </button>

            </div>

        </MainLayout>

    );

}

export default Reports;