<script>
    import SideBar from "../routes/index/SideBar.svelte";
    import { Menu } from 'lucide-svelte';
    let open = false; // Start with `open` as false

    const toggleMenu = () => {
        open = !open; // Toggle the value of `open`
    };
</script>

<SideBar bind:open/>

<nav class="z-50 fixed w-screen bg-white border-t-4 border-b-4 border-zinc-500 text-white py-3">
    <div class="max-w-screen-2xl flex justify-center items-center sm:px-16 px-4 mx-auto">
        <div>
            <span class="sm:flex gap-x-6 items-center  xl:text-base sm:text-sm text-black">
                <button on:click={toggleMenu}><Menu/></button>
                
                <a href="https://kit.svelte.dev" class="hover:brightness-75 hidden sm:block">Nasze Menu</a>
                <a href="https://kit.svelte.dev" class="hover:brightness-75 hidden sm:block">Jak to działa</a>
                
            </span>
        </div>
       <div class="mx-auto"> <a href="/"><img src="Fingrid_logo.svg"></a></div>
        <div class="flex items-center sm:gap-x-6 font-bold sm:px-11 xl:text-base sm:text-sm">
            <div class="stroke-yellow-300">
                <a href="https://kit.svelte.dev" class="hidden sm:flex items-center text-yellow-300 gap-x-3 hover:brightness-200">Zaloguj się</a>
            </div>
            <div>
                <a href="https://kit.svelte.dev" class="px-3 bg-yellow-300 sm:px-5 py-2 rounded-md text-black font-bold hover:bg-yellow-100 hover:py-3 transition-all duration-100 ease-linear">Zamów</a>
            </div>
        </div>
    </div>
</nav>
