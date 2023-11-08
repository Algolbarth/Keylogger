<script>
    import Menu from "./Menu.svelte";
    export let System;
    System;

    const barWidth = 50;
	const height = 500;
    const max = System.keys[0].inputs;
</script>

<svelte:component this={Menu} {System} />
<br/>
<div id="container">
    <svg style="width:{20 + barWidth * System.keys.length}px;height:{10 + height}px;">
        {#each System.keys as point, i}
            <rect
                width="{barWidth}" 
                height={point.inputs*(400/max)} 
                x="{10 + i * barWidth}" 
                y="{10 + height - 100 - point.inputs*(400/max)}"
                fill="rgb(30,144,255)"
                stroke="#000"
            />
            <text
                x="{10 + i * barWidth}"
                y="460"
                fill="black"
            >{point.name}</text>
            <text
                x="{10 + i * barWidth}"
                y="480"
                fill="black"
            >{point.inputs}</text>
        {/each}
    </svg>
</div>

<style>
    #container {
        overflow:auto;
    }

    svg {
        white-space: nowrap;
    }
</style>