<script>
    import Menu from "./Menu.svelte";
    export let System;
    System;
</script>

<svelte:component this={Menu} {System} />
<br/>
{#each System.inputs as input, index}
    <div class="container" on:click={() => {System.seeKeyFromData(input)}} on:keypress={()=> {}}>
        {#if index != 0}
            <div class="row-border"></div>
        {/if}
        <div>
            {input.name}
        </div>
        <div>
            {input.hour}h {input.minute}m {input.second}s {input.micro}ms
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