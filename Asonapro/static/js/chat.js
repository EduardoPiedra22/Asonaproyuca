const chatbotToggler = document.querySelector(".chatbot-toggler");
const rotateButton = document.getElementById("button-show");
const closeBtn = document.querySelector(".close-btn");
const cancel_update = document.querySelector(".cancel_update");
const usersList = document.querySelector(".users_list");
const chatbox = document.querySelector(".chatbox");
const chatbot = document.querySelector(".chatbot");
const chatInput = document.querySelector(".chat-input textarea");
const container_text = document.querySelector(".chat-input");
const sendMessage = document.querySelector(".send_btn");
const userItems = document.querySelectorAll("li.users");
//Contenedor del chat
const home = document.getElementById("home");
const messageContainer = document.getElementById("message");
//Dropdown
const dropdownContent = document.getElementById("friends-content");
const dropdownButton = document.getElementById("friends-button");

//DELETE & UPDATE
let deleteButtons = '';
let updateButtons = '';


let img_writing = $("#writing").attr("src");
let userMessage = null;
let socket = null;
let sala = "";
let get_message_list = "";
let user_id = "";
let update_message = false;
let position_upd = '';
let id_msg_upd = ''

function scrollToBottom() {
    chatbox.scrollTop = chatbox.scrollHeight;
}
const cancelUpdate = () =>{
    container_text.classList.remove('update_text')
    cancel_update.classList.add('d-none')
    sendMessage.querySelector('i').classList.remove('fa-check');
    sendMessage.querySelector('i').classList.add('fa-paper-plane');
    chatInput.value = '';
    chatInput.style.height = "55px"
    update_message = false;
}
chatbox.addEventListener('click', function(event) {
    //ELIMINAR
  if (event.target.classList.contains('dlt')) {
    let deleteButton = event.target;

    let position = Array.from(deleteButton.closest('li').parentNode.children).indexOf(deleteButton.closest('li'));

    let id_msg = deleteButton.closest('li').querySelector('input[type="radio"]').value;

    alert_action('Notificación', '¿Estas seguro de eliminar el mensaje?', function () {
        deleteMessage(id_msg, position)}, function () {
    });
    //MODIFICAR
  }else if (event.target.classList.contains('upd')){        
        container_text.classList.add('update_text')
        cancel_update.classList.remove('d-none')
        sendMessage.querySelector('i').classList.remove('fa-paper-plane');
        sendMessage.querySelector('i').classList.add('fa-check');
        update_message = true;
        let updateButtons = event.target;

        position_upd = Array.from(updateButtons.closest('li').parentNode.children).indexOf(updateButtons.closest('li'));

        id_msg_upd = updateButtons.closest('li').querySelector('input[type="radio"]').value;

        let pNode = updateButtons.closest('li').querySelector('p');
        let text = pNode.childNodes[0].data;
        chatInput.value = text;
    }
  
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != "") {
        var cookies = document.cookie.split(";");

        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
//ENVIAR DATOS AL BACKEND PARA CREAR MENSAJES
const handleChat = () => {
    userMessage = chatInput.value.trim();
    if (userMessage === "" || userMessage === null) {
        return false;
    }
    socket.send(
        JSON.stringify({
            type: "message",
            message: chatInput.value,
            message_id: "",
            message_position: "",
            sala: sala.sala_id,
            writing: "",
        })
    );
    chatInput.value = "";
};
//ENVIAR DATOS AL BACKEND PARA MODIFICAR MENSAJES
const updateMessage = () => {
    userMessage = chatInput.value.trim();
    if (userMessage === "" || userMessage === null) {
        return false;
    }
    socket.send(
        JSON.stringify({
            type: "update_message",
            message: chatInput.value,
            message_id: id_msg_upd,
            message_position: position_upd,
            sala: "",
            writing: "",
        })
    );
    chatInput.value = "";
};
//ENVIAR DATOS AL BACKEND PARA ELIMINAR MENSAJES
const deleteMessage = (id, position) => {
    socket.send(
        JSON.stringify({
            type: "delete_message",
            message: "",
            message_id: id,
            message_position: position,
            sala: "",
            writing: "",
        })
    );
}
//AGREGAR MENSAJE AL DOM
const onChatMessage = (data) => {
    const chatLi = document.createElement("li");
    let className = "";
    let spanClass = "";

    user_id != data.id ? ((className = "outgoing"), (spanClass = "pos_right")) : ((className = "incoming"), (spanClass = "pos_left"));

    chatLi.classList.add("chat", `${className}`);

    let src = $("#src_img").attr("src");

    if (data.type === "chat_message") {
        let message_writing = document.querySelector(".message_writing");
        if (message_writing) {
            message_writing.remove();
        }
        let chatContent = user_id != data.id ? `<div class="container_p d-flex"><p></p><button class="btn_msg update_msg upd"><i class="fas fa-pen upd"></i></button><button class="btn_msg delete_msg dlt"><i class="fas fa-trash dlt"></i></button></div><input type="radio" class="d-none" name="msg_id" value="${data.message_id}">` : `<img src="${src}" class="img-profile" style="height: 36px; width: 36px;" alt="" /><p></p>`;
        chatLi.innerHTML = chatContent;
        chatLi.querySelector("p").textContent = data.message;

        const timeSince = document.createElement("div");
        timeSince.innerHTML = `<span class="timesince"> ${data.created_at}</span>`;
        timeSince.classList.add("d-flex", `${spanClass}`);
        chatbox.appendChild(chatLi);
        chatbox.appendChild(timeSince);
    } else if (data.type === "writing_active") {
        let container_writing = document.querySelector(".writing");
        if (container_writing) {
            container_writing.remove();
        }
        const div_writing = document.createElement("div");
        div_writing.classList.add("writing");

        let message_writing = document.querySelectorAll(".message_writing");
        if (user_id == data.id && data.writing.length > 1) {
            let elemento = `<li class="message_writing chat incoming"><img src="${src}" class="img-circle" id="writing" style="height: 36px; width: 36px;" alt="" /><p>Escribiendo...</p></li>`;
            div_writing.innerHTML = elemento;
            chatbox.appendChild(div_writing);
        } else if (user_id == data.id && data.writing.length < 2) {
            message_writing.forEach(function (li) {
                li.remove();
            });
        }
    } 
    else if (data.type === 'updated_msg'){
        let message_writing = document.querySelector(".writing");
        if (message_writing) {
            message_writing.remove();
        }

        const listItem = document.querySelector('ul.chatbox li:nth-child(' + (data.message_position + 1) + ')');

        chatbox.classList.add('updated')

        let updated = '';
        if (user_id != data.id) {
            updated = `<div class="container_p d-flex">
            <p class="msg_upd">${data.message} <span class="status_emit" disabled>editado</span></p>
                <button class="btn_msg update_msg upd"><i class="fas fa-pen upd"></i></button>
                <button class="btn_msg delete_msg dlt"><i class="fas fa-trash dlt"></i></button>
            </div>
            <input type="radio" class="d-none" name="msg_id" value="${data.message_id}">
            `
        } else {
            updated = `<img src="${src}" class="img-profile" style="height: 36px; width: 36px;" alt="" /><p class="msg_upd">${data.message} <span class="status_receive">editado</span></p>`
        }
        listItem.innerHTML = updated;
    } 
    else if (data.type === 'delete_msg'){
        const listItem = document.querySelector('ul.chatbox li:nth-child(' + (data.message_position + 1) + ')');
        listItem.classList.add('msg_deleted')
        listItem.querySelector("p").textContent = 'Eliminado'
    }
};
//PARA CAPTURAR EL ID DEL USUARIO QUE SE HA SELECCIONADO
async function activateRadio(id) {
    const data = new FormData();
    data.append("id", id);
    data.append("action", "create_private_room");   

    await fetch("/chat/chat/sala/", {
        method: "POST",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
        },
        body: data,
    })
        .then(function (res) {
            return res.json();
        })
        .then(function (data) {
            sala = data;
            console.log('LONGITUD: ', sala.message_list.length)
            if (sala.message_list.length == 0) {               
                return false
            } else {
                sala.message_list.map((message) => {                    
                    if (message.first_user != message.second_user) {
                        get_message_list += `
                        <li class="chat incoming">
                            <img src="${message.image}" class="img-profile" style="height: 36px; width: 36px;" alt="" />
                            <p>${message.body}</p>
                        </li>
                        <div class="d-flex pos_left">
                            <span class="timesince"> ${message.date_joined}</span>
                        </div>`;
                    } else {
                        get_message_list += `
                        <li class="chat outgoing">
                            <div class="container_p d-flex" >
                                <p>${message.body}</p>
                                <button class="btn_msg update_msg upd"><i class="fas fa-pen upd"></i></button>
                                <button class="btn_msg delete_msg dlt" data-id="${message.message_id}"><i class="fas fa-trash dlt"></i></button>
                            </div>
                            <input type="radio" class="d-none" name="msg_id" value="${message.message_id}">
                        </li>
                        <div class="d-flex pos_right">
                            <span class="timesince"> ${message.date_joined}</span>
                        </div>`;
                    }
                    $('#message_list').html(get_message_list);
                });
            }
        });

    //CONEXION CON WEBSOCKET
    socket = new WebSocket(`ws://${window.location.host}/ws/${sala.sala_id}/`);
    socket.onmessage = function (e) {
        console.log("onMessage");
        onChatMessage(JSON.parse(e.data));
    };
    socket.onopen = function (e) {
        console.log("CONNECTION ESTABLISHED");
    };
    socket.onclose = function (e) {
        console.log("CONNECTION LOST");
    };
    socket.onerror = function (e) {
        console.log(e);
    };
}
//DESPLEGAR EL CHAT
chatbotToggler.addEventListener("click", () => {
    chatbot.classList.toggle("show-chatbot");
});
//VOLVER AL LISTADO DE USUARIOS
usersList.addEventListener("click", () => {
    get_message_list = "";
    chatbox.innerHTML = '<div class="writing"></div>';
    document.querySelector("#full_name").textContent = "Chat";
    home.style.display = "flex";
    messageContainer.style.display = "none";
    socket.close();
});
//CERRAR EL CHAT
closeBtn.addEventListener("click", () => {
    chatbot.classList.remove("show-chatbot");
    rotateButton.classList.remove("rotate-button");
});

//CAMBIAR IMAGEN Y NOMBRE DE USUARIO EN EL HEADER CUANDO SE SELECCIONE UN USUARIO DE LA LISTA
userItems.forEach((item) => {
    item.addEventListener("click", () => {
        const imgSrc = item.querySelector("#img_user").getAttribute("src");
        document.querySelector("#src_img").setAttribute("src", imgSrc);
        const username = item.querySelector("#username").textContent;
        document.querySelector("#full_name").textContent = username;
        home.style.display = "none";
        messageContainer.style.display = "block";

    });
});

const inputInitHeight = chatInput.scrollHeight;

chatInput.addEventListener("input", () => {
    chatInput.style.height = `${inputInitHeight}px`;
    chatInput.style.height = `${chatInput.scrollHeight}px`;
});

chatInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey && window.innerWidth > 800) {
        e.preventDefault();
        handleChat();
        chatInput.style.height = "55px";
    } else if (chatInput.value != "") {
        socket.send(
            JSON.stringify({
                type: "writing",
                message: "Escribiendo...",
                message_id: "",
                message_position: "",
                sala: sala.sala_id,
                writing: chatInput.value,
            })
        );
    }
});
sendMessage.addEventListener('click', () =>{
    if (update_message === false){
        console.log('CREAR')
        handleChat();
    }else{
        console.log('MODIFICAR')
        updateMessage();
        cancelUpdate();
    }
})
cancel_update.addEventListener('click', () =>{
    cancelUpdate();
})
