import axios from "axios";
import {buildUrl} from "@/services/Base";
import {getHeaders} from "@/services/Auth";


export function getMarks(){
    return axios
        .get(
            buildUrl("marks"),
        {
            headers: getHeaders()
             }
        )
}
