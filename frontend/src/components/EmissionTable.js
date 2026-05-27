import React, {
    useState
} from "react";

function EmissionTable({
    emissions
}) {

    const [search,
        setSearch] =
        useState("");

    return (

        <div>

            <input
                placeholder="Search activity"
                value={search}
                onChange={(e)=>
                    setSearch(
                        e.target.value
                    )
                }
            />

            <table>

                <thead>

                    <tr>
                        <th>Activity</th>
                        <th>Scope</th>
                        <th>CO₂e</th>
                        <th>Status</th>
                    </tr>

                </thead>

                <tbody>

                    {emissions
                        .filter(
                            e =>
                            e.activity_type
                            .toLowerCase()
                            .includes(
                                search
                                .toLowerCase()
                            )
                        )
                        .map(
                        e=>(

                        <tr key={e.id}>

                            <td>
                                {e.activity_type}
                            </td>

                            <td>
                                {e.scope}
                            </td>

                            <td>
                                {e.co2e}
                            </td>

                            <td>

                                <span
                                className={
                                e.is_suspicious
                                ?
                                "red"
                                :
                                "green"
                                }>

                                {
                                e.is_suspicious
                                ?
                                "Suspicious"
                                :
                                "Normal"
                                }

                                </span>

                            </td>

                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default EmissionTable;