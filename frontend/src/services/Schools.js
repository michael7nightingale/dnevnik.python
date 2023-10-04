import axios from "axios";
import {buildUrl} from "@/services/Base";
import {getHeaders} from "@/services/Auth";


export function getMySchool(){
    return axios
        .get(
            buildUrl("schools/my-school"),
        {
            headers: getHeaders()
             }
        )
}
