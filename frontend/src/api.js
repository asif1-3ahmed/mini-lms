import axios from "axios";

// FINAL FIX: Use an empty string for the baseURL.
// This makes all API calls relative to the host serving the frontend 
// (which is your live Render domain), bypassing environment variable issues.
const API_BASE_URL = "";

const API = axios.create({
  baseURL: API_BASE_URL,
});

API.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) {
    // Note: The 'Bearer' scheme is correct for Django Rest Framework JWT/Token authentication
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default API;
