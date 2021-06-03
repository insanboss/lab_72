const BASE_URL = 'http://localhost:8002'
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

let url = BASE_URL+'/api_v2/quotes/'
let button = document.getElementsByName('quotes')
let button_add = document.getElementById('add')
let button_send = document.getElementById('send')
let quotes = document.getElementById('quote')
let form = document.getElementById('form')
async function makeRequest(url, method='GET', body) {
    let headers={
        'X-CSRFToken': getCookie('csrftoken'),
        'Content-Type': 'application/json'
    }
    let response;
    if(method === 'GET'){
        response = await fetch(url, {method})
    }
    else{
        response = await fetch(url, {method, headers:headers, body:body});
    }

    if (response.ok) {  // нормальный ответ
        return await response.json();
    } else {            // ошибка
        let error = new Error(response.statusText);
        error.response = response;
        throw error;
    }
}
button[0].onclick = async () =>{
    form.style.display='none'
    quotes.innerHTML = ""
    let res = await makeRequest(url)
    console.log(res)

    for(let i of res){
        console.log(i)
        let info_id = document.createElement('p')
        info_id.innerText = `Цитата номер: ${i.id}`
        quotes.appendChild(info_id)
        let info_text = document.createElement('p')
        info_text.innerText = `Текст цитаты: ${i.text}`
        quotes.appendChild(info_text)
        let info_date = document.createElement('p')
        info_date.innerText = `Дата : ${i.created_at}`
        quotes.appendChild(info_date)
        let info_rating = document.createElement('p')
        info_rating.innerText = ` Рейтинг: ${i.rating}`
        quotes.appendChild(info_rating)
        let info_space = document.createElement('p')
        info_space.innerText = `------------`
        quotes.appendChild(info_space)
    }

}

let add = (event) => {
    event.preventDefault()
    quotes.innerHTML = ""

    form.style.display='block'
}
button_add.onclick=add

button_send.onclick =async (event)=>{
    event.preventDefault()
    let data = {
        text: document.getElementById('text').value,
        name: document.getElementById('author').value,
        email: document.getElementById('email').value
    }

    try{
        let res = await makeRequest(url,"POST", JSON.stringify(data))
        console.log(res);
    }
    catch (error){
        console.log(error);
    }
}
