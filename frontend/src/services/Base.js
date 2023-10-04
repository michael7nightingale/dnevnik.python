let baseUrl = 'http://localhost:8008/api/v1/'

export function buildUrl(path){
    return baseUrl.concat(path);
}
