<script>
    import Navbar from "$lib/Navbar.svelte";
    import "../app.css";
    import SideBar from "./index/SideBar.svelte";
    
    
    /**
     * @type {any}
     */
    let open;
  </script>
 
  
<Navbar/>

  <slot />