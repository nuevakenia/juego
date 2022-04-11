<template>
    <div>
        <!-- <p>{{ name }}</p>
        <input ref ="el" type="text" placeholder="Name" v-model="name"/>
        <div>
            <button @click="submitForm" v-bind:disabled="name.length == 0">Submit</button>
        </div>
        --> <router-link to="/test2">Test 2</router-link>&nbsp;
        <router-link to="/hello">Hello</router-link>

    <div v-for="pj in APIData" :key="pj.id">
        <h3>{{pj.nombre}}</h3>
        <h4>{{pj}}</h4>
    </div>

    </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import { getAPI } from '../axios-api.js'
import Test2 from './test2.vue'

        /* const name = ref('')
        const el = ref()
        const submitForm = () => {
            console.log(`Formulario enviado! Nombre = ${name.value}`)
        }
        console.log(el.value)
        onMounted(() =>{
            el.value.focus()
        }) */
export default {
    name:'Test1',
    data () {
        return {
            APIData: []
            }
            },
            components: {
                Test2
                },
            created () {
                getAPI.get('/api/personajes/',).then
                (response => {
                    console.log('Post Api recibido')
                    this.APIData = response.data
                }).catch(err => { console.log(err)})

                }
}

</script>

<style>
input[type='text'] {
    padding: 5px;
}
button {
    margin-top: 20px;
}
</style>