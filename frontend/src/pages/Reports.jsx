import MainLayout from "../layouts/MainLayout";

function Reports() {

    return (

        <MainLayout>

            <h1 className="text-3xl font-bold mb-5">

                Reports

            </h1>

            <button

                className="bg-green-600 text-white px-5 py-2 rounded"

            >

                Export CSV

            </button>

        </MainLayout>

    );

}

export default Reports;