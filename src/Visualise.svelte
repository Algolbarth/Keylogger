<script>
    import Menu from "./Menu.svelte";
    export let System;
    System;
</script>

<svelte:component this={Menu} {System} />
{#each System.keys as key, index}
    <div class="container" on:click={() => {System.seeKey(key)}}  on:keypress={()=> {}}>
        {#if index != 0}
            <div class="row-border"></div>
        {/if}
        <div>
            {key.name}
        </div>
        <div>
            {key.inputs}
        </div>
    </div>
{/each}
<br/>

<style>
    .container {
        display:grid;
        grid-template-columns: 0.1fr 1fr;
    }

    .container:hover {
        background:rgb(30,144,255);
        cursor:pointer;
    }

    .row-border {
        border-top: 2px solid rgb(177, 223, 255);
        grid-column: 1 / 3;
    }
</style>