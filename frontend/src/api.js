import axios from "axios";

// FINAL FIX: Use an empty string for the baseURL 
// so API calls use the current host (your Render domain).
const API_BASE_URL = ""; 

const API = axios.create({
  baseURL: API_BASE_URL,
});

API.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default API;
