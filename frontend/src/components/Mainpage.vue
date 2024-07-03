<template>
    <v-container class="fill-height align-start" justify="center" fluid>
        <v-col>

            <v-row justify="center">
                <p class="text-h4">Services</p>
            </v-row>
            <v-row>
                <v-list>
                    <v-list-item style="width: 100vW;" v-for="service in services">
                        <v-list-item-title>
                            <div class="text-h6">
                                {{ service.name }}
                            </div>
                            <div class="text-caption">
                                {{ service.status }} ...
                            </div>
                        </v-list-item-title>

                        <v-row>
                            <v-spacer></v-spacer>
                            <v-btn color="" icon="mdi-stop" @click="stop(service.id)"></v-btn>
                            <v-btn color="" icon="mdi-refresh" @click="restart(service.id)"></v-btn>
                            <v-btn color="" icon="mdi-play" @click="start(service.id)"></v-btn>
                        </v-row>
                    </v-list-item>
                </v-list>
            </v-row>
        </v-col>
    </v-container>
    <v-snackbar v-model="snackbar">
        Server Error
        <template v-slot:actions>
            <v-btn color="pink" variant="text" @click="snackbar = false">
                Close
            </v-btn>
        </template>
    </v-snackbar>
</template>

<script>
import { get } from '@/axios'

export default {
    name: 'Mainpage',
    // Your component logic goes here
    data() {
        return {
            services: [],
            snackbar: false,
        }
    },
    methods: {
        async stop(id) {
            try {
                await get("/stop?id=" + id)
            }
            catch (e) {
                this.snackbar = true;
            }
            this.getServices();
        },
        async restart(id) {
            try {
                await get("/restart?id=" + id)
            }
            catch (e) {
                this.snackbar = true;
            }
            this.getServices();

        },
        async start(id) {
            try {
                await get("/start?id=" + id)
            }
            catch (e) {
                this.snackbar = true;
            }

            this.getServices();
        },
        async getServices() {
            try {
                this.services = await get('/services')
            }
            catch (e) {
                this.snackbar = true;
            }
        }
    },
    mounted() {
        this.getServices();
    }
}
</script>

<style scoped>
/* Your component styles go here */
</style>