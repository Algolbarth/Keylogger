<script>
    import Menu from "./Menu.svelte";
    export let System;
    System;

    let array = [];
    for (const input of System.inputs) {
        if (input.name == System.see.name) {
            array.push(input);
        }
    }
</script>

<svelte:component this={Menu} {System} />
<br/>
{System.see.name} : {System.see.inputs} appuies
<br/><br/>
{#each array as input, index}
    {#if index != 0}
        <div class="row-border"></div>
    {/if}
    <div class="container">
        {input.hour}h {input.minute}m {input.second}s {input.micro}ms
    </div>
{/each}
<br/>

<style>
    .container {
        display:grid;
        grid-template-columns: 1fr;
    }

    .container:hover {
        background:rgb(30,144,255);
    }

    .row-border {
        border-top: 2px solid rgb(177, 223, 255);
        grid-column: 1 / 3;
    }
</style>