<template>
    <div>
        AAAAAAAAAAAAAAAAAA
        <p>{{ name }}</p>
        <input ref ="el" type="text" placeholder="Name" v-model="name"/>
        <div>
            <button @click="submitForm" v-bind:disabled="name.length == 0">Enviar</button>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

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