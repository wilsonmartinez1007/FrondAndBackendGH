import { useEffect } from "react";
import { getALLTasks } from '../api/tasks.api';
export function TasksList() {
    useEffect(()=>{
            function loadTasks(){
                const res = getALLTasks();
                console.log(res);
            }
        loadTasks();
    }, []);
    return <div>TasksList</div>;
    
}