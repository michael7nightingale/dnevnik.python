export function groupId(objects){
    let groupedObjects = {};
    for (const obj of objects){
        groupedObjects[obj.id] = obj;
    }
    return groupedObjects;
}


export function notFullUserName(userData){
  return `${userData.last_name} ${userData.first_name}`;
}


export function fullUserName(userData){
  return `${userData.last_name} ${userData.first_name} ${userData.father_name}`;
}
