import axios from 'axios';

const API_URL = 'http://localhost:8000/api/dishes/';

export const getDishes = () => {
    return axios.get(API_URL);
}

export const togglePublish = (dishId) => {
    return axios.post(`${API_URL}${dishId}/toggle_publish/`);
}
