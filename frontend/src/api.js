import axios from "axios";

// 🛑 CRITICAL FIX for Separate Deployment:
// Set the absolute URL of your live Render backend service.
// Replace the placeholder with your actual live Django API URL.
const API_BASE_URL = "https://mini-lms-crh4.onrender.com"; 

const API = axios.create({
  baseURL: API_BASE_URL,
});

API.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) {
    // Note: All API routes must now be prefixed with '/api/auth/' if that's your Django setup
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default API;
