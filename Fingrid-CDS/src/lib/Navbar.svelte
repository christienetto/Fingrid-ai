<script>
    import SideBar from "../routes/index/SideBar.svelte";
    import { Menu } from 'lucide-svelte';
    let open = false; // Start with `open` as false

    const toggleMenu = () => {
        open = !open; // Toggle the value of `open`
    };
</script>

<SideBar bind:open/>

<nav class="z-50 fixed w-screen bg-white border-t-4 border-b-4 border-zinc-500 text-white font-inter">
    <div class="max-w-screen-2xl flex justify-between items-center sm:px-16 px-4 mx-24">
        <!-- Left side: Menu Button and Links -->
        <div class="flex items-center gap-x-6 sm:flex  w-80">
            <button on:click={toggleMenu} class="brightness-0"><Menu/></button>
            <a href="/" class="hover:brightness-75 h-full  py-3  text-black">Official Posts</a>
            <a href="/community-posts" class="hover:brightness-75 py-3 text-black">Community Tickets</a>
        </div>

        <!-- Centered Logo -->
        <div class="flex flex-grow justify-center w-1/3"> 
            <a href="/"><img src="Fingrid_logo.svg" alt="Fingrid Logo"></a>
        </div>

        <!-- Right side: Login Button -->
        <div class="flex items-center font-bold w-80 sm:px-11 xl:text-base sm:text-sm  justify-end ">
            <a href="https://kit.svelte.dev" class="hidden sm:flex items-center text-black  py-3 gap-x-3 hover:brightness-200">Log In</a>
        </div>
    </div>
</nav>
