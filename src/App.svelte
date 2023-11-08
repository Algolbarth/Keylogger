<script>
	import Login from "./Login.svelte";
	import Historic from "./Historic.svelte";
	import Visualise from "./Visualise.svelte";
	import Key from "./Key.svelte";
	import Graphic from "./Graphic.svelte";

	export const System = {
		pages : [Login, Historic, Visualise, Key, Graphic],
		page : 0,
		changePage(newPage) {
			System.page = newPage;
		},
		date : "",
		totalInput : 0,
		inputs : [],
		keys : [],
		see : {},
		checkKey (key) {
			for (const k of System.keys) {
				if (k.name == key.name) {
					return k;
				}
			}
			return undefined;
		},
		sortKey () {
			for (let i = 1; i < System.keys.length; i++) {
				let j = i;
				while (j > 0 && System.keys[j].inputs > System.keys[j-1].inputs) {
					let temp = System.keys[j-1];
					System.keys[j-1] = System.keys[j];
					System.keys[j] = temp;
					j--;
				}
			}
		},
		addKey (key) {
			let k = System.checkKey(key);
			if (k == undefined) {
				System.keys.push({
					name : key.name,
					inputs : 1,
				});
			}
			else {
				k.inputs++;
			}
			System.totalInput++;
		},
		seeKey (key) {
			System.see = key;
			System.changePage(3);
		},
		seeKeyFromData (key) {
			System.seeKey(System.checkKey(key));
		},
		addInput (name, hour, minute, second, micro) {
			System.inputs.push({
				name : name,
				hour : hour,
				minute : minute,
				second : second,
				micro : micro,
			});
		},
	}
</script>

<div id="root">
    <svelte:component this={System.pages[System.page]} {System} />
</div>

<style>
	#root {
		background:rgb(135,206,250);
		width:100vw;
		height:100vh;
		position:fixed;
		overflow:scroll;
		padding:1vh;
		top:0;
		left:0;
		font-family:Verdana, Geneva, Tahoma, sans-serif;
	}

    :global(.key) {
        margin:0;
        padding:0;
        border:none;
        background:none;
        font-weight: bold;
    }

	:global(button) {
		color:white;
		background:rgb(65,105,225);
		border:solid;
		border-color:white;
		border-width:2px;
	}

	:global(button:hover) {
		background:rgb(25,25,112);
	}
</style>