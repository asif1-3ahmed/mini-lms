import API from '../api';

export async function registerUser(username, email, password) {
  try {
    const response = await API.post('/register/', { username, email, password });
    return response.data;
  } catch (error) {
    throw error.response?.data || error;
  }
}

export async function loginUser(username, password) {
  try {
    const response = await API.post('/login/', { username, password });
    return response.data;
  } catch (error) {
    throw error.response?.data || error;
  }
}
