<script lang="ts">
    import OfficialTile from "$lib/OfficialTile.svelte";
    import { onMount } from "svelte";
    import { ArrowRight } from 'lucide-svelte';
    import { Minus } from 'lucide-svelte';
    import Comment from '$lib/Comment.svelte'; // Import the Comment component
    import ChatComponent from '$lib/ChatComponent.svelte';
  
    let scrollContainer: HTMLDivElement | null = null;
  
    // Define the unique comments for each tile
    const allComments = [
      { id: 1, author: 'Daniel Chris', text: 'I am concerned about the service life of such a battery. What materials are you considering for the development of such a system?', parentId: null, children: [] },
      { id: 2, author: 'Jane Smith', text: 'This is a reply to John on Tile 1', parentId: 1, children: [] },
      { id: 3, author: 'Mark Taylor', text: "Is there any more information about the parameters of the battery available?", parentId: null, children: [] },
      { id: 4, author: 'Alice Brown', text: 'This is a reply to Mark on Tile 2', parentId: 3, children: [] },
      { id: 5, author: 'Paul Green', text: 'Is there any possibility of the project moving ahead of the schedule?', parentId: null, children: [] },
      { id: 6, author: 'Emma White', text: 'How will the resources used affect the environment in the Kuopio area?', parentId: 5, children: [] }
    ];
  
    // Store the comments for the active tile
    let activeComments = [];
    // Store the current tile's production tag
    let activeTileTag = '';
  
    // Store the tiles array with unique dates
    const tiles = [
      { title: "Fingrid’s New Battery Storage Project in Eastern Finland", tag: "Idea Stage", date: "09.11.2024", upvotes: 20, downvotes: 3, comments: 4, description: "Fingrid identified the issue of grid instability due to intermittent renewable energy sources, which can lead to supply fluctuations, especially in rural and remote regions like Eastern Finland. Battery storage was evaluated as a potential solution to store excess renewable energy and release it during peak demand periods, effectively acting as a “buffer” for the grid." },
      { title: "Fingrid’s New Battery Storage Project in Eastern Finland", tag: "Planning Stage", date: "15.01.2025", upvotes: 15, downvotes: 2, comments: 10, description: "Kuopio was chosen as the project site due to its proximity to renewable energy sources and its need for improved grid stability. Engineers and energy experts developed specifications for a 50 MW battery storage system, selecting technology that would provide optimal capacity, reliability, and lifespan." },
      { title: "Fingrid’s New Battery Storage Project in Eastern Finland", tag: "Development Stage", date: "10.06.2025", upvotes: 22, downvotes: 1, comments: 2, description: "Groundbreaking occurs, and the project site in Kuopio is prepared. This includes building the foundational structures, installing battery containers, and setting up necessary equipment and safety systems. Battery modules and related equipment are installed according to the design specifications. Electrical connections, cooling systems, and monitoring sensors are put in place to ensure safe and efficient operation." }
    ];
  
    // This will keep track of which tile is currently visible
    let activeTileIndex = 0;
  
    // Function to handle adding a comment
    function addComment(parentId: number | null) {
      console.log('Adding a reply to comment with ID:', parentId);
    }
  
    // Handle horizontal scrolling
    function handleWheel(event: WheelEvent) {
      if (scrollContainer) {
        scrollContainer.scrollLeft += event.deltaY; // Scroll horizontally by the delta of the wheel event
        event.preventDefault(); // Prevent default vertical scroll
      }
    }
  
    // Load unique comments based on the active tile index
    function loadCommentsForTile(index: number) {
      const commentsPerTile = 2; // Define how many comments per tile
      const startIndex = index * commentsPerTile;
      const endIndex = startIndex + commentsPerTile;
      activeComments = allComments.slice(startIndex, endIndex); // Update the activeComments to show the correct comments
      activeTileTag = tiles[index].tag; // Update the active tile tag for the header
    }
  
    // Load comments when the tile comes into view
    function loadCommentsBasedOnScroll() {
      if (scrollContainer) {
        const scrollPosition = scrollContainer.scrollLeft;
        const tileWidth = scrollContainer.offsetWidth /1.8; // Width of the scroll container
        const totalWidth = scrollContainer.scrollWidth; // Total width of all tiles combined
        const tileIndex = Math.floor(scrollPosition / tileWidth); // Determine which tile is in view
  
        // Trigger earlier by adjusting the scroll detection threshold
        const earlyThreshold = 0.8;  // Show the next tile's comments when we are 80% of the way to it
  
        // Check if we're at or nearing the next tile
        if (scrollPosition + tileWidth * earlyThreshold >= totalWidth) {
          // If we're nearing the last tile (when we're at 80% of the last tile)
          loadCommentsForTile(tiles.length - 1); // Last tile index
        } else if (tileIndex !== activeTileIndex) {
          // Only update the active tile and comments if the tile index changes
          activeTileIndex = tileIndex;
          loadCommentsForTile(tileIndex); // Load comments for the current tile
        }
      }
    }
  
    // Attach event listener to scroll container on mount
    onMount(() => {
      if (scrollContainer) {
        scrollContainer.addEventListener('wheel', handleWheel);
        scrollContainer.addEventListener('scroll', loadCommentsBasedOnScroll);
      }
      // Initially load comments for the first tile
      loadCommentsForTile(activeTileIndex);
    });
  
    // Cleanup event listeners on unmount
    onMount(() => {
      return () => {
        if (scrollContainer) {
          scrollContainer.removeEventListener('wheel', handleWheel);
          scrollContainer.removeEventListener('scroll', loadCommentsBasedOnScroll);
        }
      };
    });
  </script>
  
  <section class="bg-red-600 w-screen h-full pt-24">
    <div class="bg-zinc-300 rounded-xl mx-24 h-auto py-8">
      <!-- Scrollable container with horizontal overflow and hidden scrollbar -->
      <div
        bind:this={scrollContainer}
        class="flex flex-grow overflow-x-scroll whitespace-nowrap px-8 scrollbar-hide items-center"
      >
        {#each tiles as tile, index}
          <!-- Official Tile -->
          <div class="w-screen">
            <OfficialTile
              title={tile.title}
              author="FINGRID"
              tag={tile.tag}
              date={tile.date} 
              description={tile.description}
              image="grid.png"
              upvotes={tile.upvotes}
              downvotes={tile.downvotes}
              comments={tile.comments}
            />
          </div>
          {#if index < tiles.length - 1}
            <div class="flex px-10">
              <div class="pl-1 scale-x-[900%] scale-y-[300%]"><Minus /></div>
              <div class="scale-x-[900%] scale-y-[300%]"><Minus /></div>
              <div class="scale-[300%] pl-8"><ArrowRight /></div>
            </div>
          {/if}
        {/each}
      </div>
    </div>
    <div class="py-1"></div>
    <!-- Comment Section Below the Scrollable Tiles -->
    <div class="bg-zinc-300 rounded-xl mx-24 h-auto py-8">
        <div class=" bg-white p-4 font-inter mx-8 rounded-xl   ">
        <h2 class="text-2xl font-bold">Comments for {activeTileTag}</h2>
        <div class="comment-section mt-4">
            {#each activeComments as comment (comment.id)}
            <Comment {comment} {addComment} />
            {/each}
        </div>
        </div>
    </div>
    <div class="py-1"></div>
    <div class="bg-zinc-300 rounded-xl mx-24 h-auto py-8">
        <div class=" bg-white p-4 font-inter mx-8 rounded-xl   ">
        <h2 class="text-2xl font-bold">AI Assistant</h2>
        <ChatComponent/>
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
  
    .comment-section {
      padding-top: 20px;
    }
  </style>
