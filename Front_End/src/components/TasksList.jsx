import { useEffect } from "react";
import {getALLTasks} from "../api/tasks.api";
export function TasksList() {
    useEffect(()=>{
        
        async function loadTasks() {
            const res = await getALLTasks();
            console.log(res);
        }
        loadTasks();
    }, []);
    return <div>TasksList</div>;
    
}