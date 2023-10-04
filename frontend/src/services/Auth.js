import {meUser} from "@/services/UserService";

export function setUser(token){
    localStorage.user = token;
    meUser().then(response => {
        localStorage.userData = JSON.stringify(response.data);
        console.log(123123123123, localStorage.userData)
        console.log(getUser())
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