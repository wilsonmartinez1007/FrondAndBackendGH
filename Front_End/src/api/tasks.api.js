import { axios } from 'axios';

export const getALLTasks =()=>{
    return axios.get('http://localhost:8000/user/register/')
}