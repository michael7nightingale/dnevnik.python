import axios from "axios";
import {buildUrl} from "@/services/Base";
import {getHeaders} from "@/services/Auth";


export function getMyClass(){
    return axios
        .get(
            buildUrl("classes/my-class"),
        {
            headers: getHeaders()
             }
        )
}
