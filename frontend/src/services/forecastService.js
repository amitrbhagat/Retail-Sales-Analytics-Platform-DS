import api from "./api";

export const getForecast = async () => {

    const response = await api.get(

        "forecast/"

    );

    return response.data;

};

export const createForecast = async (data) => {

    const response = await api.post(

        "forecast/",

        data

    );

    return response.data;

};