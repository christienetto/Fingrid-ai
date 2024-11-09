<script lang="ts">
    import OfficialTile from "$lib/OfficialTile.svelte";
    import { onMount } from "svelte";
    import { ArrowRight } from 'lucide-svelte';
    import { Minus } from 'lucide-svelte';
    import Comment from '$lib/Comment.svelte'; // Import the Comment component
  
    let scrollContainer: HTMLDivElement | null = null;
  
    // Define the unique comments for each tile
    const allComments = [
      { id: 1, author: 'John Doe', text: 'This is a comment for Tile 1', parentId: null, children: [] },
      { id: 2, author: 'Jane Smith', text: 'This is a reply to John on Tile 1', parentId: 1, children: [] },
      { id: 3, author: 'Mark Taylor', text: 'This is a comment for Tile 2', parentId: null, children: [] },
      { id: 4, author: 'Alice Brown', text: 'This is a reply to Mark on Tile 2', parentId: 3, children: [] },
      { id: 5, author: 'Paul Green', text: 'This is a comment for Tile 3', parentId: null, children: [] },
      { id: 6, author: 'Emma White', text: 'This is a reply to Paul on Tile 3', parentId: 5, children: [] }
    ];
  
    // Store the comments for the active tile
    let activeComments = [];
    // Store the current tile's production tag
    let activeTileTag = '';
  
    // Store the tiles array
    const tiles = [
      { title: "Official Post 1", tag: "Idea Stage", upvotes: 20, downvotes: 3, comments: 4, description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit." },
      { title: "Official Post 2", tag: "Planning Stage", upvotes: 15, downvotes: 2, comments: 10, description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit." },
      { title: "Official Post 3", tag: "Development Stage", upvotes: 15, downvotes: 2, comments: 10, description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit." }
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
        const tileWidth = scrollContainer.offsetWidth / 2; // Width of the scroll container
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
              date="09.11.2024"
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
  