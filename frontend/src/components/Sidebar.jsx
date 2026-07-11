import { Link } from "react-router-dom";

function Sidebar() {

    return (

        <aside className="w-64 min-h-screen bg-gray-100 p-5">

            <ul className="space-y-4">

                <li>

                    <Link to="/">

                        Dashboard

                    </Link>

                </li>

                <li>

                    <Link to="/analytics">

                        Analytics

                    </Link>

                </li>

                <li>

                    <Link to="/forecast">

                        Forecast

                    </Link>

                </li>

                <li>

                    <Link to="/inventory">

                        Inventory

                    </Link>

                </li>

                <li>

                    <Link to="/assistant">

                        AI Assistant

                    </Link>

                </li>

                <li>

                    <Link to="/reports">

                        Reports

                    </Link>

                </li>

                <li>

                    <Link to="/settings">

                        Settings

                    </Link>

                </li>

            </ul>

        </aside>

    );

}

export default Sidebar;