<script lang="ts">

    import { tweened } from "svelte/motion";
    import { onMount } from "svelte";
    import OfficialTile from "$lib/OfficialTile.svelte";
  //comments
  
  </script>
  
  <section class="bg-red-600 w-screen h-full pt-24">
  <div class="bg-zinc-300 rounded-xl mx-24 h-auto py-8 ">
    <div class="mx-8">
      <div class="">
      
        
      </div>
      <OfficialTile title="Fingrid’s New Battery Storage Project in Eastern Finland" author="FINGRID" tag="Development Stage" 
      date="10.06.2025" description="In response to Finland’s increasing renewable energy generation, particularly from wind and solar, Fingrid is developing a 50 MW battery storage facility near Kuopio. This facility will act as a “grid balancer,” storing excess energy generated during periods of high renewable output and releasing it during peak demand. By enabling the storage and release of renewable energy, this project will reduce reliance on fossil-fuel backup and improve energy reliability for the region. " image="grid.png" upvotes={22} downvotes={1} comments={2}/>
      
      <OfficialTile title="Hydrogen Economy Project" author="FINGRID" tag="Idea Stage" 
      date="10.03.2025" description="Fingrid is actively researching the potential for hydrogen to complement the electricity grid. This project is exploring how hydrogen infrastructure could be integrated with existing transmission systems, offering a versatile energy storage solution and supporting Finland’s carbon-neutrality goals. " image="hydrogen-as-fuel.jpg" upvotes={38} downvotes={6} comments={4}/>
      
    </div>
  </div>
</section>
