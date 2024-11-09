<script lang="ts">
  import OfficialTile from "$lib/OfficialTile.svelte";
  import { onMount } from "svelte";
  import { ArrowRight } from 'lucide-svelte';
  import { Minus } from 'lucide-svelte';

  let scrollContainer: HTMLDivElement | null = null;

  // Horizontal scrolling with the scroll wheel
  function handleWheel(event: WheelEvent) {
    if (scrollContainer) {
      scrollContainer.scrollLeft += event.deltaY; // Scroll horizontally by the delta of the wheel event
      event.preventDefault(); // Prevent default vertical scroll
    }
  }

  // Attach wheel event listener on mount
  onMount(() => {
    if (scrollContainer) {
      scrollContainer.addEventListener("wheel", handleWheel);
    }
    return () => {
      if (scrollContainer) {
        scrollContainer.removeEventListener("wheel", handleWheel);
      }
    };
  });
</script>

<section class="bg-red-600 w-screen h-screen pt-24">
  <div class="bg-zinc-300 rounded-xl mx-24 h-auto py-8">
    <!-- Scrollable container with horizontal overflow and hidden scrollbar -->
    <div
      bind:this={scrollContainer}
      class="flex overflow-x-scroll whitespace-nowrap space-x-4 px-4 scrollbar-hide items-center"
    >
    <div class="pr-2">
      <OfficialTile
        title="Official Post 1"
        author="FINGRID"
        tag="Planning Stage"
        date="09.11.2024"
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        image="grid.png"
        upvotes={20}
        downvotes={3}
        comments={4}
        class="w-72 flex-shrink-0"
      />
    </div>
    <div class="flex">
        <div class=" scale-x-[900%] scale-y-[300%]"><Minus/></div>
        <div class="  scale-[300%]"><ArrowRight/></div>
    </div>
      <OfficialTile
        title="Official Post 2"
        author="FINGRID"
        tag="Execution Stage"
        date="09.11.2024"
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        image="grid.png"
        upvotes={15}
        downvotes={2}
        comments={10}
        class="w-72 flex-shrink-0"
      />
      <!-- Add more OfficialTile components as needed -->
    </div>
  </div>
</section>

<style>
  /* Hide scrollbar on the horizontal scrolling container */
  .scrollbar-hide::-webkit-scrollbar {
    display: none;
  }
  .scrollbar-hide {
    -ms-overflow-style: none; /* IE and Edge */
    scrollbar-width: none; /* Firefox */
  }
</style>
