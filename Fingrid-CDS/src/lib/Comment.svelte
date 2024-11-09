<script lang="ts">
    import Comment from '$lib/Comment.svelte'; // Ensure this path is correct
  
    // Define the types for the comment structure
    type CommentType = {
      id: number;
      author: string;
      text: string;
      parentId: number | null;
      children: CommentType[];
    };
  
    export let comment: CommentType; // Explicitly type the `comment` prop
    export let addComment: (parentId: number | null) => void;
  
    let replyText = '';
    let showReplyInput = false; // State to control the visibility of the reply input
    
    function handleReply() {
      if (replyText.trim()) {
        addComment(comment.id); // Pass the parent comment's ID when replying
        replyText = ''; // Clear the reply input after submitting
      }
    }
  
    function toggleReplyInput() {
      showReplyInput = !showReplyInput; // Toggle the visibility of the reply input area
    }
  </script>
  
  <div class="comment mb-4 p-4 border border-gray-300 rounded-lg">
    <div class="comment-header flex justify-between">
      <strong>{comment.author}</strong>
      <span class="comment-date text-sm text-gray-500">Posted recently</span>
    </div>
    <div class="comment-body my-2">
      {comment.text}
    </div>
  
    <div class="comment-actions flex gap-3">
      <button
        class="reply-btn bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 focus:outline-none"
        on:click={toggleReplyInput}
      >
        Reply
      </button>
    </div>
  
    {#if comment.children.length > 0}
      <div class="replies ml-5 mt-4">
        {#each comment.children as child (child.id)}
          <Comment {child} {addComment} />
        {/each}
      </div>
    {/if}
  
    {#if showReplyInput}
      <div class="reply-input mt-4">
        <textarea
          bind:value={replyText}
          placeholder="Write a reply..."
          class="w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        ></textarea>
        <button
          on:click={handleReply}
          class="mt-2 px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600 focus:outline-none"
        >
          Submit Reply
        </button>
      </div>
    {/if}
  </div>
  