import axios from 'axios';

export function api(accessToken) {
  return axios.create({
    baseURL: process.env.REACT_APP_API_URL,
    timeout: 1000,
    headers: {
      Authorization: `Bearer ${accessToken}`,
    },
  });
}
