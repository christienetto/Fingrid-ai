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

<!-- svelte-ignore a11y_consider_explicit_label -->
<!-- svelte-ignore a11y_missing_attribute -->
<a  class="w-11/12 h-[500px] mx-auto  font-inter py-6">
    <div class=" w-full h-full   ">
        <div class="">
            <div class="mx-8  relative bg-white  rounded-xl    ">
                <div class="flex border-2 border-zinc-600 rounded-xl">
                    <div class="w-2/3 mx-8  rounded-l-xl">
                        <div class="text-5xl pt-8 font-semibold"> {title}</div>
                        <div class="text-2xl w-fit pt-4 rounded-full">Posted By: {author}</div>
                        <div class="text-2xl font-normal py-4">Date: {date}</div>
                        <div class="bg-blue-500 w-fit py-3 px-3 text-2xl rounded-full font-semibold">{tag}</div>
                        <div class="py-7   "></div>
                        <div class="flex pt-4 pb-4 rounded-full justify-center text-xl font-bold  bg-zinc-400">
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
    
                    <div class="w-1/3">
                        <div class="">
                            <img src={image} class="h-[400px] w-full object-cover rounded-xl ">
                        </div>
                    </div>
                </div>
                <section class="text-2xl mx-8 py-8 ">
                    sfkjddddddddddddddaskfl    jsd fkds fj djsfka fdj sfdkf skdfsd fslafj asdif e;lf asdkfl seilf asi faf jdasklfj sadf 
                    sfkjddddddddddddddaskfllllllllllllllllllllllllllllllllllllllll    jsd fkds fj djsfka fdj sfdkf skdfsd fslafj asdif e;lf asdkfl seilf asi faf jdasklfj sadf 
                    sfkjdddddddlllllllllllllll    jsd fkds fj djsfka fdj sfdkf skdfsd fslafj asdif e;lf asdkfl seilf asi faf jdasklfj sadf 
                    sfkjdllllllllllllll    jsd fkds fj djsfka fdj sfdkf skdfsd fslafj asdif e;lf asdkfl seilf asi faf jdasklfj sadf 
                    sfkjdddddddddllllllllll    jsd fkds fj djsfka fdj sfdkf skdfsd fslafj asdif e;lf asdkfl seilf asi faf jdasklfj sadf 
                    sfkjdddddllllllllllllllllllllllll    jsd fkds fj djsfka fdj sfdkf skdfsd fslafj asdif e;lf asdkfl seilf asi faf jdasklfj sadf 
                    sfkjddddddddddddddaskflllllllllllllllllllllllllllllll    jsd fkds fj djsfka fdj sfdkf skdfsd fslafj asdif e;lf asdkfl seilf asi faf jdasklfj sadf 
                    sfkjddddddddddddllllllllll    jsd fkds fj djsfka fdj sfdkf skdfsd fslafj asdif e;lf asdkfl seilf asi faf jdasklfj sadf 
                </section>
                <section class="text-2xl mx-8 py-4 ">
                    <h1 class="font-semibold py-4 text-3xl">Files to download:</h1>
                     <div class="text-blue-600">
                        file.pdf
                     </div>
                     <div class="text-blue-600">
                        file.pdf
                     </div>
                     <div class="text-blue-600">
                        file.pdf
                     </div>
                     <div class="text-blue-600">
                        file.pdf
                     </div>
                </section>
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
