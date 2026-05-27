import React, {
    useEffect,
    useState
} from "react";

import API from "../services/api";
import DashboardCards from "../components/DashboardCards";
import EmissionTable from "../components/EmissionTable";
import ReviewTable from "../components/ReviewTable";

function Dashboard() {

    const [stats, setStats] =
        useState({
            total:0,
            suspicious:0,
            pending:0,
            co2e:0
        });

    useEffect(() => {

        loadDashboard();

    }, []);

    const loadDashboard = async() => {

        const res =
            await API.get(
                "emissions/list/"
            );

        const data =
            res.data.data;

        const suspicious =
            data.filter(
                d => d.is_suspicious
            ).length;

        const pending =
            data.filter(
                d =>
                d.review_status ===
                "PENDING"
            ).length;

        const totalCO2 =
            data.reduce(
                (a,b)=>
                a+b.co2e,
                0
            );

        setStats({

            total:
            data.length,

            suspicious,

            pending,

            co2e:
            totalCO2.toFixed(2)

        });
    };

    return (

        <div>

            <h1>
                ESG Dashboard
            </h1>

            <DashboardCards
                total={stats.total}
                suspicious={
                    stats.suspicious
                }
                pending={
                    stats.pending
                }
                co2e={
                    stats.co2e
                }
            />

        </div>
    );
}

export default Dashboard;