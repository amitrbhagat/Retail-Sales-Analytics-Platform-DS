import MainLayout from "../layouts/MainLayout";

function Settings() {

    const logout = () => {

        localStorage.removeItem("access");

        localStorage.removeItem("refresh");

        window.location.href = "/login";

    };

    return (

        <MainLayout>

            <h1 className="text-3xl font-bold mb-5">

                Settings

            </h1>

            <button

                onClick={logout}

                className="bg-red-600 text-white px-5 py-2 rounded"

            >

                Logout

            </button>

        </MainLayout>

    );

}

export default Settings;