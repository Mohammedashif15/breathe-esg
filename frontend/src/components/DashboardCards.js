import React from "react";

function DashboardCards({
    total,
    suspicious,
    pending,
    co2e
}) {

    return (

        <div className="cards">

            <div className="card">
                <h3>Total Records</h3>
                <h2>{total}</h2>
            </div>

            <div className="card">
                <h3>Suspicious</h3>
                <h2>{suspicious}</h2>
            </div>

            <div className="card">
                <h3>Pending</h3>
                <h2>{pending}</h2>
            </div>

            <div className="card">
                <h3>Total CO₂e</h3>
                <h2>{co2e}</h2>
            </div>

        </div>
    );
}

export default DashboardCards;