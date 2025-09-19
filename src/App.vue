<script setup>
import { ref } from 'vue';
import { db } from './firebase.js';
import { collection, addDoc, getDocs }  from 'firebase/firestore';

const nuevoNombre = ref("")
const nombres = ref([])

async function agregarNombre(){
  if (nuevoNombre.value.trim() !== ""){
    await addDoc(collection(db, "nombres"), {
      nombre : nuevoNombre.value
    })
    nuevoNombre.value = "";
    await cargarNombres();
  }
}

async function cargarNombres(){
  const querySnap = await getDocs(collection(db, "nombres"));
  nombres.value = querySnap.docs.map(doc => doc.data().nombre)
}

cargarNombres()
</script>

<template>
  <img class="osito-img" src="/src/assets/osito.png" alt="osito">
  <h1>Bienvenido a la pagina de mi gordita</h1>
      <input v-model="nuevoNombre" placeholder="Ingresa un nombre..." type="text" id="nombre" name="nombre">
      <button @click="agregarNombre" class="btn-sub">Enviar</button>
  <h2>Nombres</h2>
  <ul>
      <li v-for="nombre in nombres" :key="nombre"> {{ nombre }} <img src="/src/assets/bebe.png" class="icon-img" alt="icon" width="40" height="35"></li>
  </ul>
</template>

<style>
body {
  font-family: "Verdana", sans-serif;
  background: linear-gradient(to bottom, #feb9ac, #feca94);
  text-align: center;
  padding: 10px;
  height: 100vh;
}
.osito-img{
  background: transparent;
  width: 200px;
}

.icon-img{
  margin: 0;
}

h1 {
  font-size: 2.5em;
  color: white;
  text-shadow: 2px 2px #f9987a;
}

input {
  padding: 10px;
  border: none;
  border-radius: 8px;
  width: 220px;
  margin: 5px;
}

input::placeholder{
  font-size: 1.15em;
}

.btn-sub{
  background: linear-gradient(135deg, #FECA94, #FEB9AC);
  border-color: #fff;
  border-radius: 8px;
  padding: 9px 10px;
  color: #fff;
  font-weight: bold;
  cursor: pointer;
}

h2 {
  margin-top: 20px;
  color: #fff;
  text-shadow: 2px 2px #f9987a;
  font-size: 1.7em;
}

ul {
  list-style: none;
  padding: 0;
  margin: 0 auto;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  gap: 1em;
  max-width: 800px;
}

li {
  background: rgba(255, 255, 255, 0.7);
  display: flex;
  align-items: center;
  justify-content: space-evenly;
  margin: 8px;
  padding: 0.5em;
  border-radius: 12px;
  width: 120px;
  font-weight: bold;
  flex: 1 1 calc(45% - 10px);
}

@media (max-width: 480px) {
  body {
    padding: 20px;
  }

  h1 {
    font-size: 1.8em;
  }

  input {
    width: 90%;
    max-width: 250px;
  }

  ul {
    width: 100%;
    padding: 0;
    gap: 0.5em;
  }

  li {
    flex: 1 1 calc(50% - 10px);
  }
}

@media (min-width: 481px) and (max-width: 768px) {
  h1 {
    font-size: 2.2em;
  }

  ul {
    width: 100%;
    max-width: 600px;
    gap: 0.8em;
  }

  li {
    flex: 1 1 calc(33.3% - 10px);
  }
}

@media (min-width: 1024px) {
  ul {
    max-width: 800px;
    gap: 1.2em;
  }

  li {
    flex: 1 1 calc(25% - 10px);
  }

}
</style>
