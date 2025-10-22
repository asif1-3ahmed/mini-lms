import axios from "axios";

// 🛑 CRITICAL FIX: Read the URL from a Vite environment variable.
// It falls back to the local address if the environment variable is not set.
const API_BASE_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

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
