import React,{
useEffect,
useState
} from "react";

import API from "../services/api";
import ReviewTable from
"../components/ReviewTable";

function Reviews(){

const [data,
setData]=
useState([]);

const load=
async()=>{

const res=
await API.get(
"emissions/list/"
);

setData(
res.data.data
);
};

useEffect(()=>{
load();
},[]);

return(

<div>

<h1>
Reviews
</h1>

<ReviewTable
data={data}
reload={load}
/>

</div>
);
}

export default Reviews;