<script>
    export let System;
    System;
</script>

Keylog du {System.date}
<br/><br/>
<button on:click={() => {System.changePage(1)}}>Historique</button> <button on:click={() => {System.changePage(2)}}>Classement</button> <button on:click={() => {System.changePage(4)}}>Graphique</button>