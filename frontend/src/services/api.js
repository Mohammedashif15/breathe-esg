import axios from "axios";

const API = axios.create({
  baseURL: "https://breathe-esg-jxl5.onrender.com/api/",
});

API.interceptors.response.use(
  (response) => response,
  (error) => {
    console.log(
      "API Error:",
      error.response?.data || error.message
    );
    return Promise.reject(error);
  }
);

export default API;
