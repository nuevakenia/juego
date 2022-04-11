<template>
    <div>
        <p>{{ name }}</p>
        <input ref ="el" type="text" placeholder="Name" v-model="name"/>
        <div>
            <button @click="submitForm" v-bind:disabled="name.length == 0">Submit</button>
        </div>
        <router-link to="/test2">Test 2</router-link>&nbsp;
        <router-link to="/hello">Hello</router-link>
            <div v-for="pj in personajes" :key="pj.id">
        <h3>{{pj.nombre}}</h3>
        <h4>{{pj}}</h4>
    </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
        const personajes = ref([]);
        onMounted(async () => {
            const response = await fetch("http://localhost:8000/api/crear/");
        personajes.value = await response.json()
        });
        
    
        const name = ref('')
        const el = ref()
        const submitForm = () => {
            console.log(`Formulario enviado! Nombre = ${name.value}`)
        }
        console.log(el.value)
        onMounted(() =>{
            el.value.focus()
        })
        


</script>

<style>
input[type='text'] {
    padding: 5px;
}
button {
    margin-top: 20px;
}
</style>