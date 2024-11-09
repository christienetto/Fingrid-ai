<script lang="ts">

    import { tweened } from "svelte/motion";
    import { onMount } from "svelte";
    import CommunityTile from "$lib/CommunityTile.svelte";
  //comments
  
  </script>
  
  <section class="bg-red-600 w-screen h-full pt-24">
  <div class="bg-zinc-300 rounded-xl mx-24 h-auto py-8 ">
    <div class="">
      <div class="">
      
        
      </div>
      <CommunityTile title="Commmunity Post" author="Elecriticty XYZ" tag="Project Idea" 
      date="09.11.2024" description="fsjadfha fjakdsfha sdjfafdhas ufsdkjfkhg asuf hae dfhsui fhsdhdafue fuesi hfdsjfh d
      shfshfsdjkfs hdsj fhsuifgds ff djkjdgf sigfsiua fueh vauf hsi gh codsgau fhaud fhsdu vvbsiugaw yf vbcxzg ksddfg ivu sifgsi 
       sahfus hfhsk f eio vnksdfjg awofhs ds dfj " image="grid.png" upvotes={20} downvotes={3} comments={4}/>
      
       <CommunityTile title="Commmunity Post" author="Elecriticty XYZ" tag="Project Idea" 
       date="09.11.2024" description="fsjadfha fjakdsfha sdjfafdhas ufsdkjfkhg asuf hae dfhsui fhsdhdafue fuesi hfdsjfh d
       shfshfsdjkfs hdsj fhsuifgds ff djkjdgf sigfsiua fueh vauf hsi gh codsgau fhaud fhsdu vvbsiugaw yf vbcxzg ksddfg ivu sifgsi 
        sahfus hfhsk f eio vnksdfjg awofhs ds dfj " image="grid.png" upvotes={20} downvotes={3} comments={4}/>
    </div>
  </div>
</section>
