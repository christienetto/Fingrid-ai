<script lang="ts">
    /** @type {string} */
    export let title;

    /** @type {string} */
    export let tag;

    /** @type {string} */
    export let author;

    /** @type {string} */
    export let description;

    /** @type {string} */
    export let image;

    /** @type {string} */
    export let date;

    /** @type {number} */
    export let upvotes = 20;

    /** @type {number} */
    export let downvotes = 2;

    /** @type {number} */
    export let comments = 0;

    import { ArrowBigUp } from 'lucide-svelte';
    import { ArrowBigDown } from 'lucide-svelte';
    import { MessageSquare } from 'lucide-svelte';

    let userVote = null; // 'up' for upvote, 'down' for downvote, null for no vote

    function handleUpvote(event) {
        event.stopPropagation(); // Prevent the click from triggering the <a> tag navigation
        if (userVote === 'up') {
            upvotes -= 1;
            userVote = null;
        } else {
            if (userVote === 'down') {
                downvotes -= 1;
            }
            upvotes += 1;
            userVote = 'up';
        }
    }

    function handleDownvote(event) {
        event.stopPropagation(); // Prevent the click from triggering the <a> tag navigation
        if (userVote === 'down') {
            downvotes -= 1;
            userVote = null;
        } else {
            if (userVote === 'up') {
                upvotes -= 1;
            }
            downvotes += 1;
            userVote = 'down';
        }
    }
</script>

<a href="/single-post" class="w-11/12 h-[500px] mx-auto flex font-inter py-6 cursor-pointer">
    <div class="bg-white w-full h-full rounded-l-xl border-2 border-zinc-600">
        <div class="mx-8">
            <div class="text-5xl pt-8 font-semibold"> {title}</div>
            <div class="py-4 flex text-xl font-semibold gap-7">
                <div class="w-fit py-3 rounded-full">Posted By: {author}</div>
                <div class="py-3 px-3 font-normal"> {date}</div>
                <div class="bg-blue-500 w-fit py-3 px-3 rounded-full">{tag}</div>
            </div>
            <div class="text-2xl">{description}</div>
        </div>
    </div>

    <div class="flex flex-col relative right-0 w-3/5 h-full bg-zinc-400 rounded-r-xl overflow-hidden align-text-bottom border-2 border-zinc-600 border-l-0">
        <div class="h-full">
            <img src={image} class="h-full w-full object-cover rounded-tr-xl">
        </div>
        <div class="flex pt-8 pb-6 mx-4 justify-center text-xl font-bold scale-125">
            <!-- Upvote button with fixed-width number -->
            <div class="flex items-center gap-1 cursor-pointer w-1/3 justify-center" on:click={handleUpvote}>
                <ArrowBigUp class={`${userVote === 'up' ? 'fill-green-500' : ''}`} />
                <span class="vote-count">{upvotes}</span>
            </div>
            
            <!-- Downvote button with fixed-width number -->
            <div class="flex items-center gap-1 cursor-pointer w-1/3 justify-center" on:click={handleDownvote}>
                <ArrowBigDown class={`${userVote === 'down' ? 'fill-red-500' : ''}`} />
                <span class="vote-count">{downvotes}</span>
            </div>
            
            <!-- Comments button with fixed-width number -->
            <div class="flex items-center gap-2 w-1/3 justify-center">
                <MessageSquare />
                <span class="vote-count">{comments}</span>
            </div>            
        </div>
    </div>
</a>

<style>
    .fill-green-500 {
        color: #22c55e;
    }

    .fill-red-500 {
        color: #ef4444;
    }

    /* Ensures consistent width for numbers to prevent shifting */
    .vote-count {
        display: inline-block;
        width: 2rem; /* Adjust width as needed */
        text-align: center;
    }

    /* Makes the image corners rounded to match the container */
    .rounded-r-xl {
        border-top-right-radius: 1rem;
        border-bottom-right-radius: 1rem;
    }
</style>
