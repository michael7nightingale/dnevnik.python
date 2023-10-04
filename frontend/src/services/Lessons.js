import axios from "axios";
import {buildUrl} from "@/services/Base";
import {getHeaders} from "@/services/Auth";


export function getLessons(){
    return axios
        .get(
            buildUrl("lessons"),
        {
            headers: getHeaders()
             }
        )
}

