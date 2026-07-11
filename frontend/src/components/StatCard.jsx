import StatCard from "../components/StatCard";

function Dashboard() {

    return (

        <div>

            <h1 className="text-3xl font-bold mb-6">

                Dashboard

            </h1>

            <div className="grid grid-cols-4 gap-5">

                <StatCard
                    title="Revenue"
                    value="$125,000"
                />

                <StatCard
                    title="Orders"
                    value="2,540"
                />

                <StatCard
                    title="Products"
                    value="420"
                />

                <StatCard
                    title="Customers"
                    value="980"
                />

            </div>

        </div>

    );

}

export default Dashboard;