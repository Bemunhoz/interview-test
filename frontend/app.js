const { createApp } = Vue;

createApp({
    data() {
        return {
            query: "",
            operadoras: []
        };
    },
    methods: {
        async buscarOperadoras() {
            if (this.query.length === 0) return;

            const response = await fetch(`http://127.0.0.1:8000/buscar?nomeFantasia=${this.query}`);
            this.operadoras = await response.json();
        }
    }
}).mount("#app");