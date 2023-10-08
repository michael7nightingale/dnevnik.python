import axios from "axios";
import {buildUrl} from "@/services/Base";
import {getHeaders} from "@/services/Auth";


export function getSubjects(){
    return axios
        .get(
            buildUrl("lessons/subjects"),
        {
            headers: getHeaders()
             }
        )
}


