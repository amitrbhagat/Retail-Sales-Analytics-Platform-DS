import api from "./api";

export const getInventory = async () => {

    const response = await api.get(

        "inventory/"

    );

    return response.data;

};

export const createInventory = async (data) => {

    const response = await api.post(

        "inventory/",

        data

    );

    return response.data;

};