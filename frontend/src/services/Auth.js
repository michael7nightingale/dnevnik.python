import {meUser} from "@/services/UserService";

export function setUser(token){
    localStorage.user = token;
    return meUser().then(response => {
        localStorage.userData = JSON.stringify(response.data);
    })


}


export function getUser(){
    if (!localStorage.userData) return null;
    let userData = JSON.parse(localStorage.userData)
    if (userData.user){
        return userData;
    }
    return null;
}


export function getHeaders(){
    let user = localStorage.user;
    let headers = {};
    if (user){
        headers['authorization'] = `Token ${user}`;
    }
    return headers
}


export function logoutUser(){
    localStorage.removeItem("user");
    localStorage.removeItem("userData")
}


export function isTeacher(userData){
    return userData.type === "teacher";
}


export function isPupil(userData){
    return userData.type === "pupil";
}


export function isPupilOrTeacher(userData){
    return userData.type === "pupil" || userData.type === "teacher";
}



export function isAdministrator(userData){
    return userData.type === "administrator";
}
