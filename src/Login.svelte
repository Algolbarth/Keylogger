<script>
    export let System;
    System;

    let files;
    let save;
    let step;

    async function login () {
        save = await files[0].text();
        step = 0;
        System.date = readValue();
        while (step < save.length) {
            System.addInput(readValue(), readValue(), readValue(), readValue(), readValue());
        }
        for (const data of System.inputs) {
            System.addKey(data);
        }
        System.sortKey();
        System.changePage(1);
    }

    function readValue() {
        let value = "";
        while (save[step] != "_" && step < save.length) {
            value += save[step];
            step++;
        }
        step++;
        return value;
    }
</script>

<div id="root">
    <div id="title">Keylogger</div>
    <br/><br/>
    <input bind:files type="file" accept=".txt" />
    <br/><br/>
    <button class="validate" on:click={login}>Se connecter</button>
</div>

<style>
    #root {
        text-align:center;
    }
    
    #title {
        color:white;
        font-size:10vw;
    }

    input {
        border:none;
        background:rgb(65,105,225);
    }
</style>