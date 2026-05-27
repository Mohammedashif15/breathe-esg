import React from "react";
import API from "../services/api";

function ReviewTable({
    data,
    reload
}) {

    const update =
    async(id,status)=>{

        await API.post(
        "emissions/review/",
        {
            id,
            review_status:
            status
        });

        reload();
    };

    return(

        <table>

            <thead>

            <tr>
                <th>Activity</th>
                <th>Status</th>
                <th>Action</th>
            </tr>

            </thead>

            <tbody>

            {data.map(
            r=>(

            <tr key={r.id}>

                <td>
                    {r.activity_type}
                </td>

                <td>
                    {r.review_status}
                </td>

                <td>

                    <button
                    onClick={()=>
                    update(
                    r.id,
                    "APPROVED"
                    )}>
                    Approve
                    </button>

                    <button
                    onClick={()=>
                    update(
                    r.id,
                    "REJECTED"
                    )}>
                    Reject
                    </button>

                </td>

            </tr>
            ))}

            </tbody>
        </table>
    );
}

export default ReviewTable;