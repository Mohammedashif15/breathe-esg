import React,{
    useEffect,
    useState
} from "react";

import API from "../services/api";
import EmissionTable from
"../components/EmissionTable";

function Emissions(){

    const [data,
        setData] =
        useState([]);

    useEffect(()=>{

        load();

    },[]);

    const load =
    async()=>{

        const res =
        await API.get(
        "emissions/list/"
        );

        setData(
        res.data.data
        );
    };

    return(

        <div>

            <h1>
                Emissions
            </h1>

            <EmissionTable
                emissions={data}
            />

        </div>
    );
}

export default Emissions;