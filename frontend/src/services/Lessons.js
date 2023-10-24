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


export function getTeachingClasses(){
    return axios
        .get(
            buildUrl("lessons/teacher/classes/all"),
           {
            headers: getHeaders()
             }
        )
}


export function getTeachingClass(classId){
    return axios
        .get(
            buildUrl(`lessons/teacher/classes/detail/${classId}`),
           {
            headers: getHeaders()
             }
        )
}


export function updateMark(markId, newMark){
    return axios
        .patch(
            buildUrl(`lessons/marks/${markId}`),
            {
                mark: newMark
            },
            {
                headers: getHeaders()
            }
        )
}


export function createMark(lessonId, pupilId, newMark){
    return axios
        .post(
            buildUrl("lessons/marks/"),
            {
                mark: newMark,
                lesson_id: lessonId,
                pupil_id: pupilId
            },
            {
                headers: getHeaders()
            }
        )
}
