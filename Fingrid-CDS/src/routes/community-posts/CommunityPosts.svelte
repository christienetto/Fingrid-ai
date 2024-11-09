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
      <CommunityTile title="Unpredictable Congestion Charges Impacting Budget Stability for Industrial Customers" author="Stora Enso" tag="Complaint" 
      date="09.11.2024" description="Large industrial customers relying on Fingrid's transmission network are facing unexpected spikes in electricity costs due to congestion charges during peak demand periods. The unpredictable nature of these charges creates challenges for budgeting and planning, impacting their competitiveness and operational stability. Customers are calling for more transparency, advance warnings, and guidance on optimizing energy use to reduce exposure to these costs." image="bar-chart-example.svg" upvotes={20} downvotes={3} comments={4}/>
      
       <CommunityTile title="Improving Grid Stability with Real-Time Data Integration for Industrial Clients" author="Siemens" tag="Project Idea" 
       date="09.11.2024" description="Fingrid could introduce a new service aimed at industrial clients, such as large manufacturing plants or energy-intensive companies, that provides real-time data analytics and insights on grid stability. This service would leverage advanced monitoring technologies to deliver live updates on grid conditions, voltage fluctuations, and potential supply interruptions. By integrating this service with their existing systems, clients would gain better visibility into how their operations are affected by the grid. " image="images.jpg" upvotes={31} downvotes={6} comments={8}/>
    </div>
  </div>
</section>
