<script>
<<<<<<< Updated upstream
  import OfficialPosts from "./index/OfficialPosts.svelte";
import CommunityPosts from "./index/OfficialPosts.svelte";
</script>

<OfficialPosts/>
=======
  import CommunityPosts from "./index/CommunityPosts.svelte";
  import ChatComponent from "$lib/ChatComponent.svelte";
</script>

<CommunityPosts />

<div class="chat-container">
  <h2>Chat</h2>
  <ChatComponent />
</div>

<style>
  .chat-container {
    max-width: 800px;
    margin: 2rem auto;
    padding: 0 1rem;
  }
  
  h2 {
    margin-bottom: 1rem;
  }
</style>
>>>>>>> Stashed changes
