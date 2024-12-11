import axios from 'axios';
export const getALLTasks = () => {
    return axios.get('http://localhost:5173/')
}