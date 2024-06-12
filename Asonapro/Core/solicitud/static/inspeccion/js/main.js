import { data } from "./venezuela.js";

const state = document.querySelector("#Estados");
const municipio = document.querySelector("#Municipios");
const parroquia = document.querySelector("#Parroquias");



data.forEach((element) => {
  state.innerHTML += `<option value="${element.estado}">${element.estado}</option>`;
  parroquia.innerHTML += `<option value="${element.parroquia}">${element.parroquia}</option>`;
  municipio.innerHTML += `<option value="${element.municipio}">${element.municipio}</option>`;
});

state.addEventListener("change", () => {
  parroquia.innerHTML = "";
  municipio.innerHTML = "";
  data.forEach((element) => {
    if (element.estado === state.value) {
      console.log(element.estado);
      element.municipios.forEach((element) => {
        municipio.innerHTML += `<option value="${element.municipio}">${element.municipio}</option>`;
      });
    }
  });
});

municipio.addEventListener("change", () => {
  parroquia.innerHTML = "";
  console.log("not work");
  data.forEach((element) => {
    element.municipios.forEach((element) => {
      if (element.municipio === municipio.value) {
        element.parroquias.forEach((element) => {
          parroquia.innerHTML += `<option value="${element}">${element}</option>`;
        });
        console.log(element);
        console.log(element.municipio);
      }
    });
  });
});



// let statesw = {
//   "Amazonas": "Amazonas",
//   "Anzoátegui": "Anzoátegui",
//   "Apure": "Apure",
//   "Aragua": "Aragua",
//   "Barinas": "Barinas",
//   "Bolívar": "Bolívar",
//   "Carabobo": "Carabobo",
//   "Cojedes": "Cojedes",
//   "Delta Amacuro": "Delta Amacuro",
//   "Falcón": "Falcón",
//   "Guárico": "Guárico",
//   "Lara": "Lara",
//   "Mérida": "Mérida",
//   "Miranda": "Miranda",
//   "Monagas": "Monagas",
//   "Nueva Esparta": "Nueva Esparta",
//   "Portuguesa": "Portuguesa",
//   "Sucre": "Sucre",
//   "Táchira": "Táchira",
//   "Trujillo": "Trujillo",
//   "Vargas": "Vargas",
//   "Yaracuy": "Yaracuy",
//   "Zulia": "Zulia",
//   "Distrito Capital": "Distrito Capital"
// }