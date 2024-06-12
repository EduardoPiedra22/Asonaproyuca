// agregue el patron aca que desea validar o verificar
const regex = {
  numeric: /^\d{1,8}$/,
  email: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-ZÀ-ÿ\s]+$/,
  alphabetic: /^[a-zA-ZÀ-ÿ\s]{1,40}$/,
  direccion: /^[a-zA-Z0-9_.+-]/,
  telefono: /^\d{7,14}$/, // 7 a 14 numeros.
  codigo: /^\d{1,8}$/,
};

// se agregan los estilos para alertar del error con su respectivo mensaje
const addInvalidStyle = (input, message) => {
  input.classList.add("is-invalid");
  let parentInput = input.parentNode;

  if (parentInput.childNodes[3] == undefined) {
    let paragraph = document.createElement("p");
    let strong = document.createElement("strong");
    strong.appendChild(document.createTextNode(message));
    paragraph.appendChild(strong);
    paragraph.classList.add("invalid-feedback");
    paragraph.id = "message";
    parentInput.appendChild(paragraph);
  }
};


// se eliminan los estilos del error en caso 
// de que la verificacion sea exitosa
const removeInvalidStyle = (input) => {
  input.classList.remove("is-invalid");
};


// especificar el aca el tipo de mensajes
// que desea mostrar segun el tipo
const messages = {
  numeric: "La cedula tiene que ser de 7 a 8 dígitos!.",
  email: "El correo solo puede contener letras, numeros, puntos, guiones y guion bajo!.",
  alphabetic: "Solo puede contener letras y espacios!.",
  telefono: "El telefono solo puede contener numeros y el maximo son 14 dígitos!.",
  direccion: "Esto permite dígitos para el número de la casa, un espacio, un carácter seguido de un punto ,palabras para el nombre de la calle, terminado con una abreviatura.",
  codigo:"Maximo de numeros valido 9 dígitos!."
};


// se se crea una comprobacion en base a un ternario
// en caso de que exista el error se agregaran los estilos
// y se enviara el mensaje a mostrar
const validations = {
  numericField: function () {
    regex["numeric"].test(this.value)
    ? removeInvalidStyle(this)
    : addInvalidStyle(this, messages["numeric"]);
  },
  alphabeticField: function () {
    regex["alphabetic"].test(this.value)
    ? removeInvalidStyle(this)
    : addInvalidStyle(this, messages["alphabetic"]);
  },
  emailField: function () {
    regex["email"].test(this.value)
    ? removeInvalidStyle(this)
    : addInvalidStyle(this, messages["email"]);
  },
  telefonoField: function () {
    regex["telefono"].test(this.value)
    ? removeInvalidStyle(this)
    : addInvalidStyle(this, messages["telefono"]);
  },
  direccionField: function () {
    regex["direccion"].test(this.value)
    ? removeInvalidStyle(this)
    : addInvalidStyle(this, messages["direccion"]);
  },
  codigoField: function () {
    regex["codigo"].test(this.value)
    ? removeInvalidStyle(this)
    : addInvalidStyle(this, messages["codigo"])
  }
};

/*
   Objeto ids el cual le asigna una validacion al input que
   le pertenesca el id esta validacion "validations" viene del objeto 
   validations de arriba al cual hay que pasarle el tipo de campo que
   queremos validar

   NOTA: agregar los id de tu formulario aqui con el tipo de campo 
   a validar

   EJEMPLO:    id_nombre : validations["alphabeticField"]

   NOTA FINAL: los id deben ser los mismos a los ids de cada uno de los 
   input del formulario y el tipo de validacion a asignar debe ser 
   correspondiente al tipo de dato que se espera
   */
   const ids = {
    id_cedula: validations["numericField"],
    id_nombre: validations["alphabeticField"],
    id_apellido: validations["alphabeticField"],
    id_correo_electronico: validations["emailField"],
    id_telefono: validations["telefonoField"],
    id_direccion: validations["direccionField"],
    id_codigo : validations["codigoField"]
    };

// selecciona el formulario
const formulario = document.querySelector("#formulario");

// selecciona cada uno de los inputs del formulario con el id form
const inputs = document.querySelectorAll("#formulario input");
// for (let index = 1; index < formx.length; index++) {
//   if (ids[formx[index].id]) {
//     let id = formx[index].id
//     formx[index].addEventListener("keyup", ids[id]);
//     formx[index].addEventListener("blur", ids[id]);
//   }
// }

/*
   Asignacion de eventos a cada uno de los inputs del formulario
   siempre y cuando el id del input este registrado en el objeto 
   ids de arriba
   */
   inputs.forEach((input) => {
    let id = input.id;
    input.addEventListener("keyup", ids[id]);
    input.addEventListener("blur", ids[id]);
  });

