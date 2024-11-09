<script lang="ts">
  import DetailedPost from "$lib/DetailedPost.svelte";
  import Discussion from "$lib/Discussion.svelte";

  // Define an array of comments with nested replies as needed
  const comments = [
    {
      id: 1,
      author: 'John Doe',
      text: 'This is a comment',
      parentId: null,
      children: [
        {
          id: 2,
          author: 'Jane Smith',
          text: 'This is a reply to John',
          parentId: 1,
          children: [],
        },
      ],
    },
    {
      id: 3,
      author: 'Alice Johnson',
      text: 'Another top-level comment',
      parentId: null,
      children: [],
    },
  ];
</script>

<section class="bg-red-600 w-screen h-screen pt-24">
  <div class="bg-zinc-300 rounded-xl mx-24 h-auto py-8 ">
    <DetailedPost
      title="Community Post Example Title"
      author="Electricity XYZ"
      tag="Project Idea"
      date="09.11.2024"
      description="Sample description text for this community post. This would contain details about the project idea and further information."
      image="grid.png"
      upvotes={20}
      downvotes={3}
      comments={4}
    />

    <!-- Pass the comments array to the Discussion component -->
    <Discussion {comments} />
  </div>
</section>
