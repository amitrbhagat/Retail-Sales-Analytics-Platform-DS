import { useEffect, useState } from "react";

import MainLayout from "../layouts/MainLayout";

import { getInventory } from "../services/inventoryService";

function Inventory() {

    const [inventory, setInventory] = useState([]);

    useEffect(() => {

        const fetchInventory = async () => {

            try {

                const data = await getInventory();

                setInventory(data);

            }

            catch (error) {

                console.log(error);

            }

        };

        fetchInventory();

    }, []);

    return (

        <MainLayout>

            <h1 className="text-3xl font-bold mb-5">

                Inventory

            </h1>

            <pre>

                {JSON.stringify(inventory, null, 2)}

            </pre>

        </MainLayout>

    );

}

export default Inventory;