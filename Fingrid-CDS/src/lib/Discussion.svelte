<script lang="ts">
    import Comment from '$lib/Comment.svelte';  // Import the Comment component
  
    let comments = [
      {
        id: 1,
        author: 'John Doe',
        text: 'This is a comment',
        parentId: null,
        children: []
      },
      {
        id: 2,
        author: 'Jane Smith',
        text: 'This is a reply to John',
        parentId: 1,
        children: []
      }
    ];
  
    // Function to handle adding a comment
    function addComment(parentId: number | null) {
      // Add logic to add comment or reply
      console.log('Adding a reply to comment with ID:', parentId);
    }
  </script>
  
  <div class="discussion">
    {#each comments as comment}
      <Comment {comment} {addComment} />
    {/each}
  </div>
  