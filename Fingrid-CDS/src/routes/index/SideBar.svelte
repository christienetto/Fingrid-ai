<script>
    import { fly, scale } from "svelte/transition";
    import { quadOut } from "svelte/easing";
    import { Hamburger } from "svelte-hamburgers";
    
    /**
     * @type {any}
     */
    export let open;

    let links = [
  { name: "Strona Główna", url: "https://www.example.com" },
  { name: "Nasze dania", url: "https://www.example.com/nasze-dania" },
  { name: "Jak to działa?", url: "https://www.example.com/jak-to-dziala" },
  { name: "O nas", url: "https://www.example.com/o-nas" },
  { name: "FAQ & pomoc", url: "https://www.example.com/faq-pomoc" }
];

</script>

{#if open}
    <div class="h-screen bg-yellow-300 sm:w-[496px] w-screen fixed z-[60] " transition:fly={{ x: -60 }}>
        <div class="flex  w-full relative">
            <h2 class="text-xl font-medium py-3 mx-8">Menu</h2>
            <div transition:fly={{x:-60}} class="right-0 absolute"><Hamburger bind:open /></div>

        </div>
        <div
            class="flex justify-center items-center my-2  h-2/3"
            
        >
            <div class="  ">
                <h3>Mapa strony</h3>
                <div class="   h-2/3 ">
                    
                    {#each links  as link, i}
                        <div class="flex text-4xl font-semibold group items-center relative tracking-tight ">
                            <div class="pr-2 scale-0 rotate-180 group-hover:scale-75 group-hover:rotate-0 ease-linear duration-200 transition-all absolute "> o </div>
                            <a href={link.url}
                                transition:fly|global={{ x: -60, delay: 150 * (i+1) }}
                                class=" hover:translate-x-8  ease-linear transition-all duration-200  w-full py-3"
                            >
                                {link.name}
                            </a>
                        </div>
                    {/each}
                </div>

                <div class="sm:py-2 py-2 w-full"></div>
                <div transition:fly={{x:-60, delay:900}} class="border-black border-[1px] w-full"></div>

                <div  class=" flex flex-col text-3xl font-semibold items-center sm:py-0 py-3">
                    <div transition:fly={{x:-60, delay:1050}} class="pt-7 pb-10 stroke-black  text-black hover:stroke-gray-100 hover:text-gray-100 transition-all ease-linear duration-75"><a
                        href="https://kit.svelte.dev"
                        class="flex items-center justify-center    gap-x-3 "
                        >Zaloguj się
                    </a></div>

                    <div transition:fly={{x:-60, delay:1200}} class="mx-auto"><a
                        href="https://kit.svelte.dev"
                        class="px-3 w-full bg-white sm:px-16 py-3 rounded-md text-black hover:bg-neutral-200 hover:py-4 hover:text-gray-500 transition-all duration-100 ease-linear"
                    >
                        Zamów</a
                    ></div>
                </div>
            </div>
            
            <div transition:fly={{x:-60, delay:1350}} class="absolute mx-auto bottom-3 ">
           
                <div class="flex justify-center gap-x-4 py-4">
                    <div class="hover:bg-white rounded-full hover:scale-110 transition-all ease-linear duration-100"><a class=" " href="https://facebook.com">FB</a></div>
                    <div class="hover:bg-white  rounded-xl hover:scale-110 transition-all ease-linear duration-100 "><a href="https://instagram.com">INSTA</a></div>
                
                </div>
                
            </div>
        </div>
        
    </div>
{/if}
